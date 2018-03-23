import discord
import time
import datetime
import random

TOKEN = 'NDI2Njc4NDk3Njg4NDIwMzUy.DZZgBQ.Uqf0Xkk15C_MhzAcQ7QO-tMcdE8'

client = discord.Client()
current_time = datetime.datetime.now()

datavetenskapdate = datetime.datetime(2018,4,7)
databasdate = datetime.datetime(2018,5,17)
systemvetenskapdate = datetime.datetime(2018,6,12)

iaquotes = ["Vad är nav? - Victor Håkansson", "Jag fattade inte frågan så jag kryssade i båda rutorna - Victor Persson"]


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!nexttenta'):
        if current_time < datavetenskapdate:
            msg = "IAHT17s nästa tenta är 4 April 2018 i Datavetenskap (Omtentamen 2)".format(message)
            await client.send_message(message.channel, msg)
        elif current_time > datavetenskapdate and current_time < databasdate:
            msg = "IAHT17s nästa tenta är 17 Maj 2018 i Databasteknik (Omtentamen 1)".format(message)
            await client.send_message(message.channel, msg)
        elif current_time > databasdate and current_time < systemvetenskapdate:
            msg = "IAHT17s nästa tenta är 12 Juni 2018 i Systemutveckling (Omtentamen 1)".format(message)
            await client.send_message(message.channel, msg)
        else:
            print("Finns inga fler tentor inplanerade!")

    elif message.content.startswith('!contribute'):
        msg = "Vill du hjälpa till med vår Discord bot? www.github.com/femosc2/ia-discord-bot".format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!creator'):
        msg = "Felix Morau skapade mig för att han ville göra en discord bot!".format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!iahelp'):
        msg =   "!nexttenta\n!contribute\n!creator".format(message)
        await client.send_message(message.channel, msg)
        
    elif message.content.startswith('!quotes'):
        msg =   random.choice(iaquotes).format(message)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
