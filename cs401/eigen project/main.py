import numpy
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os, sys

DATASETS = os.path.join('.', 'data')

#Formula for calculating the grayscale component of pixels based on their rgb values
#https://en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale
def rgb2gray(img):
    gray = numpy.zeros(img.shape)
    R = numpy.array(img[:, :, 0])
    G = numpy.array(img[:, :, 1])
    B = numpy.array(img[:, :, 2])

    R = (R *.299)
    G = (G *.587)
    B = (B *.114)

    Avg = (R+G+B)
    gray = img.copy()

    for i in range(3):
        gray[:,:,i] = Avg
    
    return gray

#CONSTANTS
WIDTH = 175
HEIGHT = 200

NUM_SAMPLES = 2

#initialize zeroed face in shape (w*h,1)
avg = numpy.zeros(WIDTH*HEIGHT)

all = []  #final set of data, half first image examples, half second image examples

#load faces in form ./data/{dataset}/{dataset}nn.jpg
def load_face(dataset):
    global all, avg
    dataset_path = os.path.join(DATASETS,dataset)

    for i in range(NUM_SAMPLES):
        path = os.path.join(dataset_path, f'{dataset}{i:02}.jpg')
         
        #Check validity of filepath
        if not os.path.isfile(path):
            print(f"Invalid file: {path}")
            continue
        
        #Load the image at path into a matrix and display for 1 second
        img = mpimg.imread(path)
        gray = rgb2gray(img)
        

        imgplot = plt.imshow(gray)
        plt.show(block=False)
        plt.pause(1)
        plt.close()

        #Flatten grayscale image to 1D array and add to set
        r = numpy.reshape(gray[:,:,1], WIDTH*HEIGHT)
        all.append(r)
        print(f"Shape r {numpy.shape(r)}")

        avg = numpy.add(avg, r)
        print(f"Shape avg {numpy.shape(avg)}")
    
    #Get the average of all images added to array and display
    avg = numpy.true_divide(avg, NUM_SAMPLES)
    avg = numpy.reshape(avg, (HEIGHT,WIDTH)).astype(int)
    plt.imshow(avg)
    plt.show()


    



def create_cloud():
    pass

def likeness(sample, cloud):
    pass

if __name__ == "__main__":
    print("Eigen Action Heros")

    load_face("arnold")