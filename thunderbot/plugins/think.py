from telethon import events
import asyncio
from thunderbot import CMD_HELP
from thunderbot.utils import admin_cmd

@thunderbot.on(admin_cmd("think"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 288)
    
    await event.edit("thinking")
    animation_chars = [
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING... 🤔"
        ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 72])
CMD_HELP.update(
    {
        "think": "➟ `.think \nUse - Think Think Think"
    }
)
