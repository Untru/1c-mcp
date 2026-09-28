"""Пересобирает таблицу «Топ по звёздам» в README.md.

Берёт все проекты из каталога (заголовки `#### [Имя](https://github.com/owner/repo)`),
спрашивает у GitHub API звёзды и дату последнего коммита и перезаписывает блок
между маркерами <!-- TOP:START --> и <!-- TOP:END -->.

Запуск: GITHUB_TOKEN=... python scripts/update_top.py [--limit 15]
"""

import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"
START, END = "<!-- TOP:START -->", "<!-- TOP:END -->"

SECTION_RE = re.compile(r"^### (.+)$")
ENTRY_RE = re.compile(r"^#### \[([^\]]+)\]\(https://github\.com/([\w.-]+/[\w.-]+)\)")
TAGLINE_RE = re.compile(r"^\*\*(.+?)\*\*")


def parse_catalog(text):
    """Возвращает [(имя, owner/repo, раздел, слоган)] в порядке появления."""
    projects, section, current = [], None, None
    for line in text.splitlines():
        if m := SECTION_RE.match(line):
            section = m.group(1).strip()
        elif m := ENTRY_RE.match(line):
            current = [m.group(1), m.group(2), section, ""]
            projects.append(current)
        elif current and not current[3] and (m := TAGLINE_RE.match(line)):
            current[3] = m.group(1).rstrip(".")
    return projects


def fetch(repo, token):
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}")
    req.add_header("Accept", "application/vnd.github+json")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def anchor(title):
    """GitHub-якорь заголовка: нижний регистр, без пунктуации, пробелы → дефисы."""
    slug = re.sub(r"[^\w\- ]", "", title.lower(), flags=re.UNICODE)
    return "#" + slug.replace(" ", "-")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=15)
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    text = README.read_text(encoding="utf-8")

    rows = []
    for name, repo, section, tagline in parse_catalog(text):
        data = fetch(repo, token)
        if data.get("archived"):
            continue
        rows.append((data["stargazers_count"], name, data["html_url"], section, tagline, data["pushed_at"][:10]))
    rows.sort(key=lambda r: (-r[0], r[1].lower()))

    lines = [
        "| # | Проект | ⭐ | Что это | Раздел | Последний коммит |",
        "|--:|--------|--:|---------|--------|------------------|",
    ]
    for i, (stars, name, url, section, tagline, pushed) in enumerate(rows[: args.limit], 1):
        lines.append(f"| {i} | [{name}]({url}) | {stars} | {tagline} | [{section}]({anchor(section)}) | {pushed} |")

    block = f"{START}\n" + "\n".join(lines) + f"\n{END}"
    new_text = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
    if new_text != text:
        README.write_text(new_text, encoding="utf-8", newline="\n")
        print(f"README обновлён: {len(rows)} проектов, в топе {min(len(rows), args.limit)}")
    else:
        print("Изменений нет")


if __name__ == "__main__":
    main()
