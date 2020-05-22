import sys
import os
import subprocess
import discord
from discord.ext import commands

user=False
password=False

client=commands.Bot(command_prefix='!')

@client.event
async def on_ready():
	print('Disterminal is Ready.')

@client.command()
async def clear_discord(ctx,amount=100):
	await ctx.channel.purge(limit=amount)

@client.command()
async def login(ctx):
	await ctx.send('Password Please.')
	
@client.command()
async def username(ctx): # Change this variable to change the username
	global user
	user=True

@client.command()
async def password(ctx): # Change this to change the password
	global password, user
	password=True
	if(user==True and password==True):
		await ctx.send('Logged in successfully.')
		await ctx.channel.purge(limit=100)
		await ctx.send('You have logged onto your terminal. Pass commands. Use \'Log out\' to log out of your terminal.')
		channel=discord.Object(id=channel id)  #ENTER CHANNEL ID HERE
		@client.event
		async def on_message(message):
			try:
				global user, password
				command_terminal=message.content
				if(command_terminal=='Log out'):
					user=False
					password=False
					await message.channel.send('You have been logged out')
					print('If happened.')
					await ctx.channel.purge(limit=100)
					path=os.path.dirname(os.path.realpath(__file__))
					path+='/'+sys.argv[0]
					os.system(f'python3 {path}')
					quit()
				elif('cd'==command_terminal):
					new_path=message.content[:-1]
					print(new_path)
					try:
						os.chdir(new_path)
						success=True
					except Exception as e:
						success=False
						await message.channel.send(e)
					if(success==True):
						await message.channel.send(f'Directory changed to {new_path}')
				elif(user==True and password==True):
					command_terminal=command_terminal.split()
					result=subprocess.check_output(command_terminal, encoding='utf-8')
					#result=result.stdout
					print(result)
					await message.channel.send(result)
			except Exception as e:
				pass

client.run(token)       #ENTER TOKEN HERE
