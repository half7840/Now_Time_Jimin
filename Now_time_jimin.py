import discord
import time
import datetime
import zoneinfo
import pytz
import asyncio
import tasks
from discord.ext import commands
from discord.ext import tasks
from datetime import datetime
from datetime import date
from pytz import timezone
bot = commands.Bot(command_prefix="./")

current_time = datetime.now(timezone('Asia/Seoul')).strftime("%H:%M")

next_time = 0 
@bot.event
async def on_ready():
    print('다음으로 로그인합니다 : ')
    print(bot.user.name)
    print('로그인에 성공했습니다')
    await bot.change_presence(status=discord.Status.online, activity=None)
    await cal_time()    

def set_next_time():
    global next_time
    while True:
        if current_time > "01:11" and current_time < "02:22":
            next_time = "02:22"
            break

        if current_time > "02:22" and current_time < "03:33":
            next_time = "03:33"
            break

        if current_time > "03:33" and current_time < "04:44":
            next_time = "04:44"
            break

        if current_time > "04:44" and current_time < "05:55":
            next_time = "05:55"
            break

        if current_time > "05:55" and current_time < "10:10":
            next_time = "10:10"
            break

        if current_time > "10:10" and current_time < "11:11":
            next_time = "11:11"
            break

        if current_time > "11:11" and current_time < "12:12":
            next_time = "12:12"
            break

        if current_time > "12:12" and current_time < "13:11":
            next_time = "13:11"
            break

        if current_time > "13:11" and current_time < "14:22":
            next_time = "14:22"
            break

        if current_time > "14:22" and current_time < "15:33":
            next_time = "15:33"
            break

        if current_time > "15:33" and current_time < "16:44":
            next_time = "16:44"
            break

        if current_time > "16:44" and current_time < "17:55":
            next_time = "17:55"
            break

        if current_time > "17:55" and current_time < "22:10":
            next_time = "22:10"
            break

        if current_time > "22:10" and current_time < "23:11":
            next_time = "23:11"
            break

        if current_time > "23:11":
            next_time = "01:11"
            break

@bot.event
async def now_time_jimin():
    channel = bot.get_channel(915862213074493543)
    await channel.send("**<@386099935163973634> 지짐시**")
    await asyncio.sleep(60)
    await cal_time()

async def cal_time():
    set_next_time()
    while True:
        if current_time==next_time:
            await now_time_jimin()
            break
        else:
            if current_time!=next_time:
                await asyncio.sleep(60)
                await cal_time()
                break

@bot.command()
async def 지짐시(ctx):
    global next_time
    print(current_time)
    await ctx.channel.send(f'다음 지짐시는 {next_time}입니다.')

#@bot.event #지민 진정 기능
#async def on_message(message):
#    if "ㅅㅂ" in message.content: 
#        msg = await message.channel.send(f"{message.author.mention} 진정")
#        await asyncio.sleep(0.5)
#       await msg.delete()

now = datetime.now()
time = f"{str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분 {str(now.second)}초"

@bot.event
async def on_message_delete(message):
    channel = bot.get_channel(1004447909359657041)
    embed = discord.Embed(title=f"삭제됨", description=f"유저 : {message.author.mention} 채널 : {message.channel.mention}", color=0xFF0000)
    embed.add_field(name="삭제된 내용", value=f"내용 : {message.content}", inline=False)
    embed.set_footer(text=f"{message.guild.name} | {time}")
    await channel.send(embed=embed)

bot.run("MTAwMTUwOTg4Mjg4Njg4MTI4MA.GoEBhL.kDyy0fl7LIU3MMmoEpA8BF8rK7h0Qjd_Qbc7iw")
