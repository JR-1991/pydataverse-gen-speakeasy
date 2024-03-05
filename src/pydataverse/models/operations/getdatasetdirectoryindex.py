"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class GetDatasetDirectoryIndexRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    folder: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'folder', 'style': 'form', 'explode': True }})
    original: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'original', 'style': 'form', 'explode': True }})
    version: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'version', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class GetDatasetDirectoryIndexResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

