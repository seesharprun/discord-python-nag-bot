import datetime
import discord
import os
from dotenv import load_dotenv
from discord.ext import tasks, commands
import pytz

load_dotenv()

token = os.getenv("DISCORD_TOKEN")
if not token:
    raise ValueError('"DISCORD_TOKEN" is not set!')

channel_id_str = os.getenv("DISCORD_CHANNEL_ID")
if not channel_id_str:
    raise ValueError('"DISCORD_CHANNEL_ID" is not set!')
channel_id = int(channel_id_str)

run_hour_str = os.getenv("RUN_HOUR")
if not run_hour_str:
    raise ValueError('"RUN_HOUR" is not set!')
run_hour = int(run_hour_str)

run_minute_str = os.getenv("RUN_MINUTE")
if not run_minute_str:
    raise ValueError('"RUN_MINUTE" is not set!')
run_minute = int(run_minute_str)

time_zone = os.getenv("TIME_ZONE")
if not time_zone:
    raise ValueError('"TIME_ZONE" is not set!')

time_zone = pytz.timezone(time_zone)

schedule_times = [datetime.time(run_hour, run_minute, 0, 0, time_zone)]


class DiscordNagClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")
        print(f"Current time: {datetime.datetime.now(time_zone)}")

    async def setup_hook(self) -> None:
        self.loop_update.start()

    @tasks.loop(time=schedule_times)
    async def loop_update(self):
        print("Loop")
        channel = self.get_channel(channel_id)
        date = datetime.datetime.now(time_zone)
        date_string = date.strftime("%A, %B %d, %Y")
        message = f'⏰ - Good morning! Today is **{date_string}**...'
        await channel.send(message)

    @loop_update.before_loop
    async def before_loop(self):
        await self.wait_until_ready()


intents = discord.Intents.default()
intents.messages = True

client = DiscordNagClient(intents=intents)
client.run(token)
