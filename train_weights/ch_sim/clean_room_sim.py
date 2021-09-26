# Python Interpreter Module ImportError
from random import uniform

# External Module Import

# Project Module Import
from http_operation import get_env_data, post_env_data

def listDotProduct(a, b):
    assert(len(a) == len(b))
    return sum(element[0] * element[1] for element in zip(a, b))


def crSimulateNewTemperature(oldTemperature, oldHumidity, oldCO2Density, acTemperature, acWeight):
    assert(len(acTemperature) == len(acWeight))
    temp_ac_list = [(x - oldTemperature) for x in acTemperature]
    newTemperature = oldTemperature + (200 - oldHumidity) * listDotProduct(temp_ac_list, acWeight) / 100 + oldCO2Density / 100000 + uniform(0, 0.5)
    return newTemperature

def crSimulateNewHumidity(oldTemperature, oldHumidity, oldCO2Density):
    newHumidity = oldHumidity + oldCO2Density / 100000 + oldTemperature / 3000 + uniform(-5, 5)
    if newHumidity > 100:
        newHumidity = 100
    return newHumidity

def crSimulateNewCO2Density(oldTemperature, oldHumidity, oldCO2Density, newTemperature):
    newCO2Density = oldCO2Density + (newTemperature - oldTemperature) * 10 + oldHumidity / 100 + uniform(-5, 4)
    return newCO2Density
    
def crGenerateSimulationData(oldTemperature, oldHumidity, oldCO2Density, acTempSet, acWeightSet):

    # print("Input (Temp, Humid, CO2) -> (%.2f, %d, %d)" % (oldTemperature, oldHumidity, oldCO2Density))

    newTemp = crSimulateNewTemperature(oldTemperature, oldHumidity, oldCO2Density, acTempSet, acWeightSet)
    newHumid = crSimulateNewHumidity(oldTemperature, oldHumidity, oldCO2Density)
    newCO2D = crSimulateNewCO2Density(oldTemperature, oldHumidity, oldCO2Density, newTemp)
    
    # print("New (Temp, Humid, CO2) -> (%.2f, %d, %d)" % (newTemp, newHumid, newCO2D))

    return newTemp, newHumid, newCO2D

if __name__ == "__main__":
    data = crGenerateSimulationData(22.5, 50, 500, [21.0, 23.0, 23.0, 21.0], [0.25, 0.25, 0.25, 0.25])

    print(data)