import numpy as np
from app.models import User, Progress

def get_recommendations(user_id):
    user = User.query.get(user_id)
    if not user:
        return {'error': 'User not found'}
    
    # Example: Simple content-based recommendation using user progress data
    user_progress = Progress.query.filter_by(user_id=user_id).all()
    
    # Simulated recommendation logic
    topics = [p.topic for p in user_progress]
    scores = [p.score for p in user_progress]
    
    recommendations = []
    for topic, score in zip(topics, scores):
        if score < 70:  # Recommend topics where the score is low
            recommendations.append(f'Revisit {topic}')
    
    return {'recommendations': recommendations}
