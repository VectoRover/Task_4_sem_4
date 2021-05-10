from PIL import Image
from numpy import array


def main(inp1, inp2, out):
    try:
        img1 = Image.open(inp1, mode="r")
    except FileNotFoundError:
        print("Error. Cannot find file.")
        return
    try:
        img2 = Image.open(inp2, mode="r")
    except FileNotFoundError:
        print("Error. Cannot find file.")
        return
    arr1 = array(img1)
    arr2 = array(img2)
    if arr2.shape[0] < arr1.shape[0] or arr2.shape[1] < arr1.shape[1]:
        print("Error!")
        return

    for i in range(0, arr1.shape[0]):
        for j in range(0, arr1.shape[1]):
            if arr1[i, j, 0] == 0 and arr1[i, j, 1] == 0 and arr1[i, j, 2] == 0:
                arr2[i, j, 0] = 0
                arr2[i, j, 1] = 0
                arr2[i, j, 2] = 0
    img3 = Image.fromarray(arr2)
    img3.save(out, format='bmp')


inputfile1 = input()
inputfile2 = input()
outputfile = input()
main(inputfile1, inputfile2, outputfile)
