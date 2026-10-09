#!/usr/bin/env python3
"""Render public GitHub REST data as local SVG cards (Python stdlib only)."""
import argparse
from collections import Counter
from datetime import datetime, timezone
from html import escape
import json
import os
from pathlib import Path
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
COLORS = ['#6de4bf', '#64c9df', '#b6d882', '#8fa9eb', '#d6c284', '#b995d6', '#728e99']


def get_json(path):
    headers = {'User-Agent': 'earth-intelligence-profile', 'Accept': 'application/vnd.github+json',
               'X-GitHub-Api-Version': '2022-11-28'}
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = f'Bearer {token}'
    request = urllib.request.Request(f'https://api.github.com{path}', headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def collect(username):
    user = get_json(f'/users/{username}')
    repos = []
    page = 1
    while True:
        batch = get_json(f'/users/{username}/repos?type=owner&per_page=100&page={page}')
        if not isinstance(batch, list):
            raise ValueError('Repository API did not return a list')
        repos.extend(r for r in batch if not r['private'] and r['owner']['login'].lower() == username.lower())
        if len(batch) < 100:
            break
        page += 1
    original = [r for r in repos if not r['fork']]
    return {
        'username': username, 'updated': datetime.now(timezone.utc).strftime('%Y-%m-%d'),
        'repositories': len(repos), 'stars': sum(r['stargazers_count'] for r in original),
        'forks': sum(r['forks_count'] for r in original), 'followers': user['followers'],
        'languages': dict(sorted(Counter(r['language'] for r in original if r['language']).items(),
                                 key=lambda x: (-x[1], x[0]))),
    }


def svg(title, description, content):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="440" height="240" viewBox="0 0 440 240" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>
<rect x=".5" y=".5" width="439" height="239" rx="12" fill="#0c202b" stroke="#29454e"/>
<g font-family="Arial,Helvetica,sans-serif">{content}</g></svg>\n'''


def label(x, y, text, size=12, color='#a7c2cb', weight='400'):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}">{escape(str(text))}</text>'


def render(data):
    content = label(24, 34, 'GitHub at a glance', 18, '#edf6f7', '700')
    metrics = [('Public repos', data['repositories']), ('Stars earned', data['stars']),
               ('Forks received', data['forks']), ('Followers', data['followers'])]
    for i, (name, value) in enumerate(metrics):
        x, y = 24 + i % 2 * 210, 85 + i // 2 * 76
        content += label(x, y, f'{value:,}', 30, '#6de4bf', '700') + label(x, y + 23, name)
    content += label(24, 221, f'Public data · Updated {data["updated"]} UTC', 10)
    summary = '. '.join(f'{name}: {value}' for name, value in metrics)
    stats = svg('Public GitHub profile', summary, content)

    languages = list(data['languages'].items())
    if len(languages) > 7:
        languages = languages[:6] + [('Other', sum(n for _, n in languages[6:]))]
    total = sum(n for _, n in languages)
    content = label(24, 34, 'Languages across repositories', 18, '#edf6f7', '700')
    content += label(24, 55, 'Primary language · Owned public repos · No forks', 10)
    if total:
        x = 24
        for i, (name, count) in enumerate(languages):
            width = 392 * count / total
            content += f'<rect x="{x:.2f}" y="72" width="{width:.2f}" height="9" fill="{COLORS[i]}"/>'
            x += width
            lx, ly = 24 + i % 2 * 210, 107 + i // 2 * 26
            content += f'<circle cx="{lx + 4}" cy="{ly - 4}" r="4" fill="{COLORS[i]}"/>'
            content += label(lx + 15, ly, f'{name} {100 * count / total:.0f}%', 11)
        content += label(24, 221, f'{total} repositories with a detected language · {data["updated"]}', 10)
    else:
        content += label(24, 120, 'No detected languages yet.')
    description = '; '.join(f'{name}: {count} repositories' for name, count in languages)
    return stats, svg('Primary languages by repository count', description, content)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--username', default='ciaocamilo')
    parser.add_argument('--from-json', type=Path, help='Render an existing snapshot without API calls')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]{0,38}', args.username):
        parser.error('Invalid GitHub username')
    data = json.loads(args.from_json.read_text()) if args.from_json else collect(args.username)
    stats, languages = render(data)
    # Fetch and render everything before changing files. API failures preserve the last cards.
    assets = ROOT / 'assets'
    assets.mkdir(exist_ok=True)
    (assets / 'stats.svg').write_text(stats, encoding='utf-8')
    (assets / 'languages.svg').write_text(languages, encoding='utf-8')
    (assets / 'github-stats.json').write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'Updated public profile cards for {data["username"]} ({data["updated"]})')


if __name__ == '__main__':
    main()
