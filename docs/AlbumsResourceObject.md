# AlbumsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**AlbumsAttributes**](AlbumsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**AlbumsRelationships**](AlbumsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.albums_resource_object import AlbumsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsResourceObject from a JSON string
albums_resource_object_instance = AlbumsResourceObject.from_json(json)
# print the JSON string representation of the object
print(AlbumsResourceObject.to_json())

# convert the object into a dict
albums_resource_object_dict = albums_resource_object_instance.to_dict()
# create an instance of AlbumsResourceObject from a dict
albums_resource_object_from_dict = AlbumsResourceObject.from_dict(albums_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


