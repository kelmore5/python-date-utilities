# Dates

Dates is a small library of date utility functions compiled for personal needs. There's 
nothing too fancy nor anything you can't find from another library, but Dates consists of
smaller functions to be used rather than relying on larger packages.

The functions include things like current year/month/day, subtract days from datetime, to seconds,
and check if datetime is today.

## Personal Note

Dates is only on Github because I reference it in other projects. I don't have any plans 
to maintain this project, but I will update it from time to time. 

# Install

You can install this project directly from Github via:

```bash
$ pip3.7 install git+https://github.com/kelmore5/python-date-utilities.git
```

## Dependencies

- Python 3.7

# Usage

Once installed, you can import the main class like so:

    >>> from datetime import datetime
    >>> from kelmore_dates import DateTools as Dates
    >>>
    >>> x = datetime.today()                        # datetime.datetime(2019, 9, 5, 11, 26, 48, 0)
    >>>
    >>> Dates.today()                               # datetime.datetime(2019, 9, 5, 11, 26, 48, 0)
    >>> Dates.check.is_today(x)                     # True
    >>> Dates.current.day()                         # 05
    >>> Dates.current.year()                        # 2019
    >>> Dates.transform.subtract_days(x, days=3)    # datetime.datetime(2019, 9, 2, 11, 26, 48, 0)
    .
    .
    .

# Documentation

To be updated
