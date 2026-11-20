# ArtistsFollowersMultiRelationshipDataDocument

Target resource types: `artists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtistsFollowersResourceIdentifier]**](ArtistsFollowersResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artists_followers_multi_relationship_data_document import ArtistsFollowersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsFollowersMultiRelationshipDataDocument from a JSON string
artists_followers_multi_relationship_data_document_instance = ArtistsFollowersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistsFollowersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artists_followers_multi_relationship_data_document_dict = artists_followers_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtistsFollowersMultiRelationshipDataDocument from a dict
artists_followers_multi_relationship_data_document_from_dict = ArtistsFollowersMultiRelationshipDataDocument.from_dict(artists_followers_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


