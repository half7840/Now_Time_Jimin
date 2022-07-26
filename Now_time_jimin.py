import discord
import time
import datetime
import sys
import zoneinfo
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands

bot = commands.Bot(command_prefix="./")

@bot.command
async def func():
    #await bot.wait_until_ready()
    await ctx.send("지짐시")
@bot.event
async def now_time():
    await client.wait.until_ready()
    channel = client.get_channel(915862213074493540)
    msg_send = False

    while True:
        if time.hour == 01 and time.minute == 11:
            await channel.send("지짐시")
            msg_sent = True
        else:
            msg_sent = True

        if time.hour == 02 and time.minute == 22:
            await channel.send("지짐시")
            msg_sent = True
        else:
            msg_sent = True
        
        if time.hour == 02 and time.minute == 06:
            await channel.send("지짐시")
            msg_sent = True
        else:
            msg_sent = True
        if time.hour == 03 and time.minute == 33:
            await channel.send("지짐시")
            msg_sent = True
        else:
            msg_sent = True

        if time.hour == 04  and time.minute == 44:
            await channel.send("지짐시")
            msg_sent = True
        else:
            msg_sent = True

        if time.hour == 05 and time.minute == 55:
            await channel.send("지짐시")
            msg_sent = True
        else:
            msg_sent = True

        if time.hour == 13  and time.minute == 11:
            await channel.send("지짐시")
            msg_sent = True
        else:
            msg_sent = True

        if time.hour == 14 and time.minute == 22:
            await channel.send("지짐시")
            msg_sent = True
        else:
            msg_sent = True

        if time.hour == 15  and time.minute == 33:
            await channel.send("지짐시")
            msg_sent = True
        else:
            msg_sent = True

        if time.hour == 16 and time.minute == 44:
            await channel.send("지짐시")
            msg_sent = True
        else:
            msg_sent = True

        if time.hour == 17 and time.minute == 55:
            await channel.send("지짐시")
            msg_sent = True
        else:
            msg_sent = True
#@bot.event
#async def on_ready():
    #scheduler = AsyncIOScheduler()

    #scheduler.add_job(func, CronTrigger(hour="01, 02, 03, 04, 05, 13, 14, 15, 16, 17", minute="11, 22, 33, 44, 55", second="0"))

    #scheduler.start()
@bot.command()
async def 소환(ctx):
    await ctx.send('쥐미나 @')

@bot.command()
async def 지짐시(ctx):
    nowtime = datetime.datetime.now()
    await ctx.send('쥐금 시간')
    await ctx.send(nowtime)

bot.run('MTAwMTUwOTg4Mjg4Njg4MTI4MA.GXRAe7.DXfc7RDPO_6wmfiVQIJ2eEVyl8qS6utg7Q22Fs')
