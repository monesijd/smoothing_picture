import cv2
import numpy as np
import matplotlib.pyplot as plt
import picture_node_capture as capture

def fourier_transform(order_list, num_of_point):
    pi = np.pi
    
    if len(order_list) != num_of_point:
        indices = np.linspace(0, len(order_list)-1, num_of_point, dtype=int)
        order_list = order_list[indices]
    
    t_list = np.linspace(0, 1, num_of_point)
    dt = 1 / num_of_point
    
    coef_list = []
    num_of_coef = num_of_point

    # 利用黎曼和計算傅立葉級數的係數
    for n in range(num_of_coef):
        coordinate = np.array(order_list[:, 0] + 1j * order_list[:, 1])
        coef = np.sum(coordinate * (np.exp((1j)*(-2*pi*n*t_list)) * dt))
        coef_list.append(coef)
    

    coef_list = np.array(coef_list)
    point_list = np.zeros(len(t_list), dtype=complex)

    for n in range(num_of_coef):
        point_list += coef_list[n] * np.exp((1j) * (2*pi*n*t_list))

    return point_list 


input_picture = capture.picture("test.png")

num_of_point = 10000
order_list = input_picture.order_list(num_of_point) 
point_list = fourier_transform(order_list, num_of_point)

plt.plot(point_list.real, point_list.imag)
plt.axis("equal")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()