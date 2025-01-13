import cv2
import numpy as np
from scipy.spatial import KDTree
import matplotlib.pyplot as plt


def min_dis_drawing(point):
    point = np.array(point)
    order_list = [] 
    
    num = len(point)
    is_visited = np.array([False] * num)
    
    tree = KDTree(point)
    query_point = point[0]
    is_visited[0] = True

    while not np.all(is_visited):
        distances, indices = tree.query(query_point, k=num)
        for each_index in indices:
            if not is_visited[each_index]:
                min_index = each_index
                break

        order_list.append(point[min_index])
        is_visited[min_index] = True
        query_point = point[min_index]

    return np.array(order_list)

def move_to_origin_point(order_list):
    mean_point = np.mean(order_list, axis=0)
    order_list = order_list - mean_point
    return order_list


class Picture:
    def __init__(self, image, threshold_low, threshold_high):
        self.image = cv2.imread(image)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        self.edge = cv2.Canny(self.gray, threshold_high, threshold_high)
        self.height, self.width, _ = tuple(self.image.shape)


    def order_list(self, num_of_point):
        point = []
        num = 0

        for i in range(self.width):
            for j in range(self.height):
                if self.edge[j, i] == 255:
                    point.append([i, -j])
                    num += 1
        point = np.array(point)
        print(f"Original edge point: {num}")

        num = max(num // num_of_point + 1, 1)
        point = point[::num]
        print(f"Input data point: {len(point)}")

        self.order_list = min_dis_drawing(point)
        self.order_list = move_to_origin_point(self.order_list)

        return self.order_list


    def draw_points(self):
        plt.plot(self.order_list[:, 0], self.order_list[:, 1])
        plt.axis('equal')
        plt.show()


    def close_window(self):
        if cv2.waitKey(0) == ord("q"):
            plt.close("all")
            cv2.destroyAllWindows()
            return True
        return False
