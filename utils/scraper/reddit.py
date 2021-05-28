import praw

# fill in your reddit stuff here.
reddit = praw.Reddit(client_id='',
					 client_secret='', 
					 user_agent='',
					 username='')

def scrap(sub):
	subreddit = reddit.subreddit(sub)
	meme = subreddit.random()
	return meme.url, meme.author, meme.permalink

