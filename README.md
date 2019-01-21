# fnleaksbot
Discord bot (Python) to post Fortnite cosmetic leaks from /r/FortniteLeaks using PRAW

Gathers subreddit posts and checks Discord chat channel for existing content before posting new leaks

If you want to run your own bot, be sure to get Reddit API credentials to use here: 

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')

and a Discord app token:

client.run('your_token_here')