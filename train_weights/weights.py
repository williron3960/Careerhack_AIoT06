from tensorflow import keras
import numpy as np
import requests
import datetime
import time
import copy
import json
import joblib
from random import uniform
from optimal_algorithm.optimal import optimal_algo
from ch_sim.http_operation import get_env_data, post_env_data


def get_env(env_id, time):
    import requests
    url = "https://aiot-task-api.azurewebsites.net/api/GetENVData"
    querystring = {"env_id":str(env_id),"time":str(time)}
    headers = {
        'cache-control': "no-cache",
        'postman-token': "c78a3c1c-b990-3c7f-0cc0-e2f4901c5a9b"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    return response.status_code, json.loads(response.text)


def get_test_data(distance, env_time):

    ### get weight parameter ###
    # only the first one needs to get db
    test_data = [[distance[0][0]]]
    start = time.time()
    for env_id in range(1, 10):
        status, result = get_env(env_id, env_time)
        if status != 200:
            return 
        test_data[0].append(result['temperature'])
        test_data[0].append(result['humidity'])
        test_data[0].append(result['co2'])
    end = time.time()
    print('time = {:.4f}'.format(end-start))
    
    for ac in range(4):
        for env in range(9):
            if not ac == env == 0:
                temp = copy.deepcopy(test_data[0])
                temp[0] = distance[ac][env]
                test_data.append(temp)
    
    return test_data


def get_weights(test):
    
    ### load model ###
    model = keras.models.load_model('./model/TCN-std')

    ### testing data, dim : (1, 28, 1) ###
    test = np.array(test).reshape(1, len(test), 1)
    result = model.predict(test)
    
    return result[0]


def post_weight_db(factory_id, env_id, air_id, distance, weight):

    url = "https://aiot-task-api.azurewebsites.net/api/SetWeights"
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" + \
              "Content-Disposition: form-data;" + \
              "name=\"factory_id\"\r\n\r\n" + str(factory_id) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" + \
              "Content-Disposition: form-data;" + \
              "name=\"env_id\"\r\n\r\n" + str(env_id) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" + \
              "Content-Disposition: form-data;" + \
              "name=\"air_id\"\r\n\r\n" + str(air_id) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" + \
              "Content-Disposition: form-data;" + \
              "name=\"distance\"\r\n\r\n" + str(distance) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" + \
              "Content-Disposition: form-data;" + \
              "name=\"weight\"\r\n\r\n" + str(weight) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "06a774e3-a8a2-564d-492b-25dedcddff58"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


def post_ac_db(factory_id, air_id, time, temperature):

    url = "https://aiot-task-api.azurewebsites.net/api/SetACData"

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" + \
            "Content-Disposition: form-data;" + \
            "name=\"factory_id\"\r\n\r\n" + str(factory_id) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" + \
            "Content-Disposition: form-data;" + \
            "name=\"air_id\"\r\n\r\n" + str(air_id) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" + \
            "Content-Disposition: form-data;" + \
            "name=\"time\"\r\n\r\n" + str(time) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" + \
            "Content-Disposition: form-data;" + \
            "name=\"temperature\"\r\n\r\n" + str(temperature) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "51f673b0-2ee2-369f-6279-da084c5b83e6"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

def post_env_db(factory_id, env_id, time, temperature, humidity, co2):
    url = "https://aiot-task-api.azurewebsites.net/api/SetENVData"
    querystring = {"code":"ZloTdKVMQQhumzBefI5UKaeLrnhIIPe5x2vtw5yfa2aUXCgeXGVCaA=="}
    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" + \
            "Content-Disposition: form-data;" + \
            "name=\"factory_id\"\r\n\r\n" + str(factory_id) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" + \
            "Content-Disposition: form-data;" + \
            "name=\"env_id\"\r\n\r\n" + str(env_id) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" + \
            "Content-Disposition: form-data;" + \
            "name=\"time\"\r\n\r\n" + str(time) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" + \
            "Content-Disposition: form-data;" + \
            "name=\"temperature\"\r\n\r\n" + str(temperature) +"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" + \
            "Content-Disposition: form-data;" + \
            "name=\"humidity\"\r\n\r\n" + str(humidity) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" + \
            "Content-Disposition: form-data;" + \
            "name=\"co2\"\r\n\r\n" + str(co2) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "587c6ae8-faeb-3bc6-e7f5-2652af788640"
    }
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print(response.text)


    
def get_std(env):
    res = list()
    cols = ['distance','AVNET1_T','AVNET1_H','AVNET1_CO2',
            'AVNET2_T','AVNET2_H','AVNET2_CO2',
            'AVNET3_T','AVNET3_H','AVNET3_CO2',
            'AVNET4_T','AVNET4_H','AVNET4_CO2',
            'AVNET5_T','AVNET5_H','AVNET5_CO2',
            'AVNET6_T','AVNET6_H','AVNET6_CO2',
            'AVNET7_T','AVNET7_H','AVNET7_CO2',
            'AVNET8_T','AVNET8_H','AVNET8_CO2',
            'AVNET9_T','AVNET9_H','AVNET9_CO2',
            ]
    path = './std_model/'
    for i in range(28):
        model_name = path + 'scaler.save' + cols[i]
        scaler = joblib.load(model_name)
        res.append(scaler.transform(np.array([env[i]]).reshape(1, -1))[0][0])
        
    
    return res

def get_envT(env):
    T = list()
    for i in range(28):
        if i % 3 == 1:
            T.append(env[i])
    return T
    
### simulation data ###

def listDotProduct(a, b):
    assert(len(a) == len(b))
    return sum(element[0] * element[1] for element in zip(a, b))


def crSimulateNewTemperature(oldTemperature, oldHumidity, oldCO2Density, acTemperature, acWeight, outdoor):
    assert(len(acTemperature) == len(acWeight))
    temp_ac_list = [(x - oldTemperature) for x in acTemperature]
    newTemperature = oldTemperature + (200 - oldHumidity) * listDotProduct(temp_ac_list, acWeight) / 100 + oldCO2Density / 100000 + uniform(0, 0.2) + (outdoor - oldTemperature) * 0.005
    return newTemperature

def crSimulateNewHumidity(oldTemperature, oldHumidity, oldCO2Density):
    newHumidity = oldHumidity + oldCO2Density / 100000 + oldTemperature / 3000 + uniform(-3, 3)
    if newHumidity > 100:
        newHumidity = 100
    return newHumidity

def crSimulateNewCO2Density(oldTemperature, oldHumidity, oldCO2Density, newTemperature):
    newCO2Density = oldCO2Density + (newTemperature - oldTemperature) * 10 + oldHumidity / 100 + uniform(-5, 4)
    return newCO2Density
    
def crGenerateSimulationData(oldTemperature, oldHumidity, oldCO2Density, acTempSet, acWeightSet, outdoor):

    # print("Input (Temp, Humid, CO2) -> (%.2f, %d, %d)" % (oldTemperature, oldHumidity, oldCO2Density))

    newTemp = crSimulateNewTemperature(oldTemperature, oldHumidity, oldCO2Density, acTempSet, acWeightSet,outdoor)
    newHumid = crSimulateNewHumidity(oldTemperature, oldHumidity, oldCO2Density)
    newCO2D = crSimulateNewCO2Density(oldTemperature, oldHumidity, oldCO2Density, newTemp)
    
    # print("New (Temp, Humid, CO2) -> (%.2f, %d, %d)" % (newTemp, newHumid, newCO2D))

    return newTemp, newHumid, newCO2D

def get_wij(weight, index):
    W = list()
    for i in range(len(weight)):
        W.append(weight[i][index]/9)
    return W


if __name__ == '__main__':

  
    distance = [[2,1,2,3,2,3,4,3,4],
                [2,3,4,1,2,3,2,3,4],
                [4,3,4,3,2,3,2,1,2],
                [4,3,2,3,2,1,4,3,2]]


    env_list = list()
    factory_id = 1
    # env_time = '2019/12/31_23:59:00'
    env_time = '2020/01/01_06:29:00'

    end_env_time = '2020/02/01_00:09:00'

    while env_time != end_env_time:

        test_data = get_test_data(distance, env_time) # test_data = [[]*36]
        
        
        ### normalize test_data ###

        std_test_data = list()
        for i in range(36):
            std_test_data.append(get_std(test_data[i]))

        ### calculate weight ###
        weights = list()
        for ac in range(4):
            weights.append( list() )
            air_id = ac + 1
            for env in range(9):
                env_id = env + 1
                weight = get_weights(std_test_data[ac*9 + env])[0]
                weights[ac].append(weight)
                post_weight_db(factory_id, env_id, air_id, distance[ac][env], weight)
                print('ac=', ac, ', env=', env, 'weight=', weight)
            
        ### calculate ac temperature ###
        T = get_envT( test_data[0] )
        algo = optimal_algo(weights, T)
        for i in range(24):
            if datetime.datetime.strptime(env_time, '%Y/%m/%d_%H:%M:%S').hour == i:
                for j in range(9,60,10):
                    if datetime.datetime.strptime(env_time, '%Y/%m/%d_%H:%M:%S').minute == j:
                        if i <= 12:
                            now = i * 6 + (j + 1)//10 - 1
                            algo.outdoor = round((now/72) * 11 + 15)
                        elif i > 12:
                            now = (i - 12 ) * 6 + (j + 1)//10 -1
                            algo.outdoor = round(26 - (now/72) *11)
                        
        print('outdoor:', algo.outdoor)

            # if datetime.datetime.strptime(env_time, '%Y/%m/%d_%H:%M:%S').hour > 18 and datetime.datetime.strptime(env_time, '%Y/%m/%d_%H:%M:%S').hour <6 :
            #     algo.outdoor = 26
            # else: 
            #     algo.outdoor = 15
        AC = algo.optimal()
        for air_id, temperature in enumerate(AC):
            print(air_id, temperature)
            # post_ac_db(factory_id, air_id + 1, datetime.datetime.strptime(env_time, '%Y/%m/%d_%H:%M:%S') +  datetime.timedelta(minutes=1), temperature)

        ### calculate env data (for loop) ###
        temp = env_time
        for times in range(10):
            test_data = get_test_data(distance, temp)
            temp = datetime.datetime.strptime(temp, '%Y/%m/%d_%H:%M:%S') +  datetime.timedelta(minutes=10)
            temp = temp.strftime('%Y/%m/%d_%H:%M:%S')

            for i in range(9):
                index = i * 3 + 1
                W = get_wij(weights, i)
                temperature, humidity, co2 = crGenerateSimulationData(test_data[0][index], test_data[0][index + 1], test_data[0][index + 2], AC ,W, algo.outdoor)
                print('t:',temperature, 'humidity:', humidity,'co2:',co2)
                # post_env_db(factory_id, i + 1, temp , temperature, humidity, co2)

        
        env_time = datetime.datetime.strptime(env_time, '%Y/%m/%d_%H:%M:%S') + datetime.timedelta(minutes=10)
        env_time = env_time.strftime('%Y/%m/%d_%H:%M:%S')
        print('next_time =', env_time)