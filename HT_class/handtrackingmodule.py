import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self , mode=False, maxHands=2, complexity=1, detectionCon=0.75 , trackCon=0.75 ):
        self.mpHands = mp.solutions.hands  # хотим распозновать руки (hands)
        self.hands = self.mpHands.Hands(mode , maxHands , complexity, detectionCon , trackCon)
        self.mpDraw = mp.solutions.drawing_utils  # утилита для рисования
        self.fingertips =[4 , 8 , 12 , 16 , 20] # кончики пальцев
    def findHands(self , img , draw=True):
        image = cv2.flip(img , 1)  # зеркальное отражение картинки
        RGB_image = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)  # BGR -> RGB
        self.result = self.hands.process(RGB_image)  # ищем руки
        if draw:
            for handLms in self.result.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img , handLms , self.mpDraw.HAND_CONNECTIONS)
        return img
        
