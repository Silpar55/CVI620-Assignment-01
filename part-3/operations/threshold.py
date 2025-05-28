import cv2
import state


def apply(img, method='binary'):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	t_type = cv2.THRESH_BINARY if method == 'binary' else cv2.THRESH_BINARY_INV

	# For better user experience we can use OTSU's method to get the best threshold
	# https://www.geeksforgeeks.org/optimum-global-thresholding-using-otsus-method/
	# (This too much math for my brain)

	_, thresh = cv2.threshold(gray, 0, 255, t_type + cv2.THRESH_OTSU)
	result = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
	state.logs.append(f"threshold {method}")
	state.history.append(result.copy())
	return result
