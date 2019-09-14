                                        # plot dog photos from the dogs vs cats dataset
from matplotlib import pyplot
from matplotlib.image import imread

folder = 'train/'                                                   # define location of dataset

# plot first few images
for i in range(9):
    pyplot.subplot(330 + 1 + i)                                     # define subplot
    filename = folder + 'dog.' + str(i) + '.jpg'                    # define filename
    image = imread(filename)                                        # load image pixels
    pyplot.imshow(image)                                            # plot raw pixel data
    pyplot.show()                                                   # show the figure


# plot cat photos from the dogs vs cats dataset
for i in range(9):
    pyplot.subplot(330 + 1 + i)                                     # define subplot
    filename = folder + 'cat.' + str(i) + '.jpg'                    # define filename
    image = imread(filename)                                        # load image pixels
    pyplot.imshow(image)                                            # plot raw pixel data
    pyplot.show()                                                   # show the figure
