import cv2
import numpy as np
import matplotlib.pyplot as plt


def image_stitch(image1, image2):

    img1_color = cv2.imread(image1)  
    img2_color = cv2.imread(image2) 

    img1 = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)

    sift = cv2.SIFT_create()

    kp1, desc1 = sift.detectAndCompute(img1, None)
    kp2, desc2 = sift.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

    matches = bf.match(desc1, desc2)
    matches = sorted(matches, key = lambda x:x.distance)

    img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], img2, flags=2)
    plt.imshow(img3), plt.show()


    src_pts = np.float32([kp1[m.queryIdx].pt for m in matches ]).reshape(-1,1,2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches ]).reshape(-1,1,2)

    H, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    width = img1.shape[1] + img2.shape[1]
    height = img1.shape[0] + img2.shape[0]

    result = cv2.warpPerspective(img1_color, H, (width, height))
    result[0:img2_color.shape[0], 0:img2_color.shape[1]] = img2_color
    result = result[:338, :625]

    cv2.imshow('result', result)
    cv2.waitKey(0)