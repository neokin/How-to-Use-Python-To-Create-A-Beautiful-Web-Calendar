import datetime
import ephem

def get_moon_dates(year, next_fn):
    start_of_year = ephem.Date(datetime.date(year, 1, 1))
    end_of_year = ephem.Date(datetime.date(year + 1, 1, 1))
    # print(f" start_of_year {start_of_year}")
    # print(f" end_of_year {end_of_year}")
    moon_dates_nf = []
    date = start_of_year

    while date < end_of_year:
        date = next_fn(date)
        date_and_time = date.datetime() + datetime.timedelta(hours=3)
        moon_dates_nf.append(date_and_time)
    return moon_dates_nf[:-1]


def getpaylist():
    todaynow = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
    #print(f"today = {todaynow}")
    todaynowtuple = (todaynow.month, todaynow.day)
    #print(f"{todaynowtuple=}")

    year = todaynow.year

    new_moon_dates = get_moon_dates(year, ephem.next_new_moon)
    full_moon_dates = get_moon_dates(year, ephem.next_full_moon)
    fq_moon_dates = get_moon_dates(year, ephem.next_first_quarter_moon)
    lq_moon_dates = get_moon_dates(year, ephem.next_last_quarter_moon)
    #print(f"{new_moon_dates=} \n{fq_moon_dates=}\n {full_moon_dates=} \n{lq_moon_dates=}")
    ltn = [(x.month, x.day) for x in new_moon_dates]
    ltfu = [(x.month, x.day) for x in full_moon_dates]
    ltfq = [(x.month, x.day) for x in fq_moon_dates]
    ltlq = [(x.month, x.day) for x in lq_moon_dates]

    cl = ltn+ltfu+ltfq+ltlq
    print(cl)
    return cl, todaynowtuple


getpaylist()