import discord
from discord.ext import commands



class Ready(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		memberCount = 0
		print ('Logged in as')
		print ("Name: ",self.client.user.name)
		print ("ID: ",self.client.user.id)
		print ("Discord Version: ",discord.__version__)
		print ('----------------')
		print('Servers connected to:\n')
		for guild in self.client.guilds:
			try:
				print (f"{guild.name} : {guild.member_count} members.")
				memberCount = memberCount + guild.member_count
			except:
				print (f" memberCount error at {guild.name} : {guild.id}")
		print (f"\n Total Members: {memberCount}")
		print("\n Total servers: ",len(self.client.guilds))	
		print ('----------------')
		print('Ready..')
		return memberCount


def setup(client):
	client.add_cog(Ready(client))