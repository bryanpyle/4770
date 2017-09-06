"""An example of constructing a profile with two VMs connected by a LAN.

Instructions:
Wait for the profile instance to start, and then log in to either VM via the
ssh ports specified below.
"""

import geni.portal as portal
import geni.rspec.pg as rspec

request = portal.context.makeRequestRSpec()

# Create two XenVM nodes.
node1 = request.XenVM("node1")
node2 = request.XenVM("node2")

# Request public IP address
node1.routable_control_ip = True
node2.routable_control_ip = True

# Create interfaces for each node
iface1 = node1.addInterface("if1")
iface2 = node2.addInterface("if2")

# Create a link with the type of LAN.
link = request.LAN("lan")

# Add both node interfaces to the link.
link.addInterface(iface1)
link.addInterface(iface2)

portal.context.printRequestRSpec()
