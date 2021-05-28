#this is a copied and modified cog so that this bot can be run on Heroku. I dont remember the author, If your are the one and wants credits, submit an issue.
from discord import Embed, FFmpegPCMAudio
from discord.ext import commands
from discord.ext.commands import Context
from discord.utils import get

from asyncio import run_coroutine_threadsafe
from utils.tools import get_json, is_url
from re import findall
from pafy import new


class Music(commands.Cog, name='Music'):
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    def __init__(self, bot):
        self.bot = bot
        self.song_queue = {}
        self.message = {}

    @staticmethod
    async def search(author: str, arg: str):

        url = arg if is_url(arg) else f'https://www.youtube.com/results?search_query={arg}'
        resp = await get_json(url, json=False)
        video_id = findall(r"watch\?v=(\S{11})", resp)[0]
        video = new(video_id)

        embed = (Embed(title='🎵 Now playing:', description=f"[{video.title}](https://www.youtube.com/watch?v={video_id})", color=0x3498db)
                .add_field(name='Duration', value=video.duration)
                .add_field(name='Requested by', value=author)
                .add_field(name='Artist', value=video.author)
                .add_field(name='Queue:', value="Such Emptiness...")
                .set_thumbnail(url=video.thumb))

        return {'embed': embed, 'source': video.getbestaudio().url, 'title': video.title}

    async def edit_message(self, ctx: Context):
        
        embed = self.song_queue[ctx.guild.id][0]['embed']
        content = "\n".join([f"[{self.song_queue[ctx.guild.id].index(i)}] {i['title']}" for i in self.song_queue[ctx.guild.id][1:]]) if len(self.song_queue[ctx.guild.id]) > 1 else "No pending videos"
        embed.set_field_at(index = 3, name="Queue:", value=content, inline=False)
        await self.message[ctx.guild.id].delete()
        self.message[ctx.guild.id] = await ctx.send(embed=embed)


    def play_next(self, ctx: Context):
        
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        
        if len(self.song_queue[ctx.guild.id]) > 1:
            del self.song_queue[ctx.guild.id][0]
            run_coroutine_threadsafe(self.edit_message(ctx), self.bot.loop)
            voice.play(FFmpegPCMAudio(self.song_queue[ctx.guild.id][0]['source'], **Music.FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
            voice.is_playing()
        
        else:
            #run_coroutine_threadsafe(voice.disconnect(), self.bot.loop)
            run_coroutine_threadsafe(self.message[ctx.guild.id].delete(), self.bot.loop)

    @commands.command()
    async def play(self, ctx: Context, *, video: str):
        
        channel = ctx.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        song = await Music.search(ctx.author.mention, video)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        
        else:
            voice = await channel.connect()  
        
        if not voice.is_playing():
            self.song_queue[ctx.guild.id] = [song]
            self.message[ctx.guild.id] = await ctx.send(embed=song['embed'])
            voice.play(FFmpegPCMAudio(song['source'], **Music.FFMPEG_OPTIONS), after=lambda e: self.play_next(ctx))
            voice.is_playing()
        
        else:
            self.song_queue[ctx.guild.id].append(song)
            await self.edit_message(ctx)

    @commands.command(brief='$pause', description='pause')
    async def pause(self, ctx: Context):
        
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        
        if voice.is_connected():
            if voice.is_playing():
                await ctx.send('⏸️ Song Paused.', delete_after=5.0)
                voice.pause()
        
            else:
                await ctx.send('⏯️ Song Resumed.', delete_after=5.0)
                voice.resume()

    @commands.command()
    async def resume(self, ctx: Context):
        
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        
        if voice.is_connected():
            if voice.is_playing():
                pass
            else:
                await ctx.send('⏯️ Song Resumed.', delete_after=5.0)
                voice.resume()


    @commands.command()
    async def skip(self, ctx: Context):
        
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        
        if voice.is_playing():
            await ctx.send('⏭️ Song Skipped.', delete_after=5.0)
            voice.stop()

    @commands.command()
    async def remove(self, ctx: Context, num: int):
        
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        
        if voice.is_playing():
            del self.song_queue[ctx.guild.id][num]
            await self.edit_message(ctx)

    @commands.command(aliases=['quit', 'stop'], brief='', description='leave')
    async def leave(self, ctx: Context):
        
        self.song_queue[ctx.guild.id] = []
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        run_coroutine_threadsafe(voice.disconnect(), self.bot.loop)
        run_coroutine_threadsafe(self.message[ctx.guild.id].delete(), self.bot.loop)


def setup(bot):
    bot.add_cog(Music(bot))