# Victoria: law history in git

The law of Victoria as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

## What this repository holds

**Metadata only, no law text, because the Victorian legislation website states that the Government Printer owns copyright in all Victorian legislation and publishes the authorised versions for personal use only, and Australia's Copyright Act 1968 gives State Acts no exemption.** This repository records, for each Act in force, which authorised version the website lists as in force from which day, and a handful of open facts about the State's legal system. To read an Act, follow the official page link in its file, or go to [legislation.vic.gov.au](https://www.legislation.vic.gov.au).

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `catalogue/` | Catalogue of authorised versions of the Acts in force: title, act number, version number and in-force date only | 1983 | 1983 in-force days from 1 July 1997 to 28 October 2026 (13324 authorised versions of 826 Acts) |
| `statutory-rules/` | Catalogue of authorised versions of the statutory rules in force: title, rule number, version number and in-force date only | 702 | 702 in-force days from 24 September 2013 to 28 October 2026 (1248 authorised versions of 470 statutory rules) |
| `repealed-acts/` | Catalogue of authorised versions of the repealed Acts: title, number, version number, in-force date and the page's label only | 806 | 806 in-force days from 1 July 1997 to 22 October 2025 (2956 authorised versions of 506 repealed Acts) |
| `revoked-statutory-rules/` | Catalogue of authorised versions of the revoked statutory rules: title, number, version number, in-force date and the page's label only | 1880 | 1880 in-force days from 15 April 1990 to 11 March 2026 (5399 authorised versions of 1779 revoked statutory rules) |
| `legal-system/` | Legal system facts from Wikidata (CC0) | 2 | Facts Wikidata held on 30 October 2026 |

## Source

Titles, act numbers, authorised version numbers and their in-force dates are facts listed on each Act's page on the [Victorian legislation website](https://www.legislation.vic.gov.au/in-force/acts) of the Office of the Chief Parliamentary Counsel; no text of any Act or page is reproduced. The Wikidata facts are from [Wikidata](https://www.wikidata.org/wiki/Q36687) (CC0).

## Dates

A catalogue entry is dated by the date the website gives that authorised version: the day it is in force from. Each day's entries are credited to a `catalogue-<date>` record of the publisher, because the version list does not name the amending Act. Days after the retrieval date (30 October 2026) are on the `future` branch.

## How it is checked

Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`) and must match `corpus.json`; results are in `REPRODUCE.md`.

## What "author" means

The author of a commit is the law (or, for facts, the retrieval) that made the change, with an e-mail address that cannot exist (`<law key>@legislation.vic.gov.au.invalid`). The committer is always Lexifina.

## Limits

The Acts and statutory rules in force on the retrieval day are listed, and the repealed Acts and revoked statutory rules the website lists (retrieved 31 October 2026); their pages give no repeal or revocation day, so a repealed or revoked item's file stays at its last authorised version, labelled "Repealed Act" or "Revoked statutory rule". Legislation as made is not listed. The first version listed for an Act is the oldest authorised version the website holds (often from the late 1990s), not the Act as enacted. Entries do not say which Act made each change. Nothing here is an official record or an authorised version.
