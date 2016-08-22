from datetime import date,time
import datetime
import calendar

date_text = "Sun 10 May 2015 13:54:36"
date_text2= "Sun 10 May 2015 13:54:31"

d1 = datetime.datetime.strptime(date_text, "%a %d %b %Y %X")
d2 = datetime.datetime.strptime(date_text2, "%a %d %b %Y %X")





