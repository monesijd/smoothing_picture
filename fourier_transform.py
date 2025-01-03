import matplotlib.pyplot as plt
import picture_node_capture as capture

input_picture = capture.picture("test.jpg")
height = input_picture.height
width = input_picture.width

order_list = input_picture.order_list(5000) 
# 將圖像變成 3000 個點來表示

input_picture.draw_nodes()


while True:
    if input_picture.close_window():
        break