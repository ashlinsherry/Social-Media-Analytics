import json
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import re
import string
from PIL import Image
import numpy as np
from os import path
text="";
tweets_data_path = 'C:\Users\Ash\Desktop\PyScript\\twtes.txt'

tweets_data = []
tweets_file = open(tweets_data_path,"r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue


print len(tweets_data)

tweets = pd.DataFrame()
tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)

for i in range(len(tweets_data)):
   if tweets['lang'].loc[i]=='en':
         text += tweets['text'].loc[i]

str1=""
text2=TextBlob(text)
for word, pos in text2.tags:
    if pos=='JJ' and word.isalpha():
       check=word.spellcheck()
       if [x[1] for x in check] == [1.0]:
          str1 += word
          str1 += " "
      
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

alice_mask = np.array(Image.open("cloud.png"))
STOPWORDS.add("rt")


wc = WordCloud(background_color="white", max_words=100, mask=alice_mask,
               stopwords=STOPWORDS.add("https"),relative_scaling=0.5)
# generate word cloud
wc.generate(str1)


# show
plt.imshow(wc)
plt.axis("off")
plt.show()
