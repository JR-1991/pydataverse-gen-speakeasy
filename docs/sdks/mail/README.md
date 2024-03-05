# Mail
(*mail*)

### Available Operations

* [get_api_v1_mail_notifications](#get_api_v1_mail_notifications)

## get_api_v1_mail_notifications

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.mail.get_api_v1_mail_notifications()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1MailNotificationsResponse](../../models/operations/getapiv1mailnotificationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
