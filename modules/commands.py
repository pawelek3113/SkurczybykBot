import nextcord
from nextcord import client
from nextcord.ext import commands
import random

class Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        channel = self.bot.get_channel(1061270452212879360) or await self.bot.fetch_channel(1061270452212879360)
        await channel.send(f"{member.mention} joined the {channel.guild.name}")

    @commands.command(name="echo")
    async def _echo(self, ctx: commands.Context, *, msg: str):
        await ctx.channel.send(msg)

    @commands.command(name="peppa")
    async def _peppa(self, ctx: commands.Context):
        await ctx.channel.send("https://i.guim.co.uk/img/media/97ef1652ca36d1c2e553628ffca8cf95e6d01c03/470_814_4479_2688/master/4479.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=0db16315b50eb20f7325a1e8920afd08")

    @commands.command(name="roll")
    async def _roll(self, ctx: commands.Context):
        await ctx.channel.send(f"Wyrzuciles: {random.randint(1, 6)}!")

    @commands.command(name="ping")
    async def _ping(self, ctx: commands.Context):
        await ctx.channel.send(f"Pong! {client.latency * 1000:.2f}ms")


def setup(bot):
    bot.add_cog(Commands(bot))