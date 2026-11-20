# ArtworksResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ArtworksAttributes**](ArtworksAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ArtworksRelationships**](ArtworksRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artworks_resource_object import ArtworksResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ArtworksResourceObject from a JSON string
artworks_resource_object_instance = ArtworksResourceObject.from_json(json)
# print the JSON string representation of the object
print(ArtworksResourceObject.to_json())

# convert the object into a dict
artworks_resource_object_dict = artworks_resource_object_instance.to_dict()
# create an instance of ArtworksResourceObject from a dict
artworks_resource_object_from_dict = ArtworksResourceObject.from_dict(artworks_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


