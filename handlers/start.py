from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey, I'm  {bn}, an open-source bot that lets you play music in your Telegram groups.If u need any help contact me @Legend_Mr_Hacker.\n\n The Assistant must be in your group to play music in the voice chat of your group.\n\n /help to know my commands**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐎𝐖𝐍𝐄𝐑👿", url="https://t.me/XD_COBRA"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝐂𝐑𝐄𝐀𝐓𝐄𝐑👿", url="https://t.me/XD_COBRA"
                    ),
                    InlineKeyboardButton(
                        "𝐂𝐎𝐁𝐑𝐀👿", url="https://t.me/XD_COBRA"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝐀𝐃𝐃 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏👿", url="https://t.me/Legend_Mr_Musicbot?startgroup=true"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
