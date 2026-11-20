# FoldersAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_root** | **bool** | Whether this is the root folder. | 
**name** | **str** |  | 

## Example

```python
from tidal.models.folders_attributes import FoldersAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersAttributes from a JSON string
folders_attributes_instance = FoldersAttributes.from_json(json)
# print the JSON string representation of the object
print(FoldersAttributes.to_json())

# convert the object into a dict
folders_attributes_dict = folders_attributes_instance.to_dict()
# create an instance of FoldersAttributes from a dict
folders_attributes_from_dict = FoldersAttributes.from_dict(folders_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


