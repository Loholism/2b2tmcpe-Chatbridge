import discord
from discord.ext import commands
from aiohttp import ClientSession
from keep_alive import keep_alive
import os

b=commands.Bot(command_prefix='=', self_bot=True, help_command=None)

TOKEN = os.environ.get('TOKEN')

@b.event
async def on_connect():
  print("Stay halal")
  await b.change_presence(status=discord.Status.invisible)

@b.event
async def on_message(ctx):
  if ctx.channel.id==523687931483783168:
    if ctx.author.id==493718266628407306:
      channel=b.get_channel(984851691646107739) 
      content=str(ctx.content).replace("@", "[at]")
      await channel.send(content)
    else:
      WEBHOOK_URL="https://discordapp.com/api/webhooks/984872386207838300/qUje8oGc0gLo_oharqT5uTAk5CUr04H155YgeqHi1o0luJsVJdJFsTPCnDd-iNQBwyqK" #enter your webhook url here
      async with ClientSession() as session:
        webhook = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.AsyncWebhookAdapter(session))
        await webhook.send(content=str(ctx.content).replace("@", "[at]"), username=ctx.author.name, avatar_url=ctx.author.avatar_url)

keep_alive()
b.run(TOKEN)