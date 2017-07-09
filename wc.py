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
import time

sys.path.append(os.getcwd() + "/lib/wordcloud")

from wordcloud import WordCloud

text = "初鳩,はつばと,新,初花,はつはな,新,初針,はつはり,新,初春,はつはる,新,初日,はつひ,新,初日影,はつひかげ,新,初飛行,はつひこう,新," \
       "初披講,はつひこう,新,初日の出,はつひので,新,初雲雀,はつひばり,春,初富士,はつふじ,新,初冬,はつふゆ,冬,初風呂,はつぶろ,新,初箒," \
       "はつぼうき,新,初蛍,はつぼたる,夏,初参り,はつまいり,新,初松風,はつまつかぜ,新,初神籤,はつみくじ,新,初彌撒,はつみさ,新,春小袖," \
       "はるこそで,新,2,春炬燵,はるごたつ,春,2,春寒,はるさむ,春,2,春雨,はるさめ,春,春芝居,はるしばい,新,2,春近し,はるちかし,新,2,春隣," \
       "はるどなり,冬,2,春の馬,はるのうま,春,2,3,春の海,はるのうみ,春,2,3,春の蚊,はるのか,春,2,春の風,はるのかぜ,春,2,3,春の川," \
       "はるのかわ,春,2,3,春の草,はるのくさ,春,2,3,春の雲,はるのくも,春,2,3,春の暮,はるのくれ,春,2,3,春の蟬,はるのせみ,春,2,3,春の空," \
       "はるのそら,春,2,3,春の田,はるのた,春,2,春の月,はるのつき,春,2,3,春の虹,はるのにじ,春,2,3,春の野,はるのの,春,2,春の日,はるのひ," \
       "春,2,春の服,はるのふく,春,2,3,春の星,はるのほし,春,2,3,春の水,はるのみず,春,2,3,春の山,はるのやま,春,2,3,春の闇,はるのやみ,春," \
       "2,3,春の雪,はるのゆき,春,2,3,春の夜,はるのよ,春,2,春の宵,はるのよい,2,3,春日傘,はるひがさ,春,2,3,春深し,はるふかし,春,2,3,春待つ," \
       "はるまつ,冬,2,春祭,はるまつり,春,2,春めく,はるめく,春,2,春休み,はるやすみ,春,2,春夕焼,はるゆうやけ,春,2,バレンタインデー," \
       "ばれんたいんでー,春,晩夏,ばんか,夏,晩菊,ばんぎく,秋,万愚節,ばんぐせつ,春,半夏,はんげ,夏,半夏生,はんげしょう,夏,パンジー,ぱんじー," \
       "春,晩秋,ばんしゅう,秋,晩春,ばんしゅん,春,半仙戯,はんせんぎ,春,晩霜,ばんそう,春,斑猫,はんみょう,夏,晩涼,ばんりょう,夏,万緑," \
       "ばんりょく,夏,日脚伸ぶ,ひあしのぶ,冬,1,3,ビーチパラソル,びーちぱらそる,夏,ひひな,ひいな,春,柊,ひいらぎ,冬,麦酒,びーる,夏".encode('utf-8')
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
    if(today.day - start_day.day) % 7 == 0:
        wordcloud = WordCloud(background_color="white", font_path="/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc",
                              mask=current_mask, width=450, height=450).generate(text.decode('utf-8'))
        wordcloud.to_file("./current_wordcloud.png")
        print("current_wordcloud was generated.")

    if today.month in range(1, 4):
        wordcloud = WordCloud(background_color="white", font_path="/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc",
                              mask=spring_mask, width=450, height=450).generate(text.decode('utf-8'))
        wordcloud.to_file("./spring_wordcloud.png")
        print("spring_wordcloud was generated.")

    if (today.month == 1) and (today.day in range(1, 3)):
        wordcloud = WordCloud(background_color="white", font_path="/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc",
                              mask=newyear_mask, width=450, height=450).generate(text.decode('utf-8'))
        wordcloud.to_file("./newyear_wordcloud.png")
        print("newyear_wordcloud was generated.")

    elif today.month in range(4, 7):
        wordcloud = WordCloud(background_color="white", font_path="/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc",
                              mask=summer_mask, width=450, height=450).generate(text.decode('utf-8'))
        wordcloud.to_file("./summer_wordcloud.png")
        print("summer_wordcloud was generated.")

    elif today.month in range(7, 10):
        wordcloud = WordCloud(background_color="white", font_path="/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc",
                              mask=autumn_mask, width=450, height=450).generate(text.decode('utf-8'))
        wordcloud.to_file("./autumn_wordcloud.png")
        print("autumn_wordcloud was generated.")

    elif today.month in range(10, 13):
        wordcloud = WordCloud(background_color="white", font_path="/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc",
                              mask=winter_mask, width=450, height=450).generate(text.decode('utf-8'))
        wordcloud.to_file("./winter_wordcloud.png")
        print("winter_wordcloud was generated.")

    time.sleep(60)
