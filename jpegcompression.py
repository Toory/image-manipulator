from PIL import Image
import os , argparse

class ImageManipulation():

	def __init__(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('-q', '--quality', help='Change compression quality of a jpeg image file [number ranging from 1 to 100]', action='store', type=int, metavar='QUALITY',nargs=1,required=True)
		group = parser.add_mutually_exclusive_group(required=True)
		group.add_argument('-d', '--directory', help='Specify a directory, actions will be applied to all jpg files inside', action='store', type=str, metavar='DIR_PATH',nargs=1)
		group.add_argument('-i', '--image', help='Specify a single image', action='store', type=str, metavar='IMAGE_PATH',nargs=1)
		args = parser.parse_args()

		if args.quality[0] <= 0 or args.quality[0] > 100:
			print('Quality range needs to be between 1 and 100')
			return

		if args.image:
			if 'jpg' in args.image[0]:
				pass
				self.jpgcompression(args.image[0],args.quality[0])
			else:
				print(f'Error, the {args.image[0]} it\'s not jpeg format')
		elif args.directory:
			images = os.listdir(args.directory[0])
			for image in images:
				if 'jpg' in image:
					image = f'{args.directory[0]}{image}'
					self.jpgcompression(image,args.quality[0])
					print(image)
		else:
			parser.print_help()

	def jpgcompression(self,imageFile,quality):
		im = Image.open(imageFile)
		#convert to RGB to avoid transparency problems
		rgb_im = im.convert('RGB')
		rgb_im.save(imageFile,"JPEG", quality=quality, subsampling=0, optimize=True, progressive=True)
		print(f'Successfully compressed {imageFile.split("/")[-1]} [quality={quality}]')

if __name__ == '__main__':
	ImageManipulation()