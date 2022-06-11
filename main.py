from computer_vision import ComputerVision, convert_color
from face_detector import FaceDetector
from communication import RaspberryCommunication

computerVision = ComputerVision(1)

faceDetection = FaceDetector(thickness=7,
                             circle_radius=7,
                             max_number_of_faces=1)

raspberryCommunication = RaspberryCommunication('192.168.1.9', 9527)
# 192.168.1.5
is_processing = True

while is_processing:
    image = computerVision.read_capture()

    image = faceDetection.draw_mesh(image)

    image_rgb = convert_color(image)

    image = computerVision.process_image(image, image_rgb)

    image, contour_is_found = computerVision.find_contours(image)

    position = computerVision.calculate_center_of_image(image)

    computerVision.put_text_to_image(image, '+', position, 3, (0, 0, 255))

    if contour_is_found:
        position = computerVision.calculate_center_of_face()
        computerVision.put_text_to_image(image, '+', position, 4, (255, 0, 0))

        movement = computerVision.calculate_movement(threshold=40)
        print(movement)

        raspberryCommunication.send(movement)

    computerVision.show_image(image)

    is_processing = computerVision.verify_processing()
