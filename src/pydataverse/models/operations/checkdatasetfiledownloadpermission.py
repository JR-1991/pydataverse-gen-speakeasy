"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class CheckDatasetFileDownloadPermissionRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionId', 'style': 'simple', 'explode': False }})
    include_deaccessioned: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'includeDeaccessioned', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class CheckDatasetFileDownloadPermissionResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

