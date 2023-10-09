import urllib.request
from PIL import Image

url = "https://1drv.ms/i/s!AraN2vPdQTKhgo47hSiXv9C6wbE7TA?e=gM80kB"
urllib.request.urlretrieve(url, "IMG-20230906-WA0013.jpg")

img = Image.open (r "IMG-20230906-WA0013.jpg")
img.show()
