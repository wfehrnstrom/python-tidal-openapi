# FolderItemsCreateResource400ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[FolderItemsCreateResource400ResponseBodyErrorsInner]**](FolderItemsCreateResource400ResponseBodyErrorsInner.md) |  | 

## Example

```python
from tidal.models.folder_items_create_resource400_response_body import FolderItemsCreateResource400ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of FolderItemsCreateResource400ResponseBody from a JSON string
folder_items_create_resource400_response_body_instance = FolderItemsCreateResource400ResponseBody.from_json(json)
# print the JSON string representation of the object
print(FolderItemsCreateResource400ResponseBody.to_json())

# convert the object into a dict
folder_items_create_resource400_response_body_dict = folder_items_create_resource400_response_body_instance.to_dict()
# create an instance of FolderItemsCreateResource400ResponseBody from a dict
folder_items_create_resource400_response_body_from_dict = FolderItemsCreateResource400ResponseBody.from_dict(folder_items_create_resource400_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


