"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http


@dataclasses.dataclass
class GetAPIV1DataversesIdentifierStorageQuotaRequest:
    identifier: str = dataclasses.field(metadata={'path_param': { 'field_name': 'identifier', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetAPIV1DataversesIdentifierStorageQuotaResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

