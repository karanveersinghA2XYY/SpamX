
# RiZoeL X - Telegram Projects
# (c) 2022 - 2023 RiZoeL
# Don't Kang Bitch -!


import os
import sys
import asyncio
import datetime
import time
from SpamX import (HNDLR, SUDO_USERS, ALIVE_PIC, ALIVE_MSG, PING_MSG, __version__, start_time)
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import __version__ as pyro_vr             
                

pongg = PING_MSG if PING_MSG else "𝐊𝐕 -𝐱𝐃 °|"
RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/6b1e9e0212a148dc381e0.jpg"
Alivemsg = ALIVE_MSG if ALIVE_MSG else "𝐊𝐕 -𝐱𝐃 °|."


rizoel = f"⁂ {Alivemsg} ⁂\n\n"
rizoel += f"━───────╯•╰───────━\n"
rizoel += f"➠ **𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽** : `3.10.4`\n"
rizoel += f"➠ **𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝚅𝙴𝚁𝚂𝙸𝙾𝙽** : `{pyro_vr}`\n"
rizoel += f"➠ **𝙰𝙿𝙿𝙻𝙴 𝚇 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 **  : `{__version__}`\n"
rizoel += f"➠ **𝙶𝚁𝙾𝚄𝙿** : [Join.](https://t.me/AppleXEmpire)\n"
rizoel += f"━───────╮•╭───────━\n\n"
rizoel += f"➠ **𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴:** [•Repo•](https://github.com/RiZoeLX/SpamX)"


async def get_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      uptime = await get_time((time.time() - start_time))
      Fuk = await e.reply("**Pong !!**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await Fuk.edit_text(f"⌾ {pongg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴜᴘᴛɪᴍᴇ: `{uptime}` \n ༝ ᴠᴇʀsɪᴏɴ: `{__version__}`")



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
async def alive(xspam: Client, e: Message):
       if ".jpg" in RIZ_PIC or ".png" in RIZ_PIC:
              await xspam.send_photo(e.chat.id, RIZ_PIC, caption=rizoel)
       if ".mp4" in RIZ_PIC or ".MP4," in RIZ_PIC:
              await xspam.send_video(e.chat.id, RIZ_PIC, caption=rizoel)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["restart", "reboot"], prefixes=HNDLR))
async def reboot(xspam: Client, e: Message):
        reboot_text = "**Re-starting** \n\n __Wait For A While To Use it Again__ "
        await e.reply_text(reboot_text)
        try:
            xspam.disconnect()
        except Exception as e:
            pass
        args = [sys.executable, "-m", "SpamX"]
        os.execl(sys.executable, *args)
        quit()
