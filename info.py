import re
from os import environ,getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '20778875'))
API_HASH = environ.get('API_HASH', 'c49ecc77f2abfaedb1bd6bca14559702')
BOT_TOKEN = environ.get('BOT_TOKEN', '6892047030:AAGsnpQvV5MnswJOuokJcUIT8prT85ixNM8')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

#Telegraph
PICS = (environ.get('PICS', 'https://graph.org/file/54fde3e34103198dabaea.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/3af3fe9ff92d1a6c98c1d.png")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/4e1556928e3bdcaaa3373.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/e06089d66b2b556816e3d.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/ce2103c2c9a160ff1d38f.jpg'))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6924461727 5378316778 6394827136').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002055068009').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '6924461727 5378316778 6394827136').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = -1001928525228
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002127187291')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
master_chat_id = environ.get('MASTER_CHAT_ID', '-1002010455331')
MASTER_CHAT_ID = int(master_chat_id) if master_chat_id and id_pattern.search(master_chat_id) else None
reqst_channel = environ.get('REQST_CHANNEL', '-1002127187291')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://uhdprime:uhdprime@database1.riu2les.mongodb.net/?retryWrites=true&w=majority")
SECONDDB_URI = environ.get('SECONDDB_URI', "mongodb+srv://orgprime:orgprime@primefilterbot.gotwyku.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Telegram")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Collection')

# add premium logs channel id
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002139713029'))

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'publicearn.com')
SHORTLINK_API = environ.get('SHORTLINK_API', '97119e40c5fc3875820a6c37253b3c3bcee51a9d')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8086")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/moviespremium')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/orgprime')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/orgpremium/7')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', 'Hello My Dear Friends ❤️')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002139713029'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'moviespremium')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

# Online Stream and Download
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME', "primefilterbot")
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '145.223.19.132'))
FQDN = str(getenv('FQDN', '145.223.19.132:8086')) if not ON_HEROKU or getenv('FQDN', '145.223.19.132:8086') else APP_NAME+'.herokuapp.com'
URL = "http://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "http://{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'LazyPrincess'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "http://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)
    
LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
