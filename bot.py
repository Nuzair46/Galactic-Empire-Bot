import discord
from discord import Intents
from discord.ext import commands
import os
from cogs.prefix import Prefix



client = commands.Bot(command_prefix = Prefix.get_prefix, status = discord.Status.dnd, activity = discord.Game('r!help'), intents=Intents.all())
client.remove_command("help")  ##to remove the default help command in the discord.py
creds = open('token.txt', 'r')  

if __name__ == '__main__':
	
	#loading cogs	
	@client.command()
	@commands.is_owner()
	async def load(ctx, extension):
		client.load_extension(f'cogs.{extension}')
		await ctx.send(f'**{extension}** cog loaded.')

	@client.command()
	@commands.is_owner()
	async def unload(ctx, extension):
		client.unload_extension(f'cogs.{extension}')
		await ctx.send(f'**{extension}** cog unloaded.')

	@client.command()
	@commands.is_owner()
	async def reload(ctx, extension):
		client.unload_extension(f'cogs.{extension}')
		client.load_extension(f'cogs.{extension}')
		await ctx.send(f'**{extension}** cog reloaded.')

	for cogname in os.listdir('./cogs'):
		if cogname.endswith('.py'):
			client.load_extension(f'cogs.{cogname[:-3]}')

	## Don't edit under this line.
	key = creds
	client.run(key.read())