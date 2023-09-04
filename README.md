# stereo_calibration
左右目相機裁切及標定程式

1.先用take_stereoPhoto.py，拍攝數張9*6標定版照片

2.執行python camera_calibration.py img/

---

輸出參數:

__Intrinsic_mtx_1__ – output first camera matrix

__dist_1__ – output vector of distortion coefficients  (k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6]]) of 4, 5, or 8 elements. The output vector length depends on the flags.

__Intrinsic_mtx_2__ – output second camera matrix

__dist_2__ – output lens distortion coefficients for the second camera

__R__ – Output rotation matrix between the 1st and the 2nd camera coordinate systems.

__T__ – Output translation vector between the coordinate systems of the cameras.

__E__ – Output essential matrix.

__F__ – Output fundamental matrix.
