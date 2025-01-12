from flask import Flask, request, jsonify, abort
from threading import Lock

app = Flask(__name__)

# In-memory data storage
products = {}
product_id_counter = 1
lock = Lock()


# Create a new product
@app.route("/products", methods=["POST"])
def create_product():
    global product_id_counter
    data = request.get_json()
    if not data or "name" not in data or "price" not in data:
        abort(400, description="Invalid product data")

    with lock:
        product_id = product_id_counter
        products[product_id] = {"id": product_id, "name": data["name"], "price": data["price"]}
        product_id_counter += 1

    return jsonify(products[product_id]), 201


# Get all products
@app.route("/products", methods=["GET"])
def get_products():
    with lock:
        return jsonify(list(products.values())), 200


# Get a single product by ID
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    with lock:
        product = products.get(product_id)
        if not product:
            abort(404, description="Product not found")
        return jsonify(product), 200


# Update a product by ID
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()
    if not data or "name" not in data or "price" not in data:
        abort(400, description="Invalid product data")

    with lock:
        product = products.get(product_id)
        if not product:
            abort(404, description="Product not found")

        product["name"] = data["name"]
        product["price"] = data["price"]
        products[product_id] = product

    return jsonify(product), 200


# Delete a product by ID
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    with lock:
        product = products.pop(product_id, None)
        if not product:
            abort(404, description="Product not found")
        return "", 204


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
