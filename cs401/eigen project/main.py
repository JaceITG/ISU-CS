import numpy
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os, time

DATASETS = os.path.join('.', 'data')

#CONSTANTS
WIDTH = 175
HEIGHT = 200

NUM_SAMPLES = 2

#initialize zeroed face in shape (w*h,1)
avg = numpy.zeros((WIDTH*HEIGHT,1))
A = []  #final set of data, half first image examples, half second image examples

#load faces in form ./data/{dataset}/{dataset}nn.jpg
def load_face(dataset):
    dataset_path = os.path.join(DATASETS,dataset)

    for i in range(NUM_SAMPLES):
        path = os.path.join(dataset_path, f'{dataset}{i:02}.jpg')
         
        #Check validity of filepath
        if not os.path.isfile(path):
            print(f"Invalid file: {path}")
            continue
        
        #Load the image at path and display for 1 second
        img = mpimg.imread(path)
        imgplot = plt.imshow(img)
        plt.show(block=False)
        plt.pause(1)
        plt.close()



def create_cloud():
    pass

def likeness(sample, cloud):
    pass

if __name__ == "__main__":
    print("Eigen Action Heros")

    load_face("arnold")