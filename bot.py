# This example requires the 'message_content' intent.

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTE1ODc3NzIyNjE5MjQ4NjUwMA.G-8g-p.931D8ew9APKhbky1G-xEN_nhnH__Wl6992ynh4')

