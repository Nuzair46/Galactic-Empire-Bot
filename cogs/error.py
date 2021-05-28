"""
    forked from https://gist.github.com/EvieePy
"""

import discord
import traceback
import sys
from discord.ext import commands


class CommandErrorHandler(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound, )
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')
        
        # my changes
        #-----------
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing Arguments. Please pass the Arguments after the command.")
            #print(f'Logged Error: {error}.')

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('You do not have the permissions to use this command.')

        elif isinstance(error, commands.NotOwner):
            await ctx.send('You are not the owner of the bot.')

        elif isinstance(error, commands.ExtensionNotLoaded):
            await ctx.send('The extension is not loaded.')

    
        elif isinstance(error, commands.ExtensionAlreadyLoaded):
            await ctx.send('The extension already loaded.')

        elif isinstance(error, discord.HTTPException):
            print("HTTPException.")
        #----------

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except discord.HTTPException:
                pass

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
                await ctx.send('I could not find that member. Please try again.')

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
            #----------
            print(''.join(traceback.format_exception(type(error), error, error.__traceback__)))
            #----------

    @commands.command(name='repeat', aliases=['mimic', 'copy'])
    async def do_repeat(self, ctx, *, inp: str):
        await ctx.send(inp)

    @do_repeat.error
    async def do_repeat_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'inp':
                await ctx.send("You forgot to give me input to repeat!")


def setup(client):
    client.add_cog(CommandErrorHandler(client))