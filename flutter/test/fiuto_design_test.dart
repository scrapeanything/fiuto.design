import 'package:fiuto_design/fiuto_design.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  test('light and dark colors come from the tokens', () {
    expect(FiutoColors.light.surface, const Color(0xFFF4F5F2));
    expect(FiutoColors.dark.surface, const Color(0xFF0D0F0E));
    expect(FiutoColors.light.fiuto, const Color(0xFFF2A516));
    expect(FiutoColors.light.onFiuto, FiutoColors.dark.onFiuto);
  });

  test('copyWith changes only what is given', () {
    final changed = FiutoColors.light.copyWith(ink: const Color(0xFF000000));
    expect(changed.ink, const Color(0xFF000000));
    expect(changed.surface, FiutoColors.light.surface);
    expect(FiutoColors.light.copyWith().loss, FiutoColors.light.loss);
  });

  test('lerp goes from one theme to the other', () {
    expect(FiutoColors.light.lerp(FiutoColors.dark, 0).surface, FiutoColors.light.surface);
    expect(FiutoColors.light.lerp(FiutoColors.dark, 1).surface, FiutoColors.dark.surface);
    expect(FiutoColors.light.lerp(null, 0.5), same(FiutoColors.light));
  });

  testWidgets('the colors are available from the theme', (tester) async {
    late FiutoColors found;
    await tester.pumpWidget(
      MaterialApp(
        theme: ThemeData(extensions: const [FiutoColors.light]),
        home: Builder(builder: (context) {
          found = Theme.of(context).extension<FiutoColors>()!;
          return const SizedBox();
        }),
      ),
    );
    expect(found.gain, FiutoColors.light.gain);
  });

  test('text styles, spacing, radii and shadows', () {
    expect(FiutoTextStyles.figureXl.fontSize, 40);
    expect(FiutoTextStyles.figureXl.fontFamily, 'Barlow Semi Condensed');
    expect(FiutoTextStyles.body.fontFamily, 'Barlow');
    expect(FiutoSpacing.space4, 16);
    expect(FiutoRadius.md, 10);
    expect(FiutoShadows.sheetLight.single.offset, const Offset(0, -8));
    expect(FiutoShadows.sheetDark.single.blurRadius, 24);
  });
}
