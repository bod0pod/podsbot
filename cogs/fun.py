import discord
from discord.ext import commands
import random
import os

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog "fun.py" loaded.')

    # Commands

    @commands.command(aliases=['8ball', 'test'])
    async def _8ball(self, ctx, *, question):
        responses = [ "It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
                    "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
                    "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
                    "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                    "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]

        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
    
    @commands.command()
    async def flipcoin(self, ctx):
        coinSides = ['Heads', "Tails"]

        await ctx.send(f'{random.choice(coinSides)}')

    @commands.command()
    async def diceroll(self, ctx):
        outcomes = ['1', '2', '3', '4', '5', '6']

        await ctx.send(f'{random.choice(outcomes)}')

def setup(client):
    client.add_cog(Fun(client))