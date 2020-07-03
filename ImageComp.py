#RyanWalk:6/24/20:ImageComp.py
import numpy
import cv2
def mse(imageA, imageB):
    # NOTE: the two images must have the same dimension
    err = numpy.sum((imageA.astype(float) - imageB.astype(float)) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    return err
