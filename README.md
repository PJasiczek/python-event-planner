# Event planner
> A simple Python console app for planning events — add, list, and remove events, and print a calendar for a given month. Built with the standard library only, no external dependencies.

## Features
- Add an event (name, date, time), with basic checks against duplicates and past dates
- Remove an event by its index in the list
- List upcoming saved events
- Print a calendar for a chosen month/year (`calendar.month()`)
- `Event` objects support comparison (`==`, `<`, `>`) via overloaded operators, so events can be checked and ordered by date

## Notes
- Events are kept in memory only — nothing is persisted between runs.
- The CLI menu text is in Polish.

## Run
```
python main.py
```
(no dependencies to install — `requirements.txt` is empty)

## Status
**Archived** — not actively maintained.

Written in 2019 as a small coursework project to practice core Python (classes, operator overloading, the `datetime`/`calendar` modules).
