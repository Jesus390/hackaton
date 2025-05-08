from flask import render_template
from flask_login import login_required, current_user
from app.main import main_bp

from app.models.professional import Professional
from app.models.user import User
from flask import request

@main_bp.route('/')
def index():
    return render_template('main/index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('main/dashboard.html', user=current_user)


@main_bp.route('/search')
def search():
    query = request.args.get('q', '').strip()
    results = []

    if query:
        results = Professional.query.filter(Professional.profession.ilike(f'%{query}%')).all()

    return render_template('main/search_results.html', query=query, results=results)

