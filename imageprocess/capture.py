import sys
from pathlib import Path

import cv2

video = sys.argv[1]
output = Path("output")
output.mkdir(exist_ok=True)

cap = cv2.VideoCapture(video)
if not cap.isOpened():
    exit(0)

index = 0
while True:
    ret, frame = cap.read()
    if ret is False:
        break
    index += 1
    cv2.imshow("Frame", frame)
    cv2.imwrite(str(output / f"frame-{index:08}.png"), frame)

cap.release()
cv2.destroyAllWindows()
