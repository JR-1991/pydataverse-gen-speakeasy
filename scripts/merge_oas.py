import yaml
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge OpenAPI Specification files")
    parser.add_argument("--desc", help="Path to the description file")
    parser.add_argument("--spec", help="Path to the spec file")
    parser.add_argument(
        "--out", help="Output file for the merged OpenAPI Specification file"
    )

    args = parser.parse_args()

    description_file = args.desc
    spec_file = args.spec
    output_file = args.out

    specs = yaml.safe_load(open(spec_file))
    descriptions = yaml.safe_load(open(description_file))

    operation_ids = []

    for path in specs["paths"]:
        if path not in descriptions:
            continue

        description = descriptions[path]

        for method in description:
            if method not in specs["paths"][path]:
                continue

            operation_id = description[method]["operation_id"]
            index = 1
            while operation_id in operation_ids:
                operation_id += f"_{index}"
            else:
                operation_ids.append(operation_id)

            # Add operationId and summary to the method
            specs["paths"][path][method]["operationId"] = operation_id
            specs["paths"][path][method]["summary"] = description[method]["summary"]

    with open(output_file, "w") as file:
        yaml.dump(specs, file, default_flow_style=False, sort_keys=False)
