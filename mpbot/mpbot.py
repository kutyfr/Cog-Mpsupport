import discord
from discord.ext import commands

class SupportCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.support_category_id = YOUR_SUPPORT_CATEGORY_ID

    @commands.command()
    async def newticket(self, ctx):
        # Create a new support channel for the user
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        channel = await ctx.guild.create_text_channel(name=f"ticket-{ctx.author.id}", overwrites=overwrites, category=self.bot.get_channel(self.support_category_id))
        await ctx.send(f"Votre ticket a été créé : {channel.mention}")

    @commands.command()
    async def closeticket(self, ctx):
        # Close the current user's support channel
        if isinstance(ctx.channel, discord.TextChannel) and ctx.channel.category_id == self.support_category_id:
            await ctx.channel.delete()
            await ctx.send("Ticket fermé.")

class MPBot(commands.Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)
        self.add_cog(SupportCog(self))

def run_mp_bot(token):
    bot = MPBot(command_prefix="!", self_bot=True)

    @bot.event
    async def on_ready():
        print(f"MP Bot is ready. Logged in as {bot.user}")

    bot.run(token)

def setup(bot):
    bot.add_cog(SupportCog(bot))
