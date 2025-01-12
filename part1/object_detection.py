import cv2
import numpy as np
import argparse
import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.transforms import functional as F

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Object Detection on Shelf Images")
parser.add_argument("--input", required=True, help="Path to the input image")
parser.add_argument("--output", required=True, help="Path to save the output image")
args = parser.parse_args()


# Load the pre-trained Faster R-CNN model
def load_model():
    model = fasterrcnn_resnet50_fpn(pretrained=True)
    model.eval()
    return model


# Perform object detection
def detect_objects(image_path, model):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Unable to load image from {image_path}")

    # Convert the image to a tensor
    image_tensor = F.to_tensor(image).unsqueeze(0)

    # Debugging the model input shape
    print(f"Input image shape: {image_tensor.shape}")

    # Perform detection
    with torch.no_grad():
        detections = model(image_tensor)[0]

    return image, detections


# Draw bounding boxes
def draw_bounding_boxes(image, detections):
    for i in range(len(detections["boxes"])):
        box = detections["boxes"][i].cpu().numpy().astype(int)
        score = detections["scores"][i].cpu().numpy()
        label = detections["labels"][i].cpu().numpy()

        if score > 0.5:  # Only draw boxes with a confidence score above 0.5
            cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
            cv2.putText(image, f"{label} {score:.2f}", (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return image


# Main function
def main():
    # Load model
    model = load_model()

    # Detect objects
    input_image_path = args.input
    output_image_path = args.output

    original_image, detections = detect_objects(input_image_path, model)

    # Draw bounding boxes
    output_image = draw_bounding_boxes(original_image, detections)

    # Save the output
    cv2.imwrite(output_image_path, output_image)
    print(f"Output saved to {output_image_path}")


if __name__ == "__main__":
    main()