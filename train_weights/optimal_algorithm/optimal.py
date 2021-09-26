import pandas as pd 
import numpy as np
import math

class optimal_algo:
    def __init__(self, weight, Env, outdoor = 26, target = 22):
        # input
        self.outdoor = outdoor
        self.target = target

        self.weight = weight
                        
        self.Env = Env
    def determine_cost(self):
        '''
        計算電量cost矩陣
        '''
        cost = list()
        low, high= 4, 32
        for i in range(low, high+1):
            cost.append(list())
            for j in range(low,high+1):
                if i == j:
                    cost[i - 4].append( 2 - 0.01 * abs(22 - i) )
                if i < j:
                    cost[i - 4].append( cost[i - 4][j - 5] + 0.15 )
                if i > j:
                    cost[i - 4].append( cost[j - 4][i - 4] - 0.1 )
                    
        return  cost
    
    def determine_b(self):
        '''
        計算b陣列
        '''
        b = list()
        for i in range(9):
            Ac_val = float()
            for j in range(4):
                Ac_val += self.weight[j][i]
            Ac_val = (Ac_val - 1) * self.Env[i] + 22
            b.append(Ac_val)
        
        return b
    
    def optimal(self):
        '''
        計算least square solution
        '''
        cost = self.determine_cost()

        b = self.determine_b()
        A = np.array(self.weight).transpose()
        x, residuals, rank, s = np.linalg.lstsq(A,b, rcond = -1)
        algo_x = list()
        for i in range( len(x) ):
            up, low = math.floor(x[i]),  math.ceil(x[i])
            algo_x.append([up, low])
        
        probability = dict()
        print(x)
        print(algo_x)

        # 計算最小成本
        for i in range(16):
            res = int()
            location = list()
            bin_str = bin(i)[2:]
            
            lens = 4 - len(bin_str)
            for j in range(lens):
                bin_str = '0' + bin_str
            for j in range(4):
                location.append( int(bin_str[j]) )
                res += cost[self.outdoor - 4][algo_x[j][location[j]] - 4]

            probability[i] = res

        AC_location = int()
        
        # 挑出最小成本

        for name, c in probability.items():
            if c == min( list(probability.values()) ):
                AC_location = int(name)

        temp = bin(AC_location)[2:]
        lens = 4 - len(temp)
        for i in range(lens):
            temp = '0' + temp        

        # 挑出ＡＣ
        AC = list()
        for i in range(4):
            AC.append(
                    algo_x[i][ int(temp[i]) ]
                    )
        return AC
        
        
if __name__ == '__main__':

    obj = optimal_algo()
    AC = obj.optimal()
    print(AC)
    cost = obj.determine_cost()
    res = int()
    for i in range(4):
        res += cost[obj.outdoor - 4][AC[i] - 4] 
    print(res)