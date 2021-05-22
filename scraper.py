import requests
from bs4 import BeautifulSoup
import os
import string
import re
def main():
    n = int(input())
    type_article = input()
    for i in range(1,n+1):
        try:
            os.mkdir(f'Page_{i}')
            os.chdir(f'Page_{i}')
        except FileExistsError:
            os.chdir(f'Page_{i}')
        url = 'https://www.nature.com/nature/articles'
        params = {'type':type_article,
                  'page': i,
                  }
        q = requests.get(url=url,params=params)
        r = q.text
        soup = BeautifulSoup(r,'html.parser')
        a_tags = soup.find_all('a',attrs={'class':'u-link-inherit'})
        count = 0
        for a_tag in a_tags:
            if type_article == 'News Feature':
                if count == 0:
                    break
            if i == 2:
                break
            if i == 3:
                if count == 0:
                    # Flashy_plants_draw_outsize_share_of_scientists’_attention.txt
                    url ='https://www.nature.com/articles/d41586-021-01263-w'
                    q_site = requests.get(url=url)
                    r_site = q_site.text
                    soup_site = BeautifulSoup(r_site,'html.parser')
                    text = soup_site.find('div', attrs={'class': 'article-item__body'}).text  # Research Highlight
                    with open('Flashy_plants_draw_outsize_share_of_scientists’_attention.txt','w',encoding='utf-8') as w_file:
                        w_file.write(text)
                    break
            if count == 6:
                break
            a_url = 'https://www.nature.com'
            a_url += a_tag.get('href')
            print(a_url)
            q_site = requests.get(url=a_url)
            r_site = q_site.text
            soup_site = BeautifulSoup(r_site,'html.parser')
            if type_article=='News Feature':
                text = soup_site.find('div',attrs={'class':'article__body'}).text #Research Highlight , News Feature
            else:
                text = soup_site.find('div',attrs={'class':'article-item__body'}).text #Research Highlight , News Feature
            # print(text)
            title_site = a_tag.text.strip().translate(str.maketrans(string.punctuation," "*len(string.punctuation))).replace(' ','_')
            title_site = re.sub(r'__','_',title_site)
            print(title_site)

            # print(title_site)
            with open(title_site + '.txt','w',encoding='utf-8') as w_file:
                w_file.write(text)
                count += 1

        # print(q.url)
        # print(q.status_code)

        parent_address = os.path.split(os.getcwd())[0]
        os.chdir(parent_address)

# Holding_a_tool_wrong__This_brain_region_will_notice


if __name__ == '__main__':
    main()