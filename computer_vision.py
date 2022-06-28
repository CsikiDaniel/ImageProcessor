import cv2
import numpy as np


def convert_color(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


class ComputerVision:

    def __init__(self, camera_selection):
        self.capture = cv2.VideoCapture(camera_selection, cv2.CAP_DSHOW)
        self.contour_is_found = None
        self.position = None
        self.h = None
        self.w = None
        self.y = None
        self.x = None
        self.center_y = None
        self.center_x = None
        self.mask = None
        self.contours = None

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
        (self.contours, hierarchy) = cv2.findContours(self.mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.contour_is_found = False
        for contour in self.contours:
            area = cv2.contourArea(contour)
            if area > 7000:
                self.x, self.y, self.w, self.h = cv2.boundingRect(contour)
                img = cv2.rectangle(img, (self.x, self.y), (self.x + self.w, self.y + self.h), (0, 255, 0), 2, 1)
                self.contour_is_found = True

        return img, self.contour_is_found

    def show_image(self, img):
        cv2.imshow('Image', img)

    def verify_processing(self):
        if cv2.waitKey(1) & 0xFF == ord('q'):
            is_processing = False
        else:
            is_processing = True
        return is_processing

    def calculate_center_of_image(self, img):
        height, width, chanel = img.shape
        self.center_x = int(width / 2) - 15
        self.center_y = int(height / 2) + 15
        position = (self.center_x, self.center_y)
        return position, self.center_x, self.center_y

    def calculate_center_of_face(self):
        center_x = int(self.x + self.w / 2 - 20)
        center_y = int(self.y + self.h / 2 + 12)
        position = (center_x, center_y)
        return position, center_x, center_y

    def calculate_movement(self, threshold):

        if self.contours:
            movement = ''
            if (int(self.x + self.w / 2 - 20)) < self.center_x - threshold:
                # ('left')
                movement += '1'
            else:
                movement += '0'

            if (int(self.x + self.w / 2 - 20)) > self.center_x + threshold:
                # ('right')
                movement += '1'
            else:
                movement += '0'

            if (int(self.y + self.h / 2 + 12)) < self.center_y - threshold:
                # ('up')
                movement += '1'
            else:
                movement += '0'

            if (int(self.y + self.h / 2 + 12)) > self.center_y + threshold:
                # ('down')
                movement += '1'
            else:
                movement += '0'
        else:
            movement = '0000'

        return movement

    def put_text_to_image(self, img, text, position, size, color):
        cv2.putText(img, str(text), position, cv2.FONT_HERSHEY_PLAIN, int(size), color, 2)
