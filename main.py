from computer_vision import ComputerVision, convert_color
from face_detector import FaceDetector

computerVision = ComputerVision(0)

faceDetection = FaceDetector(thickness=7,
                             circle_radius=7,
                             max_number_of_faces=1)

is_processing = True

while is_processing:
    image = computerVision.read_capture()

    image = faceDetection.draw_mesh(image)

    image_rgb = convert_color(image)

    image = computerVision.process_image(image, image_rgb)

    image = computerVision.find_contours(image)

    computerVision.show_image(image)

    is_processing = computerVision.verify_processing()










