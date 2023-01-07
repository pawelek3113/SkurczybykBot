import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = nextcord.Intents.all()
# intents.message_content = True

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)

for file in os.listdir("./modules"):
    if file.endswith(".py"):
        bot.load_extension(f"modules.{file[:-3]}")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}, ID: {bot.user.id}")

bot.run(os.environ["TOKEN"])
