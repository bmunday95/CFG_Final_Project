import unittest
import json
from bool_functions import is_korean_show

class Bool_function_test(unittest.TestCase):
    def testbool_func_tvDict_is_Null(self):
        tv_dict = {'origin_country': []}
        self.assertFalse(is_korean_show(tv_dict))

    def testbool_func_tvDict_has_origincountry_Korean(self):
           tv_dict = {'origin_country': ['KR']}
           self.assertTrue(is_korean_show(tv_dict))

    def testbool_func_tvDict_has_origincountry_NonKorean(self):
           tv_dict = {'origin_country': ['US']}
           self.assertFalse(is_korean_show(tv_dict))

    def testbool_func_tvDict_has_origincountry_KoreanWithManyContry(self):
           tv_dict = {'origin_country': ['KR','US','UK','IND']}
           self.assertTrue(is_korean_show(tv_dict))