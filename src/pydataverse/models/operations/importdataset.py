"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class ImportDatasetRequest:
    identifier: str = dataclasses.field(metadata={'path_param': { 'field_name': 'identifier', 'style': 'simple', 'explode': False }})
    pid: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pid', 'style': 'form', 'explode': True }})
    release: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'release', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class ImportDatasetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

