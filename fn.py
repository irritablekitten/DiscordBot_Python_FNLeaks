# import libraries
# import pprint
import praw
import discord
import asyncio

client = discord.Client()

mods = ['FortniteLeaks', 'UppyGSY', 'FNLeak']
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')


def get_data():
    raw_data = []

    for submission in reddit.subreddit('fortniteleaks').hot(limit=25):
        # use pprint to see everything inside a submission object on the subreddit
        # pprint.pprint(vars(submission))
        for mod in mods:
            if submission.author.name == mod:
                raw_data.append(submission.url)

    return raw_data


def compare(log, data):
    results = []
    for url in data:
        if url not in log:
            results.append(url)

    return results


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


async def my_background_task():
    await client.wait_until_ready()
    log = []
    data = get_data()
    ch = client.get_channel(476951885622935573)
    async for message in ch.history(limit=100):
        log.append(message.content)
    results = compare(log, data)
    if results:
        for result in results:
            await ch.send(result)
    await asyncio.sleep(21600)


client.loop.create_task(my_background_task())
client.run('token')
