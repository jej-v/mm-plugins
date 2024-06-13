from discord.ext import commands

# List of commands here:
# ?magic8ball

async def setup(bot: commands.Bot):
    for g in bot.guilds:
        await g.get_member(bot.user.id).edit(nick="Lambda's Friend")
