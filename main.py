import functions

img_arr = functions.load_to_array("test.jpg")
img_brt = functions.make_brightness_matrix(img_arr)

for i in range(len(img_arr)):
    for j in range(len(img_brt[0])):
        if (i == j):
            print(img_arr[i][j])
            print(img_brt[i][j])
