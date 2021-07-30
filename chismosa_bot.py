import discord
import os
import random
import requests
import json
from discord.ext import commands
from datetime import date
from dotenv import load_dotenv
import re

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
    chisme = requests.get('https://jasonpersonaldomain.com/chismosabot/random')
    json_data = json.loads(chisme.text)
    quote = json_data['quote']['quote']
    return quote

@client.event
async def on_ready():
    print("Our bot is logged in as {0.user}".format(client))

def get_member_days(member):
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
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
    return delta.days

def remove_tag(username):
    chars = []
    for char in username:
        if char == '#':
            break
        chars.append(char)
    return "".join(chars)


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
        for member in mem_list:
            print("Member: {} Days in server: {}".format(member, get_member_days(member)))

    if message.content == "Chismosa I'm depressed":
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith("Hi sister"):
        await message.channel.send("Oula jermana, ya compraste tu paleta de James Charles hoy?:sunglasses:")

    if message.content.lower() == 'chisme':
        chisme = get_chisme()
        await message.channel.send(chisme)

    if re.match(re.compile("chismosa (te|té)", re.I), message.content):
        await message.channel.send("Derrama el té sister!!!:tea:")

    if re.match("days [a-z0-9_]+", message.content.lower()):
        members = get_all_members()
        username = message.content.split()[1]
        print(username)
        for member in members:
            if remove_tag(str(member)).lower() == username.lower():
                print(member, username)
                await message.channel.send("@{} has been in the server for {} days!".format(remove_tag(str(member)), get_member_days(member)))

    if re.match(re.compile("chismosa no hablo (inglés|ingles)", re.I), message.content):
        await message.channel.send("Omg, tienes que descargar Duolingou :mobile_phone:")

@client.event
async def get_member_day(message):
    print('working')

client.run(os.getenv('BOT_TOKEN'))