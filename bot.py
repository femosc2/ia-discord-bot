#!/usr/bin/python
# -*- coding: utf-8 -*-

import discord
import time
import datetime
import random
import api_keys

TOKEN = api_keys.token()

client = discord.Client()
current_time = datetime.datetime.now()

datavetenskapdate = datetime.datetime(2018,4,7)
databasdate = datetime.datetime(2018,5,17)
systemvetenskapdate = datetime.datetime(2018,6,12)

iaquotes = ["Vad är nav? - Victor Håkansson", "Jag fattade inte frågan så jag kryssade i båda rutorna - Victor Persson", "Säg inte till mig vad jag ska göra - Stoff", "Så kan det gå när man skriver tentan dagen innan - <:mange:419853258153000960>"]

@client.event
async def on_message(message):
    """when user sends a message with the parameter the bot will respond with the message defined in msg"""
    if message.author == client.user:
        return

    elif message.content.startswith('!nexttenta'):
        if current_time < datavetenskapdate:
            msg = "IAHT17s nästa tenta är 7 April 2018 i Datavetenskap (Omtentamen 2)".format(message)
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
        msg =   "!nexttenta\n!contribute\n!creator\n!quotes\n!schema\n!emotes".format(message)
        await client.send_message(message.channel, msg)
        
    elif message.content.startswith('!quotes'):
        msg =   random.choice(iaquotes).format(message)
        await client.send_message(message.channel, msg)
        
    elif message.content.startswith('!schema'):
        msg =   "http://schema.mah.se/setup/jsp/Schema.jsp?startDatum=idag&intervallTyp=m&intervallAntal=6&sprak=SV&sokMedAND=true&forklaringar=true&resurser=p.TGIAA17h".format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!emotes'):
        msg =   " <:tsanti:380391764323729409> <:2pac:380393936482467841> <:simonsbrod:380423036807151616> <:ia:380424464183328779> <:dipak:380430114250555392>: <:kappa:380447123214172162> <:stefan:380449729248755723> <:andhisname:380452684454690816> <:gachiGASM:382651346651840512> <:monkaS:383410496994279435> <:tskral:416316577471004672> <:ogtskral:416317001695232000> <:bae:416317932428197899> <:surreal:418365846294102019> <:POGGERS:419436969689612289> <:notification:419440773168234497> <:horsehead:419853153710768138> <:mange:419853258153000960> <:iablack:424178053279776768>" .format(message)
        await client.send_message(message.channel, msg)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
