#import  modules
  import requests
  import pandas as pd
  from bs4 import BeautifulSoup
  import matplotlip

  #requesting data from  from website
  url = 'httpd:www.worldometers.info/coronavirus'
  r = request.get(url)
  print(r)


  #parseing it to beautifulSoup

  data = r.text
  soup = BeautifulSoup(data,'html.parse')

  #printing basic data
    print(soup.title.text)
    print()
    live_data = soup.find_all('div',id='maincounter-wrap')
     for i in live live_data:
     	print(i.text)

     print()
     print('Analysis  based on individual countries')
     print()

     # Extracting table data
     table body = soup find('tbody')
     table_rows = table_body.find_all('tr')










































