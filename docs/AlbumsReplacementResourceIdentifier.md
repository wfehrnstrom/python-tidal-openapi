# AlbumsReplacementResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**AlbumsReplacementResourceIdentifierMeta**](AlbumsReplacementResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.albums_replacement_resource_identifier import AlbumsReplacementResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsReplacementResourceIdentifier from a JSON string
albums_replacement_resource_identifier_instance = AlbumsReplacementResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(AlbumsReplacementResourceIdentifier.to_json())

# convert the object into a dict
albums_replacement_resource_identifier_dict = albums_replacement_resource_identifier_instance.to_dict()
# create an instance of AlbumsReplacementResourceIdentifier from a dict
albums_replacement_resource_identifier_from_dict = AlbumsReplacementResourceIdentifier.from_dict(albums_replacement_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


