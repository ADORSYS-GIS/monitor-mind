import psutil
import time

network_data = None
def get_network_usage():
    """Retrieve network interface information and return usage data."""
    global network_data #Access the global variable
    
    if network_data is None or ('timestamp' in network_data and time.time() - network_data['timestamp'] > 5):
    
        #Get list of netwok interfaces
        interfaces = psutil.net_if_stats().keys()
        
        #Iinitialize an empty list t store network interface infrmation
        network_info = []
 
        #Iterate over each network interface
        for interface in interfaces:

            #Get network interface statistics
            stats = psutil.net_if_stats()[interface]

            #Get i/o counters for the interfaces
            io_counters = psutil.net_io_counters(pernic=True)[interface]
            
            #Create a dictionary to store interface information
            interface_info = {
                'interface': interface,
                'status': 'UP' if stats.isup else 'DOWN',
                'speed': stats.speed,
                'bytes_sent': io_counters.bytes_sent,
                'bytes_received': io_counters.bytes_recv
            }

            #Add interface information to the network_info list
            network_info.append(interface_info)
        
        #Store the network data along the current timestamp
        network_data = {
            'timestamp' : time.time(),
            'info': network_info

        }
        # Extract the required data for return
        network_timestamps = [info['interface'] for info in network_info]
        network_usage = [info['bytes_sent'] + info['bytes_received'] for info in network_info]

        return network_timestamps, network_usage