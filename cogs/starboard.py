import discord
from discord.ext import commands
from discord.utils import get
from utils.db.mongo import StarboardChannel

star_emoji = "⭐"

class Starboard(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_raw_reaction_add(self,payload: discord.RawReactionActionEvent) -> None:
		guild_id = payload.guild_id
		channel_id = payload.channel_id
		message_id = payload.message_id
		user_id = payload.user_id
		emoji = payload.emoji



		if str(emoji) == str(star_emoji):
			guild = self.client.get_guild(guild_id)
			chan = discord.utils.get(guild.channels, id=channel_id)
			message =  await chan.fetch_message(message_id)
			reaction = get(message.reactions, emoji=star_emoji)

			channel_ids, boo = StarboardChannel.finding(guild_id) 
			
			if boo:
				channel = discord.utils.get(guild.channels, id=int(channel_ids))

				if reaction.count == 1:
					sender = message.author
					contents = message.content
					attachment = message.attachments
					message_link = message.jump_url

					embed = discord.Embed(colour=discord.Color.green())
					embed.set_author(name=sender.name, icon_url=sender.avatar_url)
					embed.add_field(name="Orignal post.", value=f"[Jump!]({message_link})", inline=False)
					if contents != "":
						embed.add_field(name="Content", value=contents, inline=True)

					else:
						pass

					if attachment != []:
						attach_url = attachment[0].url
						attach_id = attachment[0].id
						attach_time = message.created_at.strftime("%d/%m/%Y %H:%M:%S")

						embed.set_image(url=attach_url)
						foot = str(attach_id) + " • " + str(attach_time)
						embed.set_footer(text=foot)
					else:
						attach_time = message.created_at.strftime("%d/%m/%Y %H:%M:%S")
						embed.set_footer(text=attach_time)

					await channel.send(f"{star_emoji} {message.channel.mention}",embed=embed)
			else:
				pass
		else:
			pass

	@commands.Cog.listener()
	async def on_reaction_remove(self, reaction, user):
		pass #incomplete
		



def setup(client):
	client.add_cog(Starboard(client))