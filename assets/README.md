# Assets

SVG for the guide. Diagrams and section openers paint their own dark background so they read on GitHub's light and dark themes. The mark and the masthead ship a light file and a dark file.

| Path | What it is |
| --- | --- |
| [logo-dark.svg](logo-dark.svg), [logo-light.svg](logo-light.svg) | App-icon mark. An orb, one ring, three nodes. 256×256. |
| [banner-dark.svg](banner-dark.svg), [banner-light.svg](banner-light.svg) | README masthead. Mark plus the word `agentsphere`. 1440×520. |
| [badges/](badges/) | Small pills for the README. Light and dark pair. |
| [sections/](sections/) | Openers for sections 00–09. 1200×240. |
| [diagrams/](diagrams/) | Architecture figures. Each has a Mermaid twin. See [the atlas](../docs/diagrams.md). |

`logo.svg` and `banner.svg` match the dark files, for older links.

Palette and the rules that keep a new figure on-system: [style guide](../docs/style-guide.md).

Do not add scripts, external images, or `foreignObject` to these files. GitHub renders them as images and will drop anything that looks like active content. The wordmark is outlined so it does not need a font.
