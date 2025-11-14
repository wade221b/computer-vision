import os
from ultralytics import SAM

# Load the SAM model
model = SAM("sam_b.pt")

# Directory containing your images
image_dir = "/dataset"

# Loop through all files in the directory
for filename in os.listdir(image_dir):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):  # Filter image files
        image_path = os.path.join(image_dir, filename)
        # Run inference on the image
        results = model(image_path)
        # Optionally, save or process results here
        print(f"Processed {filename}")

