"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class GetAPIV1FilesIDMetadataFmidToolparamsTidRequest:
    fmid: int = dataclasses.field(metadata={'path_param': { 'field_name': 'fmid', 'style': 'simple', 'explode': False }})
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    tid: int = dataclasses.field(metadata={'path_param': { 'field_name': 'tid', 'style': 'simple', 'explode': False }})
    locale: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'locale', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class GetAPIV1FilesIDMetadataFmidToolparamsTidResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

