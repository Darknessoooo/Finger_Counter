
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)  # поключаемся к web-камере
mp_Hands = mp.solutions.hands  # хотим распозновать руки (hands)
# создаем характеристики для распознования
hands = mp_Hands.Hands(
    model_complexity=1,
    min_detection_confidence= 0.75,
    min_tracking_confidence=0.75,
    max_num_hands=2)
mpDraw = mp.solutions.drawing_utils  # утилита для рисования
finger_Coord = [(8 , 6) , (12 , 10) , (16 , 14), (20 , 18)]  # координаты интересующих точек у пальцев (кроме большого)
thumb_Coord = (4 , 3)  # координаты интересующих точке (большого пальца)

while cap.isOpened(): # пока камера "работает"
    success , image = cap.read()  # получем кадр с web-камеры (True/False , image)
    if not success:  # если не удалось получить кадр
        print('Не удалось получить изображение с веб камеры')
        continue  # переход к заголовку цикла (while)

    image = cv2.flip(image , 1)  # зеркальное отражение картинки

    RGB_image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)  # BGR -> RGB
    prevTime = time.time()
    result = hands.process(RGB_image)  # ищем руки
    if  result.multi_hand_landmarks:  # если найдены руки
        multiLandMarks = result.multi_hand_landmarks  # извлекаем список найденных рук
        upCount = 0  # кол-во "поднятых" пальцев
        for idx , handLms in enumerate(multiLandMarks):
            lbl = result.multi_handedness[idx].classification[0].label
            print(lbl)
            mpDraw.draw_landmarks(image, handLms , mp_Hands.HAND_CONNECTIONS)  # рисуем "маску" руки
            handList = []  # Список координат пальцев в пикселях
            for lm in (handLms.landmark):
                # преобразование координат из MediaPipe в Пиксели
                h , w , c = image.shape
                cx , cy = int(lm.x * w) , int(lm.y * h)
                handList.append((cx, cy))
            for coordinate in finger_Coord:
                if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
                    upCount += 1
            side_tumb = "left" # с какой стороны находится большой палец
            if handList[17][0] < handList[5][0]:
                side_tumb = "right"
            if side_tumb == "left":
            
                if handList[thumb_Coord[0]][0] < handList[thumb_Coord[1]][0]:
                    upCount += 1
            else:
                if handList[thumb_Coord[0]][0] > handList[thumb_Coord[1]][0]:
                    upCount += 1


        print(upCount)
        cv2.putText(image , str(upCount), (50 , 300), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX , 4, (0 , 220 , 100) , 5)
    currentTime = time.time()
    fps = 1/(currentTime - prevTime)
    str_fps = f"FPS: {fps}"
    cv2.putText(image , str_fps , (50 , 50), cv2.FONT_HERSHEY_PLAIN , 4, (0 , 220 , 100) , 5)
    cv2.imshow('image' , image)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cap.release()