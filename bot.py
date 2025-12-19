import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import asyncio
import os
import subprocess

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot=commands.Bot(command_prefix='!', intents=intents)

print ("Bot is running...")
print ("Press Ctrl+C to stop.")

@bot.command()
async def start(ctx, url):
    await ctx.send('Starting download...')
    command = [
    "yt-dlp", 
    "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
    "-o", r"user\replace\own\path\%(title)s.%(ext)s", # replace with your path make sure use "\" instead of "/" ALSO dont remove \%(title)s.%(ext)s its important
    url
    ]



    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT
    )
    while True:
        line = await process.stdout.readline()
        if not line:
            break
    
    output = line.decode('utf-8').strip()
    if output:
        print("yt-dlp output: {output}")

    await process.wait()

    if process.returncode == 0:
        await ctx.send('Download completed! check the Videos folder.')
    else:
        await ctx.send('Download failed. Check console for details.')
    
































bot.run(token, log_handler=handler, log_level=logging.DEBUG)