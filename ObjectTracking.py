import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):
    # 各フレームを読み込む
    _, frame = cap.read()
    # BGRからHSVに変換する
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # 閾値を決める（上限、下限）
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # しきい値でふるいにかけるマスクを作る
    mask = cv.inRange(frame, lower_blue, upper_blue,)
    # 実際にマスクをかける
    res = cv.bitwise_and(frame, )

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
