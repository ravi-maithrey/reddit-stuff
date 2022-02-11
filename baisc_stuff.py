import praw


#giving only the three below creates a read-only instance
reddit = praw.Reddit("bot1")

for submission in reddit.subreddit("learnprogramming").new(limit=4):
    print(submission.title)