# fiuto.design

Token e loghi del design system di Fiuto, tradotti per il sito (CSS e TypeScript in `web/`) e per l'app (pacchetto Flutter in `flutter/`). Il design system "Fiuto" su Claude resta il posto dove il design si decide: `tokens/tokens.json` e `assets/logos/` ne sono la copia.

- Lingua: il codice è tutto in inglese (identificatori, commenti, messaggi); in italiano restano i documenti (README) e i testi mostrati ai clienti.
- `web/` e `flutter/lib/`, `flutter/assets/logos/` sono generati: si cambia `tokens/tokens.json` o un logo e si lancia `uv run python -m fiuto_design`. Mai modificarli a mano.
- Un cambio ai token parte dal design system: si aggiorna lì, poi si copia `tokens.json` qui.
- **Tutto il codice va consegnato con i suoi test.** `uv run pytest --cov` deve dare il 100% di copertura di righe e rami (`src/fiuto_design`); il codice Flutter generato ha i suoi test in `flutter/test/`. Niente `pragma: no cover`.
- Python 3.12, uv, ruff (`uv run ruff check . && uv run ruff format .`).
- Nessun componente qui: bottoni, card e badge stanno in fiuto.web (React) e fiuto.app (Flutter), costruiti su questi token.
- Il repository è pubblico: nessun segreto, nessun dato dei clienti.
