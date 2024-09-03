import re
import sys
from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "25581940"))
API_HASH = getenv("API_HASH" , "1e80acd755ceab02b3e2a22d49b25c18")

# ADMIN DETAILS (Your ID) 
OWNER_ID = int(getenv("OWNER_ID", "7496416021"))

OWNER_NAME = getenv("OWNER_NAME" , "VASHU") 
SUDO_USER= list(
    map(int, getenv("SUDO_USER", "6829300557").split())
)
# BOT TOKEN CONFIG VARS (get all vars detail from @botfather) 
BOT_TOKEN = getenv("BOT_TOKEN", "7498473207:AAE7oA7J_txCGDSmEfEdAnC8uryFIUapS4g") 
BOT_TOKEN2 = getenv("BOT_TOKEN2", "7385753439:AAGuART2KitVWZ6J1PE4c9YJnFTe_rfxETA") 
BOT_TOKEN3 = getenv("BOT_TOKEN3", "7472812053:AAEh5yB_EN6mygB-JXARmnBNQ1m9iT0jMHc") 
BOT_TOKEN4 = getenv("BOT_TOKEN4", "7284392965:AAEjsYoxWM57JryNGta9en2HxylAbBG6sHQ") 
BOT_TOKEN5 = getenv("BOT_TOKEN5", "7522359934:AAGEcxuO09JzsYRL4HE8-eCaZiGvgyznoxc") 
BOT_TOKEN6 = getenv("BOT_TOKEN6", "7110145199:AAFg5nm963iGUVxzx7uV4LdmWFkLqkiPWR8") 
BOT_TOKEN7 = getenv("BOT_TOKEN7", "7506293149:AAHN8iR6mVPUrZB-QmCYTMhlm-UdN8pps90") 
BOT_TOKEN8 = getenv("BOT_TOKEN8", "7065541914:AAGF2MdBCfXWhWCYz4OU4pTR9Ku_TmpGamw") 
BOT_TOKEN9 = getenv("BOT_TOKEN9", "7110145199:AAFg5nm963iGUVxzx7uV4LdmWFkLqkiPWR8") 
BOT_TOKEN10 = getenv("BOT_TOKEN10", "7394582236:AAFmVnmyA5gPTJEqXyJ_9QzVC31VyCFSJ8c") 


# EXTRA VARS
ALIVE_PIC = getenv("ALIVE_PIC") 
CMD_HNDLR = getenv("CMD_HNDLR") 







LUND = list(
    map(int, getenv("LUND", "123456789").split())
)

CHUT = list(
    map(int, getenv("CHUT", "1234576789").split())
)
