import cv2
import numpy as np


def convert_color(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


class ComputerVision:
    def __init__(self, camera_selection):
        self.mask = None
        self.capture = cv2.VideoCapture(camera_selection, cv2.CAP_DSHOW)

    def read_capture(self):
        success, img = self.capture.read()
        img = cv2.flip(img, 1)
        return img

    def process_image(self, img, img_rgb):
        low_green = np.array([0, 255, 0])
        high_green = np.array([1, 255, 1])
        green_mask = cv2.inRange(img_rgb, low_green, high_green)
        kernel = np.ones((5, 5), 'uint8')

        self.mask = cv2.dilate(green_mask, kernel)
        cv2.bitwise_and(img, img, mask=green_mask)
        return img

    def find_contours(self, img):
        (contours, hierarchy) = cv2.findContours(self.mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 8000:
                x, y, w, h = cv2.boundingRect(contour)
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
        return img


    def show_image(self, img):
        cv2.imshow('Image', img)

    def verify_processing(self):
        if cv2.waitKey(1) & 0xFF == ord('q'):
            is_processing = False
        else:
            is_processing = True
        return is_processing



