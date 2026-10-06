# Puntamedia

Sito portfolio di **Puntamedia** — studio di web design con sede sull'isola di Ugljan, Croazia. Siti su misura e multilingue (HR · EN · DE · IT) per ristoranti, negozi e piccole imprese.

## Com'è fatto

Un unico file HTML autonomo. Nessuna build, nessuna dipendenza da installare, nessun framework — si apre facendo doppio clic su `index.html`.

```
index.html          tutto il sito: markup, CSS e JavaScript
img/                fotografie di sfondo e delle sezioni (WebP)
video/              il filmato della hero + il suo poster
showcase/           le pagine dei progetti inventati, da cui escono gli screenshot
image-prompts.md    i prompt usati per generare le immagini
```

Gli screenshot nella sezione lavori si rifanno cosi, da `showcase/`:

```bash
msedge --headless=new --hide-scrollbars --force-device-scale-factor=2 --window-size=1240,806 --screenshot=out.png showcase/riva-grill.html
```

Poi si riduce a 1240x806 e si salva in `img/` come WebP. La pagina e alta
esattamente 806 px perche 1240x806 e il rapporto della finestrella (16/10.4):
cosi l'immagine entra intera, senza tagli.

Librerie esterne: nessuna. Solo i font da Google Fonts.

## Cosa contiene

- **Hero video** che si scorre con lo scroll: un carrello verso un laptop, con la pagina reale disegnata in HTML sopra lo schermo e agganciata fotogramma per fotogramma. È l'unica hero del sito.
- **Hero di ripiego** con la foto dello smartphone: compare ogni volta che quella video non parte — schermo stretto, *reduced motion*, video che non arriva — qualunque sia il motivo.
- **Bilingue HR / EN** con selettore nella navigazione, che ricorda la scelta e parte in croato per i browser croati.
- **Confronto prima/dopo** trascinabile, navigazione che si raccoglie in pillola allo scroll, menu a tutto schermo su mobile.
- Fotografie graduate in CSS tramite la variabile `--grade` (0 = naturale, 1 = duotone navy). Nessun ritocco esterno necessario.

## Pubblicarlo

È un sito statico senza passo di build: nessun comando, nessuna cartella di
output, la radice del repo è già il sito.

**Cloudflare Pages**, collegato a questo repo. Workers & Pages → Create
application → Pages → Connect to Git → `puntamedia-website`. Framework preset
*None*, build command vuoto, output directory `/`. Da lì ogni push su `main`
pubblica da solo.

`_headers` viene letto da Cloudflare e aggiunge le intestazioni di sicurezza che
un file statico non può darsi da sé. Non tocca la cache: ci pensa già Pages.

Per un dominio: Pages → il progetto → Custom domains. Un `.hr` non si può
comprare da Cloudflare, va preso da un registrar croato (serve l'OIB e una copia
di un documento) e poi si spostano i nameserver.

Niente percorsi assoluti nel markup, quindi il sito funziona a qualunque radice:
`pages.dev`, un sottodominio o un dominio proprio, senza modifiche.

## Da completare

- [ ] Email, numero WhatsApp e profili social
- [ ] Il sito di **Apartmani Kalelarga** (la scheda c'è già, la finestrella è ancora quella in lavorazione)
- [ ] Konoba Makara è un cliente vero; Riva Grill e Apartmani Kalelarga sono inventati. Se vuoi essere trasparente, basta scrivere "Concept" nella riga del tag.
