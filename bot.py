# Setup

import discord
from discord.ext import commands
import random
import os
import json

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

        return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix, intents=intents)

client.remove_command('help')

staff = ['mod', 'admin', 'owner']

# Logs and checking

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Pod's Bot | ;help"))
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = ';'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

# Cogs

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# Help

@client.command(pass_context=True)
async def help(ctx):
    embed=discord.Embed(title="Help Page", url="https://github.com/bod0pod/podsbot/blob/master/README.md", description="README.md", color=0x3df2ff)
    embed.set_author(name="Pod's Bot", url="https://steamcommunity.com/id/bodopod/", icon_url="https://i.imgur.com/dYTTMNc.png")
    embed.set_thumbnail(url="https://i.imgur.com/e8czNzi.png")
    embed.set_footer(text="Developed by Bodopod")
    await ctx.send(embed=embed)

# Commands

@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix has been changed')

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command()
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)

@client.command()
async def avatar(ctx, *, member : discord.Member=None):
    if not member:
        member = ctx.message.author
    
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)

@client.command()
async def invite(ctx):
    await ctx.send('https://discord.com/oauth2/authorize?client_id=773889464094556160&permissions=8&scope=bot')
    
# Token

f = open('token.txt', 'r')

token = f.read()

client.run(token)

f.close()