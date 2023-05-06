import discord
from discord.ext import commands
from aiohttp import ClientSession

bot = commands.Bot(command_prefix='=', self_bot=True, help_command=None)

token = #enter your accounts token here
webhook_url = #enter the url of your webhook here

@bot.event
async def on_connect():
  print("Connected as "+bot.user.name+"#"+bot.user.discriminator)

@bot.event
async def on_message(ctx):
  if ctx.channel.id==915274436347826227:
    async with ClientSession() as session:
      webhook = discord.Webhook.from_url(webhook_url, adapter=discord.AsyncWebhookAdapter(session))
      await webhook.send(content=str(ctx.content).replace("@", "[at]"), username=ctx.author.name, avatar_url=ctx.author.avatar_url)

bot.run(token)
