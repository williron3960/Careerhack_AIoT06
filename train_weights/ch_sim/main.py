import requests
import schedule
import time
from datetime import datetime, timedelta

from clean_room_sim import crGenerateSimulationData
from http_operation import get_env_data, post_env_data, get_ac_data, get_ac_weight

def simulate_gen_and_post(env_no, timestamp):

    timestamp_old = timestamp - timedelta(seconds=60)

    # Get Old Environment Data and Weight
    env_data = get_env_data(env_no, timestamp_old.strftime("%Y/%m/%d_%H:%M:%S"))

    temp = env_data['temperature']
    humid = env_data['humidity']
    co2 = env_data['co2']

    # Get AC Setting Temperature and Weights
    '''acTempList = []
    acWeightList = []
    for i in range(4):
        fetched_ac_temp = get_ac_data(i + 1, timestamp_old)
        acTempList.append(fetched_ac_temp)
        fetched_ac_weights = get_ac_weight(i + 1, env_no)
        acWeightList.append(fetched_ac_weights)'''

    # Simulate Calculation
    acTempList = [21.0, 23.0, 23.0, 21.0]
    acWeightList = [0.25, 0.25, 0.25, 0.25]
    temp_gen, humid_gen, co2_gen = crGenerateSimulationData(temp, humid, co2, acTempList, acWeightList)

    # Post New Environment Data to Cloud
    post_env_data(env_no, timestamp, temp_gen, humid_gen, co2_gen)

if __name__ == "__main__":

    time_now = datetime.now()
    time_ptr = datetime.strptime("2020/01/01_00:02:00", "%Y/%m/%d_%H:%M:%S")

    # while time_ptr < time_now():
    for env_id in range(1, 10):
        simulate_gen_and_post(env_id, time_ptr)
        print("-----------------------------------------------------------------------------")

    time_ptr = time_ptr + timedelta(seconds=60)

    print(time_ptr.strftime("%Y/%m/%d_%H:%M:%S"))


    '''schedule.every().minutes.at(":00").do(simulate_gen_and_post)
    schedule.every().minutes.at(":10").do(simulate_gen_and_post)
    schedule.every().minutes.at(":20").do(simulate_gen_and_post)
    schedule.every().minutes.at(":30").do(simulate_gen_and_post)
    schedule.every().minutes.at(":40").do(simulate_gen_and_post)
    schedule.every().minutes.at(":50").do(simulate_gen_and_post)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nEnvironment Data Simulator has stopped...")'''


'''
env: 1~5 Name: E1~E5
air: 1~4 Name: A1~A4
factory_id: 1
'''
