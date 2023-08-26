import discord
import random
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def pwd(ctx):
    await ctx.send(gen_pass())

@bot.command()
async def guess(ctx):
    global guess_game

    guess_game = random.randint(1,10)
    await ctx.send("Guess a number between 1 and 10.")

@bot.command()
async def answer(ctx, number):
    if guess_game == int(number):
        await ctx.send("Correct!")
    else:
        await ctx.send("That's wrong, try again.")

bot.run("")
