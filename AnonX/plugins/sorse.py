
import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

@app.on_message(
    command(["سورس مين","سورس","السورس","سورسي", "cr"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1488d38c8157537b9213f.jpg",
        caption=f"""╭═★⊷⌯⧼[⌞ 𝐂𝐑𝐘𝐒𝐓𝐀𝐋 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝](https://t.me/NO1BROS )⧽⌯⊶★═╮\n★‹ [⌞ 𝐂𝐑𝐘𝐒𝐓𝐀𝐋 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝𝐀](https://t.me/NO1BROS)\n★‹ [ 𝐌𝐔𝐒𝐈𝐂 『 𝒃𝒐𝒕 ⏎ 』](https://t.me/K0HBOT?startgroup=true)\n★‹ [『𝐂𝐑𝐘𝐒𝐓𝐀𝐋 ⏎ 』](https://t.me/ssxhh)\n★‹ [group help ](https://t.me/ppblb)\n╰═★⊷⌯⧼[⌞ 𝐂𝐑𝐘𝐒𝐓𝐀𝐋 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝](https://t.me/NO1BROS)⧽⌯⊶★═╯\n ⍟ Welcome to source 𝐂𝐑𝐘𝐒𝐓𝐀𝐋 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "『𝐂𝐑𝐘𝐒𝐓𝐀𝐋 ⏎ 』༄►", url=f"https://t.me/ssxhh"), 
                ],[
                    InlineKeyboardButton(
                        "⌞ 𝐂𝐑𝐘𝐒𝐓𝐀𝐋 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡️", url=f"https://t.me/NO1BROS"),
                ],[
                    InlineKeyboardButton(
                        "𝐀𝐃𝐃 𝐌𝐄💞", url=f"https://t.me/K0HBOT?startgroup=true"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )


@app.on_message(command(["صور","صوره"]))
async def ihd(client: Client, message: Message):
    rs = random.randint(39,148)
    url = f"https://t.me/GTTUTY/{rs}"
    await client.send_photo(message.chat.id,url,caption="💕 ¦ تـم اختيـار الصوره لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )


