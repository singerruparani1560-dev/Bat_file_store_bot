import os

# Bot Credentials & Configuration
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8139168935:AAGU0WZo06lwOhVGv0-UlOaSeLkdQiM8Ud0")
APP_ID = int(os.environ.get("API_ID", "35327931"))
API_HASH = os.environ.get("API_HASH", "5f3faae92787c7490a5d986f0f75f35b")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-4455628529"))
OWNER_ID = int(os.environ.get("OWNER_ID", "8144348712"))

DB_URI = os.environ.get("DATABASE_URL", "mongodb://abhirajkumar:abhiraj12345@cluster0-shard-00-00.o8k6x.mongodb.net:27017,cluster0-shard-00-01.o8k6x.mongodb.net:27017,cluster0-shard-00-02.o8k6x.mongodb.net:27017/?ssl=true&replicaSet=atlas-o8k6x-shard-0&authSource=admin&retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "abhirajdatabase")

PORT = os.environ.get("PORT", "8000")
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>© ABHIRAJ KUMAR | All Rights Reserved</b>")
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else True
