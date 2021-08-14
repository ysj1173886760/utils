import os
import aip
import http.client
import hashlib
import json
import random
import urllib
import re

def baidu_ocr(file):
    app_id = '19890128'
    api_key = 'BqvwEKnyBhHX6QAj0Ezc2KH7'
    secret_key = '2wQh1smTldG9qvKdUKvZe5uXhb6L1o59'
    ocr_text = ''
    if os.path.isfile(file):
        with open(file, 'rb') as f:
            image = f.read()
        ocr_ret = aip.AipOcr(app_id, api_key, secret_key).basicGeneral(image)
        words = ocr_ret.get('words_result')
        print(words)
        if words is not None and len(words):
            for word in words:
                ocr_text += word['words'] + ' '
            return ocr_text
    return None

def baidu_translate(content):
    app_id = '20200515000455294'
    secret_key = 'TH9UQhQX1yMCQzbVsPaa'
    http_client = None
    myurl = '/api/trans/vip/translate'
    q = content
    from_lang = 'en'
    to_lang = 'zh'
    salt = random.randint(32768, 65536)
    sign = app_id + q + str(salt) + secret_key
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + app_id + '&q=' + urllib.parse.quote(q) + \
            '&from=' + from_lang + '&to=' + to_lang + '&salt=' + str(salt) + '&sign=' + sign
    
    try:
        http_client = http.client.HTTPConnection('api.fanyi.baidu.com')
        http_client.request('GET', myurl)
        response = http_client.getresponse()
        json_response = response.read().decode('utf-8')
        js = json.loads(json_response)
        res = ''
        for result in js['trans_result']:
            res += result['dst'] + '\n'
        return res
    except Exception as e:
        print(e)
        return None
    finally:
        if http_client:
            http_client.close()

def paper_format(content):
    """ remove all "- " formatted string """
    content = re.sub('-\s', '', content)
    return content