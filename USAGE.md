<!-- Start SDK Example Usage [usage] -->
```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.access.get_api_v1_access_datafile_bundle_file_id_(file_id='<value>', file_metadata_id=793125, gbrecs=False)

if res.body is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->