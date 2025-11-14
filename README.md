# computer-vision
repo to track all computer vision models and how I use them

## Running the SAM Model on a Dataset

To run the Segment Anything Model (SAM) on all images contained in the `/dataset` directory, use the following command in your terminal:

yolo predict model=sam_b.pt source=/dataset


This command will process all images in the `/dataset` folder and output the segmentation results.
