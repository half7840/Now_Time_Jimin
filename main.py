import os
import discord
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


@bot.command(name = '일기토')
@commands.cooldown(1, 600, commands.BucketType.user)
async def blade(ctx, member: discord.Member, messageid=int):
    target = member
    author = ctx.message.author
    message = await ctx.channel.send(f'{author.mention}(이) {target.mention}을 향해 일기토를 신청합니다.')
    await ctx.message.add_reaction("👍")
    await ctx.message.add_reaction("👎")

    def check(reaction, user):
        return user == ctx.message.author and str(reaction.emoji) == '👍' or str(reaction.emoji) == '👎'
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=10.0, check=check)
        if user == ctx.message.author:
            reaction, user =await bot.wait_for('reaction_add', timeout=10.0, check=check)
            await ctx.channel.send("신청자는 투표 할 수 없습니다. 10초 내에 다시 투표해주세요")
        else:
            await asyncio.TimeoutError

    except asyncio.TimeoutError:
        await ctx.channel.send('👎')
    else:
        if reaction.count > 2 and reaction.emoji == "👍":
            await member.edit(voice_channel=None)
            await ctx.channel.send(f'{target.mention}(이)가 일기토에 패배했습니다.')

        else:
            await member.edit(voice_channel=None)
            await ctx.channel.send(f'{author.mention}(이)가 일기토에 패했습니다.')
@blade.error
async def blade_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.send(f'{ctx.author.mention}는 쿨다운 중 입니다 {round(error.retry_after, 2)}초 후 다시 사용할 수 있습니다.')

#async def cal_time():
#    global next_time
#    set_next_time()
#    while True:
#        if datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") == next_time:
#            await now_time_jimin()
#           break
#        elif datetime.now(timezone('Asia/Seoul')).strftime("%H:%M") != next_time:
#            break
#    await asyncio.sleep(70)

#@bot.event
#sync def now_time_jimin():
#    channel = bot.get_channel(915862213074493543)
#    await channel.send("**지짐시**")
#
#@bot.command()
#async def 지짐시(ctx):
#    global next_time
#    print(datetime.now(timezone('Asia/Seoul')).strftime("%H:%M"), "지짐시 호출됨")
#    print(next_time)
#    await ctx.channel.send(f'다음 지짐시는 {next_time}입니다.')

@bot.command()
async def 진정(ctx):
    await ctx.channel.send(f"{ctx.message.mentions[0].mention}, {ctx.message.author.mention}(이)가 진정하래")

@bot.event #지민 진정 기능
async def on_message(message):
    if "ㅅㅂ" in message.content:
        msg = await message.channel.send(f"{message.author.mention} 진정")
        await asyncio.sleep(0.5)
        await msg.delete()

bot.run(os.getenv('TOKEN'))
