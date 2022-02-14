import praw


#taking input from a local praw.ini file
reddit = praw.Reddit("bot1")

for submission in reddit.subreddit("learnprogramming").new(limit=1):
    submission.reply("You can easily google that")