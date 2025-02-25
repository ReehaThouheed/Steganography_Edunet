import cv2
import os

img = cv2.imread("Anime.jpg")  

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

msg += "~"

d = {chr(i): i for i in range(32, 127)} 

n, m, z = 0, 0, 0
height, width, _ = img.shape  
max_chars = height * width  

if len(msg) > max_chars:
    print("Message too large to fit in the image!")
    exit()

for char in msg:
    img[n, m, z] = d[char]
    z = (z + 1) % 3  
    if z == 0:
        m += 1
        if m >= width:  
            m = 0
            n += 1

cv2.imwrite("encryptedImage.png", img)
print("Encryption completed! Encrypted image saved as 'encryptedImage.png'.")

os.system("start encryptedImage.png")