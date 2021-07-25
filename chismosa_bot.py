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
    no_ingles_lista = ["Chismosa no hablo inglés",
     "Chismosa no hablo ingles", "Chismosa no sé inglés", "Chismosa no se ingles"]
    if message.author == client.user:
        return

    if message.content == "Chismosa I'm depressed":
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith("Hi sister"):
        await message.channel.send("Oula jermana, ya compraste tu paleta de James Charles hoy?:sunglasses:")

<<<<<<< HEAD
    if message.content == "Chisme":
=======
    if message.content == "Chisme" or "chisme":
>>>>>>> 3d2ff8f74afcfd49c8c1c5f5c282ed05cc4749c5
        n = random.randint(0, 11)
        chisme_list = ["A ver :eyes: Mira, haz de cuenta que hay algunos cangrejos bien fresones en este servidor :strawberry:, pero pues como soy buena onda y todo, no voy a soltar nombres :face_with_hand_over_mouth::nail_care:", "La Gordita a veces me cansa :sleepy::neutral_face:",
        "Secretos tengo pocos, pero chismes tengo muchos :woman_tipping_hand:", "Ugh, so not to be rude or anything, but like masculinity is basically just a social construct :woman_technologist:", "Not gonna lie, British people with like thick Spanish accents are just straight daddies from heaven", "La Ruidosa, siempre que está a dieta, me pone de entrenadora personal, literal como si yo ya supiera cómo bajar de peso:unamused:", "AyÚDENME quE yO tENGO muCHOS quERACERES :triumph::card_box:", "Mi psicóloga me quiere meter a terapia de conversión por ser “intolerablemente femenina,” o sea qué pedo??", "“Tan difícil es dejar de comer lumpia?” murmuró mi mami el otro día, y yo estuve con cara de ni que fuera a engordar como tú, señora hipopótamo :upside_down::flag_ph:", "La Cariñosa is gonna like do my nails tonight, and OMG I’m like SOOOO pumped you literally have no idea :raised_hands::nail_care:", "Dicen que lo que no mata, te hace más fuerte, pero ufff la mirada del peruano que me encontré hoy, se sentía tanto letal como debilitante :heart_eyes::drooling_face::heart:", "El que tenga un acento paisa, será el que más prioridad va a tener en mi lista de futuros esposos :smirk::flag_co:"]
        await message.channel.send(chisme_list[n])

<<<<<<< HEAD
    elif message.content == "Chismosa no hablo inglés":
        await message.channel.send("Omg, tienes que descargar Duolingou :mobile_phone:")


client.run("ODYyNzg2MTg4NjQ1NjI5OTcz.YOdaQQ.Y_fiod5Z8Lro5OccTR3b9TQDjuw")
=======
    elif message.content in no_ingles_lista:
        await message.channel.send("Omg, tienes que descargar Duolingou :mobile_phone:")

client.run()
>>>>>>> 3d2ff8f74afcfd49c8c1c5f5c282ed05cc4749c5
