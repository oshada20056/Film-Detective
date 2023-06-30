#Modified By DARK DEVIL
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    START_TXT = """𝘏𝘦𝘭𝘭𝘰𝘸 {} 𝘉𝘳𝘰🍎,
𝘐'𝘮<a href=https://t.me/{}>{}</a>, 𝘐 𝘊𝘢𝘯 𝘗𝘳𝘰𝘷𝘪𝘥𝘦 𝘔𝘰𝘷𝘪𝘦𝘴,𝘚𝘦𝘳𝘪𝘦𝘴 𝘞𝘪𝘵𝘩 𝘏𝘢𝘳𝘥𝘤𝘰𝘥𝘦 𝘚𝘪𝘯𝘩𝘢𝘭𝘢 𝘚𝘶𝘣𝘵𝘪𝘵𝘭𝘦𝘴\n𝘑𝘶𝘴𝘵 𝘈𝘥𝘥 𝘔𝘦 𝘛𝘰 𝘠𝘰𝘶𝘳 𝘎𝘳𝘰𝘶𝘱 𝘈𝘯𝘥 𝘔𝘢𝘬𝘦 𝘔𝘦 𝘈𝘥𝘮𝘪𝘯 𝘎𝘳𝘰𝘶𝘱 🍒"""
    HELP_TXT = """𝘏𝘰𝘸 𝘈𝘳𝘦 𝘠𝘰𝘶 {} 𝙱𝚁𝙾😜
𝘏𝘦𝘳𝘦 𝘐𝘴 𝘔𝘺 𝘏𝘦𝘭𝘱𝘪𝘯𝘨 𝘊𝘰𝘮𝘮𝘢𝘯𝘥\n𝘠𝘰𝘶 𝘊𝘢𝘯'𝘛 𝘜𝘴𝘦 𝘈𝘥𝘮𝘪𝘯𝘯 𝘊𝘰𝘮𝘮𝘢𝘯𝘥\n\n𝘔𝘺 𝘚𝘶𝘱𝘱𝘰𝘳𝘵 𝘎𝘳𝘰𝘶𝘱 <a href=https://t.me/Filmstudiodl>©ꜰɪʟᴍ ꜱᴛᴜᴅɪᴏ</a> """
    ABOUT_TXT = """ 🤡 𝙸 𝚊𝚖 <a href=https://t.me/@film_series_download_bot>𝙵𝙸𝙻𝙼 𝙳𝙴𝚃𝙴𝙲𝚃𝙸𝚅𝙴</a>
🏅 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/Filmstudiodl>𝘍𝘪𝘭𝘮 𝘚𝘵𝘶𝘥𝘪𝘰</a>
🥇 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
🥈 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
🥉 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱 𝙵𝚁𝙴𝙴 𝚃𝚁𝙸𝙰𝙻
🎖️ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝚆𝙷𝙾𝚃𝚃𝙾💤
🛠 ️𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0 [ 𝙱𝙴𝚃𝙰 ]
👨‍💻 𝙼𝚈 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 𝙸𝚂 <a href=https://t.me/Filmstudiodl>🍒𝘍𝘪𝘭𝘮 𝘚𝘵𝘶𝘥𝘪𝘰🍒</a>"""
    SOURCE_TXT = """<b>NOTE:</b>
- This is a privat edition. 
- Source - locked🔐

"""
    MANUELFILTER_TXT = """𝙷𝙴𝙻𝙿: <b>𝙵𝙸𝙻𝚃𝙴𝚁𝚂</b>

- Filter is the feature were users can set automated replies for a particular keyword and film-detective will respond whenever a keyword is found the message

<b>NOTE:</b>
1. film detective should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """𝙷𝙴𝙻𝙿: <b>𝙱𝚄𝚃𝚃𝙾𝙽𝚂</b>

- Film Detective Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. film detective supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/@film_series_download_bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """𝙷𝙴𝙻𝙿: <b>𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """𝙷𝙴𝙻𝙿: <b>𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽𝚂</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """𝙷𝙴𝙻𝙿: <b>𝙴𝚇𝚃𝚁𝙰 𝙼𝙾𝙳𝚄𝙻𝙴𝚂</b>

<b>NOTE:</b>
these are the extra features of Film Detective

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDB source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """𝙷𝙴𝙻𝙿: <b>𝙰𝙳𝙼𝙸𝙽 𝙼𝙾𝙳𝚂</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """🖥️ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂 𝚂𝙰𝚅𝙴𝙳: <code>{}</code>
🕵️ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
📋 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
⚖️ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
🧮 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """𝗡𝗘𝗪 𝗚𝗥𝗢𝗨𝗣
⚔️𝙶𝚁𝙾𝚄𝙿 = {}(<code>{}</code>)
🎰𝚃𝙾𝚃𝙰𝙻 𝙼𝙴𝙼𝙱𝙴𝚁𝚂= <code>{}</code>
👽𝙰𝙳𝙳𝙴𝙳 𝙱𝚈 - {}
©ꜰɪʟᴍ ꜱᴛᴜᴅɪᴏ
"""
    LOG_TEXT_P = """𝗡𝗘𝗪 𝗠𝗘𝗠𝗕𝗘𝗥
🆔𝙸𝙳 - <code>{}</code>
💡𝙽𝙰𝙼𝙴 - {}
©ꜰɪʟᴍ ꜱᴛᴜᴅɪᴏ
"""
