import cv2 as cv
import os


def get_image_paths(directory):
    image_list = []
    valid_extensions = ['.jpg', '.jpeg', '.png']
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            ext = os.path.splitext(file)[1].lower()
            if ext in valid_extensions:
                image_list.append(directory + file)
    return image_list


# Load the image paths
image_directory = './sample2/'
image_paths = get_image_paths(image_directory)
imgs = []

# Load the images
for i in range(len(image_paths)):
    imgs.append(cv.imread(image_paths[i]))
    imgs[i] = cv.resize(imgs[i], (0, 0), fx=0.075, fy=0.075)  # rescale the images

# Stitch the images
stitched_img = cv.Stitcher.create()
(dummy, output) = stitched_img.stitch(imgs)

if dummy != cv.STITCHER_OK:  # check if the stitching was successful
    print('Error during stitching')
else:
    print("Stitched image created")

# Show the stitched image
cv.imshow('Stitched Image', output)
cv.waitKey(0)
cv.destroyAllWindows()

# Save the stitched image
cv.imwrite('stitched.jpeg', output)
