import urllib
from bs4 import BeautifulSoup
from datetime import datetime

#date_in=raw_input('input date_in: ')
#date_outraw_input('input date_in: ')

date=datetime.strftime(datetime.now(), "%Y-%m")
month=datetime.strftime(datetime.now(), "%m")
start_namber=datetime.strftime(datetime.now(), "%d")

if month==['01','03','05','07','08','10','12']:
    monthday=range(int(start_namber), 31, 2)

if month==['04','06','09','11']:
    monthday=range(int(start_namber), 30, 2)

site='https://www.booking.com'

url='https://www.booking.com/searchresults.ru.html?;checkin_monthday=1&checkin_year_month=2018-04&checkout_monthday=3&checkout_year_month=2018-04&dest_id=253102&dest_type=landmark&from_history=1&group_adults=2&group_children=0&no_rooms=1&radius=10&si=ad&si=ai&si=ci&si=co&si=di&si=la&si=re&;sh_position=1'



#a=urllib.urlopen(url).read()
#soup=BeautifulSoup(a)
#print a

f=open('1.txt', 'r')
#f.write(a)
#f.close()

soup = BeautifulSoup(f)
divs=soup.find('div', class_='results-paging')
link=divs.find_all('a', class_='sr_pagination_link')[-1].get('href')
list=link.split('=')
nb=len(list)
pages=int(list[nb-1])
for i in range(0,pages+15,15):

    print i




def get_hotel_links(f):
    soup = BeautifulSoup(f)
    a_hotel=soup.find('div', id='hotellist_inner').find_all('h3', class_='sr-hotel__title')    #('a', class_="hotel_name_link url")
    hotel_links=[]
    for h3 in a_hotel:
        b=h3.find('a', class_='hotel_name_link url').get('href')
        b=b.lstrip().rstrip('#hotelTmpl').rstrip()
        #b=b.lstrip().rstrip()
        #b=b.rstrip()
        link=site+b
        hotel_links.append(link)

    #print hotel_links

#get_hotel_links(f)
