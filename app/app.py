import os
from datetime import datetime

from bson import ObjectId
from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(
    os.getenv("MONGO_URL", "mongodb://localhost:27017/"),
    serverSelectionTimeoutMS=5000,
)
db = client["hepapi"]
items = db["items"]


def serialize(doc):
    doc["_id"] = str(doc["_id"])
    for key, value in list(doc.items()):
        if hasattr(value, "isoformat"):
            doc[key] = value.isoformat()
    return doc


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/api/items", methods=["GET"])
def list_items():
    return jsonify([serialize(i) for i in items.find()]), 200


@app.route("/api/items/<id>", methods=["GET"])
def get_item(id):
    item = items.find_one({"_id": ObjectId(id)})
    if not item:
        return jsonify({"error": "not found"}), 404
    return jsonify(serialize(item)), 200


@app.route("/api/items", methods=["POST"])
def create_item():
    data = request.get_json()
    data["created"] = datetime.now()
    result = items.insert_one(data)
    return jsonify({"_id": str(result.inserted_id)}), 201


@app.route("/api/items/<id>", methods=["PUT"])
def update_item(id):
    data = request.get_json()
    result = items.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.matched_count == 0:
        return jsonify({"error": "not found"}), 404
    return jsonify({"message": "updated"}), 200


@app.route("/api/items/<id>", methods=["DELETE"])
def delete_item(id):
    result = items.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({"error": "not found"}), 404
    return jsonify({"message": "deleted"}), 200

# @app.route("/api/items/<id>", methods=["DELETE"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)