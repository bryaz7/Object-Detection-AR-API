# Project Overview

This project consists of three parts:
1. Object Detection
2. Flask-based RESTful API for Product Management
3. Object Detection with Augmented Reality (AR) Effects

## Part 1: Object Detection

### Setup

Install the required packages:

    ```sh
    pip install torch torchvision opencv-python
    ```

### Execution

Run the object detection script with the following command:

    ```sh
    python3 object_detection.py --input <path_to_input_image> --output <path_to_output_image>
    ```

Example:

```sh
python3 object_detection.py --input ../data/000000000191.jpg --output output.jpg
```

## Part 2: Flask-based RESTful API for Product Management

### Setup

    ```sh
    pip install Flask
    ```

### Execution
    ```sh
    python3 app.py
    ```

Interacting with the API using curl

Create a New Product:

    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"name": "Product1", "price": 100}' http://127.0.0.1:5000/products
    ```
Get All Products:

    ```sh
    curl -X GET http://127.0.0.1:5000/products
    ```
Get a Single Product by ID:

    ```sh
    curl -X GET http://127.0.0.1:5000/products/1
    ```
Update a Product by ID:

    ```sh
    curl -X PUT -H "Content-Type: application/json" -d '{"name": "UpdatedProduct1", "price": 150}' http://127.0.0.1:5000/products/1
    ```

## Part 3: Object Detection with Augmented Reality (AR) Effects

### Setup
1. Install the required packages:

    ```sh
    pip install torch torchvision opencv-python
    ```

### Execution
Run the object detection with AR effects script with the following command:

    ```sh
    python3 object_detection_ar.py --input <path_to_input_image> --output <path_to_output_image>
    ```

Example:

    ```sh
    python3 object_detection_ar.py --input ../data/000000000191.jpg --output output_ar.jpg
    ```