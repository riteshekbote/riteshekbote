#!/usr/bin/env python3
"""Regenerate the live-stats block in the profile README.

Runs inside a GitHub Actions step (GITHUB_TOKEN available via env).
Replaces the region between <!-- STATS:START --> and <!-- STATS:END -->.
"""
import datetime
import json
import os
import re
import urllib.request

TOKEN = os.environ.get("GH_TOKEN", "")
HDRS = {"Authorization": f"Bearer {TOKEN}", "User-Agent": "profile-stats-bot",
        "Accept": "application/vnd.github+json"}
API = "https://api.github.com"


def get(path):
    req = urllib.request.Request(API + path, headers=HDRS)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main():
    user = get("/users/riteshekbote")
    repos = get("/user/repos?affiliation=owner&per_page=100&sort=updated")
    stars = sum(r.get("stargazers_count", 0) for r in repos)
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    recent = [
        r for r in repos
        if not r.get("fork") and not r.get("private")
    ][:5]
    recent_rows = "\n".join(
        f"- [{r['name']}](https://github.com/riteshekbote/{r['name']}) — {r.get('description') or 'no description'}"
        for r in recent
    )

    block = f"""## 📊 Live Stats

| Metric | Value |
|---|---|
| Followers | **{user['followers']}** |
| Public repos | **{user['public_repos']}** |
| Total stars | **{stars}** |

**Recently updated:**

{recent_rows}

> _Last refreshed: {now} — auto-updated daily by GitHub Actions (`.github/workflows/profile-stats.yml`)_"""

    with open("README.md", encoding="utf-8") as f:
        readme = f.read()

    start = "<!-- STATS:START -->"
    end = "<!-- STATS:END -->"
    if start in readme and end in readme:
        new = re.sub(re.escape(start) + r".*?" + re.escape(end),
                     start + "\n" + block + "\n" + end,
                     readme, flags=re.S)
    else:
        new = readme + "\n" + start + "\n" + block + "\n" + end + "\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new)
    print(f"README updated: {user['followers']} followers, {user['public_repos']} repos, {stars} stars")


if __name__ == "__main__":
    main()
