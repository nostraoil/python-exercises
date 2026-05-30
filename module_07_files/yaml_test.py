import yaml

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

print(config)
print()
print(f"Type: {type(config)}")
print()
print(f"Filter basin: {config['job_settings']['basin']}")
print(f"Min pressure: {config['job_settings']['min_pressure_psi']}")
print(f"Company: {config['operator_info']['company']}")
print()
print("Enabled features:")
for feature in config["features_enabled"]:
    print(f"  - {feature}")