import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

# intents.message_content = True
class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for file in os.listdir("./modules"):
            if file.endswith(".py"):
                bot.load_extension(f"modules.{file[:-3]}")

    async def on_ready():
        print(f"Logged in as {bot.user.name}, ID: {bot.user.id}")


intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)

bot.run(os.environ["TOKEN"])
