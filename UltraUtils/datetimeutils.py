from datetime import datetime, timedelta

def get_current_datetime(): return datetime.now()
def get_current_date(): return datetime.now().date()
def get_current_time(): return datetime.now().time()
def format_datetime(dt, fmt="%Y-%m-%d %H:%M:%S"): return dt.strftime(fmt)
def parse_datetime(dt_str, fmt="%Y-%m-%d %H:%M:%S"): return datetime.strptime(dt_str, fmt)
def add_days(dt, days): return dt + timedelta(days=days)
def subtract_days(dt, days): return dt - timedelta(days=days)
def get_weekday(dt): return dt.strftime("%A")
def get_days_difference(dt1, dt2): return abs((dt2 - dt1).days)
def is_leap_year(year): return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def get_month_name(month): import calendar; return calendar.month_name[month]
def get_day_of_year(dt): return dt.timetuple().tm_yday
