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

    if message.content == "Chisme":
        flag = 0
        n = random.randint(1, 3)
        if n == 1 and flag is not n:
            await message.channel.send("A ver :eyes: Mira, haz de cuenta que hay algunos cangrejos bien fresones en este servidor :strawberry:, pero pues como soy buena onda y todo, no voy a soltar nombres :face_with_hand_over_mouth::nail_care:")
            flag = n
        elif n == 2 and flag is not n:
            await message.channel.send("La Gordita a veces me cansa :sleepy::neutral_face:")
            flag = n
        else:
            await message.channel.send("Ugh, so not to be rude or anything, but like masculinity is basically just a social construct :woman_technologist:")
            flag = n



    elif message.content == "Chismosa no hablo inglés":
        await message.channel.send("Omg, tienes que descargar Duolingou :mobile_phone:")


client.run("ODYyNzg2MTg4NjQ1NjI5OTcz.YOdaQQ.DmTEWMFEtX_abrRtyGcyaewDWqk")
