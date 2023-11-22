# import winsound
# winsound.Beep(432, 200)
# print("Първо тръгва 432Hz, после следва възход")
import winsound

for i in range(200, 4000, 200):
    winsound.Beep(i, 300)
