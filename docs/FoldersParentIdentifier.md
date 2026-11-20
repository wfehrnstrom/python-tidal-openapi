# FoldersParentIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.folders_parent_identifier import FoldersParentIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of FoldersParentIdentifier from a JSON string
folders_parent_identifier_instance = FoldersParentIdentifier.from_json(json)
# print the JSON string representation of the object
print(FoldersParentIdentifier.to_json())

# convert the object into a dict
folders_parent_identifier_dict = folders_parent_identifier_instance.to_dict()
# create an instance of FoldersParentIdentifier from a dict
folders_parent_identifier_from_dict = FoldersParentIdentifier.from_dict(folders_parent_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


