# Assets

SVG for the guide. The masthead, section openers, and diagrams are transparent, and each ships a light file and a dark file. Pages choose with `<picture>` and `prefers-color-scheme`. The app-icon mark still paints its own canvas.

| Path | What it is |
| --- | --- |
| [logo-dark.svg](logo-dark.svg), [logo-light.svg](logo-light.svg) | App-icon mark. White robot, orange antenna, two circle treatments. 256×256. |
| [banner-dark.svg](banner-dark.svg), [banner-light.svg](banner-light.svg) | README masthead. Mark, outlined `Agentsphere`, tagline `AI AGENTS REPOSITORY`. 830×300. Transparent. |
| [badges/](badges/) | Small pills for the README. Light and dark pair. |
| [sections/](sections/) | Openers for sections 00–10. 830×188. Light and dark pair. |
| [diagrams/](diagrams/) | Architecture figures, 830 wide. Light and dark pair. Each lesson figure has a Mermaid twin. See [the atlas](../docs/diagrams.md). |

`logo.svg` and `banner.svg` match the dark files, for older links.

Palette and the rules that keep a new figure on-system: [style guide](../docs/style-guide.md).

Do not add scripts, external images, or `foreignObject` to these files. GitHub renders them as images and will drop anything that looks like active content. Diagram labels are live, in `Segoe UI, Helvetica, Arial, sans-serif`, at 16px or larger inside the 830-wide viewBox. The masthead wordmark is outlined so it does not need a font.
