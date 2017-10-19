# -*- coding:utf-8 -*-
'''
Created on 2017年10月19日

@author: jeff.yang
'''
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from scipy.misc import imread
from datetime import datetime

txt = 'test.txt'
imgmask = 'timg2.jpg'
t = datetime.now()
resimg = "word_" + txt.split('.')[0] + "_" + str(t.month) + str(t.day) + str(t.hour) + str(t.minute) + str(t.second) + ".jpg"

text = open(txt).read()
words = jieba.cut(text)
wordlist = ' '.join(words)

alice_color = imread(imgmask)
fwc = WordCloud(font_path='simfang.ttf', max_words=700, background_color='white', mask=alice_color, max_font_size=100, font_step=1).generate(wordlist)
imagecolor = ImageColorGenerator(alice_color)
plt.imshow(fwc.recolor(color_func=imagecolor))
plt.axis("off")
plt.show()
fwc.to_file(resimg)
