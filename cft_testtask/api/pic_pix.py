import numpy as np
from PIL import Image, UnidentifiedImageError
import time

WHITE_1 = [1]
WHITE_L = [255]
BLACK_1_L = [0]

WHITE_RGB = [255, 255, 255]
BLACK_RGB = [0, 0, 0]

WHITE_CMYK = [0,0,0,0]
BLACK_CMYK = [179, 166, 164, 254]


def wb_analysis(pixels, mode):
	w = 0
	b = 0

	# The most of pictures are drawn or digitized in these color schemes	
	if mode in ["1"]:
		warr = np.all(pixels[0:pixels.size,0:1] == WHITE_1, axis=1)
		w = warr[warr].size
		barr = np.all(pixels[0:pixels.size,0:1] == BLACK_1_L, axis=1)
		b = barr[barr].size 
		
	elif mode in ["L", "LA", "LAB"]:
		warr = np.all(pixels[0:pixels.size,0:1] == WHITE_L, axis=1)
		w = warr[warr].size
		barr = np.all(pixels[0:pixels.size,0:1] == BLACK_1_L, axis=1)
		b = barr[barr].size 
	
	elif mode in ["RGB", "RGBA"]:
		warr = np.all(pixels[0:pixels.size,0:3] == WHITE_RGB, axis=1)
		w = warr[warr].size
		barr = np.all(pixels[0:pixels.size,0:3] == BLACK_RGB, axis=1)
		b = barr[barr].size
	
	elif mode in ["CMYK"]:
		warr = np.all(pixels[0:pixels.size,0:4] == WHITE_CMYK, axis=1)
		w = warr[warr].size
		barr = np.all(pixels[0:pixels.size,0:4] == BLACK_CMYK, axis=1)
		b = barr[barr].size 
	
	else:
		return "This color scheme is not supported"
	
	# We return results in this form, because nopython mode is not supporting dictionaries
	return str(w)+" "+str(b) 

def white_black(link):	
	try:
		img = Image.open(link)
	except TypeError:
		return {"err": "Can't open file of this format"}
	except (ValueError, UnidentifiedImageError):
		return {"err": "Error when opening file"}
	except FileNotFoundError:
		return {"err": "Actually, where you put this file?"}
	else:
		if img.size[0] > 7000 and img.size[1] > 7000:
			return {"err": "Too big picture"}
		else:
			# Because, GIF color pallette is varying
			# start = time.time()
			if img.mode == 'P':
					img = img.convert("RGB")
			pixels = np.array(img).reshape(img.size[0]*img.size[1], len(img.getbands()))
			count = wb_analysis(pixels, img.mode)
			# print(str(time.time() - start)+" s.")
			# Now, we can parse to dictionary without errors and problems
			try:
				# It is enough to transform first element into integer 
				int(count.split()[0])
			except ValueError:
				return {"err": count}
			else:
				w = int(count.split()[0])
				b = int(count.split()[1])
				if w > b:
				
					which_is = "White"
				elif w == b:
					which_is = "Draw"
				else:
					which_is = "Black"
				return {"wpx": w, "bpx": b, "wper": w / (img.size[0]*img.size[1]) * 100, "bper": b / (img.size[0]*img.size[1]) * 100, "which_is": which_is}

			
def hex(code):
	if len(code) == 3:
		return np.array([int(code[0]*2, 16), int(code[1]*2, 16), int(code[2]*2, 16)])
	elif len(code) == 6:
		return np.array([int(code[:2], 16), int(code[2:4], 16), int(code[4:6], 16)])

def hex_analysis(pixels, mode, color):
	rez = 0
	
	if mode in ["1"]:
		if color[0] == color[1] == color[2] == 0:
			pixarr = np.all(pixels[0:pixels.size,0:1] == [0], axis=1)
			rez = pixarr[pixarr].size
		elif color[0] == color[1] == color[2] == 255:
			pixarr = np.all(pixels[0:pixels.size,0:1] == [1], axis=1)
			rez = pixarr[pixarr].size
		else:
			return "This color is not supported in this color scheme!" 	
		
	elif mode in ["L", "LA"]:
		if color[0] == color[1] == color[2]:	
			pixarr = np.all(pixels[0:pixels.size,0:1] == [color[0]], axis=1)
			rez = pixarr[pixarr].size
		else:
			return "This color is not supported in this color scheme!"
	
	elif mode in ["RGB", "RGBA"]:
		pixarr = np.all(pixels[0:pixels.size,0:3] == color, axis=1)
		rez = pixarr[pixarr].size
		
	else:
		return "HEX-codes are not supported in this color scheme!"
	
	# We return results in this form, because nopython mode is not supporting dictionaries
	return str(rez) 
	
def hex_pix(link, code):	
	try:
		img = Image.open(link)
	except TypeError:
		return {"err": "Can't open file of this format"}
	except (ValueError, UnidentifiedImageError):
		return {"err": "Error when opening file"}
	except FileNotFoundError:
		return {"err": "Actually, where you put this file?"}
	else:
		if img.size[0] > 7000 and img.size[1] > 7000:
			return {"err": "Too big picture"}
		else:
			# Because, GIF color pallette is varying
			if len(code) in [3, 6]:
				color = hex(code)
				if img.mode == 'P':
					img = img.convert("RGB")
				pixels = np.array(img).reshape(img.size[0]*img.size[1], len(img.getbands()))
				print(color)
				count = hex_analysis(pixels, img.mode, color)
				try:
					int(count)
				except ValueError:
					return {"err": count}
				else:
					return {"hexpix": int(count), "hexper": int(count) / (img.size[0]*img.size[1]) * 100}
			else:
				return {"err": "Invalid HEX-code!"}
