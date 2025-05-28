import cv2
import state


def load_image():
	path = input("Image path: ")
	img = cv2.imread(path)
	# Clear the image in case has something
	if img is not None:
		state.history.clear()
		state.logs.clear()

		state.history.append(img.copy())
	else:
		print("Failed to load image.")
	return img


def save_image(filename, img):
	cv2.imwrite(filename, img)
	print(f"Image saved as {filename}")
