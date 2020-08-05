import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# 0:默认摄像头
# cv2.CAP_DSHOW是作为一部分传递的标志，可以传递很多标志，这个特定于微软，是个附加值，若要打开摄像机2，可以执行cv2.CAP_DSHOW+1

cap.open(0)

while cap.isOpened():
    flag, frame = cap.read()

    cv2.imshow('use_camera', frame)

    # ESC退出
    # 先获取键盘按键
    key_pressed = cv2.waitKey(60) # 监听键盘输入，60ms延迟

    if key_pressed == 27:
        break

# 关闭摄像头 release即释放
cap.release()
# 关闭所有窗口
cv2.destoryAllWindows()