# Assets

The masthead and the app-icon mark are the owner's artwork, cropped, with the background removed. Section openers use that same circle. Diagrams stay SVG. Each piece ships a light file and a dark file. Pages choose with `<picture>` and `prefers-color-scheme`.

| Path | What it is |
| --- | --- |
| [logo-dark.png](logo-dark.png), [logo-light.png](logo-light.png) | App-icon and favicon mark. Orange disc, white robot. Navy crescent on light, white crescent on dark. 640×640. Transparent. |
| [banner-dark.png](banner-dark.png), [banner-light.png](banner-light.png) | README masthead. Mark, `Agentsphere`, tagline `AI AGENTS REPOSITORY`. Light is 1600×542. Dark is 1600×546 and keeps the white crescent and the glow on `sphere`. Transparent. |
| [social-preview.png](social-preview.png) | Share image, 1280×640. The dark mark, `agentsphere`, the field-guide tagline, and the four levels. Used for Open Graph, Twitter, and the GitHub social preview. |
| [badges/](badges/README.md) | Small pills for the README. The four level marks link to the persona guides under `paths/`. Version, paths, references, and read-online ship a light and dark pair. |
| [sections/](sections/README.md) | Openers for sections 00–10. 1660×376. Light and dark pair. |
| [map/](map/README.md) | Clickable section cards for the README map. Light and dark pair. Each card links to one section. |
| [diagrams/](diagrams/README.md) | Architecture figures, 830 wide. Light and dark pair. Each lesson figure has a Mermaid twin. See [the atlas](../docs/diagrams.md). |

Palette and the rules that keep a new figure on-system: [style guide](../docs/style-guide.md).

Do not add scripts or `foreignObject` to the SVG diagrams. GitHub renders them as images and will drop anything that looks like active content. Diagram labels are live, in `Segoe UI, Helvetica, Arial, sans-serif`, at 16px or larger inside the 830-wide viewBox. The masthead is the cropped artwork, so it does not depend on a font.
