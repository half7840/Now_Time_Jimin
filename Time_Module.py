from tkinter import NE
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

bot = commands.Bot(command_prefix="./")

current_time = datetime.now(timezone('Asia/Seoul')).strftime("%H:%M")
def set_next_jime():
    while True:
        if current_time > "01:11" and current_time < "02:22":
            next_jime = "02:22"
            print("다음 지짐시는", next_jime, "입니다.")
            break

        if current_time > "02:22" and current_time < "03:33":
            next_jime = "03:33"
            print("다음 지짐시는", next_jime, "입니다.")
            break

        if current_time > "03:33" and current_time < "04:44":
            next_jime = "04:44"
            print("다음 지짐시는", next_jime, "입니다.")
            break

        if current_time > "04:44" and current_time < "05:55":
            next_jime = "05:55"
            print("다음 지짐시는", next_jime, "입니다.")
            break

        if current_time > "05:55" and current_time < "10:10":
            next_jime = "10:10"
            print("다음 지짐시는", next_jime, "입니다.")
            break

        if current_time > "10:10" and current_time < "11:11":
            next_jime = "11:11"
            print("다음 지짐시는", next_jime, "입니다.")
            break

        if current_time > "11:11" and current_time < "12:12":
            next_jime = "12:12"
            print("다음 지짐시는", next_jime, "입니다.")
            break

        if current_time > "12:12" and current_time < "13:11":
            next_jime = "13:11"
            print("다음 지짐시는", next_jime, "입니다.")
            break

        if current_time > "13:11" and current_time < "14:22":
            next_jime = "14:22"
            print("다음 지짐시는", next_jime, "입니다.")
            break

        if current_time > "14:22" and current_time < "15:33":
            next_jime = "15:33"
            print("다음 지짐시는", next_jime, "입니다.")
            break

        if current_time > "15:33" and current_time < "16:44":
            next_jime = "16:44"
            print("다음 지짐시는", next_jime, "입니다.")
            break

        if current_time > "16:44" and current_time < "17:55":
            next_jime = "17:55"
            print("다음 지짐시는", next_jime, "입니다.")
            break

        if current_time > "17:55" and current_time < "22:10":
            next_jime = "22:10"
            print("다음 지짐시는", next_jime, "입니다.")
            break

        if current_time > "22:10" and current_time < "23:11":
            next_jime = "23:11"
            print("다음 지짐시는", next_jime, "입니다.")
            break

        if current_time > "23:11":
            next_jime = "01:11"
            print("다음 지짐시는", next_jime, "입니다.")
            break




#schedule.every().day.at("01:11").do(job) 
#schedule.every().day.at("02:22").do(job) 
#schedule.every().day.at("03:33").do(job) 
#schedule.every().day.at("04:44").do(job) 
#schedule.every().day.at("05:55").do(job) 
#schedule.every().day.at("").do(job) 
#schedule.every().day.at("").do(job) 
#schedule.every().day.at("").do(job) 
#schedule.every().day.at("").do(job) 
#schedule.every().day.at("").do(job) 
#schedule.every().day.at("").do(job) 
#schedule.every().day.at("").do(job) 
#schedule.every().day.at("").do(job) 
#schedule.every().day.at("").do(job) 
#schedule.every().day.at("").do(job) 
@bot.event
async def now_time_jimin():
    channel = bot.get_channel(915862213074493543)
    await channel.send("**<386099935163973634> 지짐시**")
    time.sleep(60)
    time_module()
