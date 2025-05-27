import discord, json
from discord.ext import commands
from discord import Member, Embed

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    with open('Configurations/general.json') as f:
        data = json.load(f)
        ctx_guild = data.get('assigned_guild')
    @discord.slash_command(guild_ids=[ctx_guild], description="Kicks a member from the server.")
    @discord.option("member", type=discord.SlashCommandOptionType.user)
    @discord.option("reason", type=discord.SlashCommandOptionType.string)
    async def kick(self, ctx, member: Member, reason: str = None):
        await member.kick(reason=reason)
        with open('Configurations/Moderation.json') as f:
            data = json.load(f)
        channel_id = data.get('LOG_CHANNEL')
        channel = self.bot.get_channel(int(channel_id))
        embed = Embed(title="✅ SUCCESS:", description=f"{member.display_name} has been kicked.", color=0x48ff6c)
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Kick(bot))