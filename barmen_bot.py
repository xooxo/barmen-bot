import discord
#import re 




token = "NOTREAL"

class Barmen(discord.Client):
    async def on_ready(self):
        print("Barmen Hazır!")
        
    async def on_message(self,message):
        
        if message.content.startswith('!serve'):
            print(message.channel)
            await message.channel.send('İçkiler {0}\'den!'.format(message.author))
            
            
            
barmen = Barmen()

barmen.run(token)
