<!-- Start SDK Example Usage [usage] -->
```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.access.get_datafile_bundle(file_id='<id>')

if res.body is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->