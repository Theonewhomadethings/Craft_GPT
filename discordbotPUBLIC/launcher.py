import logging, os

from Tutorial.bot import Bot
from datetime import datetime

if os.name != 'nt': # A better, faster version of asyncio for Linux
    import uvloop
    uvloop.install()

def rename_log():
    os.rename("logs/latest.txt", f"logs/{datetime.now().strftime('%d-%m-%Y %I-%M-%S-%p')}.txt")

if __name__ == '__main__':
    # Does some logging stuff, have a play around with it if you want to
    """
    if os.path.exists("logs/latest.txt"):
        rename_log() # prevents overiding a log in the event the bot hard crashed
    elif not os.path.exists("logs/"):
        os.mkdir("logs/")
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%d-%m-%Y %H:%M:%S', filename="logs/latest.txt", encoding="utf-8", level=logging.INFO) # Open a logging file
    """
    bot = Bot()
    bot.run()   # This runs your bot. It is a blocking call so nothing wil run after this until the bot has exited

    logging.shutdown() # Stops the logging and allows for the file to be renamed
    #rename_log()
