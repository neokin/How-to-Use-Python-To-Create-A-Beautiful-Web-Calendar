#!/usr/bin/python -tt

import sys
from calendar import LocaleHTMLCalendar

# Constants for months referenced later
January = 1

class PayDayCalendar(LocaleHTMLCalendar):
    def __init__(self, pay_days, nowday, locale):
            print(f"locale = {locale} !!!!!!" )
            super(PayDayCalendar, self).__init__()
            self.pay_days = pay_days # attach the list of paydays as a property, so we can access it anywhere
            self.nowday = nowday

    def formatday(self, day, weekday):
        pday = 0 # var for checking if it's a payday
        nday = 0# var for checking if it's a nowday

        cal_date = (self.month, day) # create a tuple of the calendar month and day

        
        if cal_date in self.pay_days: # check if current calendar tuple date exist in our list of pay days
            #print('cal_date: ', cal_date, ' day: ', day)
            pday = day # if it does exist set the pay day var with it

        if cal_date == self.nowday:
            print('now_date: ', cal_date, ' day: ', day)
            nday = day
        """
          Return a day as a table cell.
        """
        if day == 0:
            return '<td class="noday day">&nbsp;</td>' # day outside month
        elif day == pday and day == nday:
            return '<td class="%s npday day">%d</a></td>' % (self.cssclasses[weekday], day)
        elif day == pday: # check if this is one of the pay days, then change the class
            return '<td class="%s payday day">%d</a></td>' % (self.cssclasses[weekday], day)
        elif day == nday: # check if this is one of the pay days, then change the class
            return '<td class="%s nowday day">%d</a></td>' % (self.cssclasses[weekday], day)
        else:
            return '<td class="%s day">%d</td>' % (self.cssclasses[weekday], day)
    
    def formatweek(self, theweek):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd) for (d, wd) in theweek)
        return '<tr class="week">%s</tr>' % s
    
    def formatweekheader(self):
        """
        Return a header for a week as a table row.
        """
        s = ''.join(self.formatweekday(i) for i in self.iterweekdays())
        return '<tr class="weekheader">%s</tr>' % s
    
    # override in order to add the month as a property
    def formatmonth(self, theyear, themonth, withyear=True):
        self.month = themonth
        return super(PayDayCalendar, self).formatmonth(theyear, themonth, withyear=False)
    
    def formatyear(self, theyear, width=3):
        """
        Return a formatted year as a table of tables.
        """
        v = []
        a = v.append
        width = max(width, 1)
        a('<table border="0" cellpadding="0" cellspacing="0" id="calendar">')
        a('\n')
        a('<tr id="calendar-year"><th colspan="%d" class="year">Даты буддийских упосатх в %s году</th></tr>' % (width, theyear))
        a('<tr><th colspan="%d" class="year">Даты отображаются в соответствии с часовым поясом UTC+3 (МСК). <font color="#e8e80a">Жёлтым</font> цветом помечены все дни проведения упосатхи в текущем году. </th></tr>' % (width))
        a('<tr><th colspan="%d" class="year"><font color="red">Красным</font> - сегодняшний день. <font color="green">Зелёным</font> - если сегодняшний день совпадает с днём упосатхи и она проводится сегодня.</th></tr>' % (width))
        for i in range(January, January+12, width):
            # months in this row
            months = range(i, min(i+width, 13))
            a('<tr class="month-row">')
            for m in months:
                a('<td class="calendar-month">')
                a(self.formatmonth(theyear, m, withyear=False))
                a('</td>')
            a('</tr>')
        a('<tr><th colspan="%d" class="year">Чтобы получать уведомления о начале упосатхи, вы можете воспользоваться телеграм-ботом <a target="_blank" href="https://t.me/UposathaBot">@UposathaBot</a></th></tr>' % (width))
        a('</table>')
        return ''.join(v)
    
    def formatyearpage(self, theyear, width=3, css="{{ url_for('static', filename='calendar.css')}}", encoding=None):
        """
        Return a formatted year as a complete HTML page.
        """
        if encoding is None:
            encoding = sys.getdefaultencoding()
        v = []
        a = v.append
        a('<?xml version="1.0" encoding="%s"?>\n' % encoding)
        a('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n')
        a('<html>\n')
        a('<head>\n')
        a('<meta http-equiv="Content-Type" content="text/html; charset=%s" />\n' % encoding)
        if css is not None:
            a('<link rel="stylesheet" type="text/css" href="%s" />\n' % css)
        a('<title>Даты буддийских упосатх для %d года</title>\n' % theyear)
        a('</head>\n')
        a('<body>\n')
        a('<div id="wrapper">\n')
        a(self.formatyear(theyear, width))
        a('</div>\n')
        a('</body>\n')
        a('</html>\n')
        
        # output the HTML to a webpage
        file = open('templates/index.html', 'wb')
        file.write(''.join(v).encode(encoding, "xmlcharrefreplace"))
        file.close()
        
        return 'Buddhists uposathas webpage generated'
