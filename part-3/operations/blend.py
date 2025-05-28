import cv2
import numpy as np
import state


def with_image(img1, img2_path, alpha):
	img2 = cv2.imread(img2_path)
	if img2 is None:
		print("Failed to load the second image.")
		return img1
	img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
	blended = ((1 - alpha) * img1 + alpha * img2_resized).astype(np.uint8)
	state.logs.append(f"blended with {img2_path} alpha={alpha}")
	state.history.append(blended.copy())
	return blended
