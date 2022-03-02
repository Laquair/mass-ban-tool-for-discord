import os, threading, asyncio
from multiprocessing.dummy import Pool as ThreadPool
os.system('pip install discord.py')
os.system('pip install aiohttp[speedup]')
from threading import Thread 
import discord 
from discord.ext import commands 
from discord import Member

bot = commands.Bot(command_prefix="69", intents=discord.Intents.all())
bot.remove_command('help')

token = str(input('Token :')) 
guild = int(input('guild id :'))

srvr = bot.get_guild(guild)

async def main():
   async with aiohttp.ClientSession() as session:


def ban(guild=guild, member=member):
async with session.put(f'https://discord.com/api/v10/guilds/{guild}/bans/{member}', data=b'data') as r:
   
while True:
   threading.Thread(target=ban, args=guild.id).start()
   threading.Thread(target=ban, args=guild.id).start()

pool = ThreadPool(69)
results = pool.map(ban)

bot.run(token)
