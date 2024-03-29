import datetime
import json
import random
import time

import log
import help
import os
import discord
import requests
import logging
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()

COMMAND_PREFIX=os.getenv("COMMAND_PREFIX")
DISCORD_TOKEN=os.getenv("DISCORD_TOKEN")
GOLD_API_TOKEN=os.getenv("GOLD_API_TOKEN")
OIL_API_TOKEN=os.getenv("OIL_API_TOKEN")


def get_discord_token():
    with open('config.json') as json_file:
        data = json.load(json_file)
        return data["discord_token"]


def get_gold_api_token():
    with open('config.json') as json_file:
        data = json.load(json_file)
        return data["gold_api_token"]


def get_oil_api_token():
    with open('config.json') as json_file:
        data = json.load(json_file)
        return data["oil_api_token"]


def get_prefix():
    with open('config.json') as json_file:
        data = json.load(json_file)
        return data["command_prefix"]


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=get_prefix(), intents=intents)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(name="les TCOM 2024", type=discord.ActivityType.watching))
    log.info("Logged in as " + bot.user.name)
    # Displaying all the guilds the bot is connected to
    for guild in bot.guilds:
        log.info("Connected to: " + guild.name)


@bot.command(description="Returns pong and the time taken to anwser !")
async def ping(context):
    await context.send(":ping_pong: Pong !")


@bot.command(description="Returns the current gold price, the euro/dollar conversion and the price of an oil barrel")
async def stephan(context):
    msg = await context.send("Récupération des données, veuillez patienter...")
    # Code pour récupérer le pris de l'or en dollar
    headers = {
        'x-access-token': get_gold_api_token(),
    }
    response_gold = requests.get('https://www.goldapi.io/api/XAU/USD', headers=headers)
    gold_price = json.loads(response_gold.text)['price']

    # Code pour récupérer le taux de conversion euro/dollar
    response_rate = requests.get('https://api.exchangerate-api.com/v4/latest/EUR')
    data = json.loads(response_rate.text)
    euro_to_dollar = data['rates']['USD']

    # Code pour récupérer le prix du BRENT
    response_oil = requests.get('https://www.quandl.com/api/v3/datasets/CHRIS/ICE_B1.json', params={
        'api_key': get_oil_api_token(),
    })
    data_oil = json.loads(response_oil.text)
    oil_price = data_oil['dataset']['data'][0][1]

    await msg.delete()
    await context.send(f"Cours de l'or: {str(gold_price)}\nPrix BRENT: {oil_price}$\n1€ = {euro_to_dollar}$")


@bot.command(description="Monsieur Gaillard")
async def gaillard(context):
    quotesGaillard = open("quotesGaillard.txt", "r", encoding="utf8")
    temp = quotesGaillard.read().split('\n')

    await context.send(random.choice(temp) + " - Gaillard <:gigaillard:1091265756395753492>")


@bot.command(description="Monsieur Michaux")
async def michaux(context):
    quotesMichaux = open("quotesMichaux.txt", "r", encoding="utf8")
    temp = quotesMichaux.read().split('\n')

    await context.send(random.choice(temp) + " - Michaux <:sleeping_michaux:1063746563366727740>")


@bot.command(description="Monsieur Bourbon")
async def michaux(context):
    quotesMichaux = open("quotesBourbon.txt", "r", encoding="utf8")
    temp = quotesMichaux.read().split('\n')

    await context.send(random.choice(temp) + " - Bourbon <:sleeping_michaux:1063746563366727740>")


@bot.command(description="Le chef de majeure")
async def chef(context):
    quotesStephan = open("quotesStephan.txt", "r", encoding="utf8")
    temp = quotesStephan.read().split('\n')

    await context.send(random.choice(temp) + " - Stephan <:happy_stephan:990148651680669766>")


@bot.command(description="Demande une pause à Garance")
async def pause(context):
    # Si jamais on veut spammer le responsable pauses
    #resp_pause_id = "221310481875337217"
    #await context.send(f"<@{resp_pause_id}> Est-ce qu\'on peut avoir une pause s\'il te plait ?")
    await context.send("Est-ce qu\'on peut avoir une pause s\'il te plait ?", file=discord.File('dring.gif'))


@bot.command(description="Stops the bot")
@commands.is_owner()
async def stop(context):
    await context.send("Stopping bot !")
    log.info("Stopping bot !")
    bot.loop.stop()


async def auto_stephan():
    await bot.wait_until_ready()

    while not bot.is_closed():
        channel = bot.get_channel(1072918366144168058)
        dt_now = datetime.datetime.now()

        if dt_now.hour == 17 and dt_now.minute == 44 and dt_now.day == 17:
            await channel.send("Bonjour les TCOM, voici les données pour le cours de M. Stephan")
            await stephan(bot.get_context())

        await asyncio.sleep(3600)


log.info("Discord version: " + str(discord.version_info))
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

#bot.loop.create_task(auto_stephan())
bot.run(get_discord_token(), log_handler=handler)
