# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import os
from os import path
import numpy as np
from PIL import Image
import datetime
import matplotlib.pyplot as plt
import pyodbc

import time

sys.path.append(os.getcwd() + "/lib/wordcloud")
from wordcloud import WordCloud

con_str = (r'Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};'
           r'DBQ=/U/haikooking.accdb'
           )

conn = pyodbc.connect(con_str)
cur = conn.cursor()
for table_info in cur.tables(tabletype='TABLE'):
    print(table_info.table_name)

text = "初鳩,初花,初針,初春,初日,初日影,初飛行,初披講,初日の出,初雲雀,初富士,初冬,初風呂,初箒,初蛍,初参り,初松風,初神籤,初彌撒,春小袖," \
       "春炬燵,春寒,春雨,春芝居,春近し,春隣,春の馬,春の海,春の蚊,春の風,春の川,春の草,春の雲,春の暮,春の蟬,春の空,春の田,春の月,春の虹," \
       "春の野,春の日,春の服,春,2,3,春の星,はるのほし,春,2,3,春の水,はるのみず,春,2,3,春の山,はるのやま,春,2,3,春の闇,はるのやみ,春," \
       "2,3,春の雪,はるのゆき,春,2,3,春の夜,はるのよ,春,2,春の宵,はるのよい,2,3,春日傘,はるひがさ,春,2,3,春深し,はるふかし,春,2,3,春待つ," \
       "はるまつ,冬,2,春祭,はるまつり,春,2,春めく,はるめく,春,2,春休み,はるやすみ,春,2,春夕焼,はるゆうやけ,春,2,バレンタインデー," \
       "ばれんたいんでー,春,晩夏,ばんか,夏,晩菊,ばんぎく,秋,万愚節,ばんぐせつ,春,半夏,はんげ,夏,半夏生,はんげしょう,夏,パンジー,ぱんじー," \
       "春,晩秋,ばんしゅう,秋,晩春,ばんしゅん,春,半仙戯,はんせんぎ,春,晩霜,ばんそう,春,斑猫,はんみょう,夏,晩涼,ばんりょう,夏,万緑," \
       "ばんりょく,夏,日脚伸ぶ,ひあしのぶ,ビーチパラソル,びーちぱらそる,夏,ひひな,ひいな,春,柊,ひいらぎ,冬,麦酒,びーる,夏".encode('utf-8')
d = path.dirname(__file__)

start_day = datetime.date.today()

current_mask = np.array(Image.open(
    path.join(d, os.getcwd() + "/image/logo_mask.png")))
spring_mask = np.array(Image.open(
    path.join(d, os.getcwd() + "/image/spring-mask.png")))
newyear_mask = np.array(Image.open(
    path.join(d, os.getcwd() + "/image/newyear-mask.png")))
summer_mask = np.array(Image.open(
    path.join(d, os.getcwd() + "/image/summer-mask.png")))
autumn_mask = np.array(Image.open(
    path.join(d, os.getcwd() + "/image/autumn-mask.png")))
winter_mask = np.array(Image.open(
    path.join(d, os.getcwd() + "/image/winter-mask.png")))

while True:
    today = datetime.date.today()
    # if(today.day - start_day.day) % 7 == 0:
    wordcloud = WordCloud(background_color="lightcyan", mode="RGB", font_path="/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc",
                              mask=current_mask, width=450, height=450, colormap="gist_rainbow").generate(text.decode('utf-8'))
    wordcloud.to_file("./current_wordcloud.png")
    print("current_wordcloud was generated.")

    # if today.month in range(1, 4):
    wordcloud = WordCloud(background_color="palegreen", font_path="/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc",
                              mask=spring_mask, width=450, height=450, colormap="spring").generate(text.decode('utf-8'))
    wordcloud.to_file("./spring_wordcloud.png")
    print("spring_wordcloud was generated.")

    # if (today.month == 1) and (today.day in range(1, 3)):
    wordcloud = WordCloud(background_color="moccasin", font_path="/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc",
                              mask=newyear_mask, width=450, height=450, colormap="Reds").generate(text.decode('utf-8'))
    wordcloud.to_file("./newyear_wordcloud.png")
    print("newyear_wordcloud was generated.")

    # elif today.month in range(4, 7):
    wordcloud = WordCloud(background_color="paleturquoise", font_path="/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc",
                              mask=summer_mask, width=450, height=450, colormap="summer").generate(text.decode('utf-8'))
    wordcloud.to_file("./summer_wordcloud.png")
    print("summer_wordcloud was generated.")

    # elif today.month in range(7, 10):
    wordcloud = WordCloud(background_color="darkslategray", font_path="/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc",
                              mask=autumn_mask, width=450, height=450, colormap="autumn").generate(text.decode('utf-8'))
    autumn_coloring = np.array(Image.open(path.join(d, os.getcwd() + "/image/autumn-mask.png")))

    wordcloud.to_file("./autumn_wordcloud.png")
    print("autumn_wordcloud was generated.")

    # elif today.month in range(10, 13):
    wordcloud = WordCloud(background_color="midnightblue", font_path="/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc",
                              mask=winter_mask, width=450, height=450, colormap="PuBuGn").generate(text.decode('utf-8'))
    wordcloud.to_file("./winter_wordcloud.png")
    print("winter_wordcloud was generated.")

    # 色変更テスト
    # wordcloud = WordCloud(background_color="white", font_path="/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc",
    #                      mask=spring_mask, width=450, height=450).generate(text.decode('utf-8'))

    # spring_coloring = np.array(Image.open(path.join(d, os.getcwd() + "/image/spring-mask.png")))
    # image_colors = ImageColorGenerator(spring_coloring)

    # plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")

    # wordcloud.to_file("./spring_wordcloud.png")
    # print("spring_wordcloud was generated.")

    # time.sleep(86400)

