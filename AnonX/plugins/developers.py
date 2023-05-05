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

#       #             #  #####  #####      ####
#        #           #  #         #            #     #
#          #        #  #####   #            #####     
#           #    #    #          #     ##    #     #
#              #       #####   ######   #     #
                
                
@app.on_message(
    command(["مطورين سي ار","المطورين","مطورين","مطورين cr"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/be8fb2f02cf57e1725ccd.jpg",
        caption=f"""**⩹━★⊷━⌞ 𝐂𝐑𝐘𝐒𝐓𝐀𝐋  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين cr ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 𝐂𝐑𝐘𝐒𝐓𝐀𝐋  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒『𝐂𝐑𝐘𝐒𝐓𝐀𝐋 🥱 ⏎ 』⌯►", url=f"https://t.me/ssxhh"), 
                 ],[
                    InlineKeyboardButton(
                        "group help", url=f"https://t.me/ppblb"),
                ],[
                    InlineKeyboardButton(
                        "source", url=f"https://t.me/no1bros"),
                    InlineKeyboardButton(
                        "crystal", url=f"https://t.me/ssxhh"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐂𝐑𝐘𝐒𝐓𝐀𝐋  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡", url=f"https://t.me/NO1BROS"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["مطور السورس","كرستال","كرس","مبرمج","كرستال","كرستال" ,"المطور"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("ssxhh")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐂𝐑𝐘𝐒𝐓𝐀𝐋  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐂𝐑𝐘𝐒𝐓𝐀𝐋  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["كرستالتي انجم","كرستالتي","كرستالتي","بوكمان","كرستالتي","pokman"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("ssxhh")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐂𝐑𝐘𝐒𝐓𝐀𝐋  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐂𝐑𝐘𝐒𝐓𝐀𝐋  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["كرستال انجم","كرستال","كرستال","كرستال","crystal","كرستالتي"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("ssxhh")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝐂𝐑𝐘𝐒𝐓𝐀𝐋  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━⌞ 𝐂𝐑𝐘𝐒𝐓𝐀𝐋  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/be8fb2f02cf57e1725ccd.jpg",
        caption=f"""**⩹⊷━⌞ 𝐂𝐑𝐘𝐒𝐓𝐀𝐋  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس cr\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ 𝐂𝐑𝐘𝐒𝐓𝐀𝐋  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒『𝐂𝐑𝐘𝐒𝐓𝐀𝐋 🥱 ⏎ 』⌯‹", url=f"https://t.me/ssxhh"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝐂𝐑𝐘𝐒𝐓𝐀𝐋  • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡", url=f"https://t.me/NO1BROS"),
                ],

            ]

        ),

    )



    
