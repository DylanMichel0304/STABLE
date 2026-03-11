import random
import shutil
from pathlib import Path

def sample_images(input_dir, output_dir, n_samples=700, seed=42):
    """
    Sélectionne aléatoirement n_samples images depuis input_dir
    et les copie dans output_dir.
    """
    valid_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".gif"}
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    if not input_path.exists() or not input_path.is_dir():
        raise ValueError(f"Dossier d'entrée invalide : {input_dir}")
    output_path.mkdir(parents=True, exist_ok=True)
    image_files = [
        f for f in input_path.iterdir()
        if f.is_file() and f.suffix.lower() in valid_extensions
    ]
    print(f"[{input_dir}] {len(image_files)} images trouvées.")
    if len(image_files) < n_samples:
        raise ValueError(
            f"Le dossier {input_dir} contient seulement {len(image_files)} images, "
            f"impossible d'en sélectionner {n_samples}."
        )
    random.seed(seed)
    selected_images = random.sample(image_files, n_samples)
    for img_path in selected_images:
        shutil.copy2(img_path, output_path / img_path.name)
    print(f"{n_samples} images copiées de {input_dir} vers {output_dir}")

def create_two_random_datasets(input_dir_1, output_dir_1,
                               n_samples=700, seed=42):
    """
    Traite deux dossiers d'entrée et crée deux dossiers de sortie.
    """
    sample_images(input_dir_1, output_dir_1, n_samples=n_samples, seed=seed)

if __name__ == "__main__":
    input_dataset_1 = "stable/dataset/train/images"
    output_dataset_1 = "stable/dataset/train/B_7000"
    create_two_random_datasets(
        input_dir_1=input_dataset_1,
        output_dir_1=output_dataset_1,
        n_samples=700,
        seed=42
    )