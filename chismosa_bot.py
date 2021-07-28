import discord
import os
import random
import requests
import json
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=',', intents=intents)


def get_all_members():
    guild = client.get_guild(862542952937029632)
    memberList = guild.members
    return memberList

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

    if message.content == "prueba":
        mem_list = get_all_members()
        member_list = []
        for items in mem_list:
            print(type(items))


    if message.content == "Chismosa I'm depressed":
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith("Hi sister"):
        await message.channel.send("Oula jermana, ya compraste tu paleta de James Charles hoy?:sunglasses:")

    if message.content.startswith("Chisme") or message.content.startswith("chisme"):
        #chisme = get_chisme()
        #await message.channel.send(chisme)
        #print(chisme)
        await message.channel.send("Esto es un chisme, pronto volverán xd")

    if message.content.startswith("Chismosa té") or message.content.startswith("chismosa té") or message.content.startswith("chismosa te"):
        await message.channel.send("Derrama el té sister!!!:tea:")

    elif message.content == "Chismosa no hablo inglés" or message.content == "chismosa no hablo ingles" or message.content == "chismosa no hablo ingles":
        await message.channel.send("Omg, tienes que descargar Duolingou :mobile_phone:")


client.run("")
