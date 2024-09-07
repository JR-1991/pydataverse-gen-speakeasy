# Mail
(*mail*)

## Overview

### Available Operations

* [get_mail_notifications](#get_mail_notifications) - Retrieve a list of mail notifications

## get_mail_notifications

Retrieve a list of mail notifications

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.mail.get_mail_notifications()

if res is not None:
    # handle response
    pass

```

### Response

**[operations.GetMailNotificationsResponse](../../models/operations/getmailnotificationsresponse.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
