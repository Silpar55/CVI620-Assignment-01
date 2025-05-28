"""
Flow of the program:

    - Ask for an image
    - Try to load the image
    - Run the menu
    - Call the methods that the user wants to do
    - at exiting the program will

Structure:
	Images modifiers are in the operations folder and each operation will have its own python file
	In the root of the project will be the menu (mein.py) and utils functions such as image loader, display images
	with matplotlib and shared state
"""
import cv2
from image_loader import (load_image, save_image)
from operations import (
    brightness, contrast, grayscale, padding, threshold, blend, undo
)

from preview import show_preview
import state


def main():
	img = load_image()
	if img is None:
		return

	while True:
		print("\n==== Mini Photo Editor ====")
		print("1. Adjust Brightness")
		print("2. Adjust Contrast")
		print("3. Convert to Grayscale")
		print("4. Add Padding")
		print("5. Apply Thresholding")
		print("6. Blend with Another Image")
		print("7. Undo Last Operation")
		print("8. View History of Operations")
		print("9. Save and Exit")
		choice = input("Select an option: ")

		if choice == '1':
			val = int(input("Brightness (-100 to 100): "))
			img = brightness.adjust(img, val)
		elif choice == '2':
			alpha = float(input("Contrast multiplier (example: 1.2, 0.6, etc): "))
			img = contrast.adjust(img, alpha)
		elif choice == '3':
			img = grayscale.convert(img)
		elif choice == '4':
			size = int(input("Padding size (px): "))
			btype = input("Border type (constant, reflect, replicate): ").strip().lower()

			print("Choose padding shape: square / rectangle / custom")
			ar = input("Aspect ratio? (square/custom): ").strip().lower()

			ratio = None
			if ar == 'square':
				ratio = (1, 1)
			elif ar == 'custom':
				w = int(input("Width ratio: "))
				h = int(input("Height ratio: "))
				ratio = (w, h)

			img = padding.add(img, size, btype, ratio)
		elif choice == '5':
			t_type = input("Threshold type (binary/binary_inv): ")
			img = threshold.apply(img, t_type)
		elif choice == '6':
			path = input("Second image path: ")
			alpha = float(input("Alpha (0 to 1): "))
			img = blend.with_image(img, path, alpha)
		elif choice == '7':
			img = undo.last()
		elif choice == '8':
			for i, log in enumerate(state.logs, 1):
				print(f"{i}. {log}")
		elif choice == '9':
			out = input("Save as (filename will include .jpg as default): ")
			save_image(out + '.jpg', img)
			break
		else:
			print("Invalid choice.")

		# at the end of every change compare original vs img
		show_preview(state.history[0], img)


if __name__ == "__main__":
	main()
