import discord
from discord.ext import commands
from utils.scraper.reddit import scrap
from utils.scraper.pychan import random_4chan

class Memes(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def meme(self, ctx,*, arg = None):
		flag = 1
		if arg == "dank" or arg == "dankmemes":
			sub = "Dankmemes"
		elif arg == "wholesome":
			sub = "WholesomeMemes"
		elif arg == "funny":
			sub = "Funny"
		elif arg == "linux":
			sub = "LinuxMemes"
		elif arg == "geek":
			sub = "ProgrammerHumor"
		elif arg == None:
			sub = "Memes"
	
		elif arg == "4chan":
			if ctx.channel.is_nsfw():
				flag = 0
				sub = "4chan"
			else:
				await ctx.send("**4chan only allowed in NSFW channels. Serving r/DankMemes instead.**")
				sub = "Dankmemes"
		else:
			sub = "Memes"

		embed = discord.Embed(colour=discord.Color.green())

		if flag == 1:
			meme_url, meme_author, meme_permalink = scrap(sub)

			embed.add_field(name=f"By {meme_author}.", value=f"[Jump!](https://www.reddit.com/{meme_permalink})", inline=False)
			embed.set_image(url=meme_url)

		else:
			chan_url, thread_url, board_name = random_4chan()
			embed.add_field(name=f"Board {board_name}.", value=f"[Jump!]({thread_url})", inline=False)
			embed.set_image(url=chan_url)
		
		embed.set_footer(text=f"from {sub}")

		await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Memes(client))