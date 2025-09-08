import os
import matplotlib.pyplot as plt
from PIL import Image

def crop_to_square(image):
    """Crop the image to the largest possible square in the center."""
    width, height = image.size
    if width == height:
        return image  
    elif width > height:
        left = (width - height) // 2
        right = left + height
        cropped_image = image.crop((left, 0, right, height))
    else:
        top = (height - width) // 2
        bottom = top + width
        cropped_image = image.crop((0, top, width, bottom))
    return cropped_image

def resize_image(image, target_size):
    """Resize the image to the target size."""
    return image.resize(target_size, Image.Resampling.LANCZOS)

def process_images(directory, output_directory, target_size=(256, 256)):
    square_images = []
    invalid_files = []
    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff")
    os.makedirs(output_directory, exist_ok=True)

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(valid_extensions):
                file_path = os.path.join(root, file)
                try:
                    with Image.open(file_path) as img:
                        cropped_image = crop_to_square(img)
                        resized_image = resize_image(cropped_image, target_size)

                        relative_path = os.path.relpath(file_path, directory)
                        output_path = os.path.join(output_directory, relative_path)
                        os.makedirs(os.path.dirname(output_path), exist_ok=True)
                        resized_image.save(output_path)

                        # Visualization
                        plt.figure(figsize=(10, 5))
                        plt.subplot(1, 2, 1)
                        plt.imshow(img)
                        plt.title("Original Image")
                        plt.axis("off")

                        plt.subplot(1, 2, 2)
                        plt.imshow(resized_image)
                        plt.title("Processed Image (Square)")
                        plt.axis("off")
                        plt.show()

                        square_images.append(file_path)

                except Exception as e:
                    invalid_files.append((file_path, str(e)))

    print(f"\nTotal processed images: {len(square_images)}")
    for img in square_images:
        print(f"  - {img}")

    if invalid_files:
        print(f"\nTotal invalid files: {len(invalid_files)}")
        for file, error in invalid_files:
            print(f"  - {file}: {error}")

if __name__ == "__main__":
    try:
        input_directory = "D:\\workspace\\output"
        output_directory = input("Enter the output directory to save processed images: ").strip()

        if not os.path.isdir(input_directory):
            print("The input directory does not exist. Please check the path.")
        elif not output_directory:
            print("Output directory cannot be empty. Exiting.")
        else:
            target_size_input = input("Enter target size (256 or 512): ").strip()
            if target_size_input not in ["256", "512"]:
                print("Invalid target size. Exiting.")
            else:
                target_size = (int(target_size_input), int(target_size_input))
                process_images(input_directory, output_directory, target_size=target_size)
    except Exception as e:
        print(f"An error occurred: {e}")