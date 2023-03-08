from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "23489281"))
API_HASH = getenv("API_HASH", "5fd3d83fa943f0f3d05bf1964a6d77f3")
BOT_TOKEN = getenv("BOT_TOKEN","6044849839:AAEbzXL38yXlP87K7TfCOMZEZCr3r2X92Gs")
BOT_NAME = getenv("BOT_NAME","❰ 𝗚𝗼𝗱𝗭𝗠𝘂𝘀𝗶𝗰 𝗧𝗚 ❱")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME", "BQCmlWUTtuk9O9JqKzrwVjbiZA5fJv7bNgL4CqMeJ4y57nYxFTK6yN1kPE3F1TaAOfto-ph3QByA8oTGALS-dqJ_OWs1aC3lL1UOI4QgK95sxCz2tWFYo1IhWzMN-ov3Gq8M4LGJ5L7rRdQ7M8pf9kWuuRW9WITXAEDzvmKMuN37bIBwwOnG3HAsARiU6Fkk1fFDLWzR0uQ8wFceGQYFYwdaGaXXQb-udTQ9kUeq_afFUYnH9i5q4wlQbMZBNTgpy33LgPS_c9HRxNva3C3h8y6JNKrD_HYFiT8kS6Oi0XSFUGEv3oArtvFzatE_PSVxw8P-5ldeTcu4TmpSBzis3bUHAAAAAWiCwroA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6048367290").split()))
