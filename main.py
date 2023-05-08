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
import re
from discord.utils import get
from discord.ext import commands
from discord.ext import tasks
from datetime import datetime
from datetime import date
from dotenv import load_dotenv
from pytz import timezone
from discord import option
load_dotenv()

intents = discord.Intents().all()
bot = discord.Bot(intents=intents, command_prefix="!")

openai.api_key = (os.getenv("OPENAI"))

SERVER_IDS = ["SERVER"]


#@bot.event
#async def on_ready():
#    print('다음으로 로그인합니다 : ')
#    print(bot.user.name)
#    print('로그인에 성공했습니다')
#    await now_time_jimin()

@bot.event
async def now_time_jimin():
    await bot.wait_until_ready()
    channel = bot.get_channel("CHANNEL")
    while not bot.is_closed():
        now = datetime.now(timezone('Asia/Seoul')).strftime('%H:%M')
        if now == '1:11' or now == '2:22' or now =='3:33' or now =='4:44' or now == '5:55' or now == '10:10' or now == '11:11' or now == '12:12' or now == '13:11' or now == '14:22' or now == '15:33' or now == '16:44' or now == '17:55' or now == '22:10' or now == '23:11':
            await channel.send("**지짐시**")
            await asyncio.sleep(60)
            await now_time_jimin()
        else:
            await asyncio.sleep(55)


history = dict()


def add_history(user: str, text: str, bot_answer: str):
    if not user in history:
        history[user] = []
    pair = dict(
        prompt=text,
        answer=bot_answer
    )
    history[user] = history[user][-9:] + [pair]


def get_history(user: str) -> list:
    if not user in history:
        return []
    return history[user]


def prompt_to_chat(user: str, prompt: str) -> str:
    previous = get_history(user)
    conversation = ""
    for chat in previous:
        conversation += f"Human: {chat['prompt']}\n" \
                        f"Bot: {chat['answer']}\n"
    return conversation + "\n" + f"Human: {prompt}"


def clean_bot_answer(answer: str) -> str:
    answer = answer.strip()
    answer = re.sub(r"^(\w.+\:) ", "", answer)
    return answer


def chat_with_gpt(
    user: str,
    prompt: str,
    max_tokens: int = None,
    use_history: bool = None
) -> str:
    if max_tokens is None:
        max_tokens = 200
    if use_history is None or use_history == True:
        prompt = prompt_to_chat(user, prompt)
    print('prompt:', prompt)
    bot_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.25
    )
    print('bot response:', bot_response)
    bot_answer = '\n'.join([clean_bot_answer(choice.text) for choice in bot_response.choices])
    add_history(user, prompt, bot_answer)
    return bot_answer


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await now_time_jimin()


@bot.event
async def on_connect():
    if bot.auto_sync_commands:
        await bot.sync_commands()
    print(f"{bot.user.name} connected.")


@bot.event
async def on_message(message):
    # print(message)

    user = message.author
    if user == bot.user:
        return

    text = message.content
    if text.startswith('!chat '):
        prompt = text[6:]
        try:
            # 여러 채널에서 다른 문맥을 갖고 싶다면
            # user 가 아니라 채널을 포함한 f"{user}{message.channel}" 로 변경
            bot_answer = chat_with_gpt(user, prompt)
            await message.channel.send(f"> Your prompt is: {prompt}\nAnswer: {bot_answer}")
        except:
            await message.channel.send(f"> Your prompt is: {prompt}\nSorry, Failed to answer")


@bot.slash_command(guild_ids=SERVER_IDS)
@option(
    name="prompt",
    type=str,
    description="프롬프트를 적어주세요."
)
@option(
    name="max_length",
    type=int,
    description="AI가 출력할 수 있는 최대 답변 길이. (기본값: 500)",
    required=False,
)
@option(
    name="refresh",
    type=str,
    description="대화를 새로 시작합니다. (yes or no)",
    required=False,
)
async def 지민아(context, prompt: str, max_length: int, refresh: str):
    await context.defer()
    try:
        user = context.author
        # 여러 채널에서 다른 문맥을 갖고 싶다면
        # user 가 아니라 채널을 포함한 f"{user}{context.channel}" 로 변경
        use_history = (refresh or 'no').startswith('n')
        bot_answer = chat_with_gpt(user, prompt, max_tokens=max_length, use_history=use_history)
        await context.respond(f"> {prompt}\n{bot_answer}")
    except Exception as err:
        await context.respond(f"> {prompt}\n" \
                              f"Sorry, failed to answer\n" \
                              f"> {str(err)}")


def summarize_prompt(prompt: str):
    bot_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt + "\nSummarize sentence under 2000 lengths:",
        max_tokens=3000,
        temperature=0.0
    )
    return '\n'.join([choice.text for choice in bot_response.choices])


def create_image_embed(title: str, description: str, url: str):
    embed = discord.Embed(
        title=title,
        description=description,
    )
    embed.set_thumbnail(url=url)
    embed.set_image(url=url)
    return embed


@bot.slash_command(guild_ids=SERVER_IDS)
@option(
    name="prompt",
    type=str,
    description="생성하고 싶은 이미지를 묘사해주세요."
)
@option(
    name="n",
    type=int,
    description="생성하고자 하는 이미지의 개수 (기본값: 1)",
    required=False,
)
@option(
    name="size",
    type=str,
    description="이미지 크기. 반드시 `256x256`, `512x512`, or `1024x1024` 중 하나." \
                "(기본값: 256x256)",
    required=False,
)
async def image(context, prompt: str, n: int, size: str):
    await context.defer()
    try:
        print("Image prompt:", prompt)
        response = openai.Image.create(
            prompt=prompt,
            n=n or 1,
            size=size or "256x256"
        )
        data: list = response['data']
        for index, image in enumerate(data):
            title = f"Image generated #{index+1}"
            embed = create_image_embed(title, prompt, image['url'])
            await context.send('', embed=embed)
        await context.respond(f"> Prompt: {prompt}")
    except Exception as err:
        await context.respond(f"> Prompt: {prompt}\n" \
                              f"Sorry, failed to answer\n" \
                              f"> {str(err)}")

#@bot.slash_command(guild_ids=SERVER_IDS)
#@commands.cooldown(1, 600, commands.BucketType.user)
#async def blade(ctx, member: discord.Member, messageid=int):
#    target = member
#    author = ctx.message.author
#    message = await ctx.channel.send(f'{author.mention}(이) {target.mention}을 향해 일기토를 신청합니다.')
#    await ctx.message.add_reaction("👍")
#    await ctx.message.add_reaction("👎")

#    def check(reaction, user):
#        return user == ctx.message.author and str(reaction.emoji) == '👍' or str(reaction.emoji) == '👎'
#    try:
#        reaction, user = await bot.wait_for('reaction_add', timeout=10.0, check=check)
#        if user == ctx.message.author:
#            reaction, user =await bot.wait_for('reaction_add', timeout=10.0, check=check)
#            await ctx.channel.send("신청자는 투표 할 수 없습니다. 10초 내에 다시 투표해주세요")
#        else:
#            await asyncio.TimeoutError

#   except asyncio.TimeoutError:
#        await ctx.channel.send('👎')
#    else:
#        if reaction.count > 2 and reaction.emoji == "👍":
#            await member.edit(voice_channel=None)
#            await ctx.channel.send(f'{target.mention}(이)가 일기토에 패배했습니다.')

#        else:
#            await member.edit(voice_channel=None)
#            await ctx.channel.send(f'{author.mention}(이)가 일기토에 패했습니다.')
#@blade.error
#async def blade_error(ctx, error):
#    if isinstance(error, commands.CommandOnCooldown):
#       await ctx.channel.send(f'{ctx.author.mention}는 쿨다운 중 입니다 {round(error.retry_after, 2)}초 후 다시 사용할 수 있습니다.')


bot.run(os.getenv('TOKEN'))


