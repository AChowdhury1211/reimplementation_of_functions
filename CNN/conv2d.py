import numpy as np

def Conv2d(no_filters, image, padding):
    """
    kernel size fixed to 2
    stride is 1 by default
    """
    image = np.pad(image, [(padding, padding), (padding, padding)], constant_values = 0)
    
    feature_maps_list = []
    for k in range(no_filters):
        row1 = 0
        row2 = 1
        kernel = np.random.randint(-1,1,(2,2))
        new_feature_map = []
        for i in range(len(image) - 1):
            col1 = 0
            col2 = 1
            lst = []
            for j in range(len(image[0])- 1):
                arr = np.array([[image[row1][col1],image[row1][col2]], [image[row2][col1],image[row2][col2]]])
                col1 += 1
                col2 += 1
                val = np.sum(arr * kernel)
                lst.append(val)
            new_feature_map.append(lst)
            row1 += 1
            row2 += 1
        feature_maps_list.append(new_feature_map)
    feature_maps= np.array(feature_maps_list)
    print(feature_maps)



#Test
image = np.array([[4, 5, 6,8,10], [7, 8, 9,12,2], [7, 8, 9,12,2], [1, 2, 3,4,5]])
kernel = np.array([[1,-1], [0, 1]])
Conv2d(no_filters= 10, image=image, padding = 1)