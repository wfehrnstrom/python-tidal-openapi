# DownloadLinkMeta

Metadata for download link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required_headers** | **List[str]** | HTTP headers required when requesting the download URL | [optional] 

## Example

```python
from tidal.models.download_link_meta import DownloadLinkMeta

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadLinkMeta from a JSON string
download_link_meta_instance = DownloadLinkMeta.from_json(json)
# print the JSON string representation of the object
print(DownloadLinkMeta.to_json())

# convert the object into a dict
download_link_meta_dict = download_link_meta_instance.to_dict()
# create an instance of DownloadLinkMeta from a dict
download_link_meta_from_dict = DownloadLinkMeta.from_dict(download_link_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


