from app.modules.candidate_analysis.repository.CandidateAnalysisRepository import CandidateAnalysisRepository

class CandidateAnalysisService:
    @staticmethod
    def get_region_wise_engagement():
        rows, columns = CandidateAnalysisRepository.get_region_wise_engagement()
        return [dict(zip(columns, row)) for row in rows]
    
    @staticmethod
    def get_daily_trends(candidate):
        data = CandidateAnalysisRepository.get_daily_trends(candidate)
        return [dict(row) for row in data]

    @staticmethod
    def get_weekly_comparison_with_events():
        data = CandidateAnalysisRepository.get_weekly_comparison_with_events()
        return [dict(row) for row in data]
