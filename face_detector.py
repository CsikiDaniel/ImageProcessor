import mediapipe as mp  # 0.8.3.1
from computer_vision import convert_color
import cv2


class FaceDetector:
    def __init__(self, thickness, circle_radius, max_number_of_faces):
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh

        self.faceMesh = self.mpFaceMesh.FaceMesh(max_num_faces=max_number_of_faces)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=thickness, circle_radius=circle_radius)

    def draw_mesh(self, img):
        img_rgb = convert_color(img)

        results = self.faceMesh.process(img_rgb)

        if results.multi_face_landmarks:
            for faceLandMarks in results.multi_face_landmarks:
                self.mpDraw.draw_landmarks(img,
                                           faceLandMarks,
                                           self.mpFaceMesh.FACE_CONNECTIONS,
                                           self.drawSpec,
                                           self.drawSpec)
        return img
