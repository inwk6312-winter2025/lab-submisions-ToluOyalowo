import subprocess
import textfsm
# Define command to fetch routing table
command = "show ip route"

template_path = "route_template.textfsm"

def get_routing_table(router):
    try:
        # Simulate fetching routing table (replace with actual network command)
        output = subprocess.getoutput(command)
        
        # Parse with TextFSM
        with open(template_path) as f:
            fsm = textfsm.TextFSM(f)
            parsed_data = fsm.ParseText(output)

        # Print parsed routes
        print(f"Routing Table for {router}:")
        for route in parsed_data:
            print(route)
    except Exception as e:
        print(f"Error fetching routing table for {router}: {e}")

# Example: Fetch routes for R1
get_routing_table("R1")

