'''
Description: 
Version: 1.0
Autor: z.cejay@gmail.com
Date: 2022-08-04 12:00:58
LastEditors: cejay
LastEditTime: 2022-08-04 12:51:15
'''

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run('')
