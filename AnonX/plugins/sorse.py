import asyncio 
 
import os 
import config 
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
        caption=f"""𝘛𝘏𝘌 𝘉𝘌𝘚𝘛 𝘚𝘖𝘜𝘙𝘊𝘌 𝘖𝘕 𝘛𝘌𝘓𝘌𝘎𝘙𝘈𝘔""", 
        reply_markup=InlineKeyboardMarkup( 
            [ 
                [ 
                    InlineKeyboardButton( 
                        "ꪑꪗ ᦔꫀꪜ", url=f"https://t.me/ssxhh"),  
                 
                    InlineKeyboardButton( 
                        "ᧁ𝘳ꪮꪊρ ᥴ𝘳", url=f"https://t.me/ppblb"), 
                ],[ 
                    InlineKeyboardButton( 
                        "⌞ 𝐂𝐑𝐘𝐒𝐓𝐀𝐋 • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝", url=f"https://t.me/no1bros"), 
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
                            
                            
                            @app.on_message(command(["صوره", "🕷", "صورهه", "صور"]))

async def ihd(client: Client, message: Message):

    rl = random.randint(2,50)

    url = f"https://t.me/vnnkli/{rl}"

    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار صوره لـك",parse_mode="html",

    reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")

                ],

            ]

        )

    )

@app.on_message(command(["انميي", "انمي"]))

async def ihd(client: Client, message: Message):

    rl = random.randint(2,90)

    url = f"https://t.me/LoreBots7/{rl}"

    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار انمي لـك",parse_mode="html",

    reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")

                ],

            ]

        )

    )

@app.on_message(command(["متحركه. 🎬", "متحركه"]))

async def ihd(client: Client, message: Message):

    rl = random.randint(2,90)

    url = f"https://t.me/GifWaTaN/{rl}"

    await client.send_animation(message.chat.id,url,caption="🐉 ¦ تـم اختيـار ملصق لـك",parse_mode="html",

    reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")

                ],

            ]

        )

    )

@app.on_message(command(["اقتباسات", "اقتباس"]))

async def ihd(client: Client, message: Message):

    rl = random.randint(2,90)

    url = f"https://t.me/LoreBots9/{rl}"

    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار اقتباس لـك",parse_mode="html",

    reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")

                ],

            ]

        )

    )

@app.on_message(command(["هيدرا", "هيدرات"]))

async def ihd(client: Client, message: Message):

    rl = random.randint(2,90)

    url = f"https://t.me/flflfldld/{rl}"

    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار هيدرات لـك",parse_mode="html",

    reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")

                ],

            ]

        )

    )

@app.on_message(command(["صور", "افتار بنات"]))

async def ihd(client: Client, message: Message):

    rl = random.randint(2,90)

    url = f"https://t.me/vvyuol/{rl}"

    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار صوره لـك",parse_mode="html",

    reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")

                ],

            ]

        )

    )

@app.on_message(command(["صور شباب", "افتار شباب"]))

async def ihd(client: Client, message: Message):

    rl = random.randint(2,90)

    url = f"https://t.me/vgbmm/{rl}"

    await client.send_photo(message.chat.id,url,caption="🐉 ¦ تـم اختيـار صوره لـك",parse_mode="html",

    reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")

                ],

            ]

        )

    )

@app.on_message(command(["سوره", "قران"]))

async def ihd(client: Client, message: Message):

    rl = random.randint(1,90)

    url = f"https://t.me/opuml/{rl}"

    await client.send_voice(message.chat.id,url,caption="🐉 ¦ تـم اختيـار ايـه قرآنيه لـك",parse_mode="html",

    reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")

                ],

            ]

        )

    )

@app.on_message(command(["الشيخ", "النقشبندي", "نقشبندي"]))

async def ihd(client: Client, message: Message):

    rl = random.randint(1,90)

    url = f"https://t.me/ggcnjj/{rl}"

    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار الشيخ نقشبندي لـك",parse_mode="html",

    reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")

                ],

            ]

        )

    )

@app.on_message(command(["فيلم", "فيلمك. 🎥"]))

async def ihd(client: Client, message: Message):

    rl = random.randint(1,50)

    url = f"https://t.me/gyigkk/{rl}"

    await client.send_audio(message.chat.id,url,caption="🐉 ¦ تـم اختيـار فيلم لـك",parse_mode="html",

    reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")

                ],

            ]

        )

    )

@app.on_message(command(["استوري", "استوريهات. 🥹"]))

async def ihd(client: Client, message: Message):

    rl = random.randint(1,50)

    url = f"https://t.me/yoipopl/{rl}"

    await client.send_audio(message.chat.id,url,caption="🐉 ¦ تـم اختيـار استوري لـك",parse_mode="html",

    reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")

                ],

            ]

        )

    )
    )
