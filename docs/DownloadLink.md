# DownloadLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | URL to download the content from | 
**meta** | [**DownloadLinkMeta**](DownloadLinkMeta.md) |  | 

## Example

```python
from tidal.models.download_link import DownloadLink

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadLink from a JSON string
download_link_instance = DownloadLink.from_json(json)
# print the JSON string representation of the object
print(DownloadLink.to_json())

# convert the object into a dict
download_link_dict = download_link_instance.to_dict()
# create an instance of DownloadLink from a dict
download_link_from_dict = DownloadLink.from_dict(download_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


