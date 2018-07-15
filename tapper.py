#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
from argparse import ArgumentParser
import logging

_SIZE_WIDTH = 106
_SIZE_HEIGHT = 17
_SQ = _SIZE_HEIGHT * _SIZE_WIDTH


def get_parser():
    result = ArgumentParser(
        description='Script for generating image from \'k\' \
and getting \'k\' from image \
using Tapper\'s formula'
    )

    result.add_argument(
        '-g', '--gen',
        action='store_true',
        help='generate image',
    )
    result.add_argument(
        '-c', '--count',
        action='store_true',
        help='count \'k\'',
    )
    result.add_argument(
        '-k',
        type=int,
        default=None,
        help='set \'k\' to generate image',
    )
    result.add_argument(
        '-p', '--path',
        type=str,
        default=None,
        help='set image path to get k',
    )
    result.add_argument(
        '-o',
        type=str,
        default=None,
        help='set path for generated image',
    )
    return result


def get_image(chosen_k, chosen_image_path):
    def from_k_to_bin(k):
        k //= _SIZE_HEIGHT
        binary = bin(k)[2:].rjust(_SQ, '0')
        result = [[] for i in range(_SIZE_HEIGHT)]
        for x in range(_SQ):
            result[-x % _SIZE_HEIGHT].append(binary[x])
        return result

    if chosen_k is None:
        logging.error('Undefined k')
        return

    lists = from_k_to_bin(chosen_k)

    #-----Drawing-----#
    image = Image.new("1", (_SIZE_WIDTH, _SIZE_HEIGHT), (0))
    for y in range(_SIZE_HEIGHT):
        for x in range(_SIZE_WIDTH):
            xy = (_SIZE_WIDTH - x - 1, _SIZE_HEIGHT - y - 1)
            image.putpixel(xy=xy, value=(int(lists[y][x]),))

    #-----Saving-----#
    chosen_image_path = chosen_image_path or 'result.png'

    image.save(chosen_image_path)
    logging.debug('Image has generated')
    return chosen_image_path


def get_k(chosen_image_path):
    if chosen_image_path is None:
        logging.error('Undefined image path')
    try:
        image = Image.open(chosen_image_path)
    except:
        logging.error('Image error')
        return

    if image.size != (_SIZE_WIDTH, _SIZE_HEIGHT):
        logging.error("An image has to be 106х17")
        return

    #-----Counting-----#
    image = image.convert('1')
    byteset = ""
    for x in range(_SIZE_WIDTH - 1, -1, -1):
        for y in range(_SIZE_HEIGHT):
            byteset += str(int(image.getpixel((x, y)) >= 128))
    k = int(byteset, 2) * 17

    logging.debug('k has counted')
    return k


def main():
    #-----Parsing arguments-----#
    parser = get_parser()
    args = parser.parse_args()

    #-----Setting logging level-----#
    FORMAT = '%(filename)s:%(lineno)d:%(levelname)-6s %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO)

    #-----Choose type-----#
    if args.gen == args.count:
        logging.info('Use --help')
        logging.error('Undefined type')
        return
    if args.count:
        result = get_k(args.path)
    elif args.gen:
        result = get_image(args.k, args.o)

    #-----Returning result-----#
    print(result)


if __name__ == '__main__':
    main()
