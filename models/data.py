import cv2
import numpy as np

training_set_num = 250


def print_im(im):
    _str_ = ""
    for line in im:
        for point in line:
            if point > 200:
                _str_ += "1"
            else:
                _str_ += " "
        _str_ += "\n"
    print(_str_)


def one_hot(num):
    y = np.array([0 for _ in range(10)])
    y[num] = 1
    return y


x = []
ys = []
f = open("training_set/label.txt", "r").readlines()
for line in f:
    pic_id, label = line.split()
    filename = "training_set/%s.bmp" % pic_id
    print(filename, label)
    pic = cv2.imread(filename)
    x.append(pic[:, 5:14])
    x.append(pic[:, 14:23])
    x.append(pic[:, 24:33])
    x.append(pic[:, 34:43])
    if len(label) != 4:
        print("error label")
        exit()
    for one in label:
        num = int(one)
        y = one_hot(num)
        ys.append(y)

xs = np.array(x)
ys = np.array(ys)

print(xs[0].shape)