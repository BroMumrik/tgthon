from telethon import TelegramClient
import time
# Use your own values from my.telegram.org
api_id = 12598647
api_hash = 'a3d74b73afec8463d2900b74b33e10d3'

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('anon', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))

async def main():
    while True:
        await client.send_message(-1001672659116, 'заразить рандом слабее')
        time.sleep(5)
        await client.send_message(-1001738283601, 'заразить рандом слабее')
        time.sleep(3600)


with client:
    client.loop.run_until_complete(main())