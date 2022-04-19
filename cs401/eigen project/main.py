import numpy
import numpy.linalg as la
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.figure as fig
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
        
        #Load the image at path into a matrix and display for 1 second
        img = mpimg.imread(path)

        gray = rgb2gray(img)
        #print(f'Middle of gray {i}: {gray[MIDDLE[1]][MIDDLE[0]]}')

        if show_images:
            imgplot = plt.imshow(gray)
            plt.show(block=False)
            plt.pause(0.2)
            plt.close()

        #Flatten grayscale image to 1D array and add to set
        r = numpy.reshape(gray[:,:,1], WIDTH*HEIGHT)
        all.append(r)
        #print(f"Shape r {numpy.shape(r)}")

        avg = numpy.add(avg, r)
        #print(f"Shape avg {numpy.shape(avg)}")

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
        #print(f'Middle of avg: {avgPixels[MIDDLE[1]][MIDDLE[0]]}')
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
        principal[:,j] = all[j] - avg   #FIXME: does this have to be able to go into negatives?
        princImg = numpy.repeat(principal[:,j], 3)
        princImg = numpy.reshape(princImg, (HEIGHT,WIDTH,3)).astype(int)
        print(f'Middle of princ {j}: {princImg[MIDDLE[1]][MIDDLE[0]]}')
        plt.imshow(princImg)
        plt.show(block=False)
        plt.pause(.3)
        plt.close()
    
    #Compute SVD
    print("Performing svd")
    print(f"Shape princ {numpy.shape(principal)}")
    (U,S,V) = la.svd(principal, full_matrices=False)
    print("svd done")
    phi = U[:,1:len(datasets)*NUM_SAMPLES]
    phi[:,1] = -1*phi[:,1]

    print(f"Shape phi {numpy.shape(phi)}")

    phiImg = numpy.copy(phi)
    phiImg = numpy.repeat(phi[:,1:len(datasets)*NUM_SAMPLES],3)
    phiImg = numpy.reshape(phiImg,(HEIGHT*WIDTH*3,-1))
    print(f"Shape phimg {numpy.shape(phiImg)}")
    count = 1
    #figure = fig.Figure().add_subplot(3,3)
    for i in range(3):
        for j in range(3):
            plt.subplot(3,3,count)

            im = numpy.reshape(phiImg[:,count],(HEIGHT,WIDTH,3))
            plt.imshow(200-((25000*im).astype(int)))
            count+=1
            
    plt.show(block=False)
    plt.pause(10)
    plt.close()

    

def likeness(sample, cloud):
    pass

if __name__ == "__main__":
    print("Eigen Action Heros")

    create_cloud("jer", "sus")