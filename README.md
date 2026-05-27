# Cin7 Core — Invoice Prototype

Static HTML prototype of the **Advanced Sale / Invoice** page, demonstrating two-state navigation between a Sale Order invoice and its Exchange invoice.

## States

| State | Triggered by |
|-------|-------------|
| **Invoice** — SO-12368 / INV-12360, Authorised | Default on load |
| **Exchange** — EX-12368-1 / INV-12361, Draft | Click `#EX-12368-1` in the Exchanges sidebar |

**Invoice state** shows no payments recorded and a balance due of NZD 28.69.

**Exchange state** shows PAY-001 ($5.95 / $5.95) in the sidebar and payment grid, with a balance of NZD 0.00.

Switching between states uses a smooth opacity fade (no page reload).

## Run locally

```bash
npm start
# → http://localhost:8080/preview.html
```

Requires Python 3 (no other dependencies).

## GitHub Pages

The prototype is deployed automatically to GitHub Pages on every push to `main`.

Live URL: `https://karoliang-cin7.github.io/cin7-core-invoice-prototype/`
