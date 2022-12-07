import cv2
import numpy as np
from scipy import signal, interpolate
import sys


def bf_build(image, sigma_s, sigma_i, sample_s=None, sample_i=None):
    h = image.shape[0]
    y = image.shape[1]

    sample_s = sigma_s if (sample_s is None) else sample_s
    sample_i = sigma_i if (sample_i is None) else sample_i

    flat_img = image.flatten()
    edge_diff = np.amax(flat_img) - np.amin(flat_img)
    xypadding = round(2 * (sigma_s /sample_s) + 1)
    zpadding = round(2 * (sigma_i /sample_i) + 1)

    sample_w = int(round((y - 1) / sample_s) + 1 + 2 * xypadding)
    sample_h = int(round((h - 1) / sample_s) + 1 + 2 * xypadding)
    sample_z = int(round(edge_diff / sample_i) + 1 + 2 * zpadding)

    dataflat = np.zeros(sample_h * sample_w * sample_z)

    (ygrid, xgrid) = np.meshgrid(range(y), range(h))

    x_padded = np.around(xgrid / sample_s) + xypadding
    y_padded = np.around(ygrid / sample_s) + xypadding
    z_padded = np.around((image - np.amin(flat_img)) / sample_i) + zpadding

    x_flat = x_padded.flatten()
    y_flat = y_padded.flatten()
    z_flat = z_padded.flatten()

    dim = z_flat + y_flat*sample_z+ x_flat*sample_w*sample_z
    dim = np.array(dim, dtype=int)

    dataflat[dim] = flat_img

    data = dataflat.reshape(sample_h, sample_w, sample_z)
    weights = np.array(data, dtype=bool)

    kerneldim = sigma_s / sample_s * 2 + 1
    kerneldep = 2 * sigma_i / sample_i * 2 + 1
    halfkerneldim = round(kerneldim / 2)
    halfkerneldep = round(kerneldep / 2)

    (gridx, gridy, gridz) = np.meshgrid(range(int(kerneldim)), range(int(kerneldim)), range(int(kerneldep)))
    gridx -= int(halfkerneldim)
    gridy -= int(halfkerneldim)
    gridz -= int(halfkerneldep)

    gridsqr = ((gridx * gridx + gridy * gridy) / (sigma_s / sample_s * sigma_s / sample_s)) + ((gridz * gridz) / (sigma_i / sample_i * sigma_i / sample_i))
    kernel = np.exp(-0.5 * gridsqr)

    blurdata = signal.fftconvolve(data, kernel, mode='same')

    blurweights = signal.fftconvolve(weights, kernel, mode='same')
    blurweights = np.where(blurweights == 0, -2, blurweights)

    normalblurdata = blurdata / blurweights
    normalblurdata = np.where(blurweights < -1, 0, normalblurdata)

    (ygrid, xgrid) = np.meshgrid(range(y), range(h))

    x_padded = (xgrid / sample_s) + xypadding
    y_padded = (ygrid / sample_s) + xypadding
    z_padded = (image - np.amin(flat_img)) / sample_i + zpadding

    return interpolate.interpn((range(normalblurdata.shape[0]), range(normalblurdata.shape[1]),range(normalblurdata.shape[2])), normalblurdata, (x_padded, y_padded, z_padded))
# One image by the bilateral function filter which is written above
image = cv2.imread(sys.argv[1])
if sys.argv[1] == './noisy2.jpg':
    (B, G, R) = cv2.split(image)
    bf_B = bf_build(B,12, 16, sample_s=None, sample_i=None)
    bf_G = bf_build(G, 12, 16, sample_s=None, sample_i=None)
    bf_R = bf_build(R, 12, 16, sample_s=None, sample_i=None)
    merged = cv2.merge([bf_B, bf_G, bf_R])
# Other image by open cv inbuilt bilateral function
else:
    merged = cv2.bilateralFilter(image, 33, 75, 75)

cv2.imwrite(('denoised.jpg'),merged)





