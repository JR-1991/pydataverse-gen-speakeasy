"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class GetMetricsByMonthRequest:
    metric: str = dataclasses.field(metadata={'path_param': { 'field_name': 'metric', 'style': 'simple', 'explode': False }})
    yyyymm: str = dataclasses.field(metadata={'path_param': { 'field_name': 'yyyymm', 'style': 'simple', 'explode': False }})
    country: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'country', 'style': 'form', 'explode': True }})
    parent_alias: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'parentAlias', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class GetMetricsByMonthResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

