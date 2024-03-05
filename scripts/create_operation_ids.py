import yaml
import instructor

from rich.progress import track
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Dict
from typing import Optional
import argparse


class Method(BaseModel):
    operation_id: str = Field(description="The operation id of the endpoint")

    summary: str = Field(
        description="A brief description of the endpoint functionality. Maximum 8 words."
    )


class Endpoint(BaseModel):
    url: str = Field(description="The url of the endpoint")

    get: Optional[Method] = Field(
        default=None, description="The get method of the endpoint"
    )

    post: Optional[Method] = Field(
        default=None, description="The post method of the endpoint"
    )

    put: Optional[Method] = Field(
        default=None, description="The put method of the endpoint"
    )

    delete: Optional[Method] = Field(
        default=None, description="The delete method of the endpoint"
    )


def document_endpoint(
    endpoint: Dict,
    client: OpenAI,
) -> Endpoint:
    """
    Document the endpoint by creating operation IDs and summaries.

    Args:
        endpoint (Dict): The endpoint to be documented.
        client (OpenAI): The OpenAI client used for generating documentation.

    Returns:
        Endpoint: The documented endpoint.

    """
    prompt = f"""
        Create operation IDs (short, unique, and descriptive) and short summaries for the following endpoints: \n\n {yaml.dump(endpoint).strip()}
    """.strip()

    return client.chat.completions.create(
        model="gpt-4",
        response_model=Endpoint,
        messages=[
            {
                "role": "system",
                "content": "You are proficient in understanding the Dataverse Project originated from Harvard University. You are also proficient in understanding the OpenAPI Specification. You are tasked with creating operation IDs and summaries for the following endpoints:",
            },
            {"role": "user", "content": prompt},
        ],
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="API key for OpenAI client")
    parser.add_argument("--output", help="Output file for the documented endpoints")
    parser.add_argument("--input", help="Input file for the endpoints to be documented")
    args = parser.parse_args()

    key = args.key
    in_file = args.input
    out_file = args.output

    client = instructor.patch(OpenAI(api_key=args.key))

    specs = yaml.safe_load(open(in_file))
    paths = specs["paths"]

    results = []
    for path, detail in track(paths.items()):
        result = document_endpoint(endpoint={path: detail}, client=client)
        results.append(result)

    oas_descriptions = {}

    for result, path in zip(results, paths.keys()):
        oas_descriptions[path] = result.model_dump(exclude_none=True, exclude={"url"})

    with open(out_file, "w") as file:
        yaml.dump(oas_descriptions, file)
