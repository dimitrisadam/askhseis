import tweepy
from tweepy import OAuthHandler
import sys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#pairnei thn lista me ta tweets (sunolika 10).Ta bazei ta epejergazetai ena ena
#afairwntas ta https-links ka8ws den einai lejeis kai lejeis pou periexoun mesa ton xarakthra
# '\' ka8ws upodikniei oti einai photografia.Epishs afairei memonomenes paules kai dipla kena.
#Telos, epistrefei to a8roisma twn lejewn pou metrhse sta tweets.
def countWords(alltweets):
	httpFlag = "http"
	delimeter = "\\"
	paula="-"
	doublespace=""
	totalWords = 0
	test =" "
	for i in range(len(alltweets)):
		test = str(alltweets[i])
		test = test.split(" ")
		for j in range(len(test)):
			if delimeter not in test[j] and httpFlag not in test[j] and test[j] is not paula and test[j] is not doublespace:
				totalWords+=1
				#print test[j]
	return totalWords

firstUser  = raw_input("Dwste to tweeter username tou prwtou xrhsth: \n")
secondUser = raw_input("Dwste to tweeter username tou deuterou xrhsth: \n")

#firstUserTweets = api.user_timeline(screen_name="RollingStones",count=10)

#edw diavazw kai vazei sto firsttweets ta 10 pio prosfata tweets tou prwtou user
firstUserTweets = api.user_timeline(screen_name=firstUser,count=10)
firsttweets = [[tweet.text.encode('utf-8')] for tweet in firstUserTweets]
#print firsttweets

#secondUserTweets = api.user_timeline(screen_name="rogerfederer",count=10)
#edw diavazw kai vazei sto secondtweets ta 10 pio prosfata tweets tou deuterou user
secondUserTweets = api.user_timeline(screen_name=secondUser,count=10)
secondtweets = [[tweet.text.encode('utf-8')] for tweet in secondUserTweets]
#print secondtweets

# Elegxos gia an exoun ginei ta 10 tweets. An oxi to afhnw na sunexisei 8a borousa omws na kanw kai ena sys.exit(0)
if len(firsttweets) < 10:
	print '\nWARNING: O xrhsths',firstUser,'den exei kanei 10 tweets'
if len(secondtweets) < 10:
	print '\nWARNING: O xrhsths',secondUser,'den exei kanei 10 tweets'


firstUserTotalWorlds = countWords(firsttweets)
secondUserTolalWorlds = countWords(secondtweets)

if firstUserTotalWorlds > secondUserTolalWorlds:
	print '\nPerissoteres lexeis exei o user',firstUser,'pou exei',firstUserTotalWorlds,'lexeis.O user',secondUser,'exei',secondUserTolalWorlds,'lexeis'
else:
	print '\nPerissoteres lexeis exei o user',secondUser,'pou exei',secondUserTolalWorlds,'lexeis.O user',firstUser,'exei',firstUserTotalWorlds,'lexeis'	

#print 'totalwords =',countWords(firsttweets)
#print 'totalwords =',countWords(secondtweets)