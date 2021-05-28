import discord
from discord.ext import commands

class Help(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def help(self, ctx, arg = None):
		if arg == None:
			embed=discord.Embed(title="Galactic Bot Help", url="https://discord.com/api/oauth2/authorize?client_id=764164847238643774&permissions=8&scope=bot", description="Here you can find all the help you need.", color=0xff0f0f)
			embed.set_author(name="Galactic Bot", url="https://rednek46.github.io", icon_url="https://cdn.discordapp.com/attachments/764604032861732874/792788864577830922/ico.gif")
			embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764604032861732874/792788864577830922/ico.gif")
			embed.add_field(name="Clear", value="Deletes the required amount of messages in a channel. Usage: `r!clear < amount >` Default amount = 5. Use additional `nopin` argument to avoid pinned messages.", inline=True)
			embed.add_field(name="Kick", value="Can kick members in a server. Usage: `r!kick < membername > < reason >`, Reason can be empty.", inline=True)
			embed.add_field(name="Ban", value="Can ban members in a server. Usage: `r!ban < membername > < reason >`, Reason can be empty.", inline=True)
			embed.add_field(name="Unban", value="To unban banned members. Usage: `r!unban < membername >`.", inline=True)
			embed.add_field(name="Starboard", value="Use `r!help starboard`for more info.", inline=True)
			embed.add_field(name="Userinfo", value="Can post the user info. Usage: `r!userinfo < membername >`, If Member name is empty the sender's user info is shown.", inline=True)
			embed.add_field(name="Avatar", value="Can post the avatar. Usage: `r!avatar < membername >`, If Member name is empty the sender's avatar is shown.", inline=True)
			embed.add_field(name="Publish", value="Use `r!help publish` for more info.", inline=True)
			embed.add_field(name="Prefix", value="Use `r!help prefix` for more info.", inline=True)
			embed.add_field(name="Translator", value="Use `r!help translate` for more info.", inline=True)
			embed.add_field(name="Meme", value="Use `r!help meme` for more info.", inline=True)
			embed.add_field(name="Music", value="Use `r!help music` for more info.", inline=True)
			embed.add_field(name="Invite Tracking", value="Use `r!help invite` for more info.", inline=True)
			embed.add_field(name="Spotify", value="Can post the user's Spotify activity. Usage: `r!spotify < membername >`, If Member name is empty the sender's activity is shown.", inline=True)
			embed.add_field(name="Help", value="Shows this command.", inline=True)
			embed.add_field(name="Required Permissions", value="All the permissions asked when inviting the bot are important for the bot to function properly.", inline=True)
			embed.add_field(name="Support/Contribute/Report Issues", value="Join [Galactic Empire](https://discord.gg/2URJ9HF)", inline=True)
			embed.set_footer(text="Some features may not work and some need permissions to work correctly. The default invite link has right permissions. Currently Work In Progress.")
			await ctx.send(embed=embed)

		elif arg == "meme":
			embed=discord.Embed(title="Galactic Bot Meme Help", url="https://discord.com/api/oauth2/authorize?client_id=764164847238643774&permissions=8&scope=bot", description="Can post posts from different subreddits. Usage `r!meme <subreddit>`", color=0xff0f0f)
			embed.set_author(name="Galactic Bot", url="https://rednek46.github.io", icon_url="https://cdn.discordapp.com/attachments/764604032861732874/792788864577830922/ico.gif")
			embed.add_field(name="r/DankMemes", value="`r!meme dank`", inline=True)
			embed.add_field(name="r/Memes", value="`r!meme `", inline=True)
			embed.add_field(name="r/WholesomeMemes", value="`r!meme wholesome`", inline=True)
			embed.add_field(name="r/Funny", value="`r!meme funny`", inline=True)
			embed.add_field(name="r/LinuxMemes", value="`r!meme linux`", inline=True)
			embed.add_field(name="r/ProgrammerHumor", value="`r!meme geek`", inline=True)
			embed.add_field(name="4chan", value="`r!meme 4chan`", inline=True)
			embed.set_footer(text="4chan is for NSFW channels only. Incase if its used, DankMemes is used as substitute on non-NSFW channels.")
			await ctx.send(embed=embed)

		elif arg == "invite":
			embed=discord.Embed(title="Galactic Bot Invite Tracking Help", url="https://discord.com/api/oauth2/authorize?client_id=764164847238643774&permissions=8&scope=bot", description="Can track and view inviters and number of invites by a user.", color=0xff0f0f)
			embed.set_author(name="Galactic Bot", url="https://rednek46.github.io", icon_url="https://cdn.discordapp.com/attachments/764604032861732874/792788864577830922/ico.gif")
			embed.add_field(name="Invites", value="View number of invites by a user. Usage `r!invites < membername >`. If Member name is empty the sender's invite info is shown.")
			embed.add_field(name="Set invite channel.", value="Can set channel to send new user entries and used invites. Usage: `r!set invite < channelname >`, To unset, `r!unset invite < channelname >`.")
			embed.add_field(name="Required Permissions", value="To set channels, user needs to have Manage Channels, Manage Webhooks permission. To send logs, Bot needs to have Manage Server, Manage Webhooks and Create Invites permissions.")
			await ctx.send(embed=embed)
		
		elif arg == "starboard":
			embed=discord.Embed(title="Galactic Bot Starboard Help", url="https://discord.com/api/oauth2/authorize?client_id=764164847238643774&permissions=8&scope=bot", description="Can track and view inviters and number of invites by a user.", color=0xff0f0f)
			embed.set_author(name="Galactic Bot", url="https://rednek46.github.io", icon_url="https://cdn.discordapp.com/attachments/764604032861732874/792788864577830922/ico.gif")
			embed.add_field(name="Starboard", value="Starred messages will be posted on starboard channel.")
			embed.add_field(name="Set starboard channel.", value="Can set channel to send starred messages. Usage: `r!set starboard < channelname >`, To unset, `r!unset starboard < channelname >`.")
			embed.add_field(name="Required Permissions", value="To set channels, user needs to have Manage Channels, Manage Webhooks permission. To send to starboard, Bot needs to have Send Embeds,Manage Webhooks and Manage Messages permissions.")
			await ctx.send(embed=embed)

		elif arg == "prefix":
			embed=discord.Embed(title="Galactic Bot Prefix Help", url="https://discord.com/api/oauth2/authorize?client_id=764164847238643774&permissions=8&scope=bot", description="Can track and view inviters and number of invites by a user.", color=0xff0f0f)
			embed.set_author(name="Galactic Bot", url="https://rednek46.github.io", icon_url="https://cdn.discordapp.com/attachments/764604032861732874/792788864577830922/ico.gif")
			embed.add_field(name="Prefix", value="Change the bot's prefix for the server.")
			embed.add_field(name="Set prefix.", value="Usage: `r!set prefix <prefix>`, To return to default, `r!set prefix default`.")
			embed.add_field(name="Required Permissions", value="To set channels, user needs to have Manage Channels, Manage Webhooks permission. To send to starboard, Bot needs to have Send Embeds,Manage Webhooks and Manage Messages permissions.")
			await ctx.send(embed=embed)

		elif arg == "publish":
			embed=discord.Embed(title="Galactic Bot Auto Publisher Help", url="https://discord.com/api/oauth2/authorize?client_id=764164847238643774&permissions=8&scope=bot", description="Can track and view inviters and number of invites by a user.", color=0xff0f0f)
			embed.set_author(name="Galactic Bot", url="https://rednek46.github.io", icon_url="https://cdn.discordapp.com/attachments/764604032861732874/792788864577830922/ico.gif")
			embed.add_field(name="Auto Publisher", value="Can auto publish selected announcement channels when new messages arrive.")
			embed.add_field(name="Set publish channel.", value="Can set channel to Publish (Channel needs to be an announcement channel). Usage: `r!set publish < channelname >`, To unset, `r!unset publish < channelname >`.")
			embed.add_field(name="Required Permissions", value="To set channels, user needs to have Manage Channels, Manage Webhooks permission. To publish, Bot needs Manage Messages, Manage Webhooks permissions.")
			await ctx.send(embed=embed)

		elif arg == "translate":
			embed=discord.Embed(title="Galactic Bot Translator Help", url="https://discord.com/api/oauth2/authorize?client_id=764164847238643774&permissions=8&scope=bot", description="Can track and view inviters and number of invites by a user.", color=0xff0f0f)
			embed.set_author(name="Galactic Bot", url="https://rednek46.github.io", icon_url="https://cdn.discordapp.com/attachments/764604032861732874/792788864577830922/ico.gif")
			embed.add_field(name="Translator", value="Can translate texts supported by google translate with auto detection.")
			embed.add_field(name="Usage", value="`r!translate lang < text >` or `r!translate lang < message link >`. lang = destination language (example: en,fr,ko). ")
			embed.add_field(name="Required Permissions", value="Anyone can use this command.")
			await ctx.send(embed=embed)

		elif arg == "music":
			embed=discord.Embed(title="Galactic Bot Music Help", url="https://discord.com/api/oauth2/authorize?client_id=764164847238643774&permissions=8&scope=bot", description="Can play songs in VC.", color=0xff0f0f)
			embed.set_author(name="Galactic Bot", url="https://rednek46.github.io", icon_url="https://cdn.discordapp.com/attachments/764604032861732874/792788864577830922/ico.gif")
			embed.add_field(name="Music Player", value="Can play songs from youtube with url or query. Playlists not supported.")
			embed.add_field(name="Commands", value="`play < url or query > / stop`,`pause/resume`, `remove < queue number >`.")
			embed.add_field(name="Required Permissions", value="Bot needs voice permissions.")
			await ctx.send(embed=embed)

		else:
			pass

def setup(client):
	client.add_cog(Help(client))