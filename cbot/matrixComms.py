from nio import (AsyncClient, SyncResponse, RoomMessageText)
import getpass as gpass
import asyncio
from exchangecomms import crypto_values
import json

from nio.crypto import device


# Import json secrets
def secrets_import():
    file_path = r"./cbot/secrets.json"
    f = open(file_path)
    data = json.load(f)
    usrname = data["secrets"]["usrname"]
    roomID = data["secrets"]["roomID"]
    access_token = data["secrets"]["access_token"]

    return usrname, roomID, access_token




# Asynchronous password function
async def get_pass():
    pswd = gpass.getpass()
    return pswd

async def main():
    usrname, roomID, access_token = secrets_import()

    # Creating of asynchronous cliend and providing all critical values besides password
    async_client = AsyncClient("https://matrix.org", usrname)
    async_client.user_id = usrname
    async_client.access_token = access_token

    # Recieving Return values from cryto values function
    str1, str2 = crypto_values()

    # Formatting message
    header = "Bitcoin Update\n" + 50*"-" + "\n"
    msg = f"{header}{str1}\n{str2}"

    # Sending message using async client

    await async_client.room_send(
            roomID,
            message_type="m.room.message",
            content={
                "msgtype": "m.text",
                "body": msg
            }
        )
    await async_client.close()

# Windows only event loop policy
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


asyncio.run(main())