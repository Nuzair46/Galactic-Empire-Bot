import discord
from discord.ext import commands
from utils.db.mongo import PublishChannel, StarboardChannel, InviteDump, PrefixBase

class SetUnset(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(pass_context=True)
	@commands.has_permissions(manage_messages = True, manage_webhooks = True)
	async def set(self, ctx,feature, arg):
		channel_id = arg[2:-1]
		if(feature == "publish"):
			PublishChannel.new(ctx.guild.id, channel_id)

			await ctx.send(f"Set to Publish channel {arg}")
		
		elif(feature == "starboard"):
			
			flag = StarboardChannel.new(ctx.guild.id, channel_id)
			
			if flag == 0:
				await ctx.send(f"Starboard set on {arg}")
			elif flag == 1:
				await ctx.send(f"Changed Starboard to {arg}")

		elif(feature == "invite"):
			
			flag = InviteDump.new(ctx.guild.id, channel_id)
			if flag == 0:
				await ctx.send(f"Set to dump invite logs on {arg}")
			elif flag == 1:
				await ctx.send(f"Changed Invite logs to {arg}")

		elif(feature == "prefix"):

			if (arg == "default"):
				def_prefix = "r!"
				PrefixBase.new(ctx.guild.id, def_prefix)
				await ctx.send("Prefix changed to default `r!`.")

			else:
				PrefixBase.new(ctx.guild.id, arg)
				await ctx.send(f'Prefix changed to `{arg}` .')

		else:
			await ctx.send(f"Unknwon feature **{feature}**. Use help.")


	@commands.command(pass_context=True)
	@commands.has_permissions(manage_messages = True)
	async def unset(self, ctx, feature, arg):
		channel_id = arg[2:-1]

		if(feature == "publish"):
			flag = PublishChannel.remove(ctx.guild.id, channel_id)

			if flag == 1:
				await ctx.send(f"Auto Publish off for {arg}")
			elif flag == 0:
				await ctx.send(f"To unset you have to set {arg} to auto-publish")

		elif(feature == "starboard"):

			flag = StarboardChannel.remove(ctx.guild.id, channel_id)

			if flag == 1:
				await ctx.send(f"Starboard removed from {arg}")
			elif flag == 0:
				await ctx.send(f"To unset you have to set {arg} for Starboard.")

		elif(feature == "invite"):

			flag = InviteDump.remove(ctx.guild.id, channel_id)

			if flag == 1:
				await ctx.send(f"Invite Dumping off for {arg}")
			elif flag == 0:
				await ctx.send(f"To unset you have to set {arg} for Invite Dumping.")

		else:
			await ctx.send(f"Unknwon feature **{feature}**. Use help.")

def setup(client):
	client.add_cog(SetUnset(client))
		