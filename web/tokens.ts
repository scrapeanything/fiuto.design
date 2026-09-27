// Generated from tokens/tokens.json by `python -m fiuto_design`. Do not edit.

export const lightColors = {
  "surface": "#f4f5f2",
  "surface-raised": "#ffffff",
  "surface-sunken": "#e9ebe6",
  "line": "#d7dbd4",
  "line-strong": "#7d8680",
  "ink": "#0f1311",
  "ink-muted": "#56605b",
  "fiuto": "#f2a516",
  "fiuto-soft": "#fcf0d6",
  "fiuto-ink": "#8a5300",
  "on-fiuto": "#1a1305",
  "gain": "#0b7a4b",
  "gain-soft": "#e0f3e9",
  "loss": "#c02637",
  "loss-soft": "#fbe4e6",
  "focus": "#0f1311",
  "chart-series": "#3f4b45",
  "chart-muted": "#7d8680",
} as const;

export const darkColors = {
  "surface": "#0d0f0e",
  "surface-raised": "#161a18",
  "surface-sunken": "#080a09",
  "line": "#262c29",
  "line-strong": "#606a65",
  "ink": "#eef1ed",
  "ink-muted": "#99a39e",
  "fiuto": "#f6b23a",
  "fiuto-soft": "#2c220e",
  "fiuto-ink": "#f6b23a",
  "on-fiuto": "#1a1305",
  "gain": "#45d08f",
  "gain-soft": "#0f281c",
  "loss": "#ff7d88",
  "loss-soft": "#311419",
  "focus": "#f6b23a",
  "chart-series": "#b5beb9",
  "chart-muted": "#667069",
} as const;

export type ColorToken = keyof typeof lightColors;

/** The CSS variable of a color, which follows the active theme. */
export const color = (token: ColorToken): string => `var(--color-${token})`;

export const fonts = {
  "sans": "\"Barlow\", \"Helvetica Neue\", Arial, sans-serif",
  "display": "\"Barlow Semi Condensed\", \"Barlow\", \"Arial Narrow\", sans-serif",
} as const;

export const spacing = {
  "space-1": "4px",
  "space-2": "8px",
  "space-3": "12px",
  "space-4": "16px",
  "space-5": "24px",
  "space-6": "32px",
} as const;

export const radius = {
  "radius-sm": "6px",
  "radius-md": "10px",
  "radius-lg": "16px",
} as const;

export type TextStyleToken =
  | "figure-xl"
  | "figure"
  | "title"
  | "heading"
  | "body"
  | "label"
  | "overline"
;

/** The class of a text style, defined in tokens.css. */
export const textStyle = (token: TextStyleToken): string => `type-${token}`;

export const textStyles = {
  "figureXl": "figure-xl",
  "figure": "figure",
  "title": "title",
  "heading": "heading",
  "body": "body",
  "label": "label",
  "overline": "overline",
} as const;
