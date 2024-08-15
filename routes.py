from flask import render_template, request, jsonify
from app import app, db
from app.models import User, Progress
from app.ml_models.recommendation import get_recommendations

@app.route('/')
@app.route('/index')
def index():
    return render_template('dashboard.html')

@app.route('/progress/<int:user_id>', methods=['GET'])
def get_user_progress(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    progress = Progress.query.filter_by(user_id=user_id).all()
    return jsonify([{'topic': p.topic, 'score': p.score} for p in progress])

@app.route('/recommend/<int:user_id>', methods=['GET'])
def recommend(user_id):
    recommendations = get_recommendations(user_id)
    return jsonify(recommendations)
