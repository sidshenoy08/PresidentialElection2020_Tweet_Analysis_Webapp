from flask import jsonify, request
from app.modules.candidate_analysis.service.CandidateAnalysisService import CandidateAnalysisService




class CandidateAnalysisController:
    @staticmethod
    def get_region_wise_engagement():
        data = CandidateAnalysisService.get_region_wise_engagement()
        return jsonify(data), 200
    
    @staticmethod
    def get_daily_trends():
        candidate = request.args.get('candidate', 'Trump')
        data = CandidateAnalysisService.get_daily_trends(candidate)
        return jsonify(data), 200