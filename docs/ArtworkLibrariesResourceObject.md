# ArtworkLibrariesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ArtworkLibrariesAttributes**](ArtworkLibrariesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ArtworkLibrariesRelationships**](ArtworkLibrariesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artwork_libraries_resource_object import ArtworkLibrariesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworkLibrariesResourceObject from a JSON string
artwork_libraries_resource_object_instance = ArtworkLibrariesResourceObject.from_json(json)
# print the JSON string representation of the object
print(ArtworkLibrariesResourceObject.to_json())

# convert the object into a dict
artwork_libraries_resource_object_dict = artwork_libraries_resource_object_instance.to_dict()
# create an instance of ArtworkLibrariesResourceObject from a dict
artwork_libraries_resource_object_from_dict = ArtworkLibrariesResourceObject.from_dict(artwork_libraries_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


