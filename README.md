# Smoothing Picture

After learning Integral, I want to process a picture into a smooth and closed curve. (using python)

I do the follow steps to make it:

> 1. Read jpg file, make it into the gray picture, and find its edge picture ( the array with only black or white )
> 2. Analysis every pixel of the gray picture, so that we can have an sorted point of the picture (to know which point to start point and which is the next point)
> 3. Using fourier series to approximate the origin picture

You can watch the 3b1b video, which I also used as a reference. (I think this is the best video for visualizing fourier transform.)

Fourier Transform: [可視化的傅里葉變換](https://www.youtube.com/watch?v=spUNpyF58BY)

Fourier Series: [But what is a Fourier series? From heat flow to drawing with circles | DE4](https://www.youtube.com/watch?v=r6sGWTCMz2k)

---

### Process

#### Tool

- cv2

  Using Canny and edge to make a edge picture. (Black point is edge)

- numpy
  
  To accelerate the efficience of calculating the data.

- plt
  
  To draw the final function picture.

#### Math

- Fourier series

We can approximate any periodic function to the infinite sum of the triangular function.

Here is the formula:

$$
f(t) = C_0 e^{-0 \cdot (2\pi i t)} + C_1e^{-1 \cdot (2\pi i t)} + C_2 e^{-2 \cdot (2\pi i t)} +  C_3 e^{-3 \cdot (2\pi i t)} +...
$$

$$
f(t) = \sum_{i = 0}^n C_n \cdot e^{-n \cdot (2\pi i t)}
$$

How can we find $C_n$ ?

$$
C_n = \int_0^1 f(t) \cdot e^{-n \cdot (2\pi i t)} {\rm d}t
$$

$C_n$: coefficient

$f(t)$: coordinate ( complex number ) at the time ```t```

I use Riemann sum to approximate each coefficient. 

I set the n(the number of coefficients) as many as the number of the points in the origin edge picture.


### Result

- Origin
  
![geto](https://github.com/user-attachments/assets/73d23d05-6cf1-4ee9-98db-eb8f318c8528)

- Result
  
![geto](https://github.com/user-attachments/assets/6c76043d-2ab7-42f4-b430-1aa11b5160ce)
