"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import List, Optional


@dataclasses.dataclass
class SearchQueryRequest:
    fq: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'fq', 'style': 'form', 'explode': True }})
    geo_point: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'geo_point', 'style': 'form', 'explode': True }})
    geo_radius: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'geo_radius', 'style': 'form', 'explode': True }})
    metadata_fields: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'metadata_fields', 'style': 'form', 'explode': True }})
    order: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'order', 'style': 'form', 'explode': True }})
    per_page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'per_page', 'style': 'form', 'explode': True }})
    q: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'q', 'style': 'form', 'explode': True }})
    query_entities: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query_entities', 'style': 'form', 'explode': True }})
    show_api_urls: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'show_api_urls', 'style': 'form', 'explode': True }})
    show_entity_ids: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'show_entity_ids', 'style': 'form', 'explode': True }})
    show_facets: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'show_facets', 'style': 'form', 'explode': True }})
    show_my_data: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'show_my_data', 'style': 'form', 'explode': True }})
    show_relevance: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'show_relevance', 'style': 'form', 'explode': True }})
    sort: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sort', 'style': 'form', 'explode': True }})
    start: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'start', 'style': 'form', 'explode': True }})
    subtree: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'subtree', 'style': 'form', 'explode': True }})
    type: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'type', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class SearchQueryResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    
