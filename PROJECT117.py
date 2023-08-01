import os
import cv2

path = "Img117"
img117 = []

for file in os.listdir(path):
    name , ext = os.path.splitext(file)

    if ext in ['.gif','.png','.jpg','.jpeg','jfif']:
        file_name = path + "/" + file
        print(file_name)
        img117.append(file_name)

count = len(img117)

frame = cv2.imread(img117[0])
height , width , channels = frame.shape
size = (width , height)

out = cv2.VideoWriter('PROJECT-117.mp4v' , cv2.VideoWriter_fourcc(*'DIVX') , 5 , size)

for i in range (count-1 , 0 , -1):
    frame = cv2.imread(img117[i])
    out.write(frame)

out.release()
print("Done!!")
