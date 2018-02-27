# importing the module
import tweepy
 
# personal details
consumer_key ="U8tnRTs1PphsVbWjwrXz6yfwK"
consumer_secret ="NwwzXfFwnQkzMz86JxS4sFh4pGfK8Bfn1zqt8tjaYEcEo64Fvb"
access_token ="2989649799-FkC2d1YaqXkmb8ikKcYFYvu1lhFVGN0wiVCD9vc"
access_token_secret ="vM63wZomeC3zdoraJkePGoS7jHCSCxnhqDHjM7crmsvvU"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="Hello Everyone !")
