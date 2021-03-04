ID = 00000000000000

import discord
import time
import random 

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    channel = client.get_channel(ID)
    #channels = ["general"]
    if (message.content.startswith('!spam') and message.channel.id == ID):
        while (True):
            await channel.send("Spamming a text: " + str(random.randint(100000,999999)))
            time.sleep(1.5)
    if (message.content.startswith('!test') and message.channel.id == ID):
        await channel.send("Sup!")
        

client.run("*******************", bot=False)

#-------------- Please replace the ***** With user token of spam user --------------
