# ArtistsFollowingResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**ArtistsFollowingResourceIdentifierMeta**](ArtistsFollowingResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artists_following_resource_identifier import ArtistsFollowingResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsFollowingResourceIdentifier from a JSON string
artists_following_resource_identifier_instance = ArtistsFollowingResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(ArtistsFollowingResourceIdentifier.to_json())

# convert the object into a dict
artists_following_resource_identifier_dict = artists_following_resource_identifier_instance.to_dict()
# create an instance of ArtistsFollowingResourceIdentifier from a dict
artists_following_resource_identifier_from_dict = ArtistsFollowingResourceIdentifier.from_dict(artists_following_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


