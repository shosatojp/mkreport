import cv2
import numpy as np
import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--type', type=str, choices=['grayscale', 'binary'], default=False, required=False)
parser.add_argument('-q', '--quality', type=int, default=70, help='quality')
parser.add_argument('-g', '--grayscale_threshold', type=int, default=210, help='grayscale threshold')
parser.add_argument('-o', '--outtype', type=str, choices=['jpg', 'png'], required=True, help='output image type')
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()

input_filename = args.input
output_filename = args.output if len(sys.argv) >= 3 else os.path.splitext(input_filename)[0] + '.jpg'


im = cv2.imread(input_filename, cv2.IMREAD_GRAYSCALE)

if type(im) == None:
    print('failed to load image', file=sys.stderr)
    exit(1)

if args.type == 'binary':
    im = cv2.medianBlur(im, 3)
    im = im + ((im > args.grayscale_threshold) * 255)
    im = im - ((im <= args.grayscale_threshold) * 255)
    im = np.clip(im, 0, 255)

im.astype(np.uint8)

if args.outtype == 'jpg':
    cv2.imwrite(output_filename, im, params=[cv2.IMWRITE_JPEG_QUALITY, args.quality])
elif args.outtype == 'png':
    cv2.imwrite(output_filename, im, params=[cv2.IMWRITE_PNG_COMPRESSION, 9])


print('output:', output_filename)
