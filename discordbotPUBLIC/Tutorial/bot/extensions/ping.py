import hikari, lightbulb, time

from Tutorial.bot import Bot   

plugin = lightbulb.Plugin("embed")


@plugin.command()
@lightbulb.command("embed", "Magic Function POWA", auto_defer = True)
@lightbulb.implements(lightbulb.SlashCommand)

#async def ping(ctx: lightbulb.SlashContext)->None:
 #   time.sleep(5)
#    await ctx.respond("Pong")

async def embed(ctx: lightbulb.SlashContext)-> None:
    embed = hikari.Embed(
        title = "my first embed",
        colour= "FFFFFF"
    )
    time.sleep(5)
    with open("message.txt", "r") as f:
        contents = f.read()
    

    embed.add_field("Reading from txt file attempt 1", contents)
    await ctx.respond(embed=embed)
async def listning(ctx: lightbulb.SlashContext)->None:
    await plugin.bot_update_presence

def load(bot: Bot):
    bot.add_plugin(plugin)

def unload(bot: Bot):
    bot.remove_plugin("ping")