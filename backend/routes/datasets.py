from flask import Blueprint, request, jsonify
from services.dataset_service import DatasetService

datasets_blueprint = Blueprint('datasets', __name__)
dataset_service = DatasetService()

@datasets_blueprint.route('/datasets', methods=['POST'])
def create_dataset():
    data = request.get_json()
    result = dataset_service.create_dataset(data)
    return jsonify(result), 201

@datasets_blueprint.route('/datasets', methods=['GET'])
def get_datasets():
    owner = request.args.get('owner')
    tag = request.args.get('tag')
    datasets = dataset_service.get_datasets(owner, tag)
    return jsonify(datasets), 200

@datasets_blueprint.route('/datasets/<id>', methods=['GET'])
def get_dataset(id):
    dataset = dataset_service.get_dataset(id)
    if dataset:
        return jsonify(dataset), 200
    else:
        return jsonify({"error": "Dataset not found"}), 404

@datasets_blueprint.route('/datasets/<id>', methods=['PUT'])
def update_dataset(id):
    data = request.get_json()
    result = dataset_service.update_dataset(id, data)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"error": "Dataset not found"}), 404

@datasets_blueprint.route('/datasets/<id>', methods=['DELETE'])
def delete_dataset(id):
    result = dataset_service.delete_dataset(id)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"error": "Dataset not found"}), 404
