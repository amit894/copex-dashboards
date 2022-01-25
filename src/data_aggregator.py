import math

class DataAggregator():
    def __init__(self):
        pass

    @staticmethod
    def sum(num_array):
        total_sum=0
        for num in num_array:
            total_sum+=num
        return total_sum
