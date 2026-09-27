# Puntamedia

Sito portfolio di **Puntamedia** — studio di web design con sede sull'isola di Ugljan, Croazia. Siti su misura e multilingue (HR · EN · DE · IT) per ristoranti, negozi e piccole imprese.

## Com'è fatto

Un unico file HTML autonomo. Nessuna build, nessuna dipendenza da installare, nessun framework — si apre facendo doppio clic su `index.html`.

```
index.html          tutto il sito: markup, CSS e JavaScript
img/                fotografie di sfondo e delle sezioni (WebP)
video/              il filmato della hero + il suo poster
image-prompts.md    i prompt usati per generare le immagini
```

Librerie esterne: nessuna. Solo i font da Google Fonts.

## Cosa contiene

- **Hero video** che si scorre con lo scroll: un carrello verso un laptop, con la pagina reale disegnata in HTML sopra lo schermo e agganciata fotogramma per fotogramma. Su schermi stretti o con *reduced motion* subentra automaticamente una hero alternativa in WebGL.
- **Bilingue HR / EN** con selettore nella navigazione, che ricorda la scelta e parte in croato per i browser croati.
- **Confronto prima/dopo** trascinabile, navigazione che si raccoglie in pillola allo scroll, menu a tutto schermo su mobile.
- Fotografie graduate in CSS tramite la variabile `--grade` (0 = naturale, 1 = duotone navy). Nessun ritocco esterno necessario.

## Pubblicarlo

È un sito statico: va bene qualunque hosting. Con GitHub Pages:

1. Settings → Pages → Source: `Deploy from a branch` → `main` / `root`
2. Per il dominio: Settings → Pages → Custom domain
3. Dal pannello del registrar, un record `CNAME` che punta a `<utente>.github.io`

Spuntare **Enforce HTTPS** quando il certificato è pronto (qualche minuto).

## Da completare

- [ ] Prezzi reali (adesso sono segnaposto: €490 / €890)
- [ ] Email, numero WhatsApp e profili social
- [ ] Due progetti in più nella sezione lavori
