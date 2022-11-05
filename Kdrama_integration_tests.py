import unittest
from unittest.mock import MagicMock, patch
from KDrama_Classes import KoreanShows
from KDrama_Classes import KDramaDB
from database_connection import execute_query

class KDramaIntegrationTests(unittest.TestCase):
    @patch('KDrama_Classes.requests')
    def test_get_completed(self, mock_requests):
        #Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "page": 1,
            "results": [
                {
                    "backdrop_path": "/u9ESngthtC33R7SHmkeJPZg1Xvs.jpg",
                    "first_air_date": "1999-09-29",
                    "genre_ids": [35, 18],
                    "id": 3151,
                    "name": "Popular",
                    "origin_country": ["US"],
                    "original_language": "en",
                    "original_name": "Popular",
                    "overview": "Brooke",
                    "popularity": 9.69,
                    "poster_path": "/eROSmxuiMQVIwcIqGBZHd84OPa2.jpg",
                    "vote_average": 6.6,
                    "vote_count": 30
                },
                {
                    "backdrop_path": '',
                    "first_air_date": "1997-09-07",
                    "genre_ids": [99, 10751, 10762],
                    "id": 14213,
                    "name": "Popular Mechanics for Kids",
                    "origin_country": ["KR"],
                    "original_language": "en",
                    "original_name": "Popular Mechanics for Kids",
                    "overview": "Popula",
                    "popularity": 2.962,
                    "poster_path": '',
                    "vote_average": 8.8,
                    "vote_count": 6
                }
            ],
            "total_pages": 2,
            "total_results": 2
        }

        # specify the return value of the get() method
        mock_requests.get.return_value = mock_response

        KDramaDB.korean_show_search('popular')
        #Act

        KDramaDB.insert_show_complete()

        #Assert
        query = "SELECT * FROM completed_shows"
        result = execute_query(query)
        self.assertIsNotNone(result)

    @patch('KDrama_Classes.requests')
    def test_get_show_to_watch(self, mock_requests):
        #Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "page": 1,
            "results": [
                {
                    "backdrop_path": "/u9ESngthtC33R7SHmkeJPZg1Xvs.jpg",
                    "first_air_date": "1999-09-29",
                    "genre_ids": [35, 18],
                    "id": 3151,
                    "name": "Popular",
                    "origin_country": ["US"],
                    "original_language": "en",
                    "original_name": "Popular",
                    "overview": "Brooke",
                    "popularity": 9.69,
                    "poster_path": "/eROSmxuiMQVIwcIqGBZHd84OPa2.jpg",
                    "vote_average": 6.6,
                    "vote_count": 30
                },
                {
                    "backdrop_path": '',
                    "first_air_date": "1997-09-07",
                    "genre_ids": [99, 10751, 10762],
                    "id": 14213,
                    "name": "Popular Mechanics for Kids",
                    "origin_country": ["KR"],
                    "original_language": "en",
                    "original_name": "Popular Mechanics for Kids",
                    "overview": "Popular ABC.",
                    "popularity": 2.962,
                    "poster_path": '',
                    "vote_average": 8.8,
                    "vote_count": 6
                }
            ],
            "total_pages": 2,
            "total_results": 2
        }

        # specify the return value of the get() method
        mock_requests.get.return_value = mock_response

        KDramaDB.korean_show_search('popular')
        #Act

        KDramaDB.insert_show_to_watch()

        #Assert
        query = "SELECT * FROM watch_list"
        result = execute_query(query)
        self.assertIsNotNone(result)

