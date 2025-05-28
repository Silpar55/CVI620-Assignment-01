import cv2
import state


def add(img, size, border_type, target_ratio=None):
	h, w = img.shape[:2]

	top = bottom = left = right = size

	# target_radio = (w, h)

	if target_ratio:
		target_w = int(h * target_ratio[0] / target_ratio[1])
		target_h = int(w * target_ratio[1] / target_ratio[0])

		if target_w > w:
			pad_w = target_w - w
			left = pad_w // 2
			right = pad_w - left
		elif target_h > h:
			pad_h = target_h - h
			top = pad_h // 2
			bottom = pad_h - top

	# Apply padding with additional user-defined size
	top += size
	bottom += size
	left += size
	right += size

	border_types = {
		'constant': cv2.BORDER_CONSTANT,
		'reflect': cv2.BORDER_REFLECT,
		'replicate': cv2.BORDER_REPLICATE
	}

	result = cv2.copyMakeBorder(img, top, bottom, left, right,
								border_types.get(border_type, cv2.BORDER_CONSTANT),
								value=[255, 255, 255])
	state.logs.append(f"padding {size}px {border_type} with ratio {target_ratio}")
	state.history.append(result.copy())
	return result
