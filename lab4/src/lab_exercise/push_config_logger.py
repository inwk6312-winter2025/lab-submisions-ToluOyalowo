import yaml
import logging
from jinja2 import Environment, FileSystemLoader

# Configure logging
logging.basicConfig(filename="config_push.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

try:
    # Load network data
    with open("network_info.yml") as file:
        network_data = yaml.safe_load(file)

    # Load Jinja2 template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("config_template.j2")

    for router, data in network_data['routers'].items():
        config = template.render(
            hostname=data["hostname"],
            loopback=data["loopback"],
            interfaces=data["interfaces"]
        )
        with open(f"{router}_config.txt", "w") as f:
            f.write(config)
        logging.info(f"Configuration for {router} generated successfully.")
except Exception as e:
    logging.error(f"Error generating configurations: {e}")

