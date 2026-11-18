# strix-theme-lucifer

A theme for Strix, outside the eight Roman gods: Lucifer, thrown down by the archangel Michael. Two colours: red for Lucifer (`#984742`) fills buttons, progress and his disc; gold for Michael (`#c8a65d`) draws lines and letters (links, carets, focus) and his disc. The grounds are tinted faintly toward the red.

![The wallpaper](themes/lucifer/wallpaper.jpg)

![Every component of the design system in Lucifer](preview.jpg)

## Picture

Jacob Neefs after Peter Paul Rubens, S. Michael, Antwerp, 1620 to 1680, published by Gilles Hendricx. Rijksmuseum RP-P-OB-23.930, public domain. Michael with the shield of God throws Lucifer out of heaven. Cropped to both of them and printed in the inks of the theme, like the plates of the gods, with a gold disc around Michael's head and a red one around Lucifer's, by `strixui pack` of StrixUI.

## Use it

```sh
sudo strix-theme repos add liviosysctl/strix-theme-lucifer
sudo strix-rebuild switch
sudo strix-theme set lucifer
```

Every `strix-update` then brings the newest version of this repository.

## Change it

The theme is made from `source.toml`. Change the colours, the placement or the discs there, then:

```sh
cargo run -rq --manifest-path ../strixui/tools/Cargo.toml -- pack .    # ends with FAILS 0
theme repos check .    # the theme engine of Strix, as CI runs it
```

On Strix the engine is `strix-theme`; elsewhere `cargo install --git https://github.com/liviosysctl/StrixOS theme-engine` installs it as `theme`.

The layout and the rules are those of [strix-theme-template](https://github.com/liviosysctl/strix-theme-template).
