import time
import requests

print("HUNTER_GOCAP JALAN...")

# Cek promo Gojek yang lagi aktif
# Ini cuma baca info publik, bukan nembak order

def cek_promo():
    try:
        r = requests.get("https://www.gojek.com/id-id/", timeout=10)
        print("Status Gojek:", r.status_code)
        if r.status_code == 200:
            print("Gojek online - siap hunting")
            return True
    except Exception as e:
        print("Gagal cek:", e)
    return False

while True:
    cek_promo()
    print("Tunggu 60 detik lagi...")
    time.sleep(60)
