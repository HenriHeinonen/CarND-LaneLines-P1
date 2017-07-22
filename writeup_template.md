# **Finding Lane Lines on the Road** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of several steps. First, I read the images from files using a for loop
```
kuvat = os.listdir("test_images/")
for kuva in kuvat:
   image = mpimg.imread('test_images/' + kuva)
```
and then I converted the images to grayscale, 
```
gray = grayscale(image)
```
then I make the Gaussian blur operation
```
kernel_size = 5
blur_gray = gaussian_blur(gray, kernel_size)
```
using a parameter `kernel_size = 5`.
Then I am ready to search for the Canny edges with the following parameters
```
low_threshold = 50
high_threshold = 150
edges = canny(blur_gray, low_threshold, high_threshold)
```
and storing the image to the variable `edges`.

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by ...

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![alt text][image1]


### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when ... 

Another shortcoming could be ...


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to ...

Another potential improvement could be to ...
