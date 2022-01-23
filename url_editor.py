import settings

def create_url(user_req_text):
    url = "https://search-maps.yandex.ru/v1/?"
    req_dict = {}
    req_dict['text'] = "text=" + user_req_text
    req_dict['apikey'] = "apikey=" + settings.YANDEX_API_KEY_ORG_SEARCH
    req_dict['type_obj'] = "type=biz"
    req_dict['lang'] = "lang=ru_RU"
    req_dict['results'] = "results=5"
    string = '&'.join(req_dict.values())
    return url + string

