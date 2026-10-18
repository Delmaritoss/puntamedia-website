"""Listino extra e automazioni di Puntamedia, in tre lingue.

Scrive una pagina HTML per lingua e la stampa in PDF con Chromium:

    pip install playwright && playwright install chromium
    python listino/listino.py

I prezzi stanno solo qui, in EXTRA e PACKAGES: si cambiano qui e si rilancia.
Ricordarsi di aggiornarli anche nella sezione prezzi di index.html.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent

# (chiave, attivazione, canone mensile) — None = non previsto
# il prefisso "da" (da 300 €) lo mette la lingua, tramite "from"
EXTRA = {
    "auto": [
        ("qr", 120, 20, False),
        ("reviews", 100, 25, False),
        ("booking", 200, 40, False),
        ("replies", 150, 30, False),
        ("leads", 80, 10, False),
        ("custom", 300, 30, True),
    ],
    "other": [
        ("posts", None, 60, False),
        ("lang", 80, None, False),
    ],
}
PACKAGES = [("Base", 450, 15), ("Plus", 810, 35), ("Pro", 1200, 69)]

T = {
    "it": {
        "file": "puntamedia-extra-automazioni-it.pdf",
        "doc_title": "Puntamedia — Extra e automazioni",
        "kicker": "Listino 2026",
        "title": "Extra e automazioni",
        "intro": "Piccoli strumenti che lavorano per la tua attività ogni giorno: più recensioni, più prenotazioni, meno messaggi a cui rispondere. Si aggiungono a qualsiasi sito Puntamedia oppure si prendono da soli.",
        "cols": ("Servizio", "Attivazione", "Al mese"),
        "groups": {"auto": "Automazioni", "other": "Altri extra"},
        "from": "da",
        "items": {
            "qr": ("Menu digitale con QR", "Menu online in più lingue, che aggiorni da solo quando vuoi. Il QR va sui tavoli."),
            "reviews": ("Richiesta recensioni Google", "Dopo la visita il cliente riceve un messaggio con il link per lasciare una recensione."),
            "booking": ("Prenotazioni online con promemoria", "Prenotazioni dal sito, conferma immediata e promemoria via email o WhatsApp prima dell'appuntamento."),
            "replies": ("Risposte automatiche Instagram e WhatsApp", "Orari, prezzi, posizione e disponibilità: le domande frequenti ricevono risposta subito, anche di notte."),
            "leads": ("Richieste dal sito in un foglio", "Ogni richiesta dal sito finisce in un foglio ordinato, con un riepilogo ogni lunedì."),
            "custom": ("Automazione su misura", "Fatture, ordini, magazzino o altro: la costruiamo sul tuo modo di lavorare."),
            "posts": ("Post Instagram", "4 post al mese con le tue foto, testi in due lingue."),
            "lang": ("Lingua aggiuntiva del sito", "Una lingua in più, tradotta e controllata."),
        },
        "pk_title": "I pacchetti sito",
        "per_month": "/mese",
        "pk_note": "Plus e Pro includono già menu QR e richiesta recensioni; Pro anche prenotazioni e risposte automatiche.",
        "how_title": "Come funziona",
        "how": [
            "L'attivazione si paga una volta; il canone parte dal mese della messa online.",
            "Il canone comprende server, manutenzione, aggiornamenti e assistenza entro 48 ore lavorative.",
            "Durata minima 12 mesi, poi disdetta con 30 giorni di preavviso.",
            "Pagando un anno in anticipo, 2 mesi sono gratis.",
        ],
        "valid": "Prezzi validi da ottobre 2026",
    },
    "hr": {
        "file": "puntamedia-dodaci-automatizacije-hr.pdf",
        "doc_title": "Puntamedia — Dodaci i automatizacije",
        "kicker": "Cjenik 2026",
        "title": "Dodaci i automatizacije",
        "intro": "Mali alati koji svakodnevno rade za vaš posao: više recenzija, više rezervacija, manje poruka na koje treba odgovarati. Dodaju se bilo kojoj Puntamedia stranici ili se uzimaju zasebno.",
        "cols": ("Usluga", "Postavljanje", "Mjesečno"),
        "groups": {"auto": "Automatizacije", "other": "Ostali dodaci"},
        "from": "od",
        "items": {
            "qr": ("Digitalni jelovnik s QR kodom", "Jelovnik online na više jezika, koji sami mijenjate kad god želite. QR kod ide na stolove."),
            "reviews": ("Zahtjev za Google recenziju", "Nakon posjeta gost dobiva poruku s poveznicom za recenziju."),
            "booking": ("Online rezervacije s podsjetnicima", "Rezervacije sa stranice, trenutna potvrda i podsjetnik e-mailom ili WhatsAppom prije termina."),
            "replies": ("Automatski odgovori na Instagramu i WhatsAppu", "Radno vrijeme, cijene, lokacija i dostupnost: česta pitanja dobivaju odgovor odmah, i noću."),
            "leads": ("Upiti sa stranice u tablici", "Svaki upit sa stranice sprema se u preglednu tablicu, uz sažetak svakog ponedjeljka."),
            "custom": ("Automatizacija po mjeri", "Računi, narudžbe, skladište ili nešto drugo: izrađujemo je prema vašem načinu rada."),
            "posts": ("Objave na Instagramu", "4 objave mjesečno s vašim fotografijama, tekst na dva jezika."),
            "lang": ("Dodatni jezik stranice", "Još jedan jezik, preveden i provjeren."),
        },
        "pk_title": "Paketi web stranica",
        "per_month": "/mj.",
        "pk_note": "Plus i Pro već uključuju QR jelovnik i zahtjeve za recenzije; Pro i rezervacije te automatske odgovore.",
        "how_title": "Kako funkcionira",
        "how": [
            "Postavljanje se plaća jednom; mjesečna naknada kreće od mjeseca objave.",
            "Naknada uključuje poslužitelj, održavanje, ažuriranja i podršku u roku od 48 radnih sati.",
            "Minimalno trajanje 12 mjeseci, zatim otkaz uz 30 dana najave.",
            "Uz godišnje plaćanje unaprijed, 2 mjeseca su besplatna.",
        ],
        "valid": "Cijene vrijede od listopada 2026.",
    },
    "en": {
        "file": "puntamedia-extras-automations-en.pdf",
        "doc_title": "Puntamedia — Extras & automations",
        "kicker": "Price list 2026",
        "title": "Extras & automations",
        "intro": "Small tools that work for your business every day: more reviews, more bookings, fewer messages to answer. Add them to any Puntamedia website, or take them on their own.",
        "cols": ("Service", "Setup", "Monthly"),
        "groups": {"auto": "Automations", "other": "Other extras"},
        "from": "from",
        "items": {
            "qr": ("Digital menu with QR code", "An online menu in several languages that you update yourself, any time. The QR code goes on the tables."),
            "reviews": ("Google review requests", "After their visit, guests get a message with a link to leave a review."),
            "booking": ("Online bookings with reminders", "Bookings from your site, instant confirmation and a reminder by email or WhatsApp before the visit."),
            "replies": ("Instagram & WhatsApp auto-replies", "Opening hours, prices, location and availability: common questions get answered instantly, even at night."),
            "leads": ("Website enquiries in a spreadsheet", "Every enquiry from your site lands in a tidy sheet, with a summary every Monday."),
            "custom": ("Custom automation", "Invoices, orders, stock or anything else, built around the way you work."),
            "posts": ("Instagram posts", "4 posts a month with your photos, captions in two languages."),
            "lang": ("Extra website language", "One more language, translated and checked."),
        },
        "pk_title": "Website packages",
        "per_month": "/month",
        "pk_note": "Plus and Pro already include the QR menu and review requests; Pro also includes bookings and auto-replies.",
        "how_title": "How it works",
        "how": [
            "Setup is paid once; the monthly fee starts the month you go live.",
            "The monthly fee covers hosting, maintenance, updates and support within 48 working hours.",
            "12-month minimum, then cancel with 30 days' notice.",
            "Pay a year upfront and get 2 months free.",
        ],
        "valid": "Prices valid from October 2026",
    },
}


def eur(lang, n):
    s = f"{n:,}".replace(",", ".")
    return f"€{s}".replace(".", ",") if lang == "en" else f"{s} €"


def price(lang, n, prefix):
    if n is None:
        return '<span class="none">—</span>'
    p = eur(lang, n)
    return f'<small>{T[lang]["from"]}</small> {p}' if prefix else p


CSS = """
:root{--ink:#08182B;--navy:#1C3A64;--acc:#2F6E9E;--acc-soft:#5A93BC;--tint:#F2F6FA;
  --line:#D4E0EA;--text:#152B40;--muted:#5A7489;
  --serif:"Cormorant Garamond",Georgia,serif;--sans:"Jost",system-ui,sans-serif}
*{margin:0;padding:0;box-sizing:border-box}
@page{size:A4;margin:0}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:var(--sans);color:var(--text);background:#fff;font-weight:300}
.page{width:210mm;height:297mm;display:flex;flex-direction:column;position:relative;overflow:hidden}
header{background:var(--ink);color:#EDF3F9;padding:10mm 18mm 8mm}
.mark{display:flex;align-items:center;gap:9px}
.mark svg{width:20px;height:20px}
.mark span{font-family:var(--serif);font-size:19pt;font-weight:600;letter-spacing:.01em}
.kick{margin-top:6mm;font-size:8pt;font-weight:500;letter-spacing:.26em;text-transform:uppercase;color:#7E9BB5}
h1{font-family:var(--serif);font-size:30pt;font-weight:600;line-height:1.05;margin-top:2mm}
.intro{margin-top:3mm;font-size:9.6pt;line-height:1.6;color:#A9C0D6;max-width:150mm}
main{padding:6.5mm 18mm 0;flex:1;display:flex;flex-direction:column}
table{width:100%;border-collapse:collapse}
th{font-size:7.5pt;font-weight:500;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);
  text-align:right;padding:0 0 2mm;border-bottom:1.5px solid var(--ink)}
th:first-child{text-align:left}
tr.group td{padding:3.4mm 0 1.2mm;font-size:8pt;font-weight:600;letter-spacing:.22em;
  text-transform:uppercase;color:var(--acc);border-bottom:1px solid var(--line)}
td{padding:2.1mm 0;border-bottom:1px solid var(--line);vertical-align:top}
td.n b{display:block;font-family:var(--serif);font-size:12.5pt;font-weight:700;color:var(--ink);line-height:1.2}
td.n span{display:block;font-size:8.4pt;line-height:1.45;color:var(--muted);margin-top:.4mm;max-width:118mm}
td.p{text-align:right;white-space:nowrap;font-size:11pt;font-weight:500;color:var(--ink);width:27mm;padding-top:2.4mm}
td.p small{font-size:7.5pt;font-weight:400;color:var(--muted)}
td.p .none{color:#A8BACB;font-weight:300}
.low{display:grid;grid-template-columns:1.05fr .95fr;gap:9mm;margin-top:5.5mm}
h2{font-family:var(--serif);font-size:14pt;font-weight:700;color:var(--ink);margin-bottom:3mm}
.pk{display:grid;grid-template-columns:repeat(3,1fr);gap:2.5mm}
.pk div{background:var(--tint);border-radius:2px;padding:3mm 3mm 3.2mm;border-top:2px solid var(--acc-soft)}
.pk div.f{border-top-color:var(--acc)}
.pk b{display:block;font-family:var(--serif);font-size:13pt;font-weight:700;color:var(--ink)}
.pk span{display:block;font-size:10pt;font-weight:500;color:var(--ink);margin-top:1mm}
.pk em{display:block;font-style:normal;font-size:8.3pt;color:var(--muted)}
.pknote{font-size:8.3pt;line-height:1.55;color:var(--muted);margin-top:3mm}
ul{list-style:none}
li{position:relative;font-size:8.6pt;line-height:1.5;padding-left:4.2mm;margin-bottom:1.3mm}
li::before{content:"";position:absolute;left:0;top:1.6mm;width:1.5mm;height:1.5mm;border-radius:50%;background:var(--acc-soft)}
footer{margin:auto 18mm 0;padding:3.5mm 0 7mm;border-top:1px solid var(--line);display:flex;
  justify-content:space-between;align-items:baseline;font-size:8.5pt;color:var(--muted)}
footer b{font-weight:500;letter-spacing:.14em;text-transform:uppercase;color:var(--acc);font-size:8pt}
"""

LOGO = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 4.5 L21 12 L3 19.5 L7.5 12 Z" fill="#5A93BC"/></svg>'


def page(lang):
    t = T[lang]
    rows = []
    for g in ("auto", "other"):
        rows.append(f'<tr class="group"><td colspan="3">{t["groups"][g]}</td></tr>')
        for key, setup, month, pre in EXTRA[g]:
            name, desc = t["items"][key]
            rows.append(
                f'<tr><td class="n"><b>{name}</b><span>{desc}</span></td>'
                f'<td class="p">{price(lang, setup, pre)}</td>'
                f'<td class="p">{price(lang, month, pre)}</td></tr>'
            )
    pk = "".join(
        f'<div{" class=f" if name == "Plus" else ""}><b>{name}</b>'
        f'<span>{eur(lang, s)}</span><em>+ {eur(lang, m)}{t["per_month"]}</em></div>'
        for name, s, m in PACKAGES
    )
    how = "".join(f"<li>{x}</li>" for x in t["how"])
    c1, c2, c3 = t["cols"]
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><title>{t["doc_title"]}</title>
<link rel="stylesheet" href="../fonts/fonts.css"><style>{CSS}</style></head>
<body><section class="page">
<header>
  <div class="mark">{LOGO}<span>Puntamedia</span></div>
  <div class="kick">{t["kicker"]}</div>
  <h1>{t["title"]}</h1>
  <p class="intro">{t["intro"]}</p>
</header>
<main>
  <table><thead><tr><th>{c1}</th><th>{c2}</th><th>{c3}</th></tr></thead>
  <tbody>{"".join(rows)}</tbody></table>
  <div class="low">
    <div><h2>{t["pk_title"]}</h2><div class="pk">{pk}</div><p class="pknote">{t["pk_note"]}</p></div>
    <div><h2>{t["how_title"]}</h2><ul>{how}</ul></div>
  </div>
</main>
<footer><b>puntamedia.net · hello@puntamedia.net</b><span>{t["valid"]}</span></footer>
</section></body></html>"""


def main():
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        pg = browser.new_page()
        for lang, t in T.items():
            html = HERE / f"extra-{lang}.html"
            html.write_text(page(lang), encoding="utf-8")
            pg.goto(html.as_uri())
            pg.evaluate("document.fonts.ready")
            pg.pdf(path=str(HERE / t["file"]), format="A4", print_background=True,
                   prefer_css_page_size=True)
            print("ok", t["file"])
        browser.close()


if __name__ == "__main__":
    main()
