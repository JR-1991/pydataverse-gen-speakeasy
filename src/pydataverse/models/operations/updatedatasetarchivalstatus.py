"""Code generated by Speakeasy (https://speakeasyapi.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class UpdateDatasetArchivalStatusRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    version: str = dataclasses.field(metadata={'path_param': { 'field_name': 'version', 'style': 'simple', 'explode': False }})
    request_body: Optional[str] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class UpdateDatasetArchivalStatusResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

