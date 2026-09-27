// Generated from tokens/tokens.json by `python -m fiuto_design`. Do not edit.

import 'package:flutter/material.dart';

/// The Fiuto colors, for both themes: `Theme.of(context).extension<FiutoColors>()!`.
@immutable
class FiutoColors extends ThemeExtension<FiutoColors> {
  const FiutoColors({
    required this.surface,
    required this.surfaceRaised,
    required this.surfaceSunken,
    required this.line,
    required this.lineStrong,
    required this.ink,
    required this.inkMuted,
    required this.fiuto,
    required this.fiutoSoft,
    required this.fiutoInk,
    required this.onFiuto,
    required this.gain,
    required this.gainSoft,
    required this.loss,
    required this.lossSoft,
    required this.focus,
    required this.chartSeries,
    required this.chartMuted,
  });

  /// Page and screen background.
  final Color surface;
  /// Cards, sheets, the tab bar, list rows.
  final Color surfaceRaised;
  /// Inputs, segmented controls, the stat strip inside a card.
  final Color surfaceSunken;
  /// Hairlines: card outlines, dividers between rows. Decorative only, never the only edge of a control.
  final Color line;
  /// Borders of inputs, chips and toggles (at least 3:1 on surface, surface-raised and surface-sunken in both themes).
  final Color lineStrong;
  /// Primary text and numbers, on surface, surface-raised, surface-sunken and every -soft tint.
  final Color ink;
  /// Secondary text: metadata, units, timestamps, labels. On surface, surface-raised, surface-sunken and fiuto-soft.
  final Color inkMuted;
  /// The brand amber. Fills only: the primary button, the top-score badge, the dot of the logo, the active tab indicator. Text on it is on-fiuto.
  final Color fiuto;
  /// Tinted background for highlighted deals and the brand callout; text on it is ink or fiuto-ink.
  final Color fiutoSoft;
  /// Amber as text or icon: links, the score number outside its badge. On surface, surface-raised and fiuto-soft.
  final Color fiutoInk;
  /// Text and icons on a fiuto fill (primary button label, score badge). Never white.
  final Color onFiuto;
  /// Positive margin and prices under market value, as text with a + sign. On surface, surface-raised and gain-soft.
  final Color gain;
  /// Background of a positive-margin pill; text on it is gain.
  final Color gainSoft;
  /// Negative margin, prices over market value, destructive actions, as text with a − sign. On surface, surface-raised and loss-soft.
  final Color loss;
  /// Background of a negative-margin pill; text on it is loss.
  final Color lossSoft;
  /// Keyboard focus ring: 2px solid, 2px offset. At least 9:1 on every surface in both themes.
  final Color focus;
  /// Bars and lines of a single-series chart, on surface-raised (9:1 in both themes).
  final Color chartSeries;
  /// De-emphasized marks when one value is highlighted in ink (at least 3.4:1 on surface-raised in both themes).
  final Color chartMuted;

  static const light = FiutoColors(
    surface: Color(0xFFF4F5F2),
    surfaceRaised: Color(0xFFFFFFFF),
    surfaceSunken: Color(0xFFE9EBE6),
    line: Color(0xFFD7DBD4),
    lineStrong: Color(0xFF7D8680),
    ink: Color(0xFF0F1311),
    inkMuted: Color(0xFF56605B),
    fiuto: Color(0xFFF2A516),
    fiutoSoft: Color(0xFFFCF0D6),
    fiutoInk: Color(0xFF8A5300),
    onFiuto: Color(0xFF1A1305),
    gain: Color(0xFF0B7A4B),
    gainSoft: Color(0xFFE0F3E9),
    loss: Color(0xFFC02637),
    lossSoft: Color(0xFFFBE4E6),
    focus: Color(0xFF0F1311),
    chartSeries: Color(0xFF3F4B45),
    chartMuted: Color(0xFF7D8680),
  );

  static const dark = FiutoColors(
    surface: Color(0xFF0D0F0E),
    surfaceRaised: Color(0xFF161A18),
    surfaceSunken: Color(0xFF080A09),
    line: Color(0xFF262C29),
    lineStrong: Color(0xFF606A65),
    ink: Color(0xFFEEF1ED),
    inkMuted: Color(0xFF99A39E),
    fiuto: Color(0xFFF6B23A),
    fiutoSoft: Color(0xFF2C220E),
    fiutoInk: Color(0xFFF6B23A),
    onFiuto: Color(0xFF1A1305),
    gain: Color(0xFF45D08F),
    gainSoft: Color(0xFF0F281C),
    loss: Color(0xFFFF7D88),
    lossSoft: Color(0xFF311419),
    focus: Color(0xFFF6B23A),
    chartSeries: Color(0xFFB5BEB9),
    chartMuted: Color(0xFF667069),
  );

  @override
  FiutoColors copyWith({
    Color? surface,
    Color? surfaceRaised,
    Color? surfaceSunken,
    Color? line,
    Color? lineStrong,
    Color? ink,
    Color? inkMuted,
    Color? fiuto,
    Color? fiutoSoft,
    Color? fiutoInk,
    Color? onFiuto,
    Color? gain,
    Color? gainSoft,
    Color? loss,
    Color? lossSoft,
    Color? focus,
    Color? chartSeries,
    Color? chartMuted,
  }) {
    return FiutoColors(
      surface: surface ?? this.surface,
      surfaceRaised: surfaceRaised ?? this.surfaceRaised,
      surfaceSunken: surfaceSunken ?? this.surfaceSunken,
      line: line ?? this.line,
      lineStrong: lineStrong ?? this.lineStrong,
      ink: ink ?? this.ink,
      inkMuted: inkMuted ?? this.inkMuted,
      fiuto: fiuto ?? this.fiuto,
      fiutoSoft: fiutoSoft ?? this.fiutoSoft,
      fiutoInk: fiutoInk ?? this.fiutoInk,
      onFiuto: onFiuto ?? this.onFiuto,
      gain: gain ?? this.gain,
      gainSoft: gainSoft ?? this.gainSoft,
      loss: loss ?? this.loss,
      lossSoft: lossSoft ?? this.lossSoft,
      focus: focus ?? this.focus,
      chartSeries: chartSeries ?? this.chartSeries,
      chartMuted: chartMuted ?? this.chartMuted,
    );
  }

  @override
  FiutoColors lerp(ThemeExtension<FiutoColors>? other, double t) {
    if (other is! FiutoColors) {
      return this;
    }
    return FiutoColors(
      surface: Color.lerp(surface, other.surface, t)!,
      surfaceRaised: Color.lerp(surfaceRaised, other.surfaceRaised, t)!,
      surfaceSunken: Color.lerp(surfaceSunken, other.surfaceSunken, t)!,
      line: Color.lerp(line, other.line, t)!,
      lineStrong: Color.lerp(lineStrong, other.lineStrong, t)!,
      ink: Color.lerp(ink, other.ink, t)!,
      inkMuted: Color.lerp(inkMuted, other.inkMuted, t)!,
      fiuto: Color.lerp(fiuto, other.fiuto, t)!,
      fiutoSoft: Color.lerp(fiutoSoft, other.fiutoSoft, t)!,
      fiutoInk: Color.lerp(fiutoInk, other.fiutoInk, t)!,
      onFiuto: Color.lerp(onFiuto, other.onFiuto, t)!,
      gain: Color.lerp(gain, other.gain, t)!,
      gainSoft: Color.lerp(gainSoft, other.gainSoft, t)!,
      loss: Color.lerp(loss, other.loss, t)!,
      lossSoft: Color.lerp(lossSoft, other.lossSoft, t)!,
      focus: Color.lerp(focus, other.focus, t)!,
      chartSeries: Color.lerp(chartSeries, other.chartSeries, t)!,
      chartMuted: Color.lerp(chartMuted, other.chartMuted, t)!,
    );
  }
}

/// Text styles. Flutter has no text-transform: uppercase the overline text yourself.
abstract final class FiutoTextStyles {
  /// The one headline number of a screen: estimated margin on the ad detail, total margin on Acquisti. Tabular figures.
  static const figureXl = TextStyle(
    fontFamily: 'Barlow Semi Condensed',
    fontFamilyFallback: ['Barlow', 'Arial Narrow'],
    fontSize: 40,
    height: 1.1,
    fontWeight: FontWeight.w600,
    letterSpacing: -0.4,
    fontFeatures: [FontFeature.tabularFigures()],
  );
  /// Prices and margins in cards and stat strips. Tabular figures.
  static const figure = TextStyle(
    fontFamily: 'Barlow Semi Condensed',
    fontFamilyFallback: ['Barlow', 'Arial Narrow'],
    fontSize: 22,
    height: 1.1818,
    fontWeight: FontWeight.w600,
    fontFeatures: [FontFeature.tabularFigures()],
  );
  /// Screen titles, one per screen.
  static const title = TextStyle(
    fontFamily: 'Barlow Semi Condensed',
    fontFamilyFallback: ['Barlow', 'Arial Narrow'],
    fontSize: 26,
    height: 1.1538,
    fontWeight: FontWeight.w600,
  );
  /// Card titles (make, model, engine), section headers.
  static const heading = TextStyle(
    fontFamily: 'Barlow',
    fontFamilyFallback: ['Helvetica Neue', 'Arial'],
    fontSize: 17,
    height: 1.2941,
    fontWeight: FontWeight.w600,
  );
  /// Running text, ad descriptions, form values.
  static const body = TextStyle(
    fontFamily: 'Barlow',
    fontFamilyFallback: ['Helvetica Neue', 'Arial'],
    fontSize: 15,
    height: 1.4667,
    fontWeight: FontWeight.w400,
  );
  /// Metadata rows, chips, button labels, form labels.
  static const label = TextStyle(
    fontFamily: 'Barlow',
    fontFamilyFallback: ['Helvetica Neue', 'Arial'],
    fontSize: 13,
    height: 1.3846,
    fontWeight: FontWeight.w500,
  );
  /// Uppercase labels above a figure. Set text-transform: uppercase; always in ink-muted.
  static const overline = TextStyle(
    fontFamily: 'Barlow',
    fontFamilyFallback: ['Helvetica Neue', 'Arial'],
    fontSize: 11,
    height: 1.2727,
    fontWeight: FontWeight.w600,
    letterSpacing: 0.88,
  );
}

/// Spacing in logical pixels (4px grid).
abstract final class FiutoSpacing {
  static const double space1 = 4;
  static const double space2 = 8;
  static const double space3 = 12;
  static const double space4 = 16;
  static const double space5 = 24;
  static const double space6 = 32;
}

/// Corner radii in logical pixels.
abstract final class FiutoRadius {
  static const double sm = 6;
  static const double md = 10;
  static const double lg = 16;
}

/// Shadows, per theme.
abstract final class FiutoShadows {
  static const sheetLight = [BoxShadow(offset: Offset(0, -8), blurRadius: 24, color: Color.fromRGBO(15, 19, 17, 0.1))];
  static const sheetDark = [BoxShadow(offset: Offset(0, -8), blurRadius: 24, color: Color.fromRGBO(0, 0, 0, 0.5))];
}
