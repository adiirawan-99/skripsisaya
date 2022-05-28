from ast import Return
from cProfile import label
import os
from tkinter import filedialog, Label, messagebox
from turtle import color
from unittest import result
from PIL import Image, ImageTk
import cv2
from random import randint
import numpy as np
from skimage.io import imread, imshow
from skimage.color import rgb2gray, rgb2hsv
from skimage.morphology import area_opening
from skimage.exposure import histogram
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt
import pickle
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier


image_original = ""
label_original = ""
def uploadimage():
    global image_original, label_original
    filename = filedialog.askopenfilename(initialdir="C:/Users/Adi/Documents/skripsi")
    if filename !="":
        img = Image.open(filename)
        image_original = img
        img = img.resize((520, 520))
        load = ImageTk.PhotoImage(img)

        label1 = Label(image = load)
        label1.image = load
        label1.place(
            x = 72, y =13,
            width= 520,
            height= 520
        )
        label_original = label1

def saveboar():
    if label_original != "":
        value = randint(0, 1000)
        convert = cv2.cvtColor(np.array(image_original), cv2.COLOR_RGB2BGR)
        # print(image_original)
        save_babi = cv2.imwrite("./Dataset/Babi/"+str(value)+".jpg", convert)
        label_original.configure(image="")
        label_original.destroy()
        messagebox.showinfo(title= "Succesed", message= "Image has been saved")
    else:
        messagebox.showwarning(title= "Warning", message= "Image must be choosen")

def savecow():
    if label_original != "":
        value = randint(0, 1000)
        convert = cv2.cvtColor(np.array(image_original), cv2.COLOR_RGB2BGR)
        # print(image_original)
        save_babi = cv2.imwrite("../Dataset/Sapi/"+str(value)+".jpg", convert)
        label_original.configure(image="")
        label_original.destroy()
        messagebox.showinfo(title= "Succesed", message= "Image has been saved")
    else:
        messagebox.showwarning(title= "Warning", message= "Image must be choosen")

def masked_image(image, mask):
    r = image[:,:,0] * mask
    g = image[:,:,1] * mask
    b = image[:,:,2] * mask
    return np.dstack([r,g,b])

def training(result): 
    path = 'Dataset'
    save_path = 'Dataset_Thresholding/'
    for filename in os.listdir(path):
        if not os.path.isdir(save_path + filename):
            os.mkdir(save_path + filename)
        for index, imagename in enumerate(os.listdir(os.path.join(path, filename))):
            image = imread(os.path.join(path, filename, imagename))
            gray = rgb2gray(image)
            thresh = threshold_otsu(gray)
            masking  = gray < thresh
            filtered = masked_image(image, masking)
            image = Image.fromarray(filtered)
            image = image.resize((778, 437))
            image = np.asarray(image)

            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            return cv2.imwrite(f'testingtreshold.jpg', image)

            # cv2.imwrite(f'{save_path}/{filename}/{filename}_{index + 1}.jpg', image)
            

    path_threshold = 'Dataset_Thresholding'
    save_hsv = 'HSV_Value/'
    for filename in os.listdir(path_threshold):
        if not os.path.isdir(save_hsv + filename):
            os.mkdir(save_hsv + filename)
        for imagename in os.listdir(os.path.join(path_threshold, filename)):
            image = imread(os.path.join(path_threshold, filename, imagename))

            image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            return cv2.imwrite(f'testrain.jpg', image)

            # cv2.imwrite(f'{save_hsv}/{filename}/{imagename}', image)
            
    path_hsv = 'HSV_Value/'
    data_hsv = {}
    imgname = []
    for filename in os.listdir(path_hsv):
        for imagename in os.listdir(os.path.join(path_hsv, filename)):
            if len(imgname) > 8 :
                imgname=[]
            imgname.append(imagename + " Succes To Trained")
            image = imread(os.path.join(path_hsv, filename, imagename))

            h,s,v = cv2.split(image)
            hmean = h.mean()
            smean = s.mean()
            vmean = v.mean()
            data_hsv[f'{imagename}'] = (hmean, smean, vmean, filename)

            return print([hmean, smean, vmean])

            result.configure(text = '\n'.join(x for x in imgname) + " Training Data Has Been Succesfully")
            result.update()
            
    file = open('Enkoding_KNN/hsv_value.pkl', 'wb')
    pickle.dump(data_hsv, file)
    file.close()
    xtrain, ytrain = [], []
    for key, data in data_hsv.items():
        xtrain.append([data[0], data[1], data[2]])
        ytrain.append(data[3])
    
    xtrain = np.array(xtrain)
    ytrain = np.array(ytrain)

    knn = KNeighborsClassifier(n_neighbors=7)
 
    knn.fit(xtrain, ytrain)
    print(xtrain)
    print(ytrain)

    with open('model/knn', 'wb') as f:
        pickle.dump(knn, f)
    
    messagebox.showinfo(title="Successed", message="Training Data Has Been Done")


def training_all(result):
    path = 'Dataset'
    data_hsv = {}
    imgname = []
    for filename in os.listdir(path):
        for imagename in os.listdir(os.path.join(path, filename)):
            if len(imgname) > 8 :
                imgname=[]
            imgname.append(imagename + " Succes To Trained")
            image = imread(os.path.join(path, filename, imagename))
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
            data_hsv[f'{imagename}'] = (hmean, smean, vmean, filename)
            
            # 

            # result 
            result.configure(text = '\n'.join(x for x in imgname))
            result.update()
            
            # return cv2.imwrite(f'traininghsv.jpg', hsv)

    file = open('Enkoding_KNN/hsv_value.pkl', 'wb')
    pickle.dump(data_hsv, file)
    file.close()

    # create model knn
    xtrain, ytrain = [], []
    for key, data in data_hsv.items():
        xtrain.append([data[0], data[1], data[2]])
        ytrain.append(data[3])
    
    xtrain = np.array(xtrain)
    ytrain = np.array(ytrain)

    knn = KNeighborsClassifier(n_neighbors=3)
 
    knn.fit(xtrain, ytrain)

    with open('model/knn', 'wb') as f:
        pickle.dump(knn, f)
    messagebox.showinfo(title="Successed", message="Training Data Has Been Done")

