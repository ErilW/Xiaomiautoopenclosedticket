import os
import datetime
import time

# Path direktori tempat file akan disimpan
path = r'C:\Users\eril.sanjaya\Downloads\Drive D Model N6P line 9\Drive D\HUAQIN\AL6860\FAMMI\Slot01_COM22\20240314\PASS\ONLINE'

def create_new_file():
    now = datetime.datetime.now()
    # Buat nama file dengan format 'tahunbulantanggal_jammenitdetik.txt'
    filename = now.strftime("%Y%m%d_%H%M%S.txt")
    # Gabungkan dengan path direktori
    filepath = os.path.join(path, filename)
    
    # Buka file untuk menulis
    with open(filepath, "w") as file:
        file.write("jahsdlkjfhasldkjfhalkjsdhflksajdhflkajsdhfkljhsdkjfhaskjdhfksjhfdkljasdhfkljhsdafk\n\n\n\fkjshdalkjfhalkjsdfhlkasjdfhlkajsdhflkajsdhfkjsadhflkjasdhf\n\n\n\njsdkjhsalkjfhajsfnbxcmb,mbvd\njshfdkjahsdkjfhsdft!")

# Fungsi untuk menunggu hingga menit berikutnya
def wait_until_next_minute():
    now = datetime.datetime.now()
    next_minute = (now + datetime.timedelta(minutes=1)).replace(second=0, microsecond=0)
    delta = (next_minute - now).total_seconds()
    time.sleep(delta)

# Loop utama untuk membuat file setiap menit
while True:
    create_new_file()
    print("File baru telah dibuat.")
    wait_until_next_minute()