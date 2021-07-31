import discord
import os
from discord.ext import commands
from datetime import date
from dotenv import load_dotenv
import re
from utils import remove_tag, get_chisme, get_quote

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=',', intents=intents)
load_dotenv('.env')

@client.event
async def get_member_day(message):
    print('working')

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
        for member in mem_list:
            print("Member: {} Days in server: {}".format(member, get_member_days(member)))

    if message.content == "Chismosa I'm depressed":
        quote = get_quote()
        await message.channel.send(quote)

    if re.match(re.compile("(hola|hi|hello|hey) (sister|hermana)", re.I), message.content):
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

    if re.match(re.compile("my days", re.I), message.content):
        await message.channel.send("@{} has been in the server for {} days!".format(remove_tag(str(message.author)), get_member_days(message.author)))

    if re.match(re.compile("chismosa no hablo ingl(é|e)s", re.I), message.content):
        await message.channel.send("Omg, tienes que descargar Duolingou :mobile_phone:")

    if re.search(re.compile("(p+u+t+a+|p+u+t+o+|f+u+c+k+|f+a+g+o*t*|s+h+i+t+|b+i+t+c+h+|c+u+n+t+)", re.I), message.content):
        await message.channel.send("Watch your language sister!:nail_care:")

    if re.search(re.compile("s+h+o+(pp)+i+n+g+", re.I), message.content):
        await message.channel.send("Omg did someone say shopping!:shopping_bags:")

    if re.match(re.compile("send nudes", re.I), message.content):
        await message.channel.send("At least take me to dinner first!:flushed:")

def get_all_members():
    guild = client.get_guild(862542952937029632)
    memberList = guild.members
    return memberList

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

client.run(os.getenv('BOT_TOKEN'))