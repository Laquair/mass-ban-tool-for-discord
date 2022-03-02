import discord, os, threading, asyncio, aiohttp, json, requests
from multiprocesing.dummy import Pool as ThreadPool
from  discord.ext import commands 
from  threading import Thread 
from requests import put

os.system('clear')

bot = commands.bot(command_prefix=69, intents=discord.Intents.all())
bot.remove_command('help')

token = str(input('token  :'))
server = int(input('guild id  :'))

os.system("clear")
owo = int(input('type 1 to ban   :'))
guild = bot.get_guild(server)
if owo == 1:
   def ban(guild, member):
    json = {
                'delete_message_days': '7',
                'reason': 'Laquairc op'
            }
            r = requests.put(f'https://discord.com/api/v10/guilds/{guild}/bans/{member}', headers=headers, json=json)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"killed {member.name}")

while True:
   threading.Thread(target=ban).start()
   Thread(target=ban).start()

pool = ThreadPool(69)
pool.map(ban)

bot.run(token)

#qwq

                


