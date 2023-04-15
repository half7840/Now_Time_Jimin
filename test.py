import os
import discord
import openai
import time
import datetime
import zoneinfo
from discord.client import PrivilegedIntentsRequired
import pytz
import asyncio
import tasks
from discord.utils import get
from discord.ext import commands
from discord.ext import tasks
from datetime import datetime
from datetime import date
from dotenv import load_dotenv
from pytz import timezone

load_dotenv()

intents = discord.Intents().all()
bot = commands.Bot(intents=intents, command_prefix="!")

openai.api_key = "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"

@bot.event
async def on_ready():
    print('다음으로 로그인합니다 : ')
    print(bot.user.name)
    print('로그인에 성공했습니다')
    await now_time_jimin()

@bot.event
async def now_time_jimin():
    await bot.wait_until_ready()
    channel = bot.get_channel(915862213074493543)
    while not bot.is_closed():
        now = datetime.now(timezone('Asia/Seoul')).strftime('%H:%M')
        if now == '1:11' or now == '2:22' or now =='3:33' or now =='4:44' or now == '5:55' or now == '10:10' or now == '11:11' or now == '12:12' or now == '13:11' or now == '14:22' or now == '15:33' or now == '16:44' or now == '17:55' or now == '22:10' or now == '23:11':
            await channel.send("**지짐시**")

@bot.command()
async def 지민아(ctx, *, message):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"{message}",
        temperature=0.7,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    await ctx.send(response.choices[0].text)


bot.run(os.getenv('TOKEN'))


