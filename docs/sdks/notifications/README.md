# Notifications
(*notifications*)

## Overview

### Available Operations

* [get_all_notifications](#get_all_notifications) - Retrieve all notifications
* [get_muted_emails](#get_muted_emails) - Retrieve a list of muted email notifications
* [update_muted_email_notification](#update_muted_email_notification) - Updates a muted email notification by type name
* [delete_muted_email_notification](#delete_muted_email_notification) - Deletes a muted email notification by type name
* [get_muted_notifications](#get_muted_notifications) - Retrieve all muted notifications
* [update_muted_notification](#update_muted_notification) - Update details of a specific muted notification
* [delete_muted_notification](#delete_muted_notification) - Delete a specific muted notification
* [delete_notification](#delete_notification) - Delete a notification by ID

## get_all_notifications

Retrieve all notifications

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.notifications.get_all_notifications()

if res is not None:
    # handle response
    pass

```

### Response

**[operations.GetAllNotificationsResponse](../../models/operations/getallnotificationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_muted_emails

Retrieve a list of muted email notifications

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.notifications.get_muted_emails()

if res is not None:
    # handle response
    pass

```

### Response

**[operations.GetMutedEmailsResponse](../../models/operations/getmutedemailsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_muted_email_notification

Updates a muted email notification by type name

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.notifications.update_muted_email_notification(type_name='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `type_name`        | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.UpdateMutedEmailNotificationResponse](../../models/operations/updatemutedemailnotificationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_muted_email_notification

Deletes a muted email notification by type name

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.notifications.delete_muted_email_notification(type_name='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `type_name`        | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteMutedEmailNotificationResponse](../../models/operations/deletemutedemailnotificationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_muted_notifications

Retrieve all muted notifications

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.notifications.get_muted_notifications()

if res is not None:
    # handle response
    pass

```

### Response

**[operations.GetMutedNotificationsResponse](../../models/operations/getmutednotificationsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_muted_notification

Update details of a specific muted notification

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.notifications.update_muted_notification(type_name='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `type_name`        | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.UpdateMutedNotificationResponse](../../models/operations/updatemutednotificationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_muted_notification

Delete a specific muted notification

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.notifications.delete_muted_notification(type_name='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `type_name`        | *str*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteMutedNotificationResponse](../../models/operations/deletemutednotificationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_notification

Delete a notification by ID

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth='<YOUR_API_KEY_HERE>',
)


res = s.notifications.delete_notification(id=927889)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |

### Response

**[operations.DeleteNotificationResponse](../../models/operations/deletenotificationresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |