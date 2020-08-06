import discord, youtube_dl, requests, os, random, wikipedia
from discord import Member
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('client is ready!')

# Member has joined a server
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server!')

# Member has left a server
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server...')

# Allows client to join a voice channel
@client.command()
async def join(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()

# Allows client to leave a voice channel
@client.command()
async def leave(ctx):
    if ctx.message.author.voice:
        server = ctx.message.guild.voice_client
        await server.disconnect()

# Allows the client to kick a user from the server
@client.command()
@commands.has_role('Admin')
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} was kicked!')

# Allows client to ban a user from the server
@client.command()
@commands.has_role('Admin')
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} was banned!')

# Allows client to unban a user from the server
@client.command()
@commands.has_role('Admin')
async def unban(ctx, *, user=None):
    try:
        user = await commands.converter.UserConverter().convert(ctx, user)
    except:
        await ctx.send("Error: user could not be found!")
        return

    try:
        bans = tuple(ban_entry.user for ban_entry in await ctx.guild.bans())
        if user in bans:
            await ctx.guild.unban(user, reason="Responsible moderator: " +
            str(ctx.author))
        else:
            await ctx.send("User not banned!")
            return

    except discord.Forbidden:
        await ctx.send("I do not have permission to unban!")
        return

    except:
        await ctx.send("Unbanning failed!")
        return

    await ctx.send(f'{user.mention} was unbanned!')

# Allows client to play audio from the YouTube video provided
@client.command(pass_context=True, brief="This will play a song 'play [url]'",
aliases=['pl'])
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current song to end " +
        "or use the 'leave' command.")
        return
    await ctx.send("Getting everything ready. Will play music soon...")
    print("Someone wants to play music! Let me get that ready for them...")
    voice = get(client.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, 'song.mp3')
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.volume = 100
    voice.is_playing()

# Returns user's ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

# Clears the most recent messages. Default amount is 5 but can be modified
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

# Simulates the Magic 8 Ball toy when the user asks a question
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes – definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Outlook good.',
        'Yes.',
        'Signs point to yes.',
        'Reply hazy, try again.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        "Don't count on it.",
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

# Searches the given term on Wikipedia and returns a summary from the top result
@client.command()
async def wiki(ctx, *, query):
    try:
        await ctx.send(wikipedia.summary(query))
    except Exception:
        await ctx.send("I can't find anything about " + query +
        ". Try another term.")

# Please reach out to me for the bot's token at ss5945@columbia.edu
client.run('Paste token here')
