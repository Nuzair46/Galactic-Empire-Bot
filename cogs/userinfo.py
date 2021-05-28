import discord
from discord.ext import commands

class UserInfo(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def userinfo(self, ctx, target : discord.Member = None):
		users = ctx.guild.members
		if (target == None):
			target = ctx.author

		roles = [role for role in target.roles]
		embed = discord.Embed(title="User information", colour=discord.Color.red())

		embed.set_author(name=target.name, icon_url=target.avatar_url)

		embed.set_thumbnail(url=target.avatar_url)

		fields = [("Name", str(target), False),
			   ("ID", target.id, False),
			   ("Status", str(target.status).title(), False),
			   (f"Roles ({len(roles) - 1})", " ".join([role.mention for role in roles if role.name != "@everyone"]), False),
			   ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
			   ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), False)]

		for name, value, inline in fields:
			embed.add_field(name=name, value=value, inline=inline)

		await ctx.send(embed=embed)

	@commands.command()
	async def avatar(self, ctx, target : discord.Member = None):
		if (target == None):
			target = ctx.author

		embed = discord.Embed(title=target.name, colour=discord.Color.blue())
		embed.set_image(url=target.avatar_url)

		await ctx.send(embed=embed)

def setup(client):
	client.add_cog(UserInfo(client))