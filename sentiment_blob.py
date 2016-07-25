import json
import matplotlib.pyplot as plt
from six.moves import urllib
from textblob import TextBlob
import pandas as pd
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

pos=0
neg=0
neutral=0
eng=0

for i in range(len(tweets_data)):
   if tweets['lang'].loc[i]=='en':
      
      b = TextBlob(tweets['text'].loc[i])
         
      if b.sentiment.subjectivity>0.5: 
          print b
          eng+=1
          #print b.sentiment.subjectivity

          if b.sentiment.polarity > 0:
            print'pos: '+str(b.sentiment.polarity)
            pos+=1
          elif b.sentiment.polarity < 0:
            print'neg: '+str(b.sentiment.polarity)
            neg+=1
          elif b.sentiment.polarity ==0:
            print'neutral'
            neutral+=1
      #else:
           #print b
           #print 'OBJECTIVE'
          
print pos
print neutral
print neg
print 'English: '+str(eng)

labels='negative sentiment','neutral sentiment','positive sentiment'
posperc=(pos*1.00/(pos+neg+neutral))*100
negperc=(neg*1.00/(pos+neg+neutral))*100
neutperc=(neutral*1.00/(pos+neg+neutral))*100
sizes=[negperc,neutperc,posperc]
colors=['red','grey','green']
explode=(0.2,0,0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=60)
plt.axis('equal')


plt.show()
