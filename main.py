from distutils import core
from sys import intern
import psutil

# CPU Metrics data
def getCPUMetric():
    data_times = psutil.cpu_times()
    data_core = psutil.cpu_count(logical=False)
    data_percentage = psutil.cpu_percent(interval=1, percpu=True)
    return "CPU times: ", data_times, ", CPU cores: ", data_core, ", CPU percentage: ", data_percentage


# print(getCPUMetric())

# Memory metrics data 
def getMemoryMetrics():
    memory_virtual = psutil.virtual_memory()
    memory_swap = psutil.swap_memory()
    return memory_swap, memory_virtual


x,y = getMemoryMetrics()
print("Memory Swap: {0} and Virtual Memory: {1}".format(x,y))
