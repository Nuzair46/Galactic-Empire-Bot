import discord
import asyncio
from discord.ext import commands

class Clear(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command(pass_context = True ,aliases=['clean', 'purge'])
	@commands.has_permissions(manage_messages = True)
	async def clear(self, ctx, amount = 5, pins = None):
		if pins == "nopin":
			def not_pinned(msg):
				return not msg.pinned
		else:
			not_pinned = None

		await ctx.channel.purge(limit = amount + 1, check = not_pinned)
		await ctx.send(f'Deleted {amount} messages.', delete_after = 3)

def setup(client):
	client.add_cog(Clear(client))