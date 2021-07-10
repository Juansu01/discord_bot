import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("Our bot is logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("Hi sister"):
        await message.channel.send("Omg, sister I'm like... freakin' workin'")

client.run("")

