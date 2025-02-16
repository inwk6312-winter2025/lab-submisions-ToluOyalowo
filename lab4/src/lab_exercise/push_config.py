import yaml
from jinja2 import Environment, FileSystemLoader

# Load network data from YAML
with open("network_info.yml") as file:
    network_data = yaml.safe_load(file)

# Load Jinja2 template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("config_template.j2")

# Generate configurations for each router
for router, data in network_data['routers'].items():
    config = template.render(
        hostname=data["hostname"],
        loopback=data["loopback"],
        interfaces=data["interfaces"]
    )
    # Save the config
    with open(f"{router}_config.txt", "w") as f:
        f.write(config)
    print(f"Configuration for {router} generated successfully.")

