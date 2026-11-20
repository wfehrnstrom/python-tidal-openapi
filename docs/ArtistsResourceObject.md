# ArtistsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ArtistsAttributes**](ArtistsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ArtistsRelationships**](ArtistsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artists_resource_object import ArtistsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsResourceObject from a JSON string
artists_resource_object_instance = ArtistsResourceObject.from_json(json)
# print the JSON string representation of the object
print(ArtistsResourceObject.to_json())

# convert the object into a dict
artists_resource_object_dict = artists_resource_object_instance.to_dict()
# create an instance of ArtistsResourceObject from a dict
artists_resource_object_from_dict = ArtistsResourceObject.from_dict(artists_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


