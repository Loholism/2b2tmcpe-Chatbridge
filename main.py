import discord
from discord.ext import commands
from aiohttp import ClientSession

b=commands.Bot(command_prefix='=', self_bot=True, help_command=None)

TOKEN = "" #Put your accout token in the parenthesies... google how to find it then copy it from the page WITHOUT the parenthesies that are shown.

@b.event
async def on_connect():
  print("Stay halal")
  await b.change_presence(status=discord.Status.invisible)

@b.event
async def on_message(ctx):
  if ctx.channel.id==915274436347826227:
    if ctx.author.id==700275401314009168:
      channel=b.get_channel("") #enter the id of the channel you want to have the bot send its messages to
      content=str(ctx.content).replace("@", "[at]")
      await ctx.channel.send(content)
    else:
      WEBHOOK_URL="" #enter your webhook url here
      async with ClientSession() as session:
        webhook = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.AsyncWebhookAdapter(session))
        await webhook.send(content=str(ctx.content).replace("@", "[at]"), username=ctx.author.name, avatar_url=ctx.author.avatar_url)

b.run(TOKEN)
