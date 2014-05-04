import cgi

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

# dict comprehensions
month_abbvs = dict((m[:3].lower(), m) for m in months)

# regular list comprehensions
month_list = [m for m in months]
# print month_abbvs


# everything we get from the webpage will be an str
#   so the first step should always be a conversion to the correct type
#       since the comparisons won't work properly


def valid_month(month):
    cap_month = month.capitalize()
    if cap_month in months:
        return cap_month

def valid_month_abbr(month):
    cap_month = month[:3].lower()
    if month_abbvs.get(cap_month):
        return cap_month

def valid_day(day):
    if day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return day

def valid_year(year):
    if year.isdigit():
        year = int(year)
        if year > 1900 and year < 2020:
            return year

# escape function
# checks each char in string and replaces it with an html-safe str char
def escape_html(s):
    new_str = ""
    chars = {'>': '&gt;', '<': '&lt;', '"': '&quot;', '&':'&amp;'}
    for c in s:
        if c in chars:
            new_str += chars[c]
        else:
            new_str += c
    return new_str

def cgi_escape_html(s):
    return cgi.escape(s, quote=True)