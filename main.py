from computer_vision import ComputerVision, convert_color
from face_detector import FaceDetector
from communication import RaspberryCommunication
import matplotlib.pyplot as plt
from scipy.io import savemat, loadmat
import time

computerVision = ComputerVision(0)

faceDetection = FaceDetector(thickness=7,
                             circle_radius=7,
                             max_number_of_faces=1)

raspberryCommunication = RaspberryCommunication('192.168.1.3', 9527)
# 192.168.1.5
# 192.168.1.3

is_processing = True
error_x_list = []
error_y_list = []
start_time = time.time()
fps = 0
frames = 0
while is_processing:
    image = computerVision.read_capture()


    image = faceDetection.draw_mesh(image)

    image_rgb = convert_color(image)

    image = computerVision.process_image(image, image_rgb)

    image, contour_is_found = computerVision.find_contours(image)

    position_image, center_x_img, center_y_img = computerVision.calculate_center_of_image(image)

    computerVision.put_text_to_image(image, '+', position_image, 3, (0, 0, 255))

    if contour_is_found:
        position_face, center_x_face, center_y_face = computerVision.calculate_center_of_face()
        computerVision.put_text_to_image(image, '+', position_face, 4, (255, 0, 0))
        different_x = center_x_face - center_x_img
        different_y = center_y_face - center_y_img

        print(different_x, different_y)

        error_x_list.append(different_x)
        error_y_list.append(different_y)

        movement = computerVision.calculate_movement(threshold=40)
        # print(movement)

        raspberryCommunication.send(movement)



    computerVision.show_image(image)
    frames += 1

    is_processing = computerVision.verify_processing()

end_time = time.time()

time_different = end_time - start_time
fps = frames / time_different
start_time = end_time
print("\n\n",fps,"\n\n")

#computerVision.put_text_to_image(image, int(fps), (50, 50), 4, (200, 154, 123))
savemat('error_x.mat', {"error_x": error_x_list})
savemat('error_y.mat', {"error_y": error_y_list})
