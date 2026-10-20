import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from motor.motor_asyncio import AsyncIOMotorClient
import config

# Initialize Bot
bot = Client(
    "FileStoreBot",
    api_id=config.APP_ID,
    api_hash=config.API_HASH,
    bot_token=config.TG_BOT_TOKEN
)

# MongoDB Connection
dbclient = AsyncIOMotorClient(config.DB_URI)
db = dbclient[config.DB_NAME]
users_col = db["users"]

@bot.on_message(filters.command("start") & filters.private)
async def start_handler(client: Client, message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    
    # Save user to DB
    await users_col.update_one({"id": user_id}, {"$set": {"name": user_name}}, upsert=True)
    
    start_text = f"<b>Hello {user_name}!\n\nI am a File Store Bot. Send me any file, video, or document, and I will give you a special shareable link.</b>"
    
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔥 Updates Channel", url="https://t.me/TDBotDev")],
        [InlineKeyboardButton("⚡ Developer", url="https://t.me/ABHIRAJ_KUMAR")]
    ])
    
    await message.reply_text(start_text, reply_markup=buttons, disable_web_page_preview=True)

@bot.on_message(filters.document | filters.video | filters.audio & filters.private)
async def store_file(client: Client, message: Message):
    if message.from_user.id != config.OWNER_ID:
        pass

    try:
        # Forward file to storage channel
        forwarded_msg = await message.forward(config.CHANNEL_ID)
        file_id = forwarded_msg.id
        
        share_link = f"https://t.me/{client.me.username}?start=ABHIRAJ_{file_id}"
        
        await message.reply_text(
            f"<b>✅ File Stored Successfully!</b>\n\n<b>Link:</b> <code>{share_link}</code>",
            quote=True
        )
    except Exception as e:
        await message.reply_text(f"<b>❌ Error storing file:</b> <code>{e}</code>")

# Run Bot
if __name__ == "__main__":
    print("Bot is starting...")
    bot.run()
