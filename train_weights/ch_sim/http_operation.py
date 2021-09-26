import json
from random import randint

import requests

from ch_sim.config import DATAHOSTNAME

def post_env_data(env_id, timestamp, temperature, humidity, co2density):
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "1b838371-cbee-22a2-e67c-eee4ac508a9f"
    }

    querystring = {"code":"ZloTdKVMQQhumzBefI5UKaeLrnhIIPe5x2vtw5yfa2aUXCgeXGVCaA=="}

    payload_env = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"factory_id\"\r\n\r\n%d\r\n" % 1
    payload_env += "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"env_id\"\r\n\r\n%d\r\n" % env_id
    payload_env += "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"time\"\r\n\r\n%s\r\n" % timestamp
    payload_env += "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"temperature\"\r\n\r\n%.1f\r\n" % temperature
    payload_env += "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"humidity\"\r\n\r\n%d\r\n" % humidity
    payload_env += "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"co2\"\r\n\r\n%d\r\n" % co2density
    payload_env += "------WebKitFormBoundary7MA4YWxkTrZu0gW--"

    result = requests.post("%s/api/SetENVData" % DATAHOSTNAME, headers=headers, data=payload_env, params=querystring)
    print("[%d] Time: %s ->" % (env_id, timestamp), result)


def get_env_data(env_id, time_info):
    result = requests.get("%s/api/GetENVData?env_id=%d&time=%s" % (DATAHOSTNAME, env_id, time_info))
    if result.status_code != 200:
        print("HTTP Error[%d]: %s" % (result.status_code, result.text))

    data = json.loads(result.text)
    return data

def get_ac_data(ac_id, time_info):
    result = requests.get("%s/api/GetACData?air_id=%d&time=%s" % (DATAHOSTNAME, ac_id, time_info))
    if result.status_code != 200:
        print("HTTP Error[%d]: %s" % (result.status_code, result.text))

    print(result)
    print(result.text)
    data = json.loads(result.text)
    return data

def get_ac_weight(ac_id, env_id):
    result = requests.get("%s/api/GetWeights?factory_id=1&air_id=%d&env_id=%d" % (DATAHOSTNAME, ac_id, env_id))

    print(result)
    print(result.text)
    data = json.loads(result.text)
    return data


if __name__ == "__main__":

    # print(get_ac_data(1,"2021/01/27_03:15:00"))
    '''for i in range(4):
        print("AC: %d, ENV: %d" % (i + 1, 1))
        get_ac_weight(i + 1, 1)
        print("--------------------------------")'''
    
    post_env_data(1, "2020/01/01_00:00:00", 36.0, 46, 450)
    post_env_data(2, "2020/01/01_00:00:00", 35.7, 50, 422)
    post_env_data(3, "2020/01/01_00:00:00", 36.5, 53, 489)
    post_env_data(4, "2020/01/01_00:00:00", 36.1, 49, 461)
    post_env_data(5, "2020/01/01_00:00:00", 36.2, 47, 457)
    post_env_data(6, "2020/01/01_00:00:00", 35.4, 54, 430)
    post_env_data(7, "2020/01/01_00:00:00", 36.3, 48, 427)
    post_env_data(8, "2020/01/01_00:00:00", 35.9, 55, 476)
    post_env_data(9, "2020/01/01_00:00:00", 35.6, 51, 446)
