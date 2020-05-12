import tweepy
import time

print('this is my twitter bot')

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Create API object
api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'


def retrieve_last_seen(file_name):
    f_read = open(file_name, 'r')
    last_seen = int(f_read.read().strip())
    f_read.close()
    return last_seen


def store_last_seen(last_seen, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen))
    f_write.close()
    return


def reply_tweets():
    print('retrieving.....')
    last_seen = retrieve_last_seen(FILE_NAME)
    mentions = api.mentions_timeline(last_seen, tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' ' + mention.full_text)
        last_seen = mention.id
        store_last_seen(last_seen, FILE_NAME)
        if '#hello' in mention.full_text.lower():
            print('found')
            print('responding.......')
            api.update_status('@' + mention.user.screen_name + ' ' + 'Hello, how are you doing?', mention.id)
        else:
            print('not found')


while True:
    reply_tweets()
    time.sleep(20)
