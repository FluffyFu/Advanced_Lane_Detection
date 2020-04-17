###################################
# file_name: warp.py
# author: Xinlin Song
# date: 04/13/2020
# description: This file contains the function to transform the image to
#   a bird-eye view.
###################################

import cv2

def warper(img, src, dist):
    """
    Apply perspective change to the given image. Here we assume dist is
    a rectangle
    """
    # make sure the order of the points are aligned.
    src = order_points(src)
    dist = order_points(dist)

    # since dist is a rectangle, we don't need to use distance formula.
    width = dist[1][0] - dist[0][0] # top_right - top_left (x)
    height = dist[3][1] - dist[0][1] # bottom_left - top_left (y)

    M = cv2.getPerspectiveTransform(src, dist)
    warped = cv.warpPerspective(image, M, (width, height))

    return warped

def order_points(pts):
	# initialzie a list of coordinates that will be ordered
	# such that the first entry in the list is the top-left,
	# the second entry is the top-right, the third is the
	# bottom-right, and the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype = "float32")
	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
	# return the ordered coordinates
	return rect
