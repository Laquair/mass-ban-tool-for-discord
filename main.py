import os, threading, asyncio
from multiprocessing.dummy import Pool as ThreadPool
os.system('pip install discord.py')
os.system('pip install aiohttp[speedup])
from threading import Thread 
try:
   import discord 
expect:
   os.system('pip install discord')
from discord.ext import commands 
from discord import Member

bot = commands.Bot(command_prefix="69", intents=discord.Intents.all())
bot.remove_command('help')

token = str(input('Token (with " at the start & end) :')) 
guild = int(input('guild id'))

srvr = bot.get_guild(guild)
def ban(guild, member):
   async def main():
    async with aiohttp.ClientSession() as session:
        async with session.put('http://discord.com/api/v10/guilds/{guild}/bans/{member}', data=b'data') as r:
         if r.response == "200" or r.response == "201" or r.response == "204":
               print(f"banned {member.strip()}")
    

ban()
while True:
   threading.Thread(target=ban, args=guild.id).start()
   threading.Thread(target=ban, args=guild.id).start()

pool = ThreadPool(69)
results = pool.map(ban)

bot.run(token)
