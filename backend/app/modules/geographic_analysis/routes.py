from flask import Blueprint
from app.modules.geographic_analysis.controller.GeographicAnalysisController import GeographicAnalysisController

geographic_analysis_bp = Blueprint('geographic_analysis', __name__)

geographic_analysis_bp.route('/most-tweets-by-country', methods=['GET'])(GeographicAnalysisController.get_most_tweets_by_country)
geographic_analysis_bp.route('/city-level-analysis', methods=['GET'])(GeographicAnalysisController.get_city_level_analysis)
geographic_analysis_bp.route('/top-tweets-by-region', methods=['GET'])(GeographicAnalysisController.get_top_tweets_by_region)