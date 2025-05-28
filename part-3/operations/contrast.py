import cv2
import state


# Alpha controls contrast alpha = 1 means unchanged
# Beta controls brightness beta = 0 means unchanged

def adjust(img, alpha):
	result = cv2.convertScaleAbs(img, alpha=alpha, beta=0)
	state.logs.append(f"contrast x{alpha}")
	state.history.append(result.copy())
	return result
