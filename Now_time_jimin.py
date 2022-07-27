import discord
import time
import datetime
import sys
import zoneinfo
import pytz
import asyncio
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands
from datetime import datetime
from datetime import date
from pytz import timezone

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

        if current_time == "10:10":
            print("time module ended")
            break

        if current_time == "11:11":
            print("time module ended")
            break

        if current_time == "12:12":
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
    await channel.send("**<@386099935163973634> 지짐시**")
    time.sleep(60)
    time_module()

bot.run("MTAwMTUwOTg4Mjg4Njg4MTI4MA.GoEBhL.kDyy0fl7LIU3MMmoEpA8BF8rK7h0Qjd_Qbc7iw")
