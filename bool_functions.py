def is_korean_show(tv_dict): #filter function for KR shows
    origin_country_list = tv_dict['origin_country']
    if 'KR' in origin_country_list:
        return True
    else:
        return False