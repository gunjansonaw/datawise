from flask import Blueprint, request, jsonify
from services.quality_log_service import QualityLogService

quality_logs_blueprint = Blueprint('quality_logs', __name__)
quality_log_service = QualityLogService()

@quality_logs_blueprint.route('/datasets/<dataset_id>/quality-logs', methods=['POST'])
def add_quality_log(dataset_id):
    data = request.get_json()
    result = quality_log_service.add_quality_log(dataset_id, data)
    return jsonify(result), 201

@quality_logs_blueprint.route('/datasets/<dataset_id>/quality-logs', methods=['GET'])
def get_quality_logs(dataset_id):
    quality_logs = quality_log_service.get_quality_logs(dataset_id)
    return jsonify(quality_logs), 200
