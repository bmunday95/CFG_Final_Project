import unittest
from KDrama_Classes import KoreanShows

class IsKoreanShow_test(unittest.TestCase):
    def testbool_func_tvDict_is_Null(self):
        tv_dict = {'origin_country': []}
        self.assertFalse(KoreanShows.is_korean_show(tv_dict))

    def testbool_func_tvDict_has_origincountry_Korean(self):
           tv_dict = {'origin_country': ['KR']}
           self.assertTrue(KoreanShows.is_korean_show(tv_dict))

    def testbool_func_tvDict_has_origincountry_NonKorean(self):
           tv_dict = {'origin_country': ['US']}
           self.assertFalse(KoreanShows.is_korean_show(tv_dict))

    def testbool_func_tvDict_has_origincountry_KoreanWithManyContry(self):
           tv_dict = {'origin_country': ['KR','US','UK','IND']}
           self.assertTrue(KoreanShows.is_korean_show(tv_dict))