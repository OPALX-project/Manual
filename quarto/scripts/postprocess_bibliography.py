#!/usr/bin/env python3

from __future__ import annotations

import os
import re
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "docs-quarto"
LITERATURE_SRC = Path("sections/literature/index.qmd")
LITERATURE_HTML = OUTPUT_DIR / "sections/literature/index.html"

REF_PREFIX = "ref-"
SKIP_CITE_PREFIXES = ("fig-", "eq-", "tbl-", "sec-", "lst-", "thm-", "app-")


def parse_book_order() -> list[Path]:
    order: list[Path] = []
    in_list = False
    for line in (ROOT / "_quarto.yml").read_text().splitlines():
        stripped = line.strip()
        if stripped.startswith("chapters:") or stripped.startswith("appendices:"):
            in_list = True
            continue
        if in_list and stripped.startswith("- "):
            order.append(Path(stripped[2:]))
            continue
        if in_list and stripped and not line.startswith(" "):
            in_list = False
    return order


def qmd_to_html(rel: Path) -> Path:
    if rel.name == "index.qmd":
        return OUTPUT_DIR / rel.with_suffix(".html")
    return OUTPUT_DIR / rel.with_suffix(".html")


def extract_citation_order(book_files: list[Path]) -> list[str]:
    cite_pattern = re.compile(r"(?<![\w])@([A-Za-z][A-Za-z0-9_:.+-]*)")
    order: list[str] = []
    seen: set[str] = set()

    for rel in book_files:
        if rel == LITERATURE_SRC:
            continue
        text = (ROOT / rel).read_text()
        for key in cite_pattern.findall(text):
            if key.startswith(SKIP_CITE_PREFIXES):
                continue
            if key not in seen:
                seen.add(key)
                order.append(key)
    return order


def collect_entries(book_files: list[Path]) -> dict[str, BeautifulSoup]:
    entries: dict[str, BeautifulSoup] = {}

    for rel in book_files:
        html_path = qmd_to_html(rel)
        if not html_path.exists() or rel == LITERATURE_SRC:
            continue
        soup = BeautifulSoup(html_path.read_text(), "html.parser")
        refs = soup.find("div", id="refs")
        if not refs:
            continue
        for entry in refs.find_all("div", class_="csl-entry", recursive=False):
            entry_id = entry.get("id", "")
            if not entry_id.startswith(REF_PREFIX):
                continue
            key = entry_id[len(REF_PREFIX) :]
            if key not in entries:
                entries[key] = BeautifulSoup(str(entry), "html.parser")
    return entries


def set_entry_number(entry_soup: BeautifulSoup, number: int) -> BeautifulSoup:
    entry = entry_soup.find("div", class_="csl-entry")
    if entry is None:
        return entry_soup

    left = entry.find("div", class_="csl-left-margin")
    if left is not None:
        left.string = f"[{number}] "
        return entry_soup

    left = entry_soup.new_tag("div", attrs={"class": "csl-left-margin"})
    left.string = f"[{number}] "
    right = entry.find("div", class_="csl-right-inline")
    if right is not None:
        right.insert_before(left)
    else:
        entry.insert(0, left)
    return entry_soup


def update_literature_page(ordered_keys: list[str], entries: dict[str, BeautifulSoup]) -> None:
    soup = BeautifulSoup(LITERATURE_HTML.read_text(), "html.parser")
    refs = soup.find("div", id="refs")
    if refs is None:
        raise RuntimeError("Literature page has no refs container")

    refs.clear()
    refs["class"] = ["references", "csl-bib-body"]
    refs["data-entry-spacing"] = "0"
    refs["role"] = "list"

    for index, key in enumerate(ordered_keys, start=1):
        if key not in entries:
            continue
        entry_soup = set_entry_number(entries[key], index)
        entry = entry_soup.find("div", class_="csl-entry")
        if entry is not None:
            refs.append(entry)

    LITERATURE_HTML.write_text(str(soup))


def rewrite_pages(
    book_files: list[Path],
    ordered_keys: list[str],
) -> None:
    number_for_key = {key: idx for idx, key in enumerate(ordered_keys, start=1)}

    for rel in book_files:
        html_path = qmd_to_html(rel)
        if not html_path.exists() or rel == LITERATURE_SRC:
            continue

        soup = BeautifulSoup(html_path.read_text(), "html.parser")
        refs = soup.find("div", id="refs")
        if refs is not None:
            refs.decompose()

        rel_target = os.path.relpath(LITERATURE_HTML, html_path.parent)

        for link in soup.find_all("a", attrs={"role": "doc-biblioref"}):
            href = link.get("href", "")
            if "#ref-" not in href:
                continue
            key = href.split("#ref-", 1)[1]
            if key not in number_for_key:
                continue
            link["href"] = f"{rel_target}#ref-{key}"
            link.string = f"[{number_for_key[key]}]"

        html_path.write_text(str(soup))


def main() -> None:
    book_files = parse_book_order()
    citation_order = extract_citation_order(book_files)
    entries = collect_entries(book_files)

    for key in entries:
        if key not in citation_order:
            citation_order.append(key)

    update_literature_page(citation_order, entries)
    rewrite_pages(book_files, citation_order)


if __name__ == "__main__":
    main()
