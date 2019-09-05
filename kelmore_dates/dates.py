from __future__ import annotations

from datetime import date as dates, datetime, timedelta
from typing import Optional, Type


class DatesCheck:

    @staticmethod
    def is_today(date: datetime) -> bool:
        return DateTools.today().now().date() == date.date()


class DatesCurrent:

    @staticmethod
    def day() -> str:
        return DateTools.today().strftime('%d')

    @staticmethod
    def month() -> str:
        return DateTools.today().strftime('%M')

    @staticmethod
    def year() -> str:
        return DateTools.today().strftime('%Y')


class DatesTransform:

    @staticmethod
    def date(date: datetime) -> dates:
        return date.date()

    @staticmethod
    def subtract(date: datetime, **kwargs) -> datetime:
        return date - timedelta(**kwargs)

    @staticmethod
    def subtract_days(date: datetime, days: int = 1) -> datetime:
        return DatesTransform.subtract(date, days=days)

    @staticmethod
    def to_date(date_string: str, format_string: str) -> datetime:
        return datetime.strptime(date_string, format_string)

    @staticmethod
    def to_seconds(date: datetime) -> float:
        """
        :param date: The datetime to be formatted
        :return: The number of seconds since the epoch for the datetime
        """
        epoch: datetime = datetime.utcfromtimestamp(0)
        return (date - epoch).total_seconds()

    @staticmethod
    def to_string(date: datetime, format_string: str) -> str:
        return date.strftime(format_string)


class DateTools:
    check: Type[DatesCheck] = DatesCheck
    current: Type[DatesCurrent] = DatesCurrent
    transform: Type[DatesTransform] = DatesTransform

    @staticmethod
    def today() -> datetime:
        return datetime.today()

    @staticmethod
    def yesterday() -> datetime:
        today: datetime = datetime.today()
        return DatesTransform.subtract_days(today)


class DatesCheckWrapper:
    _wrapper: DatesWrapper

    def __init__(self, wrapper: DatesWrapper):
        self._wrapper = wrapper

    def datetime(self):
        return self._wrapper.datetime

    def is_today(self) -> bool:
        return DatesCheck.is_today(self.datetime())


class DatesTransformWrapper:
    _wrapper: DatesWrapper

    def __init__(self, wrapper: DatesWrapper):
        self._wrapper = wrapper

    def datetime(self):
        return self._wrapper.datetime

    def subtract(self, **kwargs) -> DatesWrapper:
        return DatesWrapper(DatesTransform.subtract(self.datetime(), **kwargs))

    def subtract_days(self, days: int = 1) -> DatesWrapper:
        return DatesWrapper(DatesTransform.subtract_days(self.datetime(), days=days))

    def to_date(self) -> datetime:
        return DatesTransform.date(self.datetime())

    def to_seconds(self) -> float:
        return DatesTransform.to_seconds(self.datetime())

    def to_string(self, format_string) -> str:
        return DatesTransform.to_string(self.datetime(), format_string)


class DatesWrapper:
    datetime: datetime

    check: DatesCheckWrapper
    transform: DatesTransformWrapper

    def __init__(self, datetime_obj: Optional[datetime] = None):
        self.datetime = datetime_obj if datetime_obj else DateTools.today()

        self.check = DatesCheckWrapper(self)
        self.transform = DatesTransformWrapper(self)

    @staticmethod
    def from_string(date_string: str, format_string: str) -> DatesWrapper:
        formatted: datetime = DatesTransform.to_date(date_string, format_string)
        return DatesWrapper(datetime_obj=formatted)
