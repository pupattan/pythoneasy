import requests
from bs4 import BeautifulSoup
from random import randint


def get_random_image():
    """
    Get a random image from pixels.com
    :return:
    """
    try:
        headers = {"X-Requested-With": "XMLHttpRequest",
                   "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, "
                                 "like Gecko) Chrome/36.0.1985.125 Safari/537.36"}
        URL = 'https://www.pexels.com/search/computer/'
        response = requests.get(URL, headers=headers)

        # print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')

        photos_box = soup.find('div', attrs={'class': 'photos'})

        images = photos_box.find_all('img', {"class": "photo-item__img"})
        return images[randint(0, len(images))]['src']
    except Exception as e:
        print(e)
        return ''


if __name__ == "__main__":
    print(get_random_image())
