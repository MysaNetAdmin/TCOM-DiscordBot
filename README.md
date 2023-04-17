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
The file should follow this format and be named ``config.json``

```
{
    "command_prefix": "chosen_prefix",
    "discord_token": "your_token",
    "gold_api_token": "your_token",
    "oil_api_token": "your_token"
}
```

To get your discord token API key go at this [address](https://discordapp.com/developers/applications/).
Then if you haven't already configured your application, make a new application with the desired name
and logo for your bot.

How to get other tokens:
- GOLD API: https://www.goldapi.io/
- BRENT API: https://data.nasdaq.com/sign-up

Finally get your token key in the ``Bot`` section.

## Running the bot

After configuring your json file, you can launch the bot with 
``python bot.py``