import discord
import os
from discord.ext import commands
from datetime import date
from dotenv import load_dotenv
import re
from utils import remove_tag, get_chisme, get_quote
import asyncio
from discord.ext import tasks
from datetime import datetime, timedelta
from keep_alive import keep_alive
import random

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=',', intents=intents)
load_dotenv('.env')
my_secret = os.environ['key']

def trigger_function():
    asyncio.run(role_routine())

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


async def role_routine():
    channel = client.get_channel(862591362369191966)
    await channel.send("Checking roles :woman_technologist:")
    member_list = get_all_members()
    for member in member_list:
        days = get_member_days(member)
        roles = member.roles
        role = discord.utils.get(member.guild.roles, name="Spambot 🤖")
        if role in roles:
            continue
        if days >= 30 and days < 90:
            print("Granting: {} role: Sister".format(member))
            new_role = discord.utils.get(member.guild.roles, name="Sister")
            old_role = discord.utils.get(member.guild.roles, name="Hermanastra")
            await member.add_roles(new_role)
            await member.remove_roles(old_role)
        elif days >= 90 and days < 180:
            print("Granting: {} role: Sister Menor".format(member))
            new_role = discord.utils.get(member.guild.roles, name="Sister Menor")
            old_role = discord.utils.get(member.guild.roles, name="Sister")
            await member.add_roles(new_role)
            await member.remove_roles(old_role)
        elif days >= 180 and days < 300:
            print("Granting: {} role: Hermana del Medio".format(member))
            new_role = discord.utils.get(member.guild.roles, name="Hermana del Medio")
            old_role = discord.utils.get(member.guild.roles, name="Sister Menor")
            await member.add_roles(new_role)
            await member.remove_roles(old_role)
        elif days >= 300:
            print("Granting: {} role: Sister Mayor".format(member))
            new_role = discord.utils.get(member.guild.roles, name="Sister Mayor")
            old_role = discord.utils.get(member.guild.roles, name="Hermana del Medio")
            await member.add_roles(new_role)
            await member.remove_roles(old_role)
        else:
            continue
    await channel.send("All members checked:white_check_mark: :woman_tipping_hand:")


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

    if message.content == "do routine":
        if str(message.author) == "JuanC#1899":
          await role_routine()

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
    
    if re.match(re.compile("days all", re.I), message.content):
        members = get_all_members()
        names = []
        for member in members:
            names.append("@{}: {} days".format(remove_tag(str(member)), get_member_days(member)))
        await message.channel.send("\n".join(names))

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

    if re.match(re.compile("s+e+n+d+ n+u+d+e+s+", re.I), message.content):
        await message.channel.send("At least take me to dinner first!:flushed:")
    
    if re.search(re.compile("(l+i+k+e+|l+o+v+e+)", re.I), message.content):
        return
        n = random.randint(0, 1)
        if n == 0:
          await message.channel.send("i… LOVE :woman_gesturing_ok:")
        else:
          await message.channel.send("I literally LOVE :woman_gesturing_ok:")

    if message.content == "Count our sisters":
        members = get_all_members()
        count = len(members)
        await message.channel.send("We currently have {} sisters :woman_technologist: ".format(count))

@tasks.loop(hours=24)
async def called_once_a_day():
    await role_routine()

@called_once_a_day.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start()
keep_alive()
client.run(my_secret)
