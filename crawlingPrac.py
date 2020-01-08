import urllib.request, urllib.error
from bs4 import BeautifulSoup
import time

def get_html(url):
    _html = ""
    _open = urllib.request.urlopen(url)
    resp = _open.read().decode('utf-8')

    if _open.status == 200:
        _html = resp
        return _html


def main():
    while True:
        URL = 'https://www.daum.net'
        title_list = []

        html = get_html(URL)
        soup = BeautifulSoup(html, 'html.parser')
        realtime_hotissue = soup.find('div', {'class':'realtime_part'}).find({'h4'}) 
        rank_count_title = soup.find('div', {'class':'realtime_part'}).find_all({'a':'link_issue'})

        for line in rank_count_title:
            title_list.append(line.text)

        title_list = list(set(title_list))

        print(realtime_hotissue.text,"\n")
        for i in range(len(title_list)):
            print(f"{i+1}위 {title_list[i]}")
        time.sleep(10)
if __name__ == '__main__':
    main()