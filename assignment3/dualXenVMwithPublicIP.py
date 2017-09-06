"""An example of constructing a profile with two VMs connected bya LAN.

Instructions:
Wait for the profile instance to start, and then log in to either VM via 
ssh ports specified below.
"""

import geni.portal as portal
import geni.rspec.pg as rspec

request = portal.context.makeRequestRSpec()

# Create two XenVM nodes.
node1 = request.XenVM("node1")
node2 = request.XenVM("node2")

# Request public IP addresses
node1.routable_control_ip = True
node2.routable_control_ip = True

portal.context.printRequestRSpec()
