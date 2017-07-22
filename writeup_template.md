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
Then I mask the image to remove areas that are probably not the actual lane lines by making some vertices and use them with previous step's edges to form the `masked_image` using the helper function `region_of_interest`. After that I am ready to find the Hough lines with using some parameters from the quiz. The helper function is `hough_lines` and the image will be stored to `line_img` variable. 

After that I am using my version of the draw_lines() function. In order to draw a single line on the left and right lanes, I modified the draw_lines() function by first finding the center of the x coordinates and storing that value to variable `half`. This is done by querying the image shape property `line_img.shape[1]` and dividing it by two. I will stores Hough lines to a variable called `lines` by using the cv2's function HoughLinesP(). Then I will use two nested for loops to stores the Hough lines' end points (x1, y1) and (x2, y2) to arrays. I will also make x1array and x2array np.arrays for the trick I will need.

I am going to assume that Hough lines that have x values smaller than the x coordinate of the center of the image (`half`) are those with the raising lines (slope > 0, meaning the left lane line) and Hough lines that have x values greater than the x coordinate are those with the lowering lines (slope < 0, meaning the right lane line). The right lane line was easy to find, but there were some problems with the left lane line, so I had to do some modifications to my plans and even after that the solution was not perfect. I am drawing two lines to make the left lane line
```
cv2.line(line_image,(apu_x,apu_y),(x_b,y_b),(255,0,0),10)
cv2.line(line_image,(apu_x-(x_b-apu_x),apu_y-(y_b-apu_y)),(apu_x,apu_y),(255,0,0),10)
```
and one line to make the right lane line
```
cv2.line(line_image,(x_c,y_c),(x_d,y_d),(255,0,0),10)
```

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![alt text][image1]


### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when ... 

Another shortcoming could be ...


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to ...

Another potential improvement could be to ...
