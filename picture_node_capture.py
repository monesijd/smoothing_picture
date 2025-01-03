import cv2
import numpy as np
from scipy.spatial import KDTree
import matplotlib.pyplot as plt


def dfs_drawing(node):
    node = np.array(node)
    order_list = [] 
    
    num = len(node)
    is_visited = np.array([False] * num)
    
    tree = KDTree(node)
    query_node = node[0]
    is_visited[0] = True

    while not np.all(is_visited):
        distances, indices = tree.query(query_node, k=num)
        for each_index in indices:
            if not is_visited[each_index]:
                min_index = each_index
                break

        order_list.append(node[min_index])
        is_visited[min_index] = True
        query_node = node[min_index]

    return np.array(order_list)

def move_to_origin_point(order_list):
    mean_point = np.mean(order_list, axis=0)
    order_list = order_list - mean_point
    return order_list


class picture:
    def __init__(self, image):
        self.image = cv2.imread(image)
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        self.edge = cv2.Canny(self.gray, 50, 150)
        self.height, self.width, _ = tuple(self.image.shape)


    def order_list(self, num_of_nodes):
        node = []
        num = 0

        for i in range(self.width):
            for j in range(self.height):
                if self.edge[j, i] == 255:
                    node.append([i, -j])
                    num += 1
        node = np.array(node)

        N = max(num//num_of_nodes, 1)
        reduced_node = node[::N]
        self.order_list = dfs_drawing(reduced_node)
        self.order_list = move_to_origin_point(self.order_list)

        return self.order_list


    def draw_nodes(self):
        plt.scatter(self.order_list[:, 0], self.order_list[:, 1], s=1, c='black', marker=".")
        plt.axis('equal')
        plt.show()


    def close_window(self):
        if cv2.waitKey(0) == ord("q"):
            plt.close("all")
            cv2.destroyAllWindows()
            return True
        return False
