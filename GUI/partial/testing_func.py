from fileinput import filename
import os
from tkinter import filedialog, Label, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from skimage.io import imread, imshow
from skimage.color import rgb2gray, rgb2hsv
from skimage.morphology import area_opening
from skimage.exposure import histogram
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt
import pickle
import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances

image_original = ""
label_original = ""
filepath = ''

def uploadimage():
    global image_original, label_original, filepath
    filename = filedialog.askopenfilename(initialdir="C:/Users/Adi/Documents/skripsi")
    if filename !="":
        img = Image.open(filename)
        image_original = img
        img = img.resize((516, 290))
        load = ImageTk.PhotoImage(img)

        label1 = Label(image = load)
        label1.image = load
        label1.place(
            x = 75, y = 20,
            width= 516,
            height= 290
        )
        label_original = label1
        filepath = filename

def masked_image(image, mask):
    r = image[:,:,0] * mask
    g = image[:,:,1] * mask
    b = image[:,:,2] * mask
    return np.dstack([r,g,b])

def testing(result):
    global label_original, image_original, filepath
    if label_original != "":
        image = imread(filepath)
        gray = rgb2gray(image)
        thresh = threshold_otsu(gray)
        masking  = gray < thresh
        filtered = masked_image(image, masking)
        image = Image.fromarray(filtered)
        image = image.resize((778, 437))
        image = np.asarray(image)


        # img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(hsv)
        hmean = h.mean()
        smean = s.mean()
        vmean = v.mean()

        load = ImageTk.PhotoImage(Image.fromarray(image).resize((280, 156)))
        label2 = Label(image = load)
        label2.image = load
        label2.place(
            x = 35, y = 412,
            width= 280,
            height= 156
        )

        loadhsv = ImageTk.PhotoImage(Image.fromarray(hsv).resize((280, 156)))
        label3 = Label(image = loadhsv)
        label3.image = loadhsv
        label3.place(
            x = 355, y = 412,
            width= 280,
            height= 156
        )

        file = open('Enkoding_KNN/hsv_value.pkl', 'rb')
        data_hsv=pickle.load(file)
        file.close()

        # create model knn
        xtrain, ytrain = [], []
        for key, data in data_hsv.items():
            xtrain.append([data[0], data[1], data[2]])
            ytrain.append(data[3])
        
        xtrain = np.array(xtrain)
        ytrain = np.array(ytrain)

        # knn = KNeighborsClassifier(n_neighbors=3)
 
        # knn.fit(xtrain, ytrain)

        xtest = [hmean, smean, vmean]
        xtest = np.expand_dims(xtest, axis=0)


        with open('model/knn', 'rb') as f:
            knn = pickle.load(f)
        
            
        decission = knn.predict(xtest)
        ed = euclidean_distances(xtrain, xtest)

        
        ed_sort = sorted(ed, key=lambda x:x[0])
        print(ed_sort)
        # result 
        # result.configure(text = f'H Value : {xtest[0][0]}\nS Value : {xtest[0][1]}\nV Value : {xtest[0][2]}\nED 1, 2: {ed_sort[0][0]}, {ed_sort[1][0]}\nED 3, 4 : {ed_sort[2][0]}, {ed_sort[3][0]}\nED 5, 6 : {ed_sort[4][0]}, {ed_sort[5][0]}\nED 7, 8 : {ed_sort[6][0]}, {ed_sort[7][0]}\nED 9, 10 : {ed_sort[8][0]}, {ed_sort[9][0]}\nED 11 : {ed_sort[10][0]}\nDecission : {decission[0]}')

        # result.configure(text = f'H Value : {xtest[0][0]}\nS Value : {xtest[0][1]}\nV Value : {xtest[0][2]}\nEuclidean Distance 1 : {ed_sort[0][0]}\nEuclidean Distance 2 : {ed_sort[1][0]}\nEuclidean Distance 3 : {ed_sort[2][0]}\nEuclidean Distance 4 : {ed_sort[3][0]}\nEuclidean Distance 5 : {ed_sort[4][0]}\nEuclidean Distance 6 : {ed_sort[5][0]}\nEuclidean Distance 7 : {ed_sort[6][0]}\nEuclidean Distance 8 : {ed_sort[7][0]}\nEuclidean Distance 9 : {ed_sort[8][0]}\nEuclidean Distance 10 : {ed_sort[9][0]}\nEuclidean Distance 11 : {ed_sort[10][0]}\nDecission : {decission[0]}')

        result.configure(text = f'H Value : {xtest[0][0]}\nS Value : {xtest[0][1]}\nV Value : {xtest[0][2]}\nEuclidean Distance 1 : {ed_sort[0][0]}\nEuclidean Distance 2 : {ed_sort[1][0]}\nEuclidean Distance 3 : {ed_sort[2][0]} \nDecission : {decission[0]}')


    else:
        messagebox.showwarning(title= "Warning", message= "Image must be choosen")