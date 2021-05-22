import requests
from bs4 import BeautifulSoup

def main():
    print("Input the URl:")
    url = 'https://www.imdb.com/title/tt0080684/'
    header = {'Accept-Language':'en-US,en;q=0.5'}
    q = requests.get(url=url,headers=header)
    if q:
        r = q.content
        soup = BeautifulSoup(r,'lxml')
        title_content = soup.find('h1',attrs={'class':'long'}).text.split(sep='(')[0][:-1]
        description = soup.find('div',class_='summary_text').text.strip()
        site_dict = {
            'title':title_content,
            'description':description,
        }
        print(site_dict)
    else:
        print('Invalid quote resource!')

if __name__ == '__main__':
    main()