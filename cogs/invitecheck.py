import discord
from discord.ext import commands, tasks
from discord.utils import get
import DiscordUtils
from utils.db.mongo import InviteDump

class Invite(commands.Cog):

	def __init__(self, client):
		self.client = client
		self.CurrentInvites.start()
		self.tracker = DiscordUtils.InviteTracker(self.client)

	@tasks.loop(seconds=3.0)
	async def CurrentInvites(self):
		await self.tracker.cache_invites()

	@commands.Cog.listener()
	async def on_invite_create(self, invite):
		await self.tracker.update_invite_cache(invite)

	@commands.Cog.listener()
	async def on_guild_join(self, guild):
		await self.tracker.update_guild_cache(guild)

	@commands.Cog.listener()
	async def on_invite_delete(self, invite):
		await self.tracker.remove_invite_cache(invite)

	@commands.Cog.listener()
	async def on_guild_remove(self, guild):
		await self.tracker.remove_guild_cache(guild)

	@commands.Cog.listener()
	async def on_member_join(self, member):
		inviteDude = await self.tracker.fetch_inviter(member)
		channel_id, boo = InviteDump.finding(member.guild.id) 
			
		if boo:
			totalInvites = 0

			guild = self.client.get_guild(member.guild.id)
			for inv in await guild.invites():
				if inv.inviter == inviteDude:
					totalInvites += inv.uses

			channel = discord.utils.get(guild.channels, id=int(channel_id))
			if inviteDude == None:
				await channel.send(f"{member.mention} joined the server. I'm not able to track this invite.")
			else:
				await channel.send(f"{member.mention} joined the server. Invited by **{inviteDude}** ({totalInvites} Invites).")
		else:
			pass

	@commands.command()
	async def invites(self, ctx, user : discord.Member = None):
		if user == None:
			user = ctx.author
		totalInvites = 0
		for inv in await ctx.guild.invites():
			if inv.inviter == user:
				totalInvites += inv.uses
		await ctx.send(f"**{user.mention}** invited **{totalInvites}** member{'' if totalInvites == 1 else 's'} to **{ctx.guild.name}**!")

def setup(client):
	client.add_cog(Invite(client))
