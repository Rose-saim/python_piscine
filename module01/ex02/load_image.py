from PIL import Image
import numpy as np


def load(path: str) -> np.ndarray:
    """This function loads an image, prints its format, \
and its pixels content in RGB format."""
    try:
        image = Image.open(path)
        array = np.array(image)
        print("The shape of image is: ", array.shape)
        return array
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    load("../landscape.jpg")

if __name__ == "__main__":
    main()
