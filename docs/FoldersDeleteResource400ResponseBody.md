# FoldersDeleteResource400ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[FoldersDeleteResource400ResponseBodyErrorsInner]**](FoldersDeleteResource400ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.folders_delete_resource400_response_body import FoldersDeleteResource400ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersDeleteResource400ResponseBody from a JSON string
folders_delete_resource400_response_body_instance = FoldersDeleteResource400ResponseBody.from_json(json)
# print the JSON string representation of the object
print(FoldersDeleteResource400ResponseBody.to_json())

# convert the object into a dict
folders_delete_resource400_response_body_dict = folders_delete_resource400_response_body_instance.to_dict()
# create an instance of FoldersDeleteResource400ResponseBody from a dict
folders_delete_resource400_response_body_from_dict = FoldersDeleteResource400ResponseBody.from_dict(folders_delete_resource400_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


