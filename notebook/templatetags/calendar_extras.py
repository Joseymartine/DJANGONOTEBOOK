import calendar
from django import template
from datetime import datetime

register = template.Library()

@register.filter
def make_calendar(date_str, _=None):
    """
    Given a date string 'YYYY-MM-01', return a list of weeks for the month,
    where each week is a list of days (integers or None for empty days).
    """
    year, month, _ = map(int, date_str.split('-'))
    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month)
    # Replace 0 with None for empty days
    return [[day if day != 0 else None for day in week] for week in month_days]
