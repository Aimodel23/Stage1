from flask import Blueprint, request, jsonify
from src.storage import StorageManager

# Initialize Blueprint
user_bp = Blueprint('user', __name__)

# Initialize Storage Manager
storage_manager = StorageManager()

@user_bp.route('/storage', methods=['POST'])
def save_data():
    data = request.json
    if 'data' in data:
        file_id = storage_manager.save_data(data['data'])
        return jsonify({'file_id': file_id}), 201
    return jsonify({'error': 'Invalid data'}), 400

@user_bp.route('/storage/<file_id>', methods=['GET'])
def get_data(file_id):
    data = storage_manager.retrieve_data(file_id)
    if data:
        return jsonify({'data': data}), 200
    return jsonify({'error': 'File not found'}), 404

@user_bp.route('/storage/<file_id>', methods=['DELETE'])
def delete_data(file_id):
    success = storage_manager.delete_data(file_id)
    if success:
        return jsonify({'message': 'File deleted'}), 200
    return jsonify({'error': 'File not found'}), 404
