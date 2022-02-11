import praw

reddit = praw.Reddit(
    client_id="WfBi7pJ4J9LwUA",
    client_secret="ySGhjPD-jNXSwjwkp38jERqR6Jc",
    user_agent="linux:com.example.scra:v0.1 (by u/dvskarna)"
)

print(reddit.read_only)