# image-manipulator
image-manipulator is a simple script that adjusts the compression of a jpg file

## Installation

	git clone 'https://github.com/Toory/image-manipulator'
	cd image-manipulator/src/
	virtualenv env
	source ./env/bin/activate
	python image-manipulator.py

## Usage

    usage: jpegcompression.py [-h] -q QUALITY (-d DIR_PATH | -i IMAGE_PATH)

    optional arguments:
      -h, --help            show this help message and exit
      -q QUALITY, --quality QUALITY
                        Change compression quality of a jpeg image file
                        [number ranging from 1 to 100]
      -d DIR_PATH, --directory DIR_PATH
                        Specify a directory, actions will be applied to all
                        jpg files inside
      -i IMAGE_PATH, --image IMAGE_PATH
                        Specify a single image
