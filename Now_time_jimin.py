import discord
import time
import datetime
import sys
import zoneinfo
import pytz
import asyncio
import schedule
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands
from datetime import datetime
from datetime import date
from pytz import timezone

datetime.now(timezone('Asia/Seoul'))
time = datetime.now(timezone('Asia/Seoul'))
bot = commands.Bot(command_prefix="./")
def time_module():
    print("time module in use")
    while True:
        current_time = datetime.now(timezone('Asia/Seoul')).strftime("%H:%M")
        if current_time == "01:11":
            print("time module ended")
            break

        if current_time == "02:22":
            print("time module ended")
            break
        
        if current_time == "03:33":
            print("time module ended")
            break
        
        if current_time == "04:44":
            print("time module ended")
            break
        
        if current_time == "05:55":
            print("time module ended")    
            break

        if current_time == "13:11":
            print("time module ended")
            break

        if current_time == "14:22":
            print("time module ended")
            break

        if current_time == "15:33":
            print("time module ended")
            break

        if current_time == "16:44":
            print("time module ended")
            break

        if current_time == "17:55":
            print("time module ended")
            break

time_module()

@bot.event
async def on_ready():
    channel = bot.get_channel(915862213074493543)
    await channel.send(f"지짐시, {386099935163973634}")
@bot.command()
async def 소환(ctx):
    await ctx.send('쥐미나 @')

@bot.command()
async def 지짐시(ctx):
    nowtime = datetime.now(timezone('Asia/Seoul'))
    await ctx.send('쥐금 시간')
    await ctx.send(nowtime)

bot.run('MTAwMTUwOTg4Mjg4Njg4MTI4MA.GXRAe7.DXfc7RDPO_6wmfiVQIJ2eEVyl8qS6utg7Q22Fs')
