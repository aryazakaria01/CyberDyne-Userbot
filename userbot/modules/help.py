# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot help command"""

import asyncio
from userbot import CMD_HELP, DEFAULTUSER
from userbot.events import register

modules = CMD_HELP


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit(
                f"#WRONG\n**PLUGIN** : `{args}` ❌ **\nMohon Ketik Nama Plugin Dengan Benar.**"
            )
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t|  "
        await event.edit("⚡")
        await asyncio.sleep(2.5)
        await event.edit(
            f"**[⚡ℂ𝕪𝕓𝕖𝕣𝔻𝕪𝕓𝕖-𝕌𝕤𝕖𝕣𝕓𝕠𝕥⚡](t.me/Badboyanim01_bot)**\n\n"
            f"**◑» Bᴏᴛ ᴏꜰ {DEFAULTUSER}**\n**◑» Pʟᴜɢɪɴ : {len(modules)}**\n\n"
            "**• Mᴀɪɴ Mᴇɴᴜ :**\n"
            f"╰►| {string} ◄─\n\n"
            f"**License : [Raphielscape Public License 1.d](https://github.com/aryazakaria01/CyberDyne-Userbot/blob/CyberDyne-Userbot/LICENSE)**\n"
            f"**Copyright © 2021 [CyberDyne-Userbot LLC Company](https://aryazakaria01.github.io/CyberDyne-Userbot/)**"
        )
        await event.reply(
            "\n**Contoh** : Ketik » `.help admin` Untuk Informasi Pengunaan Plugin Admin."
        )

        await asyncio.sleep(1000)
        await event.delete()
