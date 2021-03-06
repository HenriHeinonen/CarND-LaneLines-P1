# **Finding Lane Lines on the Road** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report

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

After that I am using my version of the draw_lines() function. In order to draw a single line on the left and right lanes, I modified the draw_lines() function by first finding the center of the x coordinates and storing that value to variable `half`. This is done by querying the image shape property `line_img.shape[1]` and dividing it by two. I will store the Hough lines to a variable called `lines` by using the cv2's function HoughLinesP(). Then I will use two nested for loops to store the Hough lines' end points (x1, y1) and (x2, y2) to arrays. I will also make x1array and x2array np.arrays for the trick I will need.

I am going to assume that Hough lines that have x values smaller than the x coordinate of the center of the image (`half`) are those with the raising lines (slope > 0, meaning the left lane line) and Hough lines that have x values greater than the x coordinate are those with the lowering lines (slope < 0, meaning the right lane line). The trick I mentioned is this 
```
x_b = max( max(x1array[x1array<half]), max(x2array[x2array<half]) )
```
which is taking only the x values that are smaller than the value `half`. I need to find the largest x value from the left Hough lines. That is why I need to remove that right Hough lines by using this trick.

The right lane line was easy to find, but there were some problems with the left lane line, so I had to do some modifications to my plans and even after that the solution was not perfect. At least, in some pictures, there was some noise (a white car, perhaps?) that was introducing some extra Hough lines. The extra stuff was near the horizon so I decided to use the mean values of the Hough lines that are farther away from the horizon!
```
apu_x = mean( [ mean(x1array[x1array<half]), mean(x2array[x2array<half])] )
apu_y = mean([mean(y1array), mean(y2array)])
```

I am drawing two lines to make the left lane line
```
cv2.line(line_image,(apu_x,apu_y),(x_b,y_b),(255,0,0),10)
cv2.line(line_image,(apu_x-(x_b-apu_x),apu_y-(y_b-apu_y)),(apu_x,apu_y),(255,0,0),10)
```
and one line to make the right lane line
```
cv2.line(line_image,(x_c,y_c),(x_d,y_d),(255,0,0),10)
```

I also had to create the output directory `test_images_muokattu` first manually or the script did not work at all! It also seems that mpimg.imsave can only store PNG images!

I was not able to make the videos work at all! I worked for about 30 hours for this project (the suggested goal being 10 hours a week for the course if I remember right). It took lots of time to make the environment work at all.

![alt text](https://raw.githubusercontent.com/HenriHeinonen/CarND-LaneLines-P1/master/step1.png "The original image")

### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when there are double lane lines.

Another shortcoming could be vehicles (=noise) coming to the region of interest. That could disturb the pipeline.


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to follow the left lane lines even better. Now I am just using the horizon and the average values to draw the left lines.

Another potential improvement could be to fix the environment somehow to make the videos work.
