// Puntamedia: contact form -> email.
//
// A Cloudflare Worker, NOT part of the static site. It is pasted into the
// Cloudflare dashboard (see worker/README.md) and answers POST requests on
// puntamedia.net/api/contact. The form in index.html sends there; if this
// worker is missing or fails, the form falls back to opening the visitor's
// email app, so the site never loses a message because of it.
//
// It needs, in the worker's Settings:
//   - a "Send email" binding named MAILER
//   - a variable TO: the inbox(es) that receive enquiries, comma separated.
//     Each one must be a verified destination address in Email Routing.
//   - optional variable FROM, default form@puntamedia.net (any address on the
//     domain works; it does not need to exist as an inbox).

import { EmailMessage } from "cloudflare:email";

const ALLOWED_ORIGINS = [
  "https://puntamedia.net",
  "https://www.puntamedia.net",
  "https://puntamedia.pages.dev",
];

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    const allowed = ALLOWED_ORIGINS.includes(origin) || origin.endsWith(".puntamedia.pages.dev");

    if (request.method === "OPTIONS") return reply(null, 204, origin, allowed);
    if (request.method !== "POST") return reply({ ok: false, error: "method" }, 405, origin, allowed);
    if (!allowed) return reply({ ok: false, error: "origin" }, 403, origin, false);

    let data;
    try {
      data = await request.json();
    } catch {
      return reply({ ok: false, error: "bad_request" }, 400, origin, allowed);
    }

    // Honeypot: people never see this field, spam bots fill it in.
    // Pretend it worked so they don't try again.
    if (String(data.website || "").trim()) return reply({ ok: true }, 200, origin, allowed);

    const line = (v, max) => String(v ?? "").replace(/[\r\n]+/g, " ").trim().slice(0, max);
    const name = line(data.name, 120);
    const email = line(data.email, 200);
    const business = line(data.business, 160);
    const lang = line(data.lang, 5);
    const message = String(data.message ?? "").trim().slice(0, 5000);

    if (!name || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      return reply({ ok: false, error: "invalid" }, 422, origin, allowed);
    }

    const to = String(env.TO || "").split(",").map((s) => s.trim()).filter(Boolean);
    if (!env.MAILER || !to.length) return reply({ ok: false, error: "not_configured" }, 500, origin, allowed);
    const from = env.FROM || "form@puntamedia.net";

    const subject = "New project enquiry" + (business ? " — " + business : "");
    const text =
      "Name: " + name + "\n" +
      "Email: " + email + "\n" +
      (business ? "Business: " + business + "\n" : "") +
      (lang ? "Site language: " + lang + "\n" : "") +
      "\n" + (message || "(no message)") + "\n\n" +
      "Reply to this email to answer " + name + " directly.\n";

    try {
      for (const rcpt of to) {
        const raw = mime({ from, to: rcpt, replyTo: email, replyName: name, subject, text });
        await env.MAILER.send(new EmailMessage(from, rcpt, raw));
      }
    } catch (err) {
      console.error("send failed", err);
      return reply({ ok: false, error: "send_failed" }, 502, origin, allowed);
    }
    return reply({ ok: true }, 200, origin, allowed);
  },
};

function reply(body, status, origin, allowed) {
  const headers = { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" };
  if (allowed && origin) {
    headers["Access-Control-Allow-Origin"] = origin;
    headers["Access-Control-Allow-Methods"] = "POST, OPTIONS";
    headers["Access-Control-Allow-Headers"] = "Content-Type";
    headers["Vary"] = "Origin";
  }
  return new Response(body === null ? null : JSON.stringify(body), { status, headers });
}

// A plain-text email, with names and subject encoded so accents and
// Croatian letters (č, ć, š, ž, đ) arrive intact.
function mime({ from, to, replyTo, replyName, subject, text }) {
  const domain = from.split("@")[1] || "puntamedia.net";
  return [
    "From: " + displayName("Puntamedia website") + " <" + from + ">",
    "To: <" + to + ">",
    "Reply-To: " + displayName(replyName) + " <" + replyTo + ">",
    "Subject: " + (ascii(subject) ? subject : encoded(subject)),
    "Date: " + new Date().toUTCString(),
    "Message-ID: <" + crypto.randomUUID() + "@" + domain + ">",
    "MIME-Version: 1.0",
    "Content-Type: text/plain; charset=UTF-8",
    "Content-Transfer-Encoding: base64",
    "",
    b64(text).replace(/.{1,76}/g, "$&\r\n"),
  ].join("\r\n");
}

function ascii(s) {
  return /^[\x20-\x7e]*$/.test(s);
}

// RFC 2047: each encoded piece stays under 75 characters, so long subjects
// are split into several pieces on folded header lines.
function encoded(s) {
  const parts = [];
  let chunk = "";
  for (const ch of s) {
    if (new TextEncoder().encode(chunk + ch).length > 45) { parts.push(chunk); chunk = ""; }
    chunk += ch;
  }
  if (chunk) parts.push(chunk);
  return parts.map((p) => "=?UTF-8?B?" + b64(p) + "?=").join("\r\n ");
}

function displayName(s) {
  return ascii(s) && !/["\\]/.test(s) ? '"' + s + '"' : encoded(s);
}

function b64(s) {
  const bytes = new TextEncoder().encode(s);
  let bin = "";
  for (let i = 0; i < bytes.length; i++) bin += String.fromCharCode(bytes[i]);
  return btoa(bin);
}
