import discord, os, threading, asyncio,  aiohttp, requests, json
from discord.ext import commands 
from discord import Member 
from  threading import Thread 
from requests import put
from multiprocesing.dummy import Pool as ThreadPool
os.system('clear')

idk = commands.Bot(command_prefix="69", intents=discord.Intents.all())
idk.remove_command('help')

token = str(input('Token   :'))
saa = int(input('Guild id  :'))

guild = bot.get_guild(saa)

print('got guild')
os.system('clear')


def ban(guild, member):
  try:
    ##################################
    json = {
      'delete_message_days': '7'
      'reason': 'Laquairc op'
    }
    #################################
    r = requests.put(f'https://discord.com/api/v10/guilds/{guild}/bans/{member}', headers=headers, json=json)
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
      print(f"killed {member.name}")
    else:
      print('failed to kill {member.name}')
      
while True:
  threading.Thread(target=ban)

pool = ThreadPool(69)
pool.map(ban)

print('1 massban')
kk = input(' int :')
if kk == 1:
  ban()



idk.run(token)
 
