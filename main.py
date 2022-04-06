import discord
from discord.ext import commands
from aiohttp import ClientSession

b=commands.Bot(command_prefix='=', self_bot=True, help_command=None)

TOKEN = #enter your accounts token here

blacklist=["EDestroyer10", "Pyrobyte6948", "Bloominghat7956", "GalaxyGamer661", "KLP SUPRISE", "Chaos agent5246", "ExtinctOpti"]

@b.event
async def on_connect():
  print("Stay halal")
  await b.change_presence(status=discord.Status.invisible)

@b.event
async def on_message(ctx):
  if ctx.channel.id==915274436347826227:
    if ctx.author.id==700275401314009168:
      channel=b.get_channel()#enter the id of the channel you want to have the bot send its messages to
      content=str(ctx.content).replace("@", "[at")
      for i in blacklist:
        if content==f":green_circle: {i} joined the server":
          content+=" "
          break
      await channel.send(content)
    else:
      WEBHOOK_URL="https://discord.com/api/webhooks/961344091348668496/opAAEByYqKBCtlmTdIZ6QV0GACfhJC4GO8_ssLCeNHFDADJU-iM9K_AeKhUn6a7Gji1v"
      async with ClientSession() as session:
        webhook = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.AsyncWebhookAdapter(session))
        await webhook.send(content=str(ctx.content).replace("@", "[at]"), username=ctx.author.name, avatar_url=ctx.author.avatar_url)

b.run(TOKEN)
