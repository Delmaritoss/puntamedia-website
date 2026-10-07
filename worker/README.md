# Modulo contatti → email

`contact-form.js` è un Worker di Cloudflare, separato dal sito. Riceve il modulo
contatti su `puntamedia.net/api/contact` e manda la richiesta come email.

Finché il worker non c'è, il sito funziona lo stesso: il modulo apre l'app email
del visitatore con il messaggio già scritto, come prima.

## Attivarlo (una volta, dalla dashboard di Cloudflare)

1. **Workers & Pages → Create → Create Worker.** Nome `puntamedia-contact`,
   poi **Deploy**.
2. **Edit code**: cancella tutto, incolla `contact-form.js`, **Deploy**.
3. **Settings → Bindings → Add → Send email.** Nome della variabile: `MAILER`.
   Lascia libero il destinatario, oppure scegli l'indirizzo verificato.
4. **Settings → Variables and Secrets → Add.** Nome `TO`, valore: la casella o
   le caselle che ricevono le richieste, separate da una virgola. Devono essere
   tra le *Destination addresses* verificate di Email Routing.
5. **Settings → Domains & Routes → Add → Route.** Zona `puntamedia.net`, route
   `puntamedia.net/api/contact*`. Se si usa anche `www`, aggiungi
   `www.puntamedia.net/api/contact*`.

## Provarlo

Sul sito compila il modulo e premi *Send message*. Se tutto va, sotto il
pulsante compare "Thank you, your message has arrived" e l'email arriva in
casella, con *Rispondi* che va dritto al cliente.

Se invece si apre l'app email, il worker non ha risposto: controlla la route
(passo 5) e i log del worker (**Workers → puntamedia-contact → Logs**).

Se la route non si riesce a usare, il worker ha anche un indirizzo suo
(`puntamedia-contact.<account>.workers.dev`): basta scriverlo in `index.html`
nell'attributo `data-endpoint` del `<form id="contactForm">`.

## Cosa fa contro lo spam

- un campo nascosto che le persone non vedono e i bot compilano: quei messaggi
  vengono scartati in silenzio;
- accetta richieste solo da `puntamedia.net`, `www.puntamedia.net` e
  `puntamedia.pages.dev` (anteprime comprese);
- taglia i campi troppo lunghi (messaggio massimo 5000 caratteri).
