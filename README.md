# Image Stitching

## Description

Given 2 images of an object from different perspectives, this project attempts to stitch these images together to get a single image with all the elements from both these images.


## Data

* Sign 1

![alt text](/data/sign1.png)

* TSign 2

![alt text](/data/sign2.png)


## Approach

* Match Features between the two images

* Find the Homography Matrix

* Warp Image

* Stitch images together by replacing parts of Image 1 with 2


## Output

* Feature Matching

![alt text](/output/feature_match.png)

* Stitched Image

![alt text](/output/stitched_img.png)



## Getting Started

### Dependencies

<p align="left"> 
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>&ensp; </a>
<a href="https://numpy.org/" target="_blank" rel="noreferrer"> <img src="https://www.codebykelvin.com/learning/python/data-science/numpy-series/cover-numpy.png" alt="numpy" width="40" height="40"/>&ensp; </a>
<a href="https://opencv.org/" target="_blank" rel="noreferrer"> <img src="https://avatars.githubusercontent.com/u/5009934?v=4&s=400" alt="opencv" width="40" height="40"/>&ensp; </a>

* [Python 3](https://www.python.org/)
* [NumPy](https://numpy.org/)
* [OpenCV](https://opencv.org/)


### Executing program

* Clone the repository into any folder of your choice.
```
git clone https://github.com/ninadharish/Image-Stitching.git
```

* Open the repository and navigate to the `src` folder.
```
cd Image-Stitching/src
```

* Run the program.
```
python main.py
```


## Authors

👤 **Ninad Harishchandrakar**

* [GitHub](https://github.com/ninadharish)
* [Email](mailto:ninad.harish@gmail.com)
* [LinkedIn](https://linkedin.com/in/ninadharish)