
import os
import yaml

root_directory = '.'


def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def read_all_yaml_files(root_dir):
    yaml_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(('fleet.yaml', 'fleet.yml')):
                yaml_files.append(os.path.join(root, file))
    return yaml_files

def read_yaml_files_recursively(root_dir):
    all_data = {}
    yaml_files = read_all_yaml_files(root_dir)
    for yaml_file in yaml_files:
        data = read_yaml(yaml_file)
        # You can customize how you want to combine the data
        # For example, add each file's data to a list:
        all_data[yaml_file] = data
    return all_data

# This is the main file that will be executed to transform the fleet data to Zarf data
def transfrom_fleet_to_zarf(yaml_data):
    zarf_data = {}
    for file, data in yaml_data.items():
        # Transform the data here
        # For example, if the data is a list of dictionaries, you can transform it like this:
        zarf_data[file] = [{'name': item['name'], 'type': item['type']} for item in data]
    return zarf_data

def writezarf(zarf_data):
    with open('zarf.yaml', 'w') as file:
        yaml.dump(zarf_data, file)


if __name__ == "__main__":
    yaml_data = read_yaml_files_recursively(root_directory)
    zarf_data = transfrom_fleet_to_zarf(yaml_data)
    writezarf(zarf_data)
    print("Zarf data written to file")
    print("Exiting program")
