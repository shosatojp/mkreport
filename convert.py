import cv2
import numpy as np
import os
import sys

JPEG_QUALITY = 70
GRAYSCALE_THRESHOLD = 190

input_filename = sys.argv[1]
output_filename = sys.argv[2] if len(sys.argv) >= 3 else os.path.splitext(input_filename)[0] + '.jpg'


im = cv2.imread(input_filename, cv2.IMREAD_GRAYSCALE)

if type(im) == None:
    print('failed to load image', file=sys.stderr)
    exit(1)

im = cv2.medianBlur(im, 3)

im = im + ((im > GRAYSCALE_THRESHOLD) * 255)
im = im - ((im <= 190) * 255)
im = np.clip(im, 0, 255)

im.astype(np.uint8)
cv2.imwrite(output_filename, im, params=[cv2.IMWRITE_PNG_COMPRESSION, 9])
# cv2.imwrite(output_filename, im, params=[cv2.IMWRITE_JPEG_QUALITY, JPEG_QUALITY])
print('output:', output_filename)
