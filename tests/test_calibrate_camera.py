###################################
# file_name: test_calibrate_camera.py
# author: Xinlin Song
# date: 04/14/2020
# description: unit test for cameraCalibration.py
###################################
from laneDetection.cameraCalibration import calibrate_camera
import numpy as np

def test_calibrate_camera():
    cal_path = '../camera_cal/calibration*.jpg'
    nx = 9
    ny = 6

    mtx, dist = calibrate_camera(cal_path, nx, ny)
    assert mtx.shape == (3, 3)
    assert dist.shape == (1, 5)
