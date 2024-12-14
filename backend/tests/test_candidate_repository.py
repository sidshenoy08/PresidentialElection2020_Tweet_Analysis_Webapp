import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from app import create_app
from app.modules.candidate_analysis.repository.CandidateAnalysisRepository import CandidateAnalysisRepository

class TestCandidateAnalysisRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a Flask app context for the test
        cls.app = create_app()
        cls.app.config.update({
            "TESTING": True,
        })
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

    # @classmethod
    # def tearDownClass(cls):
    #     # Pop the app context after tests
    #     cls.app_context.pop()

    @patch('app.modules.candidate_analysis.repository.CandidateAnalysisRepository.db.session.execute')
    @patch('app.modules.candidate_analysis.repository.CandidateAnalysisRepository.text')
    def test_get_region_wise_engagement(self, mock_text, mock_execute):
        # Mock SQL text and db session execute
        mock_text.return_value = 'mock_sql'
        mock_result = MagicMock()
        mock_result.fetchall.return_value = [(100, 'USA')]
        mock_result.keys.return_value = ['total_engagement', 'country']
        mock_execute.return_value = mock_result

        # Call the repository function
        result = CandidateAnalysisRepository.get_region_wise_engagement()
        expected = [(100, 'USA')], ['total_engagement', 'country']

        # Assertions
        self.assertEqual(result, expected)
        mock_text.assert_called_once()
        mock_execute.assert_called_once_with('mock_sql')


if __name__ == '__main__':
    unittest.main()