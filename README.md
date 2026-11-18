# news-image-20261117 (v2)

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/a25822457/makefun-news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/a25822457/makefun-news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

Sum up 17 November's world news in one image — a newspaper front page for
**Tuesday, 17 November 2026**. The date is printed large in the nameplate
so there is no doubt which day the page sums up, and every story on it
happened (or was first reported) on that day.

## Why v2

The v1 front page scored 9 wins, 2 draws, 1 loss in development judging —
rank 3566 of 4808. It won games but by little: seven stories squeezed
into the page, a thin lead illustration, and dense text. This version
rebuilds the page on the layout of the sibling 18 November entry, which
went 12–0 in development judging: one hero lead story with a large
illustration, two medium stories, three small stories — six stories
total, bigger headlines, bigger pictures, more air.

## The day's stories

| # | Story | Tag |
| --- | --- | --- |
| 1 | Ukraine hits the Crimea (Kerch) Bridge for a second day; a road span falls into the strait, as Russia pounds bridges across the Dnipro in Kyiv — the war's biggest drone raid, Russia saying it downed 1,441 drones | Ukraine · Conflict |
| 2 | US jets strike an IRGC missile site on Iran's Qeshm Island in "self-defence", hours after Iranian drones targeted a US radar at Isa Air Base in Bahrain; the drones were intercepted | US–Iran · Middle East |
| 3 | Trump flies to Asia to meet Xi Jinping and Vladimir Putin, heading to Shenzhen for a trilateral nuclear-arms meeting, after signing a trade deal in Manila | Diplomacy · Asia |
| 4 | Nvidia reports Q3 revenue of $115.8bn, up 103% year on year — but the board says ousted founder Jensen Huang will not be reinstated as CEO | Tech · Nvidia |
| 5 | Global markets slide as the Nasdaq enters a correction; the S&P 500 drops 1.9%, the Dow 1.4% | Markets · Economy |
| 6 | Israel: Knesset elects Matan Kahana speaker 66–52, ousting a Netanyahu ally and handing the agenda to the Eisenkot bloc | Israel |
| — | Also today — France: 146,000 march in a public-sector strike over pay | France |

Sources: Reuters, Al Jazeera, Times of Israel, Ctech, Manila Times. Every
story was verified against reporting dated 17 November 2026 before the
image was drawn. The jokes sit in the tone and the drawings — a "BOOM!",
a startled tanker, "Day two — and yes, the bridge again." — never in the
news: every fact stays straight.

## Files

- `main.py` — the entry program (Python 3.13, standard library only):
  copies `entry.png` to `/output/entry.png`. No network, deterministic.
- `entry.png` — the front page, 1024×1024. v3: the externally refined
  version of the v2 render — same layout, same 6 stories, all text
  unchanged. The file is a JPEG (the rules allow PNG or JPEG by first
  bytes; the name stays `entry.png`), quality 92, ~470 KB.
- `render_v2.py` — the script that drew the v2 `entry.png` (PIL, DejaVu fonts).
- `README.md`, `LICENSE` (MIT).

## Reproduce

```sh
python3 render_v2.py        # redraws the v2 original (not the refined entry.png)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
