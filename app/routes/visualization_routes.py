from flask import Blueprint, render_template, jsonify
from app.visualization.charts import create_visualization

visualization_bp = Blueprint('visualization', __name__)

@visualization_bp.route('/visualization')
def visualization():
    return render_template('visualization.html')

@visualization_bp.route('/api/visualize', methods=['POST'])
def generate_visualization():
    data = request.get_json()
    chart = create_visualization(data)
    return jsonify(chart)
