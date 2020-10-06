#!/usr/bin/python -tt

from PayDayCalendar import PayDayCalendar
from datetime import datetime
import moondates

"""
    
    @Project:		CIG Payday Calendar
    @Author:		Garth Humphreys
    @Description:	Yearly CIG Payday Calendar
    @Created:		01/18/2013
    @Version:		1.0.1
    @Docs:			www.gov.ky
    
"""

def generatewebpage():
    pay_days, nowday = moondates.getpaylist()
#    nowday = (10, 10)
    current_year = datetime.today().year # get from today, the current year
    locale='ru_RU.utf8'
    c = PayDayCalendar(pay_days, nowday=nowday, locale=locale).formatyearpage(current_year, 4)
    print(locale)
    print(c)

if __name__ == '__main__':
    generatewebpage()