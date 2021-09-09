import urllib.request
import time

fileName = 'links.txt'

def readLineCount():
  file = open(fileName, "r")
  line_count = 0
  for line in file:
    if line != "\n":
        line_count += 1
  file.close()
  return line_count

def downloadImages():
  if readLineCount() == 0:
    print('Links.txt dosyası boş')
  else:
    print('İndirme İşlemi Başladı...')
    count = 0
    file1 = open(fileName, 'r')
    Lines = file1.readlines()
    for line in Lines:
      count += 1
      urllib.request.urlretrieve(line, "output/{}.jpg".format(count))
    print('İndirme İşlemi Tamamlandı!')

print('Tüm linklerinizi links.txt dosyasına satır satır kaydedin ve işlemlere devam edin.')
process = input('Links.txt dosyanız işleme hazır mı? E/H: ')
if process.lower() == 'e':
  
  try:
    downloadImages()
    
  except:
    print('Bir hata oluştu!')
else:
  print('Program Sonlanıyor...')
  time.sleep(1)