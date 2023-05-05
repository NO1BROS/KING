import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from AnonX.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 10:
        bar = "â—‰â€”â€”â€”â€”â€”â€”â€”â€”â€”"
    elif 10 < anon < 20:
        bar = "â€”â—‰â€”â€”â€”â€”â€”â€”â€”â€”"
    elif 20 <= anon < 30:
        bar = "â€”â€”â—‰â€”â€”â€”â€”â€”â€”â€”"
    elif 30 <= anon < 40:
        bar = "â€”â€”â€”â—‰â€”â€”â€”â€”â€”â€”"
    elif 40 <= anon < 50:
        bar = "â€”â€”â€”â€”â—‰â€”â€”â€”â€”â€”"
    elif 50 <= anon < 60:
        bar = "â€”â€”â€”â€”â€”â—‰â€”â€”â€”â€”"
    elif 60 <= anon < 70:
        bar = "â€”â€”â€”â€”â€”â€”â—‰â€”â€”â€”"
    elif 70 <= anon < 80:
        bar = "â€”â€”â€”â€”â€”â€”â€”â—‰â€”â€”"
    elif 80 <= anon < 95:
        bar = "â€”â€”â€”â€”â€”â€”â€”â€”â—‰â€”"
    else:
        bar = "â€”â€”â€”â€”â€”â€”â€”â€”â€”â—‰"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="â–·",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="â˜†", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="â€£â€£I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="â–¢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="âŒž ð˜¾ð™ ð–¢» âŒ¯ ÙŽÙð™ˆÙŽÙð™ÙŽÙð™ŽÙŽÙð™„ÙŽÙð˜¾ âŒ¯ Ë¹ðŸŽ§Ë¼â©", url=f"https://t.me/no1bros"
            )
        ],
        [
            InlineKeyboardButton(
                text="âœ¯ á´„ÊŸá´sá´‡ âœ¯", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 10:
        bar = "â—‰â€”â€”â€”â€”â€”â€”â€”â€”â€”"
    elif 10 < anon < 20:
        bar = "â€”â—‰â€”â€”â€”â€”â€”â€”â€”â€”"
    elif 20 <= anon < 30:
        bar = "â€”â€”â—‰â€”â€”â€”â€”â€”â€”â€”"
    elif 30 <= anon < 40:
        bar = "â€”â€”â€”â—‰â€”â€”â€”â€”â€”â€”"
    elif 40 <= anon < 50:
        bar = "â€”â€”â€”â€”â—‰â€”â€”â€”â€”â€”"
    elif 50 <= anon < 60:
        bar = "â€”â€”â€”â€”â€”â—‰â€”â€”â€”â€”"
    elif 60 <= anon < 70:
        bar = "â€”â€”â€”â€”â€”â€”â—‰â€”â€”â€”"
    elif 70 <= anon < 80:
        bar = "â€”â€”â€”â€”â€”â€”â€”â—‰â€”â€”"
    elif 80 <= anon < 95:
        bar = "â€”â€”â€”â€”â€”â€”â€”â€”â—‰â€”"
    else:
        bar = "â€”â€”â€”â€”â€”â€”â€”â€”â€”â—‰"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="â–·",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="â€£â€£I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="â–¢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="âŒž ð˜¾ð™ ð–¢» âŒ¯ ÙŽÙð™ˆÙŽÙð™ÙŽÙð™ŽÙŽÙð™„ÙŽÙð˜¾ âŒ¯ Ë¹ðŸŽ§Ë¼â©", url=f"https://t.me/no1bros"
            )
        ],
        [
            InlineKeyboardButton(
                text="âœ¯ á´„ÊŸá´sá´‡ âœ¯", callback_data=f"close"
            )
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="â–·",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="â˜†", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="â€£â€£I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="â–¢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="âŒž ð˜¾ð™ ð–¢» âŒ¯ ÙŽÙð™ˆÙŽÙð™ÙŽÙð™ŽÙŽÙð™„ÙŽÙð˜¾ âŒ¯ Ë¹ðŸŽ§Ë¼â©", url=f"https://t.me/no1bros"
            )
        ],
        [
            InlineKeyboardButton(
                text="âœ¯ á´„ÊŸá´sá´‡ âœ¯", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="â–·",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="â€£â€£I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="â–¢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="âŒž ð˜¾ð™ ð–¢» âŒ¯ ÙŽÙð™ˆÙŽÙð™ÙŽÙð™ŽÙŽÙð™„ÙŽÙð˜¾ âŒ¯ Ë¹ðŸŽ§Ë¼â©", url=f"https://t.me/no1bros"
            )
        ],
        [
            InlineKeyboardButton(
                text="âœ¯ á´„ÊŸá´sá´‡ âœ¯", callback_data=f"close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="â—",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="â–·",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="âœ¯ á´„ÊŸá´sá´‡ âœ¯", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="â–·",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="â˜†", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="â€£â€£I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="â–¢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="âŒž ð˜¾ð™ ð–¢» âŒ¯ ÙŽÙð™ˆÙŽÙð™ÙŽÙð™ŽÙŽÙð™„ÙŽÙð˜¾ âŒ¯ Ë¹ðŸŽ§Ë¼â©", url=f"https://t.me/no1bros"
            )
        ],
        [
            InlineKeyboardButton(
                text="âœ¯ á´„ÊŸá´sá´‡ âœ¯", callback_data=f"close"
            )
        ],
    ]
    return buttons
