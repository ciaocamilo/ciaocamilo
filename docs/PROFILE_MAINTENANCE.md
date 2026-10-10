# Earth & Intelligence profile

The profile stays in `README.md`. The banner and statistics are local SVG files, so viewing the profile does not contact a third-party card service.

## Banner

`assets/earth-intelligence.svg` is an original, self-contained vector illustration. It uses CSS animation, no scripts, fonts or external resources. The satellite follows a slow orbit; reduced-motion preferences disable the animation. The static composition remains complete when animation is unsupported. The continent shapes and mountain landscape are illustrative, not geographic data.

Three.js cannot run inside the GitHub README. A future interactive portfolio could use the same visual direction on a separate site; this change does not deploy a website.

## Statistics

`python3 scripts/update_stats.py` fetches the public user profile and paginated public repository metadata and every original repository’s language breakdown from GitHub's REST API using only Python's standard library. It outputs:

- `assets/stats.svg`: all owned public repositories, stars/forks received on original public repositories, and followers.
- `assets/languages.svg`: total bytes per language reported by the GitHub REST `/repos/{owner}/{repo}/languages` endpoint, aggregated over owned public non-fork repositories. Each share is language bytes divided by all detected bytes; the top seven categories are shown separately and the rest grouped as Other. These are not skill ratings or time spent coding. Jupyter Notebook and HTML are retained as GitHub reports them, so notebooks and exported reports may dominate. Private professional work is absent. Display percentages are apportioned in tenths to avoid a rounding total above 100%; a nonzero share below display precision is labeled <0.1%.
- `assets/github-stats.json`: the public snapshot used for the cards, including its UTC date, metric identifier, aggregate bytes and auditable per-repository language bytes. Old repository-count snapshots are rejected rather than silently treated as bytes.

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

## Project images and technology logos

The README embeds actual screenshots and plots from the featured public repositories, with descriptive alt text, captions and links to full-size images. Images stored in repositories use pinned revisions to keep the reviewed captures stable. The Tolima dashboard capture is the existing GitHub attachment linked from that project’s README; it shows historical data, not a live feed. Its long portrait layout is displayed as a compact overview. Update the URLs when a newer capture is reviewed.

Technology logos are vendored from [Devicon v2.17.0](https://github.com/devicons/devicon/tree/v2.17.0), with the upstream MIT license in `assets/icons/LICENSE-devicon.txt`. Logos identify technologies, not endorsements. Social link badges are local text SVGs matching the profile palette; text links in the academic section and footer preserve indexable professional profile names.

The weekly workflow makes one language API request per original public repository, in batches of up to four concurrent requests. Any failed request aborts the refresh before files are written, avoiding partially aggregated statistics.

## Professional presentation and counter

The short professional introduction and technology logos precede selected projects. The full technology table and language distribution are expandable. Experience is stated consistently as 12+ combined years, covering development, coordination and teaching. Project summaries distinguish implementation or evaluation from deliverables without inventing commercial impact.

The footer restores Komarev with the original `username=ciaocamilo`, a muted turquoise color, flat-square styling and an unabridged count. The number is an approximate image-request counter, not unique visitors or Google search traffic. No artificial base offset is used. Historical continuity depends on the provider retaining the original record.

Counter troubleshooting: verify the image URL actually rendered by GitHub (Camo), not only the provider URL. The original restored URL returned HTTP 200 at the provider but HTTP 404 through Camo; its URL was refreshed while retaining the same username. This does not reset or artificially offset the counter.
