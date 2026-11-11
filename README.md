# strix-theme-lucifer

A theme for Strix, outside the eight Roman gods: Lucifer under the foot of the archangel Michael. Two colours: red for Lucifer (`#984742`) fills buttons, progress and his disc; gold for Michael (`#c8a65d`) draws lines and letters (links, carets, focus) and his disc. The grounds are tinted faintly toward the red.

![The wallpaper](themes/lucifer/wallpaper.jpg)

![Every component of the design system in Lucifer](preview.jpg)

## Picture

Pieter de Bailliu (I) after Guido Reni, The Archangel Michael Tramples Satan, Rome, 1623 to 1660, published by Giovanni Battista de' Rossi. Rijksmuseum RP-P-BI-486, public domain. The whole scene is set on a ground of ink and printed in the inks of the theme, with a gold disc around Michael's head and a red one around Lucifer's, by `tools/pack.py` of StrixUI.

## Use it

- Later, Settings › Themes in Strix: connect this repository by its URL.
- Until then, in `machine.nix`, with a checkout of this repository next to it:

  ```nix
  strix.theme.extraThemes.lucifer = ./strix-theme-lucifer/themes/lucifer;
  strix.theme.default = "lucifer";    # optional: start with it
  ```

  Then `sudo strix-rebuild switch` and `sudo strix-theme set lucifer`.

## Change it

The theme is made from `source.toml`. Change the colours, the placement or the discs there, then:

```sh
python3 ../strixui/tools/pack.py .    # ends with FAILS 0
python3 check.py
```

The layout and the rules are those of [strix-theme-template](https://github.com/liviosysctl/strix-theme-template).
