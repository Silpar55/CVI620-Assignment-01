import cv2
import state

"""
At the moment of converting an BGR image into a grayscale, we'll lose the 3 channels 
leading to unexpected behaviours at the moment of calling other image modifications
therefore, it is need to convert the gray scale into BGR again to get the 3 channels 
and preserve the grayscale
"""


def convert(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	result = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
	state.logs.append("grayscale")
	state.history.append(result.copy())
	return result
