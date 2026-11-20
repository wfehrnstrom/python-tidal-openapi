# FolderItemsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_status** | **str** |  | 
**reference** | **bool** | Whether this item references a subject in another owner&#39;s tree, regardless of its current availability. | 

## Example

```python
from tidal.models.folder_items_attributes import FolderItemsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of FolderItemsAttributes from a JSON string
folder_items_attributes_instance = FolderItemsAttributes.from_json(json)
# print the JSON string representation of the object
print(FolderItemsAttributes.to_json())

# convert the object into a dict
folder_items_attributes_dict = folder_items_attributes_instance.to_dict()
# create an instance of FolderItemsAttributes from a dict
folder_items_attributes_from_dict = FolderItemsAttributes.from_dict(folder_items_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


