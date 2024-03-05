"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class AccessDatafileAuxiliaryCreateRequestBody:
    pass


@dataclasses.dataclass
class AccessDatafileAuxiliaryCreateRequest:
    file_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'fileId', 'style': 'simple', 'explode': False }})
    format_tag: str = dataclasses.field(metadata={'path_param': { 'field_name': 'formatTag', 'style': 'simple', 'explode': False }})
    format_version: str = dataclasses.field(metadata={'path_param': { 'field_name': 'formatVersion', 'style': 'simple', 'explode': False }})
    request_body: Optional[AccessDatafileAuxiliaryCreateRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    



@dataclasses.dataclass
class AccessDatafileAuxiliaryCreateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    
