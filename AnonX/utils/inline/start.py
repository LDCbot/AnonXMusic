from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AnonX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𖨆.ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ.𖨆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="⁂.ʜᴇʟᴩ.⁂",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="♪.ᴅᴇᴠᴇʟᴏᴘᴇʀ.♪", user_id=OWNER),
            InlineKeyboardButton(
                text="ᴥ︎︎︎.sᴜᴩᴩᴏʀᴛ.ᴥ︎︎︎", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="𖨆.ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.𖨆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⁂.ʜᴇʟᴩ.⁂", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER),
            InlineKeyboardButton(
                text="ᴥ︎︎︎.sᴜᴩᴩᴏʀᴛ.ᴥ︎︎︎", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="☼︎.ғᴇᴅᴇʀᴀᴛɪᴏɴ.☼︎", url=f"https://t.me/Death_Soul_Federation"
                )
        ],
     ]
    return buttons
