import numpy as np
import cv2

video_dir="C:/Users/jeongseokoon/Downloads/20210611_광각2_4.mp4"
cap = cv2.VideoCapture(video_dir)

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')

delay = round(1000/fps)

out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))
if not out.isOpened():
    print('File open failed!')
    cap.release()
    sys.exit()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    sliced=frame[:,:w//2].copy()

    out.write(sliced)

cap.release()
out.release()
cv2.destroyAllWindows()
print("Video stop")