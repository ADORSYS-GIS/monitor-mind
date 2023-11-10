  ** Network Interface Monitoring and Listing with Python **
  This project demonstrates how to list and monitor network interfaces using Python. It utilizes the psutil library to retrieve network interface data.

  * Prerequisites 
   Make sure you have the following installed:

   -Python (version 3.6 or higher)
   -psutil library (can be installed using pip install psutil)
   -Listing Network Interfaces.

  ** Listing Network Interface **
  To list network interfaces in Python, follow these steps:

1) Import the psutil module in your Python script:

   import psutil

2) Use the net_if_stats() function from psutil to retrieve network interface statistics:

   # To list all network interface 
   network_interfaces = psutil.net_if_stats()
   interface_names = network_interfaces.keys()

   for interface_name in interface_names:
        print(interface_name)

   This code will print the names of all network interfaces available on your system.

  ** Monitoring Network Interfaces **
  To monitor network interfaces in Python, follow these steps:

1) Import the psutil module in your Python script:

   import psutil

2) Choose the network interface you want to monitor and assign its name to the interface_name variable:

   interface_name = "eth0"  # Replace with the name of the desired interface.

3) Use the net_io_counters() function from psutil to continuously monitor the bytes sent and received on the specified network interface:

   while True:
         network_stats = psutil.net_io_counters(pernic=True)
         if interface_name in network_stats:
             interface_stats = network_stats[interface_name]
             print(f"Bytes Sent: {interface_stats.bytes_sent}")
             print(f"Bytes Received: {interface_stats.bytes_recv}")
         else:
            print("Interface not found")
  This code will continuously display the bytes sent and received on the specified network interface.

  Remember to replace "eth0" with the actual name of the interface you want to monitor.

  ** Conclusion **
  -By following the steps outlined above, you can easily list and monitor network interfaces using Python and the psutil library.

  -Feel free to customize and integrate this functionality into your own projects or applications
