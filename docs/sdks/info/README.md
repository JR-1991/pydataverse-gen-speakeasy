# Info
(*info*)

### Available Operations

* [get_api_terms_of_use_info](#get_api_terms_of_use_info) - Retrieve the terms of use of the API
* [get_dataset_metrics_1](#get_dataset_metrics_1) - Retrieve dataset metrics based on the data location and parent alias
* [get_datasets_by_subject](#get_datasets_by_subject) - Retrieve datasets by subject according to specified data location and parent alias
* [get_monthly_subject_metrics](#get_monthly_subject_metrics) - Retrieve monthly metrics for datasets by subject
* [get_monthly_dataset_metrics](#get_monthly_dataset_metrics) - Retrieve monthly metrics of datasets based on data location and parent alias.
* [get_past_days_metrics](#get_past_days_metrics) - Retrieve metrics of datasets from past specified days
* [get_monthly_dataset_metrics_1](#get_monthly_dataset_metrics_1) - Retrieve dataset metrics for a specific month
* [get_metrics_dataverses](#get_metrics_dataverses) - Retrieves metrics of dataverses based on parent alias
* [get_metrics_by_category](#get_metrics_by_category) - Retrieves metrics of dataverses sorted by category
* [get_metrics_by_subject](#get_metrics_by_subject) - Retrieve metrics of dataverses by subject
* [get_monthly_dataverse_metrics](#get_monthly_dataverse_metrics) - Retrieve the monthly metrics of a specific dataverse
* [get_metrics_past_days](#get_metrics_past_days) - Retrieves the number of dataverses created over the past specified number of days
* [get_monthly_metrics_for_dataverses](#get_monthly_metrics_for_dataverses) - Retrieve the metrics for dataverses up to the specified month.
* [get_download_metrics](#get_download_metrics) - Retrieve download metrics based on a parent alias.
* [get_monthly_downloads](#get_monthly_downloads) - Retrieve monthly download metrics
* [get_past_days_downloads](#get_past_days_downloads) - Retrieve download metrics for the past specified number of days
* [get_download_metrics_to_month](#get_download_metrics_to_month) - Retrieve download metrics till a specific month
* [get_file_downloads_metrics](#get_file_downloads_metrics) - Retrieve File Downloads Metrics
* [get_monthly_file_downloads](#get_monthly_file_downloads) - Retrieve the monthly count of file downloads
* [get_file_downloads_to_month](#get_file_downloads_to_month) - Retrieve file download metrics for a specific month
* [get_file_info_metrics](#get_file_info_metrics) - Retrieve metrics information for files
* [get_metrics_by_file_type](#get_metrics_by_file_type) - Retrieve file metrics information categorized by file type
* [get_files_by_type_monthly](#get_files_by_type_monthly) - Retrieve monthly metrics for files by type
* [get_monthly_files_metrics](#get_monthly_files_metrics) - Retrieve monthly metrics for files
* [get_files_metrics](#get_files_metrics) - Retrieve metrics for files from the past specified number of days
* [get_monthly_files_info](#get_monthly_files_info) - Retrieve files metrics information for a specific month
* [get_metric_data](#get_metric_data) - Retrieve specific metric data by country and parentAlias
* [get_monthly_data_count_metrics](#get_monthly_data_count_metrics) - Retrieve the monthly data count metrics identified by the provided metric name
* [get_metrics_by_month](#get_metrics_by_month) - Retrieves data metrics for a specific month
* [get_metrics_tree](#get_metrics_tree) - Fetches the metrics tree based on the provided parent alias
* [get_monthly_metrics_by_alias](#get_monthly_metrics_by_alias) - Retrieve monthly metrics for a specific alias
* [get_unique_downloads](#get_unique_downloads) - Retrieve unique download metrics data for a particular alias
* [get_monthly_unique_downloads](#get_monthly_unique_downloads) - Retrieve monthly unique downloads metrics
* [get_monthly_unique_downloads_1](#get_monthly_unique_downloads_1) - Retrieve the number of unique downloads for a specified month
* [get_unique_file_downloads](#get_unique_file_downloads) - Retrieve the number of unique file downloads
* [get_monthly_unique_file_downloads](#get_monthly_unique_file_downloads) - Retrieve the count of unique file downloads per month
* [get_unique_file_downloads_1](#get_unique_file_downloads_1) - Fetches unique file downloads up to a specific month
* [get_open_api_info](#get_open_api_info) - Retrieve OpenAPI info in specified output format
* [get_server_info](#get_server_info) - Retrieve server information
* [get_dataset_publish_popup_custom_text](#get_dataset_publish_popup_custom_text) - Retrieve the custom text for dataset publish popup.
* [get_max_embargo_duration_in_months](#get_max_embargo_duration_in_months) - Retrieve the maximum duration of embargo in months from the settings
* [get_incomplete_metadata_settings](#get_incomplete_metadata_settings) - Retrieves the status of incomplete metadata settings
* [get_version_info](#get_version_info) - Retrieve the current version information
* [get_zip_download_limit](#get_zip_download_limit) - Retrieve the current zip file download limit

## get_api_terms_of_use_info

Retrieve the terms of use of the API

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_api_terms_of_use_info()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetAPITermsOfUseInfoResponse](../../models/operations/getapitermsofuseinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_dataset_metrics_1

Retrieve dataset metrics based on the data location and parent alias

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_dataset_metrics_1(data_location='<value>', parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `data_location`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetDatasetMetrics1Response](../../models/operations/getdatasetmetrics1response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_datasets_by_subject

Retrieve datasets by subject according to specified data location and parent alias

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_datasets_by_subject(data_location='<value>', parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `data_location`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetDatasetsBySubjectResponse](../../models/operations/getdatasetsbysubjectresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monthly_subject_metrics

Retrieve monthly metrics for datasets by subject

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_monthly_subject_metrics(yyyymm='<value>', data_location='<value>', parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `data_location`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMonthlySubjectMetricsResponse](../../models/operations/getmonthlysubjectmetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monthly_dataset_metrics

Retrieve monthly metrics of datasets based on data location and parent alias.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_monthly_dataset_metrics(data_location='<value>', parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `data_location`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMonthlyDatasetMetricsResponse](../../models/operations/getmonthlydatasetmetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_past_days_metrics

Retrieve metrics of datasets from past specified days

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_past_days_metrics(days=970072, data_location='<value>', parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `days`             | *int*              | :heavy_check_mark: | N/A                |
| `data_location`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetPastDaysMetricsResponse](../../models/operations/getpastdaysmetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monthly_dataset_metrics_1

Retrieve dataset metrics for a specific month

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_monthly_dataset_metrics_1(yyyymm='<value>', data_location='<value>', parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `data_location`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMonthlyDatasetMetrics1Response](../../models/operations/getmonthlydatasetmetrics1response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_metrics_dataverses

Retrieves metrics of dataverses based on parent alias

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_metrics_dataverses(parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMetricsDataversesResponse](../../models/operations/getmetricsdataversesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_metrics_by_category

Retrieves metrics of dataverses sorted by category

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_metrics_by_category(parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMetricsByCategoryResponse](../../models/operations/getmetricsbycategoryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_metrics_by_subject

Retrieve metrics of dataverses by subject

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_metrics_by_subject(parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMetricsBySubjectResponse](../../models/operations/getmetricsbysubjectresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monthly_dataverse_metrics

Retrieve the monthly metrics of a specific dataverse

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_monthly_dataverse_metrics(parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMonthlyDataverseMetricsResponse](../../models/operations/getmonthlydataversemetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_metrics_past_days

Retrieves the number of dataverses created over the past specified number of days

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_metrics_past_days(days=651880, parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `days`             | *int*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMetricsPastDaysResponse](../../models/operations/getmetricspastdaysresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monthly_metrics_for_dataverses

Retrieve the metrics for dataverses up to the specified month.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_monthly_metrics_for_dataverses(yyyymm='<value>', parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMonthlyMetricsForDataversesResponse](../../models/operations/getmonthlymetricsfordataversesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_download_metrics

Retrieve download metrics based on a parent alias.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_download_metrics(parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetDownloadMetricsResponse](../../models/operations/getdownloadmetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monthly_downloads

Retrieve monthly download metrics

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_monthly_downloads(parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMonthlyDownloadsResponse](../../models/operations/getmonthlydownloadsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_past_days_downloads

Retrieve download metrics for the past specified number of days

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_past_days_downloads(days=336932, parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `days`             | *int*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetPastDaysDownloadsResponse](../../models/operations/getpastdaysdownloadsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_download_metrics_to_month

Retrieve download metrics till a specific month

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_download_metrics_to_month(yyyymm='<value>', parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetDownloadMetricsToMonthResponse](../../models/operations/getdownloadmetricstomonthresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_file_downloads_metrics

Retrieve File Downloads Metrics

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_file_downloads_metrics(parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetFileDownloadsMetricsResponse](../../models/operations/getfiledownloadsmetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monthly_file_downloads

Retrieve the monthly count of file downloads

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_monthly_file_downloads(parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMonthlyFileDownloadsResponse](../../models/operations/getmonthlyfiledownloadsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_file_downloads_to_month

Retrieve file download metrics for a specific month

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_file_downloads_to_month(yyyymm='<value>', parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetFileDownloadsToMonthResponse](../../models/operations/getfiledownloadstomonthresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_file_info_metrics

Retrieve metrics information for files

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_file_info_metrics(parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetFileInfoMetricsResponse](../../models/operations/getfileinfometricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_metrics_by_file_type

Retrieve file metrics information categorized by file type

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_metrics_by_file_type(parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMetricsByFileTypeResponse](../../models/operations/getmetricsbyfiletyperesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_files_by_type_monthly

Retrieve monthly metrics for files by type

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_files_by_type_monthly(parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetFilesByTypeMonthlyResponse](../../models/operations/getfilesbytypemonthlyresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monthly_files_metrics

Retrieve monthly metrics for files

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_monthly_files_metrics(parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMonthlyFilesMetricsResponse](../../models/operations/getmonthlyfilesmetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_files_metrics

Retrieve metrics for files from the past specified number of days

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_files_metrics(days=694967, parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `days`             | *int*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetFilesMetricsResponse](../../models/operations/getfilesmetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monthly_files_info

Retrieve files metrics information for a specific month

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_monthly_files_info(yyyymm='<value>', parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMonthlyFilesInfoResponse](../../models/operations/getmonthlyfilesinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_metric_data

Retrieve specific metric data by country and parentAlias

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_metric_data(metric='<value>', country='<value>', parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `metric`           | *str*              | :heavy_check_mark: | N/A                |
| `country`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMetricDataResponse](../../models/operations/getmetricdataresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monthly_data_count_metrics

Retrieve the monthly data count metrics identified by the provided metric name

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_monthly_data_count_metrics(metric='<value>', country='<value>', parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `metric`           | *str*              | :heavy_check_mark: | N/A                |
| `country`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMonthlyDataCountMetricsResponse](../../models/operations/getmonthlydatacountmetricsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_metrics_by_month

Retrieves data metrics for a specific month

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_metrics_by_month(metric='<value>', yyyymm='<value>', country='<value>', parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `metric`           | *str*              | :heavy_check_mark: | N/A                |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `country`          | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMetricsByMonthResponse](../../models/operations/getmetricsbymonthresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_metrics_tree

Fetches the metrics tree based on the provided parent alias

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_metrics_tree(parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMetricsTreeResponse](../../models/operations/getmetricstreeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monthly_metrics_by_alias

Retrieve monthly metrics for a specific alias

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_monthly_metrics_by_alias(yyyymm='<value>', parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMonthlyMetricsByAliasResponse](../../models/operations/getmonthlymetricsbyaliasresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_unique_downloads

Retrieve unique download metrics data for a particular alias

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_unique_downloads(parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetUniqueDownloadsResponse](../../models/operations/getuniquedownloadsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monthly_unique_downloads

Retrieve monthly unique downloads metrics

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_monthly_unique_downloads(parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMonthlyUniqueDownloadsResponse](../../models/operations/getmonthlyuniquedownloadsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monthly_unique_downloads_1

Retrieve the number of unique downloads for a specified month

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_monthly_unique_downloads_1(yyyymm='<value>', parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMonthlyUniqueDownloads1Response](../../models/operations/getmonthlyuniquedownloads1response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_unique_file_downloads

Retrieve the number of unique file downloads

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_unique_file_downloads(parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetUniqueFileDownloadsResponse](../../models/operations/getuniquefiledownloadsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_monthly_unique_file_downloads

Retrieve the count of unique file downloads per month

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_monthly_unique_file_downloads(parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetMonthlyUniqueFileDownloadsResponse](../../models/operations/getmonthlyuniquefiledownloadsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_unique_file_downloads_1

Fetches unique file downloads up to a specific month

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_unique_file_downloads_1(yyyymm='<value>', parent_alias='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `yyyymm`           | *str*              | :heavy_check_mark: | N/A                |
| `parent_alias`     | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[operations.GetUniqueFileDownloads1Response](../../models/operations/getuniquefiledownloads1response.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_open_api_info

Retrieve OpenAPI info in specified output format

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_open_api_info(output_format='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `output_format`    | *str*              | :heavy_check_mark: | N/A                |


### Response

**[operations.GetOpenAPIInfoResponse](../../models/operations/getopenapiinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_server_info

Retrieve server information

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_server_info()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetServerInfoResponse](../../models/operations/getserverinforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_dataset_publish_popup_custom_text

Retrieve the custom text for dataset publish popup.

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_dataset_publish_popup_custom_text()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetDatasetPublishPopupCustomTextResponse](../../models/operations/getdatasetpublishpopupcustomtextresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_max_embargo_duration_in_months

Retrieve the maximum duration of embargo in months from the settings

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_max_embargo_duration_in_months()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetMaxEmbargoDurationInMonthsResponse](../../models/operations/getmaxembargodurationinmonthsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_incomplete_metadata_settings

Retrieves the status of incomplete metadata settings

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_incomplete_metadata_settings()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetIncompleteMetadataSettingsResponse](../../models/operations/getincompletemetadatasettingsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_version_info

Retrieve the current version information

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_version_info()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetVersionInfoResponse](../../models/operations/getversioninforesponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_zip_download_limit

Retrieve the current zip file download limit

### Example Usage

```python
import pydataverse

s = pydataverse.PyDataverse(
    api_key_auth="<YOUR_API_KEY_HERE>",
)


res = s.info.get_zip_download_limit()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.GetZipDownloadLimitResponse](../../models/operations/getzipdownloadlimitresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
