from flask import Blueprint
from app.modules.candidate_analysis.controller.CandidateAnalysisController import CandidateAnalysisController

candidate_analysis_bp = Blueprint('candidate_analysis_bp', __name__)
candidate_analysis_bp.route('/region-wise-engagement', methods=['GET'])(CandidateAnalysisController.get_region_wise_engagement)
candidate_analysis_bp.route('/daily-trends', methods=['GET'])(CandidateAnalysisController.get_daily_trends)
candidate_analysis_bp.route('/weekly-comparison-events', methods=['GET'])(CandidateAnalysisController.get_weekly_comparison_with_events)