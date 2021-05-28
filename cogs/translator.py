import discord
from discord.ext import commands
from utils.scraper.translation import language

class Translator(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def translate(self, ctx, lang, *, arg):
		if arg.startswith("https://discord.com/channels/"):
			link = arg.split('/')
			server_id = int(link[4])
			channel_id = int(link[5])
			msg_id = int(link[6])

			server = self.client.get_guild(server_id)
			channel = server.get_channel(channel_id)
			message = await channel.fetch_message(msg_id)
			contents = message.content
			try:
				text,src = language.translateto(contents,lang)
				await ctx.send(f"Translated from **{src}** : ```\n{text}```")
			except:
				await ctx.send("This message is can't be translated.")
		else:
			try:
				text,src = language.translateto(arg,lang)
				await ctx.send(f"Translated from **{src}** : ```\n{text}```")
			except:
				await ctx.send("Unsupported input for translation.")

		


def setup(client):
	client.add_cog(Translator(client))
