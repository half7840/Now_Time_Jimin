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
    await client.wait.uni


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
