import cv2
import state


# Alpha controls contrast alpha = 1 means unchanged
# Beta controls brightness beta = 0 means unchanged
def adjust(img, value):
	result = cv2.convertScaleAbs(img, alpha=1, beta=value)
	state.logs.append(f"brightness {value}")
	state.history.append(result.copy())
	return result
