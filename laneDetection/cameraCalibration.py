###################################
# file_name: cameraCalibration.py
# author: Xinlin Song
# date: 04/13/2020
# description: this file contains functions used for camera calibration.
###################################
import glob
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def calibrate_camera(path, nx, ny):
    """
    calibrate camera with the images contained in path.

    Args:
        path(string): directory that contains calibration images.

        nx(int): number of corners in each row.

        ny(int): number of corner in each column.

    Returns:
        mtx(np.array, shape=(3,3)): camera matrix.

        dist(np.array, shape=(1,5)): distortion coefficients: k1, k2, p1, p2, k3.

    """
    images = glob.glob(path)

    objpoints = []
    imgpoints = []

    objp = np.zeros((nx * ny, 3), np.float32)
    objp[:,:2] = np.mgrid[0:nx + 1, 0:ny + 1].T.reshape(-1, 2)

    for frame in images:
        img = mpimg.imread(frame)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)

        if ret:
            imgpoints.append(corners)
            objpoints.append(objp)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
        objpoints, imgpoints, gray.shape[::-1], None, None)

    return mtx, dist
