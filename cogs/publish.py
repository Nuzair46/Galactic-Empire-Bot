import discord
from discord.ext import commands
from utils.db.mongo import PublishChannel

class Publish(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_message(self, message):
		try:
			if PublishChannel.finding(message.guild.id, message.channel.id):
				await message.publish()
		except: 
			pass
def setup(client):
	client.add_cog(Publish(client))