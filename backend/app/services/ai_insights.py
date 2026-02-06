def generate_insights(score_data):
    return f"""
    Financial Score: {score_data['score']}
    Risk Level: {score_data['risk']}

    Recommendation:
    Improve profit margins and reduce unnecessary expenses.
    """
