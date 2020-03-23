import tweepy
from textblob import TextBlob
import csv
import matplotlib.pyplot as plt

#Authenticate
consumer_key= '1ABX3f53bqw7wX6XiWTRTpTln'
consumer_secret= 'QoFb2NU2LKn7MnCSCtpkVjkUG3RUqmL9RPrCxozesSO3kXO4Xd'

access_token='1130723592088559616-gCV58YpXMY4AIxcB4WsZQ9H12I7hDS'
access_token_secret='a27yaEB30gs12TnmCRhC3qXUwJ9SY1Mlbr6I1PpYJiY3I'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

c = input("Enter the coordinates of the area you want the tweets to be focused on (Type in 20.5937,78.9629 for India , Enter 'n' for worldwide tweets) : ")


api = tweepy.API(auth)

#Retrieve Tweets
if c == 'n':
	public_tweets = api.search('covid' ,lang = 'en',result_type = 'recent')
else :
	c = c + ",50000km"
	public_tweets = api.search('covid' ,lang = 'en',result_type = 'recent' , geocode = c)

cp = 0 #positive tweets count
cn = 0 #negative "        "
cnu = 0#neutral   "		   "


with open('tweets.csv', 'w') as file:
    writer = csv.writer(file)
    tweets = []
    for tweet in public_tweets:
    	
    	analysis = TextBlob(tweet.text)
    	if analysis.sentiment.polarity>0:
    		tone = 'Sentiment: positive'
    		cp+=1
    	elif analysis.sentiment.polarity == 0:
    		tone = 'Sentiment: neutral'
    		cnu+=1
    	else:
    		tone = 'Sentiment: negative'
    		cn+=1
    	tweets.append([tweet.text])
    	tweets.append([tone])
    	tweets.append(["_________________________________________________________________________"])
    for i in tweets:
    	writer.writerow(i)

# Data to plot
labels = 'Positive', 'Negative', 'Neutral'
sizes = [cp , cn , cnu]
colors = ['blue', 'red', 'lightcoral']
explode = (0.1, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.title("The Sentiments of the people in India about COVID-19 on Twitter")
plt.show()
# for tweet in public_tweets:
#     print(tweet.text)
    
#     #Step 4 Perform Sentiment Analysis on Tweets
#     analysis = TextBlob(tweet.text)
#     if analysis.sentiment.polarity>0:
#     	tone = 'positive'
#     elif analysis.sentiment.polarity == 0:
#     	tone = 'neutral'
#     else:
#     	tone = 'negative'
#     print("The sentiment analysis of this tweet is: " + tone)
#     print("__________________________________________________________")

