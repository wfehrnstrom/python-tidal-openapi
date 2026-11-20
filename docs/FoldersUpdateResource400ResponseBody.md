# FoldersUpdateResource400ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[FoldersDeleteResource400ResponseBodyErrorsInner]**](FoldersDeleteResource400ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.folders_update_resource400_response_body import FoldersUpdateResource400ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersUpdateResource400ResponseBody from a JSON string
folders_update_resource400_response_body_instance = FoldersUpdateResource400ResponseBody.from_json(json)
# print the JSON string representation of the object
print(FoldersUpdateResource400ResponseBody.to_json())

# convert the object into a dict
folders_update_resource400_response_body_dict = folders_update_resource400_response_body_instance.to_dict()
# create an instance of FoldersUpdateResource400ResponseBody from a dict
folders_update_resource400_response_body_from_dict = FoldersUpdateResource400ResponseBody.from_dict(folders_update_resource400_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


