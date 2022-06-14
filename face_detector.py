import mediapipe as mp  # 0.8.3.1
from computer_vision import convert_color
import cv2


class FaceDetector:
    def __init__(self, thickness, circle_radius, max_number_of_faces):
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_face_mesh = mp.solutions.face_mesh

        self.face_mesh = self.mp_face_mesh.FaceMesh(max_num_faces=max_number_of_faces)
        self.draw_spec = self.mp_draw.DrawingSpec(thickness=thickness, circle_radius=circle_radius)

    def draw_mesh(self, img):
        img_rgb = convert_color(img)

        results = self.face_mesh.process(img_rgb)

        if results.multi_face_landmarks:
            for faceLandMarks in results.multi_face_landmarks:
                self.mp_draw.draw_landmarks(img,
                                            faceLandMarks,
                                            self.mp_face_mesh.FACE_CONNECTIONS,
                                            self.draw_spec,
                                            self.draw_spec)
        return img
