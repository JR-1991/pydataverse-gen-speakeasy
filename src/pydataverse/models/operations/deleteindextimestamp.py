"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http


@dataclasses.dataclass
class DeleteIndexTimestampRequest:
    dv_object_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'dvObjectId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class DeleteIndexTimestampResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

