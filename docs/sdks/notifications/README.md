# Notifications
(*notifications*)

### Available Operations

* [get_api_v1_notifications_all](#get_api_v1_notifications_all)
* [get_api_v1_notifications_muted_emails](#get_api_v1_notifications_muted_emails)
* [put_api_v1_notifications_muted_emails_type_name_](#put_api_v1_notifications_muted_emails_type_name_)
* [delete_api_v1_notifications_muted_emails_type_name_](#delete_api_v1_notifications_muted_emails_type_name_)
* [get_api_v1_notifications_muted_notifications](#get_api_v1_notifications_muted_notifications)
* [put_api_v1_notifications_muted_notifications_type_name_](#put_api_v1_notifications_muted_notifications_type_name_)
* [delete_api_v1_notifications_muted_notifications_type_name_](#delete_api_v1_notifications_muted_notifications_type_name_)
* [delete_api_v1_notifications_id_](#delete_api_v1_notifications_id_)

## get_api_v1_notifications_all

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.notifications.get_api_v1_notifications_all()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1NotificationsAllResponse](../../models/operations/getapiv1notificationsallresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_notifications_muted_emails

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.notifications.get_api_v1_notifications_muted_emails()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1NotificationsMutedEmailsResponse](../../models/operations/getapiv1notificationsmutedemailsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_v1_notifications_muted_emails_type_name_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.notifications.put_api_v1_notifications_muted_emails_type_name_(type_name='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `type_name`        | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PutAPIV1NotificationsMutedEmailsTypeNameResponse](../../models/operations/putapiv1notificationsmutedemailstypenameresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_notifications_muted_emails_type_name_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.notifications.delete_api_v1_notifications_muted_emails_type_name_(type_name='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `type_name`        | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAPIV1NotificationsMutedEmailsTypeNameResponse](../../models/operations/deleteapiv1notificationsmutedemailstypenameresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_api_v1_notifications_muted_notifications

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.notifications.get_api_v1_notifications_muted_notifications()

if res.status_code == 200:
    # handle response
    pass
```


### Response

**[operations.GetAPIV1NotificationsMutedNotificationsResponse](../../models/operations/getapiv1notificationsmutednotificationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_api_v1_notifications_muted_notifications_type_name_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.notifications.put_api_v1_notifications_muted_notifications_type_name_(type_name='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `type_name`        | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.PutAPIV1NotificationsMutedNotificationsTypeNameResponse](../../models/operations/putapiv1notificationsmutednotificationstypenameresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_notifications_muted_notifications_type_name_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.notifications.delete_api_v1_notifications_muted_notifications_type_name_(type_name='<value>')

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `type_name`        | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAPIV1NotificationsMutedNotificationsTypeNameResponse](../../models/operations/deleteapiv1notificationsmutednotificationstypenameresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## delete_api_v1_notifications_id_

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse()


res = s.notifications.delete_api_v1_notifications_id_(id=44071)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `id`               | *int*              | :heavy_check_mark: | N/A                |


### Response

**[operations.DeleteAPIV1NotificationsIDResponse](../../models/operations/deleteapiv1notificationsidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
