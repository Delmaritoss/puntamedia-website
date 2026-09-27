# Puntamedia — AI image prompts

Two kinds of image here:

- **BACKGROUNDS** — sit behind text. Must be dark, low-contrast, with empty space in the middle. Used at 8–18% opacity.
- **SHOWCASE** — seen properly, at full strength. These sell the *kind* of business you build for.

Everything is written for a 2026-era photorealistic model (Midjourney, Firefly, Flux, Imagen, GPT Images). Paste the prompt, then append the matching **style suffix** at the bottom of this file.

---

## The house look

Your site is navy `#08182B`, logo navy `#1C3A64`, wave blue `#5A93BC`, on cool white `#F6F9FC`. Two rules do most of the work:

1. **One clear light source, everything else falling away.** That is what makes a photo read as part of a set instead of a stock photo.
2. **Leave the middle empty.** Backgrounds carry headlines. Compose the interest at the edges.

> **Grading is handled in CSS now** — you do not need Photoshop. Every photo runs through a navy `mix-blend-mode: color` layer driven by one variable, `--grade` (0 natural → 1 full duotone). So generate them looking natural; I tune the brand shift on the page.

---

# BACKGROUNDS

### 1 — About section · Adriatic at dusk
```
A calm Adriatic sea at deep dusk photographed from a low stone shoreline, near-black water with barely visible ripples, a single thin band of warm gold light along the horizon where the sun has just gone, deep charcoal-blue sky above with no stars, distant island silhouette barely readable on the far right, vast empty negative space across the centre of the frame, no people, no boats, minimal and contemplative, shot on a Sony A7R IV with a 35mm lens at f/8, long exposure smoothing the water to glass, deep shadows, muted desaturated palette of near-black and warm gold only
```

### 2 — Contact section · island coastline at night
```
Aerial drone view looking down at a small Croatian island harbour at night, the land almost entirely black, a scattering of tiny warm gold harbour lights tracing the curve of the coastline and a stone pier, black sea filling most of the frame, no moon, no boats lit up, extremely dark and quiet, large areas of pure shadow for text to sit on, shot from 300m with a 24mm lens, long exposure, deep blacks, warm gold points of light as the only colour
```

### 3 — Services section · lime plaster wall
```
Extreme close-up of an old Dalmatian lime-plaster wall in warm grey, raking side light from the far left grazing across the surface to reveal fine texture, trowel marks and hairline cracks, the right two-thirds of the frame falling into deep shadow, no objects, no people, pure surface, shot on a 90mm macro lens at f/11, studio side light, warm neutral grey tones only, subtle and tactile, fills the frame edge to edge
```

### 4 — Process section · light trails
```
Abstract long-exposure photograph of thin warm gold light trails curving slowly through pure black space, four or five separate strands flowing left to right with soft falloff, everything else pure black, no subject, no background detail, elegant and restrained, shot at f/16 with a 30-second exposure, gold and black only, generous empty space in the upper and lower thirds
```

---

# SHOWCASE

### 5 — Laptop at a Croatian beach resort  *(your idea — use this one as the Services or About feature image)*
```
An open silver laptop on a weathered teak table at an upscale Croatian beach club, golden hour, the Adriatic sea blurred softly in the background with a stone terrace and a single olive tree, a linen napkin and an espresso cup beside the laptop, warm late-afternoon sun raking across the table from the left, screen dark and reflective so no interface is visible, shallow depth of field at f/1.8 on an 85mm lens, shot on a Canon R5, warm gold and deep shadow, relaxed and expensive, no people, no logos, no brand names
```
> Keep the screen **dark and reflective** — then you can composite your own site onto it later.

### 6 — Elegant Adriatic fish restaurant entrance  *(your idea)*
```
The entrance of an elegant Adriatic seafood restaurant at blue hour, an arched doorway in honey-coloured Brac stone with a warm glow spilling out from inside, a slate menu board on a small easel to the left, olive trees in terracotta pots either side, worn stone steps, brass fittings catching the light, a glimpse of white linen tables through the doorway, shot on a 35mm lens at f/2.8, deep blue evening sky above, warm gold interior light against cool stone, refined and inviting, no people, no readable text, no brand names
```

### 7 — Croatian night club  *(your idea)*
```
The interior of a sophisticated Adriatic night club just after opening, a long backlit bar in warm amber, blurred silhouettes of well-dressed people in conversation, exposed stone wall on one side, low pendant lighting, polished concrete floor reflecting the amber glow, deep shadows filling the upper half of the frame, shot on a 35mm lens at f/1.4 with motion blur on the figures, warm gold and near-black only, atmospheric and upmarket, no faces in focus, no logos, no readable signage
```

### 8 — Konoba terrace at sunset
```
A stone terrace of a family-run Dalmatian konoba at sunset, a long wooden table set for dinner under a grapevine pergola, the sea just visible between stone pillars, warm low sun flaring through the vine leaves, simple white plates and a carafe of wine, worn stone underfoot, shot on a 50mm lens at f/2, golden hour, warm and unpretentious, no people, no text
```

### 9 — Small shop / boutique interior
```
The interior of a small upmarket coastal boutique, warm wood shelving against a white-washed stone wall, a few carefully spaced products, a brass pendant lamp, daylight falling through a small window on the left, deep shadow on the right side of the frame, shot on a 35mm lens at f/2.8, warm neutral palette, calm and curated, no people, no readable branding
```

### 10 — Artisan bakery / café counter
```
A small artisan bakery counter at early morning, warm light from a window falling across a wooden counter, a few loaves and pastries arranged simply, a brass till and a ceramic cup, flour dust catching the light in the air, the back of the shop falling into deep shadow, shot on a 50mm lens at f/1.8, warm golden light against dark wood, honest and tactile, no people, no text
```

---

# Style suffixes — append one

**For backgrounds:**
```
--ar 21:9 · photorealistic, cinematic colour grade, heavily crushed blacks, desaturated except for warm gold highlights, no text, no watermark, no logos, no people, generous empty negative space in the centre of the frame
```

**For showcase images:**
```
--ar 3:2 · photorealistic editorial photography, cinematic colour grade, warm gold highlights against deep shadow, natural light, no text, no watermark, no logos, no recognisable faces
```

---

# Negative prompt (use on every generation)

```
text, watermark, logo, signage, brand names, oversaturated colours, HDR, teal and orange grading, blue neon, purple, lens flare artefacts, cluttered composition, busy background, plastic skin, distorted hands, extra fingers, stock photo look, cheesy, tourists, crowds
```

---

# Before you put them on the site

1. **Do not grade them yourself.** The site does it in CSS with `--grade`, per image. Send them natural.
2. **Export WebP at quality 75–80.** They publish as separate files alongside the page, so a couple of hundred KB each is fine. PNG is OK too — I convert it (the harbour PNG went 471KB → 19KB).
3. **Dark photos go on dark sections, pale photos on light sections.** Getting this backwards is the one thing that actually hurts readability.

Send me the files and I will place, convert, grade and publish them.

---

# PALE BACKGROUNDS — for the light sections

**Read this first.** Pricing, Before & After and What I do are *light* sections (white ground, navy text). The earlier prompts in this file were written for dark sections and ask for crushed blacks — using one of those here would wreck readability. These three must come back **pale, high-key and almost white**, with even brightness across the whole frame so text can sit anywhere on them.

### A — What I do · shallow water from above
```
Calm shallow Adriatic water photographed from directly above at midday, very pale aquamarine and white, soft sunlight caustics rippling gently across a pale sandy seabed, extremely low contrast, washed out and bright, no horizon line, no objects, no people, no boats, a pure surface filling the frame edge to edge, shot on a 50mm lens at f/8 from four metres up, high-key exposure, airy and almost white overall
```

### B — Before & after · morning light on a plaster wall
```
Soft morning sunlight falling across a smooth white-washed plaster wall, casting two or three broad gently-edged rectangles of light from an unseen window, faint warm cream in the lit areas and pale cool grey between them, fine plaster texture just catching the light, extremely low contrast with no hard shadow edges, nothing else in the frame, no furniture, no plants, no people, no window visible, shot on a 35mm lens at f/5.6, high-key exposure, calm and almost white overall
```
> Concrete rather than abstract, and it earns its place here: old surface, new light falling on it.

### C — Pricing · olive shadows on a stone terrace
```
Midday sun filtering through olive branches and casting soft dappled shadows across a pale limestone terrace, delicate leaf patterns scattered over worn honey-white stone with visible joints and age, light hazy and slightly overexposed, extremely low contrast with no deep shadow anywhere, no furniture, no people, no branches or trees in the frame itself, only the shadows they cast, shot looking down on a 35mm lens at f/8, high-key exposure, warm pale stone and soft silver-grey shadow, calm and almost white overall
```
> Pattern rather than blank surface, and unmistakably Adriatic. If you would rather it read premium and minimal, swap the subject for *pale Carrara marble with faint soft grey veining, bright even light, no polish reflections*.

## Style suffix for these three — do NOT use the dark one above
```
--ar 21:9 · photorealistic, high-key exposure, very low contrast, pale and washed out, no deep shadows, no vignette, even brightness across the whole frame, no text, no watermark, no logos, no people
```

## Extra negatives for these three
```
dark, black, deep shadows, moody, dramatic lighting, high contrast, vignette, silhouette, night, low key
```

> Send them over and I'll place and grade them. They'll go in at roughly 20-30% so they read as a surface, never as a picture.

---

# HERO VIDEO — scroll-scrubbed dolly

The scroll position drives the video frame, Apple-style. That puts hard constraints on the shot: **one continuous move, constant speed, locked camera, no cuts.** Any shake or speed change reads as a glitch when the viewer scrolls slowly, because they control the playhead.

## Prompt
```
A slow continuous forward dolly toward an open silver laptop on a dark wooden desk in a dim modern office at night, one warm lamp off to the left and cool blue light spilling from the laptop screen, the camera moves steadily straight ahead on a rail with no shake and no cuts, starting wide enough to see the whole desk and ending with the laptop screen completely filling the frame, the screen shows only soft defocused blue light with no interface and no text, shallow depth of field, cinematic, constant speed throughout, locked horizon, photorealistic
```

## Negative prompt
```
cuts, scene change, camera shake, handheld, zoom blur, speed ramp, text, user interface, logos, people, hands, fast motion, flicker
```

## Specs
- **1280x720** is the sweet spot. 1920x1080 only if the file stays under ~12 MB after re-encoding.
- **5 seconds**, 24 or 30 fps. Longer means a longer scroll before anything else happens.
- **One shot.** No cut, no transition, no fade in or out.
- **Ends** with the screen filling the whole frame, showing plain defocused blue light — that final frame is what gets handed over to the rest of the page, so it must be clean and free of detail.
- Send MP4, MOV or WebM. Format does not matter, I re-encode it.

## What I do with it
Re-encode every frame as a keyframe (`ffmpeg -g 1`). Normal video has a keyframe roughly every 250 frames, and seeking between them forces the browser to decode forward, which is exactly why most scroll-scrubbed video stutters. All-keyframe makes each seek instant, at the cost of a bigger file — that trade is the whole trick.

## Start frame
```
A wide, straight-on shot of an open silver laptop sitting on a dark walnut desk in a dim modern office at night, the camera at screen height and perfectly square to the laptop so nothing is angled, the laptop small and centred in the frame with generous empty space all around it, the screen glowing with soft defocused blue light showing no interface, no text and no icons, a warm desk lamp just out of frame on the left casting a low amber pool across the desk surface, the rest of the room falling into deep shadow with the faint suggestion of a window behind, a closed notebook and a ceramic cup set off to one side, shallow depth of field with the laptop sharp, photorealistic, cinematic, calm and premium, cool blue and deep navy with a single warm accent
```
Generate at 4K, 16:9. The end frame gets cropped out of this file.

## End frame — only if the crop is not usable
```
Extreme close-up of a laptop screen filling the entire frame edge to edge, showing only soft defocused blue light with a gentle gradient from deeper navy at the corners to slightly brighter blue toward the centre, no interface, no text, no icons, an extremely faint warm amber bloom spilling in from the upper left where a desk lamp sits out of frame, very subtle screen surface texture, no bezel and no edges of the laptop visible anywhere, shallow depth of field, photorealistic, cinematic, calm, cool blue and deep navy
```
Negatives, in addition to the shared list: `bezel, laptop edges, keyboard, desk, room, reflection, interface, text`

## Length
**5 seconds.** Not a pacing choice — it is frame count. At 24 fps that is 120 frames across roughly 300vh of scroll, about 17px of scroll per frame, which reads as continuous. All-keyframe encoding at 720p on dark, low-detail footage lands near 8 MB, comfortably under the 15 MB ceiling. If the model only offers 4 / 8 / 12, take **4** — 8 is too long and doubles the file for nothing.
