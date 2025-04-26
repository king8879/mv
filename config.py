import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = "7751391316:AAEl3Sjwt5PHxZw9QtffalbXHVUB0hmkazA"
    # Telegram API ki ID
    API_ID = 22923037
    # Telegram API ki hash key
    API_HASH = "dfb3666878b3851460a58461c5a50f5b"
    # Admin users ki IDs (comma se separate ki hui)
    ADMIN = ''.split('6554343173')
    # Admin IDs ko integer list mein convert karna
    ADMIN_ID = [int(id) for id in ADMIN]
    # MongoDB database ka URL
    DB_URL = "mongodb+srv://vikassonawale0:JWyQFas7vlG1bkaL@cluster0.beermge.mongodb.net/?retryWrites=true&w=majority"
    # Database ka naam
    DB_NAME = "Cluster0"
    # Text log channel ki ID
    TXT_LOG = -1002261145026
    # Authentication log channel ki ID
    AUTH_LOG = -1002595530340
    # Hit log channel ki ID
    HIT_LOG = -1002649937778
    # DRM dump channel ki ID
    DRM_DUMP = -1002647629976
    # Main channel ki ID
    CHANNEL = -1002574084986
    # Channel ka link
    CH_URL = "https://t.me/+DY3YLoeE6yU0OTg1"
    # Bot ke owner ka Telegram link
    OWNER = "t.me/vighnesh9820"
    # Thumbnail image ka URL
    THUMB_URL = "https://telegra.ph/file/example-thumb-image.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "https://www.masterapi.tech/"

