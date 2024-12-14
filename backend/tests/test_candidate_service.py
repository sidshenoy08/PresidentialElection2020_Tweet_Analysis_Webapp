import unittest
from unittest.mock import patch
from app.modules.candidate_analysis.service.CandidateAnalysisService import CandidateAnalysisService

class TestCandidateAnalysisService(unittest.TestCase):

    @patch('app.modules.candidate_analysis.service.CandidateAnalysisService.CandidateAnalysisRepository.get_region_wise_engagement')
    def test_get_region_wise_engagement(self, mock_get_region_wise_engagement):
        mock_get_region_wise_engagement.return_value = ([(100, 'USA')], ['engagement_count', 'region'])
        result = CandidateAnalysisService.get_region_wise_engagement()
        expected = [{'engagement_count': 100, 'region': 'USA'}]
        self.assertEqual(result, expected)

    @patch('app.modules.candidate_analysis.service.CandidateAnalysisService.CandidateAnalysisRepository.get_daily_trends')
    def test_get_daily_trends(self, mock_get_daily_trends):
        mock_get_daily_trends.return_value = ([(50, '2020-11-03')], ['tweet_count', 'date'])
        candidate = 'Trump'
        result = CandidateAnalysisService.get_daily_trends(candidate)
        expected = [{'tweet_count': 50, 'date': '2020-11-03'}]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()