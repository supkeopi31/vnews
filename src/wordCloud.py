# -*- coding: utf-8 -*-

from requests import get
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

newsURL = "https://www.yna.co.kr/view/AKR20221024073200017?input=1195m"

def wordCloud():
  f = open("news.txt", "r").read()

  wordCloud = WordCloud(
    font_path= "/Users/myosotis1089/Desktop/Noto_Sans_KR/NotoSansKR-Bold.otf",
    width=400,
    height=400,
    max_font_size=100,
    background_color="white",
    mask = np.array(Image.open("/Users/myosotis1089/Desktop/DRX.png"))
  ).generate_from_text(f)

  plt.figure()
  plt.imshow(wordCloud)
  plt.axis('off')
  plt.show()

def newsScrap(target):
  f = open("news.txt", "w", encoding="UTF-8")
  
  response = get(target)
  soup = BeautifulSoup(response.content, "html.parser")
  writings = soup.find_all('p')
  
  for writing in writings:
    f.writelines(writing.text)
  f.close()

def main():
  newsScrap(newsURL)
  wordCloud()

if __name__=="__main__":
  main()
