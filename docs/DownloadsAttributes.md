# DownloadsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_links** | [**List[DownloadLink]**](DownloadLink.md) |  | [optional] 

## Example

```python
from tidal.models.downloads_attributes import DownloadsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadsAttributes from a JSON string
downloads_attributes_instance = DownloadsAttributes.from_json(json)
# print the JSON string representation of the object
print(DownloadsAttributes.to_json())

# convert the object into a dict
downloads_attributes_dict = downloads_attributes_instance.to_dict()
# create an instance of DownloadsAttributes from a dict
downloads_attributes_from_dict = DownloadsAttributes.from_dict(downloads_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


