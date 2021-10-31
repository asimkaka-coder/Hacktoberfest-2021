rom PIL import Image
import matplotlib.pyplot as plt


def count_ordered(input_arr):
    output_array = input_arr;
    current_tag = 0;
    labels_array = []
    for y in range(0, len(output_array)):
        row = output_array[y]
        for x in range(0, len(row)):
            if (output_array[y][x] == 0):
                continue
            left_val = 0
            top_val = 0
            if (x > 0):
                left_val = output_array[y][x - 1]
            if (y > 0):
                top_val = output_array[y - 1][x]
            if (left_val == 0 and top_val == 0):  # New block found
                current_tag += 1
                output_array[y][x] = current_tag
            elif (left_val != 0 and top_val != 0):  # Overlap found
                if (left_val != top_val):
                    min_val = min(left_val, top_val)
                    max_val = max(left_val, top_val)
                    tuple_label = (min_val, max_val)
                    if (labels_array.count(tuple_label) == 0):
                        labels_array.append((min_val, max_val))
                    output_array[y][x] = min_val
                else:
                    output_array[y][x] = left_val
            elif (min(left_val, top_val) == 0):
                output_array[y][x] = max(left_val, top_val)

            pass
        print(output_array[y])
        pass

    print("-----------")
    print(labels_array)

    print('Second pass')

    for y in range(0, len(output_array)):
        row = output_array[y]
        for x in range(0, len(row)):
            val = output_array[y][x]
            for link in labels_array:
                if (val == link[1]):
                    val = link[0]
                    output_array[y][x] = val
                pass
        print(output_array[y])
    return output_array


def binarize(img):
    # decide the threshold
    threshold = 203

    # load the pixels of the image
    pix = img.load()
    # get width and height of the input image
    width, height = img.size
    # iterate through all the pixels
    for x in range(width):
        for y in range(height):
            if pix[x, y] > threshold:
                pix[x, y] = 0
            else:
                pix[x, y] = 255
    return img


img = Image.open('Lab5-image.png').convert('L')
img = binarize(img)

pix = img.load()
width, height = img.size
arr = []
for x in range(width):
    row = []
    for y in range(height):
        row.append(pix[x, y])
    arr.append(row)

x = count_ordered(arr)
plt.imshow(x, cmap='nipy_spectral')
plt.show()
