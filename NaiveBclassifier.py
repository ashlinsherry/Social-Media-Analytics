import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
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

 
def word_feats(words):
    return dict([(word, True) for word in words])
 
negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')
 
negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
 
negcutoff = len(negfeats)
poscutoff = len(posfeats)

print negcutoff
print poscutoff
 
trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
 
classifier = NaiveBayesClassifier.train(trainfeats)
pos=0
neg=0
neutral=0
eng=0

for i in range(len(tweets_data)):
   if tweets['lang'].loc[i]=='en':
      if TextBlob(tweets['text'].loc[i]).subjectivity>0.5:
          b = tweets['text'].loc[i]
          label= classifier.classify(word_feats(b.split()))
          print b
          eng+=1

          if label=='pos':
            print'pos'
            pos+=1
          elif label=='neg':
            print'neg'
            neg+=1
            
          
print pos
print neg
print 'English: '+str(eng)

labels='negative sentiment','positive sentiment'
posperc=(pos*1.00/(pos+neg))*100
negperc=(neg*1.00/(pos+neg))*100
sizes=[negperc,posperc]
colors=['red','green']
explode=(0.2,0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=60)
plt.axis('equal')


plt.show()
