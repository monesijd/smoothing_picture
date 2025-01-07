import cv2
import numpy as np
import matplotlib.pyplot as plt
import picture_node_capture as capture
from matplotlib.animation import FuncAnimation


def fourier_transform(order_list, num_of_coef):
    pi = np.pi
    
    num_of_point = len(order_list)

    if num_of_coef % 2 == 1:
        num_of_coef += 1

    t_list1 = np.linspace(0, 1, num_of_point, endpoint=False)    # 計算係數的黎曼和陣列
    t_list2 = np.linspace(0, 1, max(10000, num_of_point), endpoint=True)    # 用來畫產生的函數圖形
    dt = 1 / num_of_point

    coef_list = []
    
    # 利用黎曼和計算傅立葉級數的係數
    for n in range(-num_of_coef//2, num_of_coef//2+1):
        coordinate = order_list[:, 0] + 1j * order_list[:, 1]
        coef = np.sum(coordinate * (np.exp((1j) * (-2*pi*n*t_list1)) * dt))
        coef_list.append(coef)
    

    coef_list = np.array(coef_list)
    point_list = np.zeros(len(t_list2), dtype=complex)

    for n in range(-num_of_coef//2, num_of_coef//2+1):
        point_list += coef_list[n + num_of_coef//2] * np.exp((1j) * (2*pi*n*t_list2))

    return point_list 


input_picture = capture.Picture("picture_dir/test.jpg", threshold_low=50, threshold_high=240)
# threshold_low 和 threshold_high 為偵測邊緣的閥值 ( 使用 cv2.edge )

order_list = input_picture.order_list(num_of_point=20000)   
point_list = fourier_transform(order_list, num_of_coef=len(order_list))
plt.plot(point_list.real, point_list.imag)
plt.axis("equal")
plt.show()


fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

height = input_picture.height
width = input_picture.width

ax.set_xlim(-width//2-100, width//2+100)
ax.set_ylim(-height//2-100, height//2+100)
ax.set_aspect('equal')
ax.set_title("Fourier Series Reconstruction")
text = ax.text(width//2+80, height//2+80, '', fontsize=15, ha='right', va="top", color='blue')

def init():
    line.set_data([], [])
    text.set_text('')
    return line,

def update(num_of_coef):
    point_list = fourier_transform(order_list, num_of_coef=num_of_coef)
    line.set_data(point_list.real, point_list.imag)
    text.set_text(f'n = {num_of_coef}')
    return line,

ani = FuncAnimation(
    fig, 
    update, 
    frames=range(0, 501, 10),  # num_of_coef 範圍
    init_func=init, 
    blit=False, 
    interval=50
)

plt.show()