from nextcord.ext import commands
import nextcord
import datetime
import humanfriendly

class mute(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def mute(self, ctx, member:nextcord.Member, time, *, reason):
        time = humanfriendly.parse_timespan(time)
        
        await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=time))
        await ctx.reply(f"{member.mention} has been muted for the reason of {reason}")
        await member.send(f"You've been muted")
    
    @commands.command()
    async def unmute(self, ctx, member:nextcord.Member, *, reason):
        await member.edit(timeout=None)
        
        await ctx.reply(f"{member.mention} has been unmuted for the reason of {reason}")
        await member.send(f"You've been unmuted")

def setup(bot):
    bot.add_cog(mute(bot))