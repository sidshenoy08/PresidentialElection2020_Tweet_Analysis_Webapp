from app.modules.candidate_analysis.repository.CandidateAnalysisRepository import CandidateAnalysisRepository

class CandidateAnalysisService:
    @staticmethod
    def get_region_wise_engagement():
        rows, columns = CandidateAnalysisRepository.get_region_wise_engagement()
        return [dict(zip(columns, row)) for row in rows]
    
    @staticmethod
    def get_daily_trends(candidate):
        rows, columns = CandidateAnalysisRepository.get_daily_trends(candidate)
        return [dict(zip(columns, row)) for row in rows]