import requests
from bs4 import BeautifulSoup
import os
import time

def get_html(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    r = requests.get(url,timeout=(5, 3))
    if r.status_code == 200:
        soup = BeautifulSoup(r.text,'html.parser')
        return soup
    else:
        print(f"Error:{r.status_code}")
        return None

count = 0
def get_list_link(url,link_list):
    global count
    soup = get_html(url)
    try:
        try:
            get_link_of_arrow = soup.find_all('a', attrs={'class': 'kf-tLbr-4923d'})[1].get('href')
        except:
            get_link_of_arrow = soup.find('a', attrs={'class': 'kf-tLbr-4923d'}).get('href')
        new_url = 'https://re.kufar.by' + get_link_of_arrow
        if new_url in link_list:
            return link_list
        link_list.append(new_url)
        count += 1
        return get_list_link(new_url,link_list)
    except:
        return link_list

def main():
    url = "https://re.kufar.by/l/minsk/snyat/komnatu-dolgosrochno/1-k?cur=USD&prc=r%3A0%2C120"
    list_link = []
    try:
        with open('link.txt','r',newline='\n',encoding='utf-8') as r_file:
            for line in r_file:
                list_link.append(line)
    except FileNotFoundError:
        list_link = get_list_link(url,list_link)
        with open('link.txt','w',encoding='utf-8') as w_file:
            for line in list_link:
                w_file.write(line)
                w_file.write('\n')
    list_link.insert(0,url)
    print(len(list_link))
    global count
    count = 0
    with open('offers.html','w',encoding='utf-8') as w_file:
        head_html = """
        <!DOCTYPE html>
        <html>
         <head>
          <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
          <link rel="stylesheet" href="https://content.kufar.by/static/kufar-fe-realty/_next/static/css/d04794759ccf6eb8f01d5c20a6b03e56b0a9d18c_CSS.c9eb0dff.chunk.css"/>
            <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,900" rel="stylesheet"/>
            <link rel="stylesheet" href="https://content.kufar.by/static/kufar-fe-realty/_next/static/css/5c42c3598a1de5b3d847a710e95e92fcde9575c2_CSS.0c85f4e3.chunk.css"/>
            <link rel="stylesheet" href="https://content.kufar.by/static/kufar-fe-realty/_next/static/css/static/v9w87N45IEip4wOaE56dc/pages/_app.js.c29897a3.chunk.css"/>
            <link rel="stylesheet" href="https://content.kufar.by/static/kufar-fe-realty/_next/static/css/40ce7e15e4e1055701dc93e289515c0071dcd966_CSS.5c644419.chunk.css"/>
            <link rel="stylesheet" href="https://content.kufar.by/static/kufar-fe-realty/_next/static/css/47292896456333888cfd031f7f5cb361f1aae1ec_CSS.ccc050d8.chunk.css"/>
            <link rel="stylesheet" href="https://content.kufar.by/static/kufar-fe-realty/_next/static/css/static/v9w87N45IEip4wOaE56dc/pages/listings.js.a38ab0a4.chunk.css"/>
            <link rel="stylesheet" href="domovit.css">
          <title>Пример веб-страницы</title>
         </head>
         <body>
         <main style="display:flex;flex-direction:row;justify-content:space-between;">
         <div class="kufar_me" style="width:50%;">
        """
        w_file.write(head_html)
        for i in list_link:
            time.sleep(5)
            print(count)
            print(i)
            soup = get_html(i)
            block_flats = soup.find('div',attrs={'class':'kf-nmx-82b2d'})
            # flats = soup.find_all('a',attrs={'class':'kf-nNVZ-61772'})
            # if flats is None:
            #     flats = soup.find_all('a',attrs={'class':'kf-nNVZ-61772'})
            # print(flats)
            count += 1
            # for flat in flats:
            #     w_file.write(flat.prettify())
            w_file.write(block_flats.prettify())
            if block_flats:
                print('done!')
            else:
                print("wrong!")
        w_file.write("""
        </div> 
        <div id="kufar_me" style="width:50%;">
        """)
        for i in range(5):
            soup = get_html(f'https://domovita.by/minsk/room/rent?price%5Bmin%5D=&price%5Bmax%5D=120&price_type=all_usd&page={i}')
            flats = soup.find_all('a',attrs={'class':'ORoomRent'})
            for flat in flats:
                w_file.write("<div class>"+flat.prettify()+"</div>")
            print("done!")
        w_file.write(
        """
        </div> 
        </main>  
        </body>
        </html>
        """)

if __name__ == '__main__':
    main()