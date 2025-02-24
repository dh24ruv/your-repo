import os
import pandas as pd
import matplotlib.pyplot as plt

def check_file_exists(filepath):
    """Check if a file exists at the given path."""
    if os.path.exists(filepath):
        print(f"✅ File found: {filepath}")
    else:
        print(f"❌ File not found: {filepath}")


expected_files = ["dataset.csv", "distance_classification.py", "notebook.ipynb"]


for file in expected_files:
    check_file_exists(file)


image_path = "images/sample_image.png"
check_file_exists(image_path)

try:
    df = pd.read_csv("dataset.csv")
    print("✅ Dataset loaded successfully!")
    print(df.head())
except Exception as e:
    print(f"❌ Failed to load dataset: {e}")

try:
    img = plt.imread(image_path)
    plt.imshow(img)
    plt.axis("off")
    plt.show()
    print("✅ Image displayed successfully!")
except Exception as e:
    print(f"❌ Failed to display image: {e}")
