import discord
from discord.ext import commands
from discord import Spotify

class Activity(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def spotify(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
            pass
        if user.activities:
            for activity in user.activities:
                if isinstance(activity, Spotify):
                    embed = discord.Embed(
                        title = f"{user.name}'s Spotify",
                        description = "Listening to **{}**".format(activity.title),
                        color = 0xC902FF)
                    embed.set_thumbnail(url=activity.album_cover_url)
                    embed.add_field(name="Artist", value=activity.artist)
                    embed.add_field(name="Album", value=activity.album)
                    embed.add_field(name="Play", value=f"[Spotify](https://open.spotify.com/track/{activity.track_id})")
                    embed.set_footer(text="Song started at {}".format(activity.created_at.strftime("%H:%M")))
                    await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Activity(client))