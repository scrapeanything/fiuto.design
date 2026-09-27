# fiuto.design

I token del design system di Fiuto tradotti in codice, per il sito (React) e per l'app (Flutter). Il design si decide e si guarda nel design system "Fiuto" su Claude; questo repository ne è la copia per il codice.

| file | cosa contiene |
|---|---|
| `tokens/tokens.json` | i token, esportati dal design system: unica fonte |
| `assets/logos/` | i quattro loghi in SVG |
| `web/tokens.css` | variabili CSS (`--color-surface`, `--space-4`, `--radius-md`, `--font-display`…), tema chiaro e scuro, classi dei testi (`.type-figure`, `.type-label`…) |
| `web/tokens.ts` | gli stessi valori tipizzati, `color("surface")`, `textStyle("figure")` |
| `flutter/` | pacchetto `fiuto_design`: `FiutoColors` (ThemeExtension, chiaro e scuro), `FiutoTextStyles`, `FiutoSpacing`, `FiutoRadius`, `FiutoShadows`, loghi |

I file in `web/` e `flutter/lib/` si generano, non si scrivono a mano:

```sh
uv run python -m fiuto_design          # rigenera dopo un cambio a tokens/tokens.json o ai loghi
uv run python -m fiuto_design --check  # la CI fallisce se non sono aggiornati
```

## Tema scuro

Il sito segue l'impostazione del sistema; `<html data-theme="light">` o `data-theme="dark"` la forzano. Nell'app: `ThemeData(extensions: [FiutoColors.light])` e `darkTheme: ThemeData(extensions: [FiutoColors.dark])`, poi `Theme.of(context).extension<FiutoColors>()!`.

## Usarlo

Sito (`package.json`):

```json
"@scrapeanything/fiuto-design": "github:scrapeanything/fiuto.design#<commit>"
```

```ts
import "@scrapeanything/fiuto-design/tokens.css";
import { color, textStyle } from "@scrapeanything/fiuto-design";
```

App (`pubspec.yaml`):

```yaml
fiuto_design:
  git:
    url: https://github.com/scrapeanything/fiuto.design
    ref: <commit>
    path: flutter
```

I caratteri (Barlow e Barlow Semi Condensed) vengono da Google Fonts: il sito li carica con un `<link>`, l'app li include tra i suoi asset.

## Sviluppo

La CI prova il generatore (copertura di righe e rami al 100%), che i file generati siano aggiornati, il TypeScript con `tsc --strict` e il pacchetto Flutter con `flutter analyze` e `flutter test`.
