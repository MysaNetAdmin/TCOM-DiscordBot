# TCOM Bot

**TCOM** is a simple bot designed in ```Python``` for the [Discord](https://discordapp.com) platform. 
It works on the web, mobile and desktop version.

| Environments | Status |
| ------ | ------ |
| Windows | *Viable* |
| macOS | *Viable* |
| Linux | *Viable* |

## The Bot

For the moment the bot purpose is to give real-time prices for gold, euro/dollar conversion and an oil barrel

## Installation

To install all the packages needed to run this bot, simply type the following command 
``pip install -r Pipfile``

## Configuration Files

To run this bot need a json file containing the prefix to use and the discord token.
The file should follow this format and be named ``.env``

```
COMMAND_PREFIX=YOUR_TOKEN
DISCORD_TOKEN=YOUR_TOKEN
GOLD_API_TOKEN=YOUR_TOKEN
OIL_API_TOKEN=YOUR_TOKEN
```

To get your discord token API key go at this [address](https://discordapp.com/developers/applications/).
Then if you haven't already configured your application, make a new application with the desired name
and logo for your bot.
Finally get your token key in the ``Bot`` section.

For the bot to function properly you have to get the tokens for gold and oil API, you can get them here:
- GOLD API: https://www.goldapi.io/
- BRENT API: https://data.nasdaq.com/sign-up



## Running the bot

After configuring your json file, you can launch the bot with 
``python bot.py``