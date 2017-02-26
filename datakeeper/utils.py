import yaml

__all__ = ["load_yaml_file", "AttrDict", "RegisteredClass", "RegisteredType"]


def load_yaml_file(path):
    with open(path, "r") as f:
        data = yaml.load(f)
    return data


