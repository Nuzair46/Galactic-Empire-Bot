import discord
from discord.ext import commands
from utils.db.mongo import PrefixBase

class Prefix(commands.Cog):

	def __init__(self, client):
		self.client = client

	def get_prefix(self, message):
		try:
			prefixes = PrefixBase.finding(message.guild.id)
			return prefixes
		except:
			return "r!"


	@commands.Cog.listener()
	async def on_guild_join(self, guild):
		PrefixBase.adding(guild.id)

	@commands.Cog.listener()
	async def on_guild_remove(self, guild):
		PrefixBase.remove(guild.id)

def setup(client):
	client.add_cog(Prefix(client))