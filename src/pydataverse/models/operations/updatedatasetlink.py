"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http


@dataclasses.dataclass
class UpdateDatasetLinkRequest:
    linked_dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'linkedDatasetId', 'style': 'simple', 'explode': False }})
    linking_dataverse_alias: str = dataclasses.field(metadata={'path_param': { 'field_name': 'linkingDataverseAlias', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class UpdateDatasetLinkResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

