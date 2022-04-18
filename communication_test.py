from communication import RaspberryCommunication
from face_detector import FaceDetector
from computer_vision import ComputerVision
import computer_vision
import numpy as np
import pytest
import os
import time
import cv2

ip_address = '192.168.1.9'
port = 9527


def test_echo():
    raspberry_communication = RaspberryCommunication(ip_address, port)
    sended_data = "Hello World!"
    raspberry_communication.send(sended_data)
    recived_data = raspberry_communication.recive()
    assert sended_data == recived_data


def test_sending_time():
    raspberry_communication = RaspberryCommunication(ip_address, port)
    sending_data = 'Hello World!'
    start_time = time.time()
    raspberry_communication.send(sending_data)
    reciving_data = raspberry_communication.recive()
    end_time = time.time()
    delta_time = end_time - start_time
    print(delta_time)
    assert delta_time < raspberry_communication.timeout


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images


def test_find_face():
    face_detector = FaceDetector(7, 7, 1)
    images = load_images_from_folder('test_face_images')
    face_counter = 0
    computerVision = ComputerVision()

    for image in images:
        img = face_detector.draw_mesh(image)
        image_rgb = computer_vision.convert_color(img)
        img = computerVision.process_image(img, image_rgb)
        img, contour_is_found = computerVision.find_contours(img)
        if contour_is_found:
            face_counter += 1

    assert face_counter == len(images)


def test_dont_find_face():
    face_detector = FaceDetector(7, 7, 1)
    images = load_images_from_folder('test_not_face_images')
    face_counter = 0
    computerVision = ComputerVision()

    for image in images:
        img = face_detector.draw_mesh(image)
        image_rgb = computer_vision.convert_color(img)
        img = computerVision.process_image(img, image_rgb)
        img, contour_is_found = computerVision.find_contours(img)
        if contour_is_found:
            face_counter += 1

    assert face_counter == 0
