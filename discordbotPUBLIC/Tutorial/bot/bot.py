import logging, hikari, lightbulb

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import utc # This is needed for the scheduler

# Set up the bot class
class Bot(lightbulb.BotApp):
    def __init__(self) -> None:
        self.scheduler = AsyncIOScheduler()     
        self.scheduler.configure(timezone=utc)  # Set up the scheduler

        # This is where your Discord bot token is stored, keep this safe! It is like a password and can compromise your Discord account if you loose it
        with open("notsecret.txt", mode="r", encoding="utf-8") as f:
            token = f.read().strip()

        super().__init__(
            token = token,
            default_enabled_guilds=(1074027606296494100),   # This is your guild ID for testing your bot
                                                            # you should remove then when making it global
            help_slash_command=False,       # Dissables the automatic help command
            intents = hikari.Intents.ALL    # This sets your intents
        )

    def run(self) -> None:
        self.event_manager.subscribe(hikari.StartingEvent, self.on_starting)    # Triggered when the bot is starting
        self.event_manager.subscribe(hikari.StartedEvent, self.on_started)      # Triggered when the bot has started
        self.event_manager.subscribe(hikari.StoppingEvent, self.on_stopping)    # Triggered when the bot is stopping
        self.event_manager.subscribe(hikari.StoppedEvent, self.on_stopped)      # Triggered when the bot has stopped

        with open("Tutorial/version.txt") as file:
            version = file.read().strip() # Just personal preference but I like versioning :)

        super().run(
            activity=hikari.Activity(
                name=f"Version {version}",          # Displays on the side, discord presence in this case
                type=hikari.ActivityType.PLAYING    # This can be PLAYING, LISTENING, WATCHING or COMPETING
                                                    # In this case "Playing Version 0.0.1"
            )
        )

    # These are all the functions that get called when an event we subscribed to earlier gets triggered
    async def on_starting(self, event: hikari.StartingEvent) -> None:
        self.load_extensions_from("./Tutorial/bot/extensions") # Load all extensions from the extensions dir
        logging.info("All extensions loaded")

    async def on_started(self, event: hikari.StartedEvent) -> None:
        self.scheduler.start()
        await self.update_presence(status=hikari.Status.ONLINE)
        logging.info("BOT READY")

    async def on_stopping(self, event: hikari.StoppingEvent) -> None:
        self.scheduler.shutdown()
        await self.update_presence(status=hikari.Status.DO_NOT_DISTURB)
        logging.info("BOT STOPPING")

    async def on_stopped(self, event:hikari.StoppedEvent) -> None:
        logging.info("BOT STOPPED")
