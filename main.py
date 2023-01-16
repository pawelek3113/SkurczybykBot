import nextcord
from nextcord.ext import commands, tasks
import os
from dotenv import load_dotenv
from itertools import cycle

load_dotenv()


@tasks.loop(seconds=15)
async def change_status(bot):
    await bot.change_presence(status=nextcord.Status.idle, activity=nextcord.Game(next(Bot.bot_status)))

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for file in os.listdir("./modules"):
            if file.endswith(".py"):
                self.load_extension(f"modules.{file[:-3]}")

    bot_status = cycle(["with yo mama", "with yo papa"])
    
    async def on_ready(self):
        print(f"Logged in as {self.user.name}, ID: {self.user.id}")
        change_status.start(self)


intents = nextcord.Intents.all()
bot = Bot(command_prefix="!", case_insensitive=True, intents=intents)

bot.run(os.environ["TOKEN"])
