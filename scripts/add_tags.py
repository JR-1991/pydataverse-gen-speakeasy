import yaml
from bigtree import list_to_tree, print_tree

if __name__ == "__main__":

    specification = yaml.safe_load(open("dataverse_openapi_raw.yaml"))

    # Turn all paths into a tree
    paths = specification["paths"].keys()
    tree = list_to_tree(paths)

    print_tree(tree)

    # Add third element of path to tags of each method
    # api/v1/(datasets)/...

    for path in specification["paths"]:
        for method in specification["paths"][path]:
            if "tags" not in specification["paths"][path][method]:
                specification["paths"][path][method]["tags"] = []

            category = path.split("/")[3].capitalize()
            specification["paths"][path][method]["tags"].append(category)

    with open("dataverse_openapi.yaml", "w") as file:
        yaml.dump(specification, file, default_flow_style=False, sort_keys=False)
