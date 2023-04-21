import json
import random
import log
import discord
import requests
import logging

from discord.ext import commands, tasks


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


@bot.command(description="Monsieur Michaux")
async def chef(context):
    quotesStephan = open("quotesStephan.txt", "r", encoding="utf8")
    temp = quotesStephan.read().split('\n')

    await context.send(random.choice(temp) + " - Stephan <:happy_stephan:990148651680669766>")


@bot.command(description="Demande une pause à Garance")
async def pause(context):
    # Si jamais on veut spammer le responsable pauses
    # resp_pause_id = "221310481875337217"
    # await context.send(f"<@{resp_pause_id}> Est-ce qu\'on peut avoir une pause s\'il te plait ?")
    await context.send("Est-ce qu\'on peut avoir une pause s\'il te plait ?", file=discord.File('dring.gif'))


@bot.command(description="Stops the bot")
@commands.is_owner()
async def stop(context):
    await context.send("Stopping bot !")
    log.info("Stopping bot !")
    bot.loop.stop()


# Message 1
@tasks.loop(seconds=5)
async def called_once_a_day():
    tcom_general_id = 1072918366144168058
    message_channel = bot.get_channel(tcom_general_id)
    await message_channel.send("test 1")


@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")


# called_once_a_day.start()

log.info("Discord version: " + str(discord.version_info))
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
bot.run(get_discord_token(), log_handler=handler)
