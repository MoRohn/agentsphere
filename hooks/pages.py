"""Build hooks for the Agentsphere MkDocs site.

The markdown in the repository is also the GitHub view. These hooks adapt it
for Material at build time:

- Markdown inside ``<details>`` is parsed (GitHub does this; Python-Markdown
  does not, unless the tag opts in).
- ``<picture>`` light/dark pairs become two images with Material's
  ``#only-light`` / ``#only-dark`` suffixes, so the header toggle selects the
  file. ``prefers-color-scheme`` would follow the operating system instead.
- Relative ``.md`` links left in raw HTML are pointed at the page MkDocs
  actually writes (``README.md`` is served as ``index.html``).
- A ``data-agentsphere="github-only"`` block on the repository README is
  dropped. GitHub still shows it (the attribute is ignored). The site home
  page does not repeat a link to itself.
- The home page's banner is the hero. The visible ``# agentsphere`` title is
  left out, because the banner already carries it, and a screen-reader heading
  keeps the outline. The four level pills become cards whose lines come from
  the "Choose a level" table. The guide map drops its copy of that masthead.
  The GitHub files are unchanged.
"""

from __future__ import annotations

import logging
import os
import posixpath
import re
from html import escape
from urllib.parse import unquote, urlsplit, urlunsplit

from mkdocs.utils import get_relative_url

log = logging.getLogger("mkdocs")

_FENCE_RE = re.compile(r"(^[ \t]*```[^\n]*\n.*?^[ \t]*```[ \t]*$)", re.M | re.S)
_GITHUB_ONLY_RE = re.compile(
    r"[ \t]*<p\b[^>]*\bdata-agentsphere\s*=\s*([\"'])github-only\1[^>]*>.*?</p>[ \t]*\n?",
    re.I | re.S,
)
_DETAILS_RE = re.compile(r"<details\b([^>]*)>", re.I)
_PROTECT_RE = re.compile(r"<pre\b[^>]*>.*?</pre>|<code\b[^>]*>.*?</code>", re.I | re.S)
_PICTURE_RE = re.compile(r"<picture\b[^>]*>.*?</picture>", re.I | re.S)
_SOURCE_RE = re.compile(r"<source\b[^>]*>", re.I)
_IMG_RE = re.compile(r"<img\b[^>]*>", re.I)
_ATTR_RE = re.compile(r"""([\w:-]+)\s*=\s*(["'])(.*?)\2""", re.S)
_HREF_RE = re.compile(
    r"""(<a\b[^>]*?\bhref\s*=\s*)(["'])(.*?)\2""",
    re.I | re.S,
)
_SRC_RE = re.compile(
    r"""(<(?:img|source)\b[^>]*?\b(?:src|srcset)\s*=\s*)(["'])(.*?)\2""",
    re.I | re.S,
)
_TOKEN = "\x00AGP{0}\x00"
_BANNER_P_RE = re.compile(
    r"<p\b[^>]*>\s*<img\b[^>]*banner-light\.png[^>]*>\s*<img\b[^>]*banner-dark\.png[^>]*>\s*</p>\s*",
    re.I,
)
_META_P_RE = re.compile(
    r"<p\b[^>]*>\s*<a\b[^>]*>\s*<img\b[^>]*version-light\.svg[^>]*>.*?</p>\s*",
    re.I | re.S,
)
_LEVELS_P_RE = re.compile(
    r"<p\b[^>]*>\s*"
    r"<a\b[^>]*>\s*<img\b[^>]*level-explorer\.svg[^>]*>\s*</a>\s*(?:&nbsp;\s*)?"
    r"<a\b[^>]*>\s*<img\b[^>]*level-builder\.svg[^>]*>\s*</a>\s*(?:&nbsp;\s*)?"
    r"<a\b[^>]*>\s*<img\b[^>]*level-operator\.svg[^>]*>\s*</a>\s*(?:&nbsp;\s*)?"
    r"<a\b[^>]*>\s*<img\b[^>]*level-power\.svg[^>]*>\s*</a>\s*</p>",
    re.I | re.S,
)
_TABLE_RE = re.compile(r"<table\b[^>]*>.*?</table>", re.I | re.S)
_HOME_H1_RE = re.compile(r"^[ \t]*# agentsphere[ \t]*$", re.M)
_ROW_RE = re.compile(r"<tr\b[^>]*>(.*?)</tr>", re.I | re.S)
_CELL_RE = re.compile(r"<t[dh]\b[^>]*>(.*?)</t[dh]>", re.I | re.S)
_ANCHOR_RE = re.compile(
    r"<a\b[^>]*\bhref\s*=\s*([\"'])([^\"']+)\1[^>]*>(.*?)</a>",
    re.I | re.S,
)
_TAG_RE = re.compile(r"<[^>]+>")


def on_page_markdown(markdown, *, page, config, files):
    """Adapt README-only HTML, and let Markdown inside ``<details>`` render."""
    parts = _FENCE_RE.split(markdown)
    home = page.file.src_uri == "README.md"
    removed_titles = 0
    for index, part in enumerate(parts):
        if index % 2 == 1:
            continue
        if home:
            part = _GITHUB_ONLY_RE.sub("\n", part)
            part, removed = _HOME_H1_RE.subn("", part)
            removed_titles += removed
        parts[index] = _DETAILS_RE.sub(_details_opt_in, part)
    if home and removed_titles != 1:
        log.warning(
            "Home page should drop exactly one '# agentsphere' title (dropped %s).",
            removed_titles,
        )
    return "".join(parts)


def on_page_content(html, *, page, config, files):
    """Swap theme images and point raw HTML links at built pages."""
    protected, slots = _protect(html)
    protected = _PICTURE_RE.sub(lambda match: _picture_to_scheme_imgs(match, page), protected)
    protected = _HREF_RE.sub(lambda match: _rewrite_href(match, page, files), protected)
    protected = _TABLE_RE.sub(lambda match: f'<div class="as-scroll">{match.group(0)}</div>', protected)
    _check_media(protected, page, config)
    html = _restore(protected, slots)
    if page.file.src_uri == "README.md":
        html = _polish_home(html)
    elif page.file.src_uri == "docs/README.md":
        html = _strip_guide_masthead(html)
    return html


def _polish_home(html: str) -> str:
    """Mark the masthead and replace the level pills with cards from the table."""
    if not re.search(r"<h1\b", html, re.I):
        html = '<h1 class="as-sr">Agentsphere</h1>\n' + html
    html = _BANNER_P_RE.sub(lambda match: _tag_p(match.group(0), "as-hero"), html, count=1)
    html = _META_P_RE.sub(lambda match: _tag_p(match.group(0), "as-meta"), html, count=1)
    cards = _level_cards(html)
    html, count = _LEVELS_P_RE.subn(cards or _keep_level_pills, html, count=1)
    if count != 1:
        log.warning("Home page is missing the four level links.")
    elif cards is None:
        log.warning("Home page level table did not yield four paths.")
    return html


def _keep_level_pills(match: re.Match) -> str:
    return _tag_p(match.group(0), "as-levels")


def _level_cards(html: str) -> str | None:
    """Build the four entry cards from the rendered "Choose a level" table."""
    levels = _levels_from_table(html)
    if levels is None or len(levels) != 4:
        return None
    cards = ["<div class=\"as-levels\">"]
    for name, href, start, able in levels:
        cards.append(
            "<a class=\"as-level\" href=\"{href}\">"
            "<span class=\"as-level__name\">{name}</span>"
            "<span class=\"as-level__kicker\">Start here if you</span>"
            "<span class=\"as-level__line\">{start}</span>"
            "<span class=\"as-level__kicker\">You will be able to</span>"
            "<span class=\"as-level__line\">{able}</span>"
            "<span class=\"as-level__go\">Open the guide</span>"
            "</a>".format(
                href=escape(href, quote=True),
                name=escape(name),
                start=escape(start),
                able=escape(able),
            )
        )
    cards.append("</div>")
    return "".join(cards)


def _levels_from_table(html: str) -> list[tuple[str, str, str, str]] | None:
    for table in _TABLE_RE.finditer(html):
        rows = _ROW_RE.findall(table.group(0))
        if not rows:
            continue
        headers = [_plain_text(cell) for cell in _CELL_RE.findall(rows[0])]
        try:
            level_at = headers.index("Level")
            start_at = headers.index("Start here if you")
            able_at = headers.index("You will be able to")
        except ValueError:
            continue
        levels: list[tuple[str, str, str, str]] = []
        for row in rows[1:]:
            cells = _CELL_RE.findall(row)
            if len(cells) <= max(level_at, start_at, able_at):
                continue
            link = _ANCHOR_RE.search(cells[level_at])
            if link is None:
                continue
            name = _plain_text(link.group(3))
            href = link.group(2).strip()
            start = _plain_text(cells[start_at])
            able = _plain_text(cells[able_at])
            if name and href and start and able:
                levels.append((name, href, start, able))
        return levels
    return None


def _plain_text(fragment: str) -> str:
    return re.sub(r"\s+", " ", _TAG_RE.sub("", fragment)).strip()


def _strip_guide_masthead(html: str) -> str:
    """The home page already shows this banner and these four links."""
    html = _BANNER_P_RE.sub("", html, count=1)
    html = _LEVELS_P_RE.sub("", html, count=1)
    return html


def _tag_p(html: str, class_name: str) -> str:
    html = html.replace("<p", f'<p class="{class_name}"', 1)
    if class_name == "as-levels":
        html = html.replace("&nbsp;", "")
    return html


def _details_opt_in(match: re.Match) -> str:
    attrs = match.group(1)
    if re.search(r"\bmarkdown\s*=", attrs, re.I):
        return match.group(0)
    return f'<details markdown="1"{attrs}>'


def _protect(html: str) -> tuple[str, list[str]]:
    slots: list[str] = []

    def stash(match: re.Match) -> str:
        slots.append(match.group(0))
        return _TOKEN.format(len(slots) - 1)

    return _PROTECT_RE.sub(stash, html), slots


def _restore(html: str, slots: list[str]) -> str:
    for index, block in enumerate(slots):
        html = html.replace(_TOKEN.format(index), block)
    return html


def _attrs(tag: str) -> dict[str, str]:
    return {match.group(1).lower(): match.group(3) for match in _ATTR_RE.finditer(tag)}


def _picture_to_scheme_imgs(match: re.Match, page) -> str:
    block = match.group(0)
    images = _IMG_RE.findall(block)
    if not images:
        log.warning("Doc file '%s' has a <picture> with no <img>.", page.file.src_uri)
        return block
    dark = _dark_srcset(block)
    if not dark:
        log.warning(
            "Doc file '%s' has a <picture> with no dark-mode source.",
            page.file.src_uri,
        )
        return block
    light_tag = images[0]
    light_src = _attrs(light_tag).get("src")
    if not light_src:
        log.warning("Doc file '%s' has a <picture> image with no src.", page.file.src_uri)
        return block
    light = _with_scheme_hash(_replace_src(light_tag, light_src), "only-light")
    dark_img = _with_scheme_hash(_replace_src(light_tag, dark), "only-dark")
    return light + dark_img


def _dark_srcset(block: str) -> str | None:
    fallback = None
    for source in _SOURCE_RE.findall(block):
        attrs = _attrs(source)
        srcset = attrs.get("srcset", "").strip()
        if not srcset:
            continue
        # A srcset can list several candidates. These figures use one URL.
        url = srcset.split(",")[0].strip().split()[0]
        if fallback is None:
            fallback = url
        if "dark" in attrs.get("media", ""):
            return url
    return fallback


def _replace_src(img_tag: str, new_src: str) -> str:
    def swap(match: re.Match) -> str:
        return f"{match.group(1)}{match.group(2)}{new_src}{match.group(2)}"

    replaced, count = re.subn(
        r"""(\bsrc\s*=\s*)(["'])(.*?)\2""",
        swap,
        img_tag,
        count=1,
        flags=re.I | re.S,
    )
    if count:
        return replaced
    return img_tag[:-1] + f' src="{new_src}">'


def _with_scheme_hash(img_tag: str, scheme: str) -> str:
    def swap(match: re.Match) -> str:
        url = match.group(3).split("#", 1)[0]
        return f"{match.group(1)}{match.group(2)}{url}#{scheme}{match.group(2)}"

    return re.sub(
        r"""(\bsrc\s*=\s*)(["'])(.*?)\2""",
        swap,
        img_tag,
        count=1,
        flags=re.I | re.S,
    )


def _rewrite_href(match: re.Match, page, files) -> str:
    prefix, quote, url = match.group(1), match.group(2), match.group(3)
    rewritten = _markdown_href_to_built_url(url, page, files)
    if rewritten is None:
        return match.group(0)
    return f"{prefix}{quote}{rewritten}{quote}"


def _markdown_href_to_built_url(url: str, page, files) -> str | None:
    parts = urlsplit(url)
    if parts.scheme or parts.netloc or not parts.path:
        return None
    path = unquote(parts.path)
    if not path.endswith(".md"):
        return None
    target_uri = posixpath.normpath(posixpath.join(posixpath.dirname(page.file.src_uri), path))
    if target_uri.startswith("../") or target_uri == "..":
        log.warning(
            "Doc file '%s' contains a link '%s' that leaves the site.",
            page.file.src_uri,
            url,
        )
        return None
    target = files.get_file_from_path(target_uri)
    if target is None:
        log.warning(
            "Doc file '%s' contains a link '%s', but '%s' is not a page.",
            page.file.src_uri,
            url,
            target_uri,
        )
        return None
    built = get_relative_url(target.url, page.file.url)
    return urlunsplit(("", "", built, parts.query, parts.fragment))


def _check_media(html: str, page, config) -> None:
    docs_dir = config.docs_dir
    for match in _SRC_RE.finditer(html):
        raw = match.group(3).strip()
        if not raw:
            continue
        # srcset entries are "url descriptor". Figures use a single URL.
        url = raw.split(",")[0].strip().split()[0]
        parts = urlsplit(url)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        path = unquote(parts.path).split("#", 1)[0]
        if not path:
            continue
        relative = posixpath.normpath(posixpath.join(posixpath.dirname(page.file.src_uri), path))
        if relative.startswith("../"):
            log.warning(
                "Doc file '%s' refers to '%s', which leaves the site.",
                page.file.src_uri,
                url,
            )
            continue
        disk = os.path.join(docs_dir, relative)
        if not os.path.isfile(disk):
            log.warning(
                "Doc file '%s' refers to '%s', but that file is not in the site sources.",
                page.file.src_uri,
                relative,
            )
