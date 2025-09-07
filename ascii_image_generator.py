import sys
from PIL import Image

# --- Configuration ---
# The list of characters, from darkest to lightest.
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
NEW_WIDTH = 100

# --- Functions ---

def resize_image(image):
    """Resizes an image while maintaining aspect ratio, accounting for character height."""
    width, height = image.size
    # The 1.65 factor adjusts for the fact that characters are taller than they are wide.
    ratio = height / (width * 1.65) 
    new_height = int(NEW_WIDTH * ratio)
    resized_image = image.resize((NEW_WIDTH, new_height))
    return resized_image

def grayscale(image):
    """Converts an image to grayscale."""
    return image.convert("L")

def pixels_to_ascii(image):
    """Maps each pixel to an ASCII character and returns the full string."""
    pixels = image.getdata()
    ascii_str = ""
    # The range of a pixel is 0-255. We divide by 25 to map it to our 11 ASCII characters.
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25] 
    return ascii_str

# --- Main Logic ---

def main():
    """The main function that runs the conversion process."""
    # Check if a path was provided when running the script
    if len(sys.argv) != 2:
        print("Usage: python ascii_art.py <path_to_image>")
        print("Example: python ascii_art.py my_cat.jpg")
        return

    image_path = sys.argv[1]
    
    try:
        img = Image.open(image_path)
        print("Image opened successfully.")
    except FileNotFoundError:
        print(f"Error: The image file was not found at '{image_path}'")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # 1. Resize the image
    resized_image = resize_image(img)

    # 2. Convert to grayscale
    grayscale_image = grayscale(resized_image)

    # 3. Convert pixels to ASCII string
    ascii_art_str = pixels_to_ascii(grayscale_image)

    # 4. Print the result
    img_width = grayscale_image.width
    for i in range(0, len(ascii_art_str), img_width):
        print(ascii_art_str[i:i+img_width])

# --- Run the script ---
if __name__ == '__main__':
    main()