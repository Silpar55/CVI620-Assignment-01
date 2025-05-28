import matplotlib.pyplot as plt
import cv2


def show_preview(original, modified):
	fig, axs = plt.subplots(1, 2, figsize=(10, 5))
	axs[0].imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
	axs[0].set_title("Original")
	axs[1].imshow(cv2.cvtColor(modified, cv2.COLOR_BGR2RGB))
	axs[1].set_title("Modified")
	for ax in axs:
		ax.axis("off")
	plt.tight_layout()
	plt.show()
