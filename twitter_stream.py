#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
#retiradas de apps.twitter.com
#Aplicaco Self-Service Study

access_token = "78308928-aOpEscYyFfXYysTGJ6oXtuglSnypWDR1r0QjXQJYA"
access_token_secret = "Er54hP2V08kYTYyL3aOzZiMx2zOA5JTv7y6yLX5F1csBg"
consumer_key = "FGeq3xl3dffj8j4rhYmKXootw"
consumer_secret = "waDj0QuuOqkgtdrIaEzC57Uej0dlg1I41uuq7otFs34b0rPiwH"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'Eduardo Cunha'
    stream.filter(track=['Eduardo Cunha'])
