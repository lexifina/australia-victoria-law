# How this repository was made (Victoria)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Victorian legislation website (Office of the Chief Parliamentary Counsel): Acts in force, version history of each Act | <https://www.legislation.vic.gov.au/in-force/acts> | 2026-10-30 | Facts only (title, act number, authorised version number and its in-force date); no text of any Act or page is reproduced |
| Victorian legislation website (Office of the Chief Parliamentary Counsel): statutory rules in force, version history of each rule | <https://www.legislation.vic.gov.au/in-force/statutory-rules> | 2026-10-30 | Facts only (title, rule number, authorised version number and its in-force date); no text of any rule or page is reproduced |
| Victorian legislation website (Office of the Chief Parliamentary Counsel): repealed Acts, version history of each | <https://www.legislation.vic.gov.au/repealed-revoked/acts> | 2026-10-31 | Facts only (title, number, authorised version number and its in-force date, and the repealed or revoked label on its page); no text of any Act, rule or page is reproduced |
| Victorian legislation website (Office of the Chief Parliamentary Counsel): revoked statutory rules, version history of each | <https://www.legislation.vic.gov.au/repealed-revoked/statutory-rules> | 2026-10-31 | Facts only (title, number, authorised version number and its in-force date, and the repealed or revoked label on its page); no text of any Act, rule or page is reproduced |
| Wikidata | <https://www.wikidata.org/wiki/Q36687> | 2026-10-30 | CC0 1.0 |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `catalogue` | Catalogue of authorised versions of the Victorian Acts in force (title, act number, version number and in-force date only) | 1983 | 1997-07-01 to 2026-10-28 |
| `statutory-rules` | Catalogue of authorised versions of the Victorian statutory rules in force (title, rule number, version number and in-force date only) | 702 | 2013-09-24 to 2026-10-28 |
| `repealed-acts` | Catalogue of authorised versions of the repealed Victorian Acts (title, act number, version number and in-force date only) | 806 | 1997-07-01 to 2025-10-22 |
| `revoked-statutory-rules` | Catalogue of authorised versions of the revoked Victorian statutory rules (title, rule number, version number and in-force date only) | 1880 | 1990-04-15 to 2026-03-11 |
| `legal-system` | Victoria: legal system facts (Wikidata) | 2 | 1851-07-01 to 2026-10-30 |

The build made 5373 commits:

| Commits | Kind |
| ---: | --- |
| 5 | first version of an act |
| 5368 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 1 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 5368 laws in the record.
- 10741 tags.

## Dates

Each commit is dated at noon (Australia/Melbourne) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Catalogue entries are dated by the date the Victorian legislation website gives each authorised version (the day that version is in force from); they describe versions and are not law text. https://www.legislation.vic.gov.au/in-force/acts

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `dba26311df48da85936d458426ed222b9fbfbf92f92ae3a1d023f8e5c8fccd15` (15723829 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

5373 versions of 5 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- No law text is published: the Victorian legislation website states that the Government Printer owns copyright in all Victorian legislation and that authorised electronic versions are published there for personal use only, and the Copyright Act 1968 (Cth) gives no exemption for State Acts. No Act text was fetched.
- The catalogue holds facts only: for each Act in force, its title, act number, and each authorised version number with the date the website lists it as in force from. One file per Act; each new authorised version updates that file on its in-force day.
- Each day's entries are credited to a "catalogue-<date>" record of the publisher, not to the amending Act: the version list does not name the Act that made each change.
- Where an Act has two authorised versions dated the same day, the entry shows the higher version number.
- Coverage: the Acts in force listed in the website's sitemap on the retrieval day. Statutory rules in force are catalogued the same way in statutory-rules/. The repealed Acts and revoked statutory rules listed in the sitemap are catalogued the same way in repealed-acts/ and revoked-statutory-rules/, each entry also giving the label on its page ("Repealed Act", "Revoked statutory rule"); their pages give no repeal or revocation day, so each file stays at its last authorised version and no commit marks the repeal or revocation. Legislation as made is not included. The earliest version listed for an Act is the oldest one the website holds (often from the late 1990s), not the Act as enacted.
- Versions dated after the retrieval day go on the "future" branch.
- Wikidata facts (CC0) form the "legal-system" act.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code with Claude Opus 5.5 wrote Lexifina's code and chose the sources; it did not write or alter any legal text. The code is deterministic and runs no model.
