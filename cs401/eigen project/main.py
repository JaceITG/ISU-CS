import numpy
import numpy.linalg as la
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.figure as fig
import os, sys

from yaml import unsafe_load

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
MIDDLE = (WIDTH//2, HEIGHT//2)

NUM_SAMPLES = 10

#initialize zeroed face in shape (w*h,1)
avg = numpy.zeros(WIDTH*HEIGHT)

all = []  #final set of data, half first image examples, half second image examples

#load faces in form ./data/{dataset}/{dataset}nn.jpg and add to average
def load_face(dataset, show_images=True):
    global all, avg
    dataset_path = os.path.join(DATASETS,dataset)

    for i in range(NUM_SAMPLES):
        path = os.path.join(dataset_path, f'{dataset}{i:02}.jpg')
         
        #Check validity of filepath
        if not os.path.isfile(path):
            print(f"Invalid file: {path}")
            continue
        
        #Load the image at path into a matrix and display if chosen
        img = mpimg.imread(path)

        gray = rgb2gray(img)

        if show_images:
            imgplot = plt.imshow(gray)
            plt.show(block=False)
            plt.pause(0.2)
            plt.close()

        #Flatten grayscale image to 1D array and add to set
        r = numpy.reshape(gray[:,:,1], WIDTH*HEIGHT)
        all.append(r)

        avg = numpy.add(avg, r)

def get_average(*datasets, show_images=True):
    global avg

    #load the faces of each dataset and add to avg
    for d in datasets:
        load_face(d, show_images=show_images)
    
    #Get the average of all images added to array and display
    print(f"Dividing by {NUM_SAMPLES*len(datasets)}")
    avg = numpy.true_divide(avg, NUM_SAMPLES*len(datasets))

    if show_images:
        avgPixels = numpy.repeat(avg, 3)  #repeat out the grayscale value for each pixel rgb to show image

        avgPixels = numpy.reshape(avgPixels, (HEIGHT,WIDTH,3)).astype(int)

        plt.imshow(avgPixels)
        plt.show(block=False)
        plt.pause(1)
        plt.close()




def create_cloud(*datasets):
    global all, avg
    get_average(*datasets, show_images=False)
    
    #Get "principal components" of each face by subtracting the cooresponding average value
    principal = numpy.zeros((WIDTH*HEIGHT,len(datasets)*NUM_SAMPLES))
    for j in range(len(datasets)*NUM_SAMPLES):
        principal[:,j] = all[j] - avg
        princImg = numpy.repeat(principal[:,j], 3)
        princImg = numpy.reshape(princImg, (HEIGHT,WIDTH,3)).astype(numpy.uint8)    #FIXME: unsure if cast type affecting eigenfaces?
    
    #Compute SVD
    (U,S,V) = la.svd(principal, full_matrices=False)
    phi = U[:,1:len(datasets)*NUM_SAMPLES]
    phi[:,1] = -1*phi[:,1]

    phiImg = numpy.reshape(phi,(HEIGHT*WIDTH,-1))   #group phi into set of H*W images

    #display first 9 eigengfaces
    count = 1
    for i in range(3):
        for j in range(3):
            plt.subplot(3,3,count)
            im = numpy.repeat(phiImg[:, count], 3)
            im = numpy.reshape(im,(HEIGHT,WIDTH,3))
            plt.imshow(200-((25000*im).astype(int)))
            count+=1
            
    plt.show(block=False)
    plt.pause(.5)
    plt.close()

    #Create clouds from dataset images
    cloud1 = numpy.zeros(numpy.shape(principal[:,:NUM_SAMPLES]))
    for i in range(NUM_SAMPLES):
        imvec = principal[:,i]
        cloud1[:,i] = imvec.conj().T * phi[:,1] * phi[:,2] * phi[:,3]   #Transpose imvec onto first 3 svd
    
    cloud2 = numpy.zeros(numpy.shape(principal[:,:NUM_SAMPLES]))
    for i in range(NUM_SAMPLES):
        imvec = principal[:,NUM_SAMPLES+i]
        cloud2[:,i] = imvec.conj().T * phi[:,1] * phi[:,2] * phi[:,3]   #Transpose imvec onto first 3 svd

    #Plot transposed images onto 3d figure
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(cloud1[1,:], cloud1[2,:], cloud1[3,:], c='r')
    ax.scatter(cloud2[1,:], cloud2[2,:], cloud2[3,:], c='b')
    plt.autoscale(enable=True, axis='both', tight=None)

    plt.show(block=False)
    plt.pause(1)
    plt.close()

    return phi, cloud1, cloud2

    

def likeness(sample, phi, *clouds):
    global avg
    path = os.path.abspath(sample)

    #Check validity of filepath
    if not os.path.isfile(path):
        print(f"Invalid file: {path}")
        return
    
    #Load the image at path into a matrix and display for 1 second
    img = mpimg.imread(path)

    #grayscale loaded sample and subtract average of datasets
    gray = rgb2gray(img)
    u = numpy.reshape(gray, HEIGHT*WIDTH, 1) - avg
    #transpose image data onto svd data
    upts = u.conj().T * phi[:,1] * phi[:,2] * phi[:,3]





if __name__ == "__main__":
    print("Eigen Action Heros")

    phi, *clouds = create_cloud("jer", "sus")

    likeness("", phi, clouds)