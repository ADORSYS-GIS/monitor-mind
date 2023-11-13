#importing the necessary libraries
import psutil
import os
import time

#define function to run
def memory():
    pid= os.getpid()
    python_process = psutil.Process(pid)
    
    #converting the memery occupied by the runnning process to GB
    mem_info = python_process.memory_info()[0]/2.**30
    print('memory use: {}GB'.format(mem_info))
   
memory()
    
#initialising and infinite loop which runs continuosly to give us 
#a continues count through out
while True:
  def cpu_ussage():
    cpu_threshold = 14
    cpusage = psutil.cpu_percent(interval = 0.5) 
    if cpusage > cpu_threshold:
       print('The cpu ussage is above threshold value:{}%'.format(cpusage))
       
  cpu_ussage()

  def virtual_memory():
    vitual_memory_threshold = 54.7
    usage = (psutil.virtual_memory)
    if float(usage()[2]) > vitual_memory_threshold:
    #selecting the ram used from the all the other statistics
     print("virtual memory(RAM) used: {}%".format(psutil.virtual_memory()[2]))
        
  virtual_memory()
  def frequency_usage():
    frequency_threshold = 343
    frequsage = int(psutil.cpu_freq().current)
    if frequency_threshold <  frequsage:
     print("the processor frequency is above threshold:{}MHz".format(frequsage))

  frequency_usage()
  cpusage = psutil.cpu_percent(interval = 0.5) 
  frequsage = float(psutil.cpu_freq().current)
  usage = (psutil.virtual_memory)
  time.sleep(15)

  continue
         
        
