import cv2
import matplotlib.pyplot as plt

image = cv2.imread('person-2.jpg')

## Checking the data type, tells us the image is a Numpy Array
print(type(image))

print(image.shape)

plt.imshow(image)

#### Changing the color channel from BGR to RGB
converting_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(converting_img)

### Converting a Colour Image To Grayscale Image
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(grey_img)

#### Saving the converted image
cv2.imwrite('image_to_be_saved.jpg', grey_img)


## Loading A Grey Scale Image Directly with Conversion
image_grey = cv2.imread('my_grey_image.jpg', cv2.IMREAD_GRAYSCALE)

### Slicing to Obtain Different Colour Channels With CV2
blue, green, red = image[:,:,0], image[:,:,1], image[:,:,2]

# And you can plot each colour channel
