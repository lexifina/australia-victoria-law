"""Victoria: write repo/README.md, LICENSE, jurisdiction.json from corpus.json.

    python -X utf8 docs.py [--partial N]     # N = number of Acts in force listed in the sitemap
"""
import datetime, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[0] / 'world-law'))
import p3lib as L

import os
c = json.load(open(HERE / os.environ.get('VIC_CORPUS', 'corpus.json'), encoding='utf8'))
by = {a['slug']: a for a in c['acts']}
cat, la, sr = by['catalogue'], by['legal-system'], by.get('statutory-rules')
docs = c['sources'][0]['retrieved']


def stats(a):
    n = len(a['versions'][0]['units']) + len({k for v in a['versions'][1:] for k in v.get('changes', {})} - set(a['versions'][0]['units']))
    past = [v for v in a['versions'] if v['from'] <= docs]
    fut = [v for v in a['versions'] if v['from'] > docs]
    nver = sum(len(v.get('units') or v.get('changes') or {}) for v in a['versions'])
    return n, past, fut, nver


nacts, past, fut, nver = stats(cat)
partial = None
if '--partial' in sys.argv:
    partial = int(sys.argv[sys.argv.index('--partial') + 1])
sr_total = int(sys.argv[sys.argv.index('--rules') + 1]) if '--rules' in sys.argv else None


def d(s):
    x = datetime.date.fromisoformat(s)
    return f'{x.day} {x.strftime("%B")} {x.year}'


holds = ("**Metadata only, no law text, because the Victorian legislation website states that the Government Printer owns "
         "copyright in all Victorian legislation and publishes the authorised versions for personal use only, and Australia's "
         "Copyright Act 1968 gives State Acts no exemption.** This repository records, for each Act in force, which authorised "
         "version the website lists as in force from which day, and a handful of open facts about the State's legal system. "
         "To read an Act, follow the official page link in its file, or go to [legislation.vic.gov.au](https://www.legislation.vic.gov.au).")
if partial:
    holds += (f"\n\n**Partial build:** {nacts} of the {partial} Acts in force are catalogued so far (in alphabetical order, the "
              "Constitution Act 1975 first). The rest are being added; history for them will be inserted at their own dates, so "
              "`main` may be rebuilt as it grows.")
if sr and sr_total and stats(sr)[0] < sr_total:
    holds += f" Statutory rules: {stats(sr)[0]} of the {sr_total} in force are catalogued so far."
elif not sr:
    holds += " Statutory rules are not catalogued yet." if partial else ""
hist = f"{len(past)} in-force days from {d(cat['versions'][0]['from'])} to {d(past[-1]['from'])} ({nver} authorised versions of {nacts} Acts)"
if fut:
    hist += f"; {len(fut)} later day(s) on the `future` branch"
rows = [('catalogue', 'Catalogue of authorised versions of the Acts in force: title, act number, version number and in-force date only', len(cat['versions']), hist),
        ] + ([('statutory-rules', 'Catalogue of authorised versions of the statutory rules in force: title, rule number, version number and in-force date only',
                len(sr['versions']), (lambda n, p, f, v: f"{len(p)} in-force days from {d(sr['versions'][0]['from'])} to {d(p[-1]['from'])} ({v} authorised versions of {n} statutory rules)"
                + (f"; {len(f)} later day(s) on the `future` branch" if f else ''))(*stats(sr)))] if sr else []) + [
        ] + [(a['slug'], f'Catalogue of authorised versions of the {what}: title, number, version number, in-force date and the page\'s label only',
              len(a['versions']), (lambda n, p, f, v: f"{len(p)} in-force days from {d(a['versions'][0]['from'])} to {d(p[-1]['from'])} ({v} authorised versions of {n} {what})")(*stats(a)))
             for a, what in ((by.get('repealed-acts'), 'repealed Acts'), (by.get('revoked-statutory-rules'), 'revoked statutory rules')) if a] + [
        ('legal-system', 'Legal system facts from Wikidata (CC0)', len(la['versions']), 'Facts Wikidata held on 30 October 2026')]
rp = by.get('repealed-acts') or by.get('revoked-statutory-rules')
source = ("Titles, act numbers, authorised version numbers and their in-force dates are facts listed on each Act's page on the "
          "[Victorian legislation website](https://www.legislation.vic.gov.au/in-force/acts) of the Office of the Chief Parliamentary "
          "Counsel; no text of any Act or page is reproduced. The Wikidata facts are from [Wikidata](https://www.wikidata.org/wiki/Q36687) (CC0).")
dates = ("A catalogue entry is dated by the date the website gives that authorised version: the day it is in force from. Each day's "
         "entries are credited to a `catalogue-<date>` record of the publisher, because the version list does not name the amending "
         "Act. Days after the retrieval date (30 October 2026) are on the `future` branch.")
limits = ("" + ("The Acts and statutory rules in force on the retrieval day are listed, and the repealed Acts and revoked statutory "
                 "rules the website lists (retrieved 31 October 2026); their pages give no repeal or revocation day, so a "
                 "repealed or revoked item's file stays at its last authorised version, labelled \"Repealed Act\" or "
                 "\"Revoked statutory rule\". Legislation as made is not listed." if sr and rp else
                "Only the Acts and statutory rules in force on the retrieval day are listed: repealed or revoked legislation and legislation as made are not." if sr else "Only the Acts in force on the retrieval day are listed: repealed Acts, Acts as made and statutory rules are not.") + " The first "
          "version listed for an Act is the oldest authorised version the website holds (often from the late 1990s), not the Act as "
          "enacted. Entries do not say which Act made each change. Nothing here is an official record or an authorised version.")
lic = """No law text is published. This repository holds metadata only.

Catalogue entries (Act title, act number, authorised version number and in-force date) are facts listed on the
Victorian legislation website (https://www.legislation.vic.gov.au) of the Office of the Chief Parliamentary Counsel,
Victoria. No text of any Act or web page is reproduced.

The "legal-system" facts come from Wikidata (https://www.wikidata.org), released under CC0 1.0.

The Government Printer for the State of Victoria owns copyright in all Victorian legislation. Authorised versions are
published on the Victorian legislation website under section 62 of the Interpretation of Legislation Act 1984 for
personal use only. They are not copied here. Copyright enquiries: Office of the Chief Parliamentary Counsel."""
L.write_docs(HERE, 'australia-victoria', 'AU-VIC', 'Victoria', rows, holds, source, dates, limits, lic, 'legislation.vic.gov.au')
print('docs written', nacts, 'acts', nver, 'versions', len(past), 'days', len(fut), 'future')
