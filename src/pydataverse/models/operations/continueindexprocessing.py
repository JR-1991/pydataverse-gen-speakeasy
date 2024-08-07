"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from typing import Optional


@dataclasses.dataclass
class ContinueIndexProcessingRequest:
    num_partitions: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'numPartitions', 'style': 'form', 'explode': True }})
    partition_id_to_process: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'partitionIdToProcess', 'style': 'form', 'explode': True }})
    preview_only: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'previewOnly', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class ContinueIndexProcessingResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    

