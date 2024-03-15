from string import ascii_lowercase
import os
from pathlib import Path
import re
from itertools import product
from string import ascii_lowercase
import random
import string
import time

panjang_string = 10

file_content = []
past_value = None

def f_path(path):
    home = str(Path.home())
    path_reg = "^"+re.sub("[^/]+$","", home) + "[^/]+"
    return re.sub(path_reg,home,path)

# membuka file log dan menampilkannya
file = open("/content/coba/sample.txt", "r")
# print(file.read())

#memisahkan tiap line log menjadi satu satu array
for line in file:
  file_content.append(line.strip())
#print salah satu data array hasil pisahan
print(file_content[4])


while True:
  #menyimpan 1 data array kedalam satu variabel
  current_file_content=file_content[4]
  #pengecekan dan perbandingan perubahan data pada satu array
  if current_file_content != past_value:
    print("current value :", current_file_content)
    print("mesin aman")
    past_value = current_file_content
  else:
    print("mesin bermasalah")
  
  # buat simulasi perubahan data
  teks_acak = ''.join(random.choices(string.ascii_letters + string.digits, k=panjang_string))
  file_content[4]= str(teks_acak)

  time.sleep(2)
  







  










