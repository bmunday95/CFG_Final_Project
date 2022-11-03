import unittest
from unittest.mock import MagicMock, patch
from KDrama_Classes import KoreanShows

class KoreanShowSearch(unittest.TestCase):
    @patch('KDrama_Classes.requests')
    def test_find_album_by_id_success(self, mock_requests):
        # mock the response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
          "page": 1,
          "results": [
            {
              "backdrop_path": "/u9ESngthtC33R7SHmkeJPZg1Xvs.jpg",
              "first_air_date": "1999-09-29",
              "genre_ids": [ 35, 18 ],
              "id": 3151,
              "name": "Popular",
              "origin_country": [ "US" ],
              "original_language": "en",
              "original_name": "Popular",
              "overview": "Brooke McQueen, a popular cheerleader at Jacqueline Kennedy High School, and Sam McPherson, the editor of the school paper, are polar opposites. When their single parents unexpectedly meet and get engaged, Brooke and Sam have to deal with their new situation on top of regular teenage girl problems.",
              "popularity": 9.69,
              "poster_path": "/eROSmxuiMQVIwcIqGBZHd84OPa2.jpg",
              "vote_average": 6.6,
              "vote_count": 30
            },
            {
              "backdrop_path": '',
              "first_air_date": "1997-09-07",
              "genre_ids": [ 99, 10751, 10762 ],
              "id": 14213,
              "name": "Popular Mechanics for Kids",
              "origin_country": [ "KR" ],
              "original_language": "en",
              "original_name": "Popular Mechanics for Kids",
              "overview": "Popular Mechanics for Kids is an educational Canadian television series based on Popular Mechanics magazine. It was notable for starting the careers of both Elisha Cuthbert and Jay Baruchel. The show's purpose was to teach viewers how things work. It was awarded the Parents Choice Award in 2003, and was nominated for the Gemini Awards.\n\nThe series aired from 1997 to 2001, and re-runs of the show continued to air on many channels until 2008. It aired on BBC Kids and Discovery Kids until December 31, 2009. After the closure of Discovery Kids Canada, BBC Kids stopped airing re-runs in all countries except Canada. The reruns on BBC Kids in Canada ended on May 14, 2011. As of 2013 re-runs of the show continue to air on Knowledge Network. Along with Cuthbert and Baruchel, the cast included Charles Powell nicknamed \"Charlie\" for the series, Tyler Kyte, and eventually Vanessa Lengies.\n\nThe show was filmed primarily in Montreal, Quebec, and is currently distributed on VHS / DVD by Koch Vision.",
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

        lst = KoreanShows.korean_show_search('popular')
        self.assertEqual(len(lst), 3)

        self.assertIn('Show title', lst[0], "Show Title didn't find.")
        self.assertIn('Show release date', lst[1], "Show Release date didn't find.")
        self.assertIn('Show overview', lst[2], "Show Overview didn't find.")

    @patch('KDrama_Classes.requests')
    def test_find_album_by_id_success(self, mock_requests):
        # mock the response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
          "page": 1,
          "results": [
            {
              "backdrop_path": "/u9ESngthtC33R7SHmkeJPZg1Xvs.jpg",
              "first_air_date": "1999-09-29",
              "genre_ids": [ 35, 18 ],
              "id": 3151,
              "name": "Popular",
              "origin_country": [ "US" ],
              "original_language": "en",
              "original_name": "Popular",
              "overview": "Brooke McQueen, a popular cheerleader at Jacqueline Kennedy High School, and Sam McPherson, the editor of the school paper, are polar opposites. When their single parents unexpectedly meet and get engaged, Brooke and Sam have to deal with their new situation on top of regular teenage girl problems.",
              "popularity": 9.69,
              "poster_path": "/eROSmxuiMQVIwcIqGBZHd84OPa2.jpg",
              "vote_average": 6.6,
              "vote_count": 30
            }
          ],
          "total_pages": 1,
          "total_results": 1
        }

        # specify the return value of the get() method
        mock_requests.get.return_value = mock_response

        lst = KoreanShows.korean_show_search('popular')
        self.assertEqual(len(lst), 0)
