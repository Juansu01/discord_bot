import discord
import os
import random
import requests
import json
from discord.ext import commands
from datetime import date
from dotenv import load_dotenv


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=',', intents=intents)
load_dotenv('.env')

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
    chisme = requests.get('https://jasonpersonaldomain.com/chismosabot/random').json()['quote']
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

    if message.content == "members_count":
        mem_list = get_all_members()
        guild = client.get_guild(862542952937029632)
        guild_create = guild.created_at
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        for member in mem_list:
            mem_join = member.joined_at
            member_join_date = mem_join.strftime("%d/%m/%Y")
            date0 = d1
            date1 = member_join_date
            day0 = int(date0[:2])
            morep0 = date0.replace("/", "")
            month0 = int(morep0[2:-4])
            year0 = int(date0[6:])
            day1 = int(date1[:2])
            morep1 = date1.replace("/", "")
            month1 = int(morep1[2:-4])
            year1 = int(date1[6:])
            date0 = date(year0, month0, day0)
            date1 = date(year1, month1, day1)
            delta = date0 - date1
            print("Member: {} Days in server: {}".format(member, delta.days))

    if message.content == "Chismosa I'm depressed":
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith("Hi sister"):
        await message.channel.send("Oula jermana, ya compraste tu paleta de James Charles hoy?:sunglasses:")

    if message.content.startswith("Chisme".lower()):
        chisme = get_chisme()
        await message.channel.send(chisme)
        # await message.channel.send("Esto es un chisme, pronto volverán xd")

    if message.content.startswith("Chismosa té") or message.content.startswith("chismosa té") or message.content.startswith("chismosa te"):
        await message.channel.send("Derrama el té sister!!!:tea:")

    elif message.content == "Chismosa no hablo inglés" or message.content == "chismosa no hablo ingles" or message.content == "chismosa no hablo ingles":
        await message.channel.send("Omg, tienes que descargar Duolingou :mobile_phone:")

client.run(os.getenv('BOT_TOKEN'))