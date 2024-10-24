from flask import Blueprint, request, jsonify
from src.main.factories.calculator_4_factory import calculator_4_factory


calc_bp = Blueprint('calc_routes', __name__)

@calc_bp.route('/calculator4', methods=['POST'])
def calculator_4():
    try:
        data = request.json
        numbers = data.get("numbers")

        response = calculator_4_factory.calculate_average(numbers)
        return jsonify(response), 200
    except Exception as exception:
        return jsonify(exception)