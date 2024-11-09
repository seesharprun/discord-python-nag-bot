# Python Nag bot for Discord

Sample bot that sends a message at a configured interval

## Run it

1. Open dev environment (use GitHub Codespaces)

1. Create an *.env* file

1. Set these settings:

    ```dotenv
    DISCORD_TOKEN="<your-refresh-token>"
    DISCORD_CHANNEL_ID="<your-channel-id>"
    RUN_HOUR=08
    RUN_MINUTE=00
    ```

1. Install libraries

    ```shell
    pip install -r requirements.txt
    ```

1. Run the application

    ```shell
    python app.py
    ```

> [!NOTE]
> In this example, the bot will run every morning at 8:00 AM in the EDT time zone.

## Read more

- <https://discordpy.readthedocs.io/en/stable/faq.html#where-can-i-find-usage-examples>
- <https://stackoverflow.com/questions/64167141/how-do-i-schedule-a-function-to-run-everyday-at-a-specific-time-in-discord-py>
