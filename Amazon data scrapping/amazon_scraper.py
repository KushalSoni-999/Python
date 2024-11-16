import csv
import  os
import json
import requests
import time
import pandas as pd
from datetime import datetime
import bs4 as bs

def get_data(*args):
    url_list = list(args)
    for url in url_list:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        response = requests.get(url , headers=headers)
        soup = bs.BeautifulSoup(response.text, 'html.parser')
        # print(soup.prettify())
        if 'amazon' in url:
            title = soup.find(id='productTitle').get_text().strip()
            site = 'Amazon'
            date = datetime.now().date()
            time = datetime.now().time().strftime('%H:%M:%S')
            price = soup.find('span' , class_='a-price-whole').text.strip()
            emi = soup.find('span', class_='a-hidden').text
        else:
            title = soup.find('span' , class_='VU-ZEz').text.strip()
            site = 'Flipkart'
            date = datetime.now().date()
            time = datetime.now().time().strftime('%H:%M:%S')
            price = soup.find('div' , class_='Nx9bqj CxhGGd').text.strip()
            emi = soup.find('span', class_='+-2B3d row').text
        print(f'title: {title} \ndate: {date} \ntime: {time} \nprice: {price} \nemi: {emi}')
        yield title,site,date,time,price,emi

def make_xlsx(file):
    if not os.path.exists(file):
        df = pd.DataFrame(columns=['Title' ,'Site', 'Date', 'Time', 'Price', 'Emi'])
        df.to_excel(file, index=False)
    else:
        print('File already exists')

def append_to_xlsx(file,data_gen):
    df1 = pd.read_excel(file)
    for data in data_gen: 
        df2 = pd.DataFrame([data] , columns=['Title' ,'Site', 'Date', 'Time', 'Price', 'Emi'])
        df_combined = pd.concat([df1, df2], ignore_index=True)
        df1 = df_combined
        print(f'df_combined: {df_combined}')
    df1.to_excel(file, index=False)    

def main():
    url_list = ['https://www.amazon.in/Lenovo-IdeaPad-i7-13620H-38-1cm-83EM008GIN/dp/B0D6NCVQZQ' ,
                'https://www.flipkart.com/lenovo-ideapad-slim-5-wuxga-ips-ai-pc-intel-core-ultra-125h-16-gb-512-gb-ssd-windows-11-home-14imh9-thin-light-laptop/p/itm05b18e8ca334f?pid=COMHYXV9PVH3CHZY&lid=LSTCOMHYXV9PVH3CHZYNLNSHT&marketplace=FLIPKART&q=ideapad+slim+5&store=6bo%2Fb5g&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_2_8_sc_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_8_sc_na_na&fm=organic&iid=fff4d893-961c-4bc4-a97a-458cf96ec446.COMHYXV9PVH3CHZY.SEARCH&ppt=hp&ppn=homepage&ssid=i6niw5rj5s0000001726744379986&qH=e4df4d9e9c359fdd',
                'https://www.amazon.in/Lenovo-IdeaPad-i7-13620H-38-1cm-83EM008GIN/dp/B0D6NCVQZQ' , 
                'https://www.amazon.in/ASUS-Vivobook-i9-13900H-Fingerprint-X1605VA-MB946WS/dp/B0CHMYJ9BK']
    file_path = 'C:/Users/sonik/python/projects/Amazon data scrapping/laptops.xlsx'
    # get_data(url)
    make_xlsx(f'{file_path}')
    while True:
        append_to_xlsx(file_path, get_data(*url_list))
        time.sleep(10) # For 1 day timer change 10 to 86400

if __name__ == '__main__':
    main()
