# DownloadsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**DownloadsAttributes**](DownloadsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**DownloadsRelationships**](DownloadsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.downloads_resource_object import DownloadsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadsResourceObject from a JSON string
downloads_resource_object_instance = DownloadsResourceObject.from_json(json)
# print the JSON string representation of the object
print(DownloadsResourceObject.to_json())

# convert the object into a dict
downloads_resource_object_dict = downloads_resource_object_instance.to_dict()
# create an instance of DownloadsResourceObject from a dict
downloads_resource_object_from_dict = DownloadsResourceObject.from_dict(downloads_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


