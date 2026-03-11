from pathlib import Path
import random
import shutil
import sys
 
 
def move_random_images(input_folder: str, output_folder: str, n_images: int = 250) -> None:
    input_path = Path(input_folder)
    output_path = Path(output_folder)
 
    if not input_path.exists() or not input_path.is_dir():
        raise ValueError(f"Input folder does not exist or is not a folder: {input_folder}")
 
    output_path.mkdir(parents=True, exist_ok=True)
 
    # Common image extensions
    image_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp"}
 
    images = [p for p in input_path.iterdir() if p.is_file() and p.suffix.lower() in image_extensions]
 
    if len(images) < n_images:
        raise ValueError(
            f"Not enough images in input folder. Found {len(images)}, but {n_images} are required."
        )
 
    selected_images = random.sample(images, n_images)
 
    for img_path in selected_images:
        destination = output_path / img_path.name
 
        # Avoid overwriting if a file with the same name already exists
        if destination.exists():
            stem = img_path.stem
            suffix = img_path.suffix
            counter = 1
            while destination.exists():
                destination = output_path / f"{stem}_{counter}{suffix}"
                counter += 1
 
        # Move = transferred to output and removed from input
        shutil.move(str(img_path), str(destination))
 
    print(f"Moved {n_images} images from '{input_folder}' to '{output_folder}'.")
 
 
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python move_random_images.py <input_folder> <output_folder>")
        sys.exit(1)
 
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
 
    move_random_images(input_folder, output_folder)