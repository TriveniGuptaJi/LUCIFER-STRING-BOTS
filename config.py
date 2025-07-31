from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","29011373"))
API_HASH = getenv("API_HASH","6353b0072f63a9701014fe9b5f907102"))

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID","7532420990"))

MONGO_DB_URI = getenv("mongodb+srv://xO9AW3OvKg8MmPFy:xO9AW3OvKg8MmPFy@cluster0.uo4mhiz.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN","LuciferBotss")
