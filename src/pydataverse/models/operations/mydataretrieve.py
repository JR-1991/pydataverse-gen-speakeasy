"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import List, Optional


@dataclasses.dataclass
class MyDataRetrieveRequest:
    dataset_valid: Optional[List[bool]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'dataset_valid', 'style': 'form', 'explode': True }})
    dvobject_types: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'dvobject_types', 'style': 'form', 'explode': True }})
    filter_validities: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter_validities', 'style': 'form', 'explode': True }})
    mydata_search_term: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'mydata_search_term', 'style': 'form', 'explode': True }})
    published_states: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'published_states', 'style': 'form', 'explode': True }})
    role_ids: Optional[List[int]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'role_ids', 'style': 'form', 'explode': True }})
    selected_page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'selected_page', 'style': 'form', 'explode': True }})
    user_identifier: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'userIdentifier', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class MyDataRetrieveResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    string: Optional[str] = dataclasses.field(default=None)
    r"""OK"""
    

