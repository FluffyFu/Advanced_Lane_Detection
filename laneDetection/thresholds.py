###################################
# file_name: thresholds.py
# author: Xinlin Song
# date: 04/15/2020
# description: this file contains functions used for generating
#   binary image with directional gradient, magnitude of gradient,
#   direction of gradient and color thresholds.
###################################
import numpy as np
import cv2

def sobel_x_thresh(img, ksize, min_thresh, max_thresh):
	"""
	Apply Sobel filter along x-axis and returns a binary image
	according to the given thresholds.
	"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	sobel = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=ksize)

    abs_sobel = np.abs(sobel)
    scale_sobel = np.uint8(255 * abs_sobel / np.max(abs_sobel))

    binary_output = np.zeros_like(scale_sobel)
    binary_output[(scale_sobel > thresh_min) & (scale_sobel < thresh_max)] = 1
    return binary_output

def sobel_y_thresh(img, ksize, min_thresh, max_thresh):
	"""
	Apply Sobel filter along y-axis and returns a binary image
	according to the given thresholds.
	"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	sobel = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

    abs_sobel = np.abs(sobel)
    scale_sobel = np.uint8(255 * abs_sobel / np.max(abs_sobel))

    binary_output = np.zeros_like(scale_sobel)
    binary_output[(scale_sobel > thresh_min) & (scale_sobel < thresh_max)] = 1
    return binary_output

def sobel_mag_thresh(img, ksize, min_thresh, max_thresh):
	"""
	Apply Sobel filter along x-axis, y-axis and calculate the magnitude,
    and returns a binary image according to the given thresholds.
	"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	x = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
	y = cv2.Sobel(gray, cv2.CV_64F, 1, 0)

    mag = np.sqrt(np.square(x) + np.square(y))

    scale_sobel = np.uint8(255 * mag / np.max(mag))

    binary_output = np.zeros_like(scale_sobel)
    binary_output[(scale_sobel > thresh_min) & (scale_sobel < thresh_max)] = 1
    return binary_output

def sobel_dir_thresh(img, ksize, min_thresh, max_thresh):
    """
    Apply Sobel filter along x-axis and y-axis and calculate the
    direction, and returns a binary image according to the given thresholds.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	x = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
	y = cv2.Sobel(gray, cv2.CV_64F, 1, 0)

    x_abs = np.abs(x)
    y_abs = np.abs(y)

    angle = np.arctan2(y_abs, x_abs)
    binary_output = np.zeros_like(angle)
    binary_output[(angle > thresh_min) & (angle < thresh_max)] = 1
    return binary_output

def s_channel_thresh(img, min_thresh, max_thresh):
    """
    Covert image color to HLS representation and apply the threshold
    to S channel and returns a binary image.
    """
    # TODO might need to change GBR
    hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    S = hls[:, :, 2]

    binary_output = np.zeros_like(S)
    binary_output[(S > min_thresh) & (S <= max_thresh)] = 1
    return binary_output
