#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import pyglet

#Variables that contains the user credentials to access Twitter API 
access_token = "742213257453146114-iZlAt1vAj3iFq7fh48QuFhGXQu1CkdY"
access_token_secret = "Tt6f8nETMfFA15sy38XVv3OgO3Ctefx447GdlEsDwzMgE"
consumer_key = "LQ19MPaZuyBhB6RBE0Ai2NQvR"
consumer_secret = "ouu3QWNJWI9N3DSqACL0FXxVprUv8OBEvabbO2GiiaT2w0qRq1"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
  try: 
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['tesco','@Tesco','#tesco','#Tesco','Tesco'])
  except:
    music = pyglet.resource.media('Hero.mp3')
    music.play()

    def exiter(dt):
        pyglet.app.exit()
    
    pyglet.clock.schedule_once(exiter,30)
    pyglet.app.run()
