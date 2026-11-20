# ArtistsFollowersResourceIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Resource id | 
**meta** | [**ArtistsFollowersResourceIdentifierMeta**](ArtistsFollowersResourceIdentifierMeta.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.artists_followers_resource_identifier import ArtistsFollowersResourceIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsFollowersResourceIdentifier from a JSON string
artists_followers_resource_identifier_instance = ArtistsFollowersResourceIdentifier.from_json(json)
# print the JSON string representation of the object
print(ArtistsFollowersResourceIdentifier.to_json())

# convert the object into a dict
artists_followers_resource_identifier_dict = artists_followers_resource_identifier_instance.to_dict()
# create an instance of ArtistsFollowersResourceIdentifier from a dict
artists_followers_resource_identifier_from_dict = ArtistsFollowersResourceIdentifier.from_dict(artists_followers_resource_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


