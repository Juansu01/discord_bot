import discord
import os
import random
import requests
import json

activity = discord.Activity(name="James Charles' latest video", type=discord.ActivityType.watching)
client = discord.Client(activity=activity)

def get_quote():
    response = requests.get("http://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -James Charles"
    return(quote)

def get_chisme():
    chisme = requests.get('http://143.198.232.116/random').json()['quote']
    return chisme

@client.event
async def on_ready():
    print("Our bot is logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "Chismosa I'm depressed":
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith("Hi sister"):
        await message.channel.send("Oula jermana, ya compraste tu paleta de James Charles hoy?:sunglasses:")

    if message.content == "Chisme" or message.content == "chisme":
        chisme = get_chisme()
        await message.channel.send(chisme)

    elif message.content == "Chismosa no hablo inglés":
        await message.channel.send("Omg, tienes que descargar Duolingou :mobile_phone:")


client.run("")
