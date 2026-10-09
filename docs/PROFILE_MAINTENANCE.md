# Earth & Intelligence profile

The profile stays in `README.md`. The banner and statistics are local SVG files, so viewing the profile does not contact a third-party card service.

## Banner

`assets/earth-intelligence.svg` is an original, self-contained vector illustration. It uses CSS animation, no scripts, fonts or external resources. The satellite follows a slow orbit; reduced-motion preferences disable the animation. The static composition remains complete when animation is unsupported. The continent shapes and mountain landscape are illustrative, not geographic data.

Three.js cannot run inside the GitHub README. A future interactive portfolio could use the same visual direction on a separate site; this change does not deploy a website.

## Statistics

`python3 scripts/update_stats.py` fetches the public user profile and paginated public repository metadata from GitHub's REST API using only Python's standard library. It outputs:

- `assets/stats.svg`: all owned public repositories, stars/forks received on original public repositories, and followers.
- `assets/languages.svg`: repository counts grouped by their primary detected language, excluding forks and repositories without a language. These percentages are not code-byte shares, skill ratings or time spent coding.
- `assets/github-stats.json`: the public aggregate snapshot used for the cards, including its UTC date.

The updater finishes fetching and rendering before changing these files. A network or API failure fails the job before committing, preserving the published cards. A rejected push also fails visibly rather than overwriting concurrent changes.

The workflow runs once a week (Tuesday, 06:23 Colombia), on relevant changes merged into `master`, or manually from Actions. It uses the repository's built-in `GITHUB_TOKEN`; no personal token or third-party hosting is required. The scheduled run takes effect only after the workflow reaches the default branch. GitHub may delay scheduled runs or disable schedules in inactive public repositories; re-enable them in Actions if needed.

To regenerate a saved snapshot without network access:

```sh
python3 scripts/update_stats.py --from-json assets/github-stats.json
```

## Content

Edit project summaries and technologies directly in the README. Keep academic projects described as such and link only to public repositories. English is the main profile language; the Spanish introduction is available in an expandable section.

The old `assets/banner.png` remains available for rollback. Repository pins and account-level profile settings are outside this README change.

## Professional identity and search discoverability

The README starts with one H1 containing the full name, followed by professional roles and current research interests as visible HTML text. The introduction explicitly connects the name to `ciaocamilo`. Keep the spelling and accents consistent across professional profiles.

Core identity, qualifications and project descriptions must remain available as text, independent of the banner or statistics cards. The short Spanish introduction stays visible; the expandable section provides additional context. Image alternatives describe the actual visuals, without keyword lists. Project titles link directly to their public repositories.

Keep GeoAI and remote sensing as general interests. Do not disclose the early-stage thesis title, topic, study area, objectives or methodology in the profile. Do not imply completed research results or qualifications not yet obtained. Search visibility is a goal, not a guaranteed outcome; GitHub controls the page metadata and indexing infrastructure.

The name remains indexable in a centered HTML H1. The banner uses a complementary motto instead of repeating the name. Preserve the existing illustration and animation when editing banner text.

Future work, outside this draft: align account bio and social links; add a return link to the GitHub profile from other professional pages where supported; review each featured repository's description, topics and README according to its actual content. A separate portfolio may later provide controllable metadata and a Three.js experience alongside accessible HTML text.
