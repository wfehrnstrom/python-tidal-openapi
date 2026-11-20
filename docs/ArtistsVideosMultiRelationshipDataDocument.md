# ArtistsVideosMultiRelationshipDataDocument

Target resource types: `videos`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtistsVideosResourceIdentifier]**](ArtistsVideosResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artists_videos_multi_relationship_data_document import ArtistsVideosMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsVideosMultiRelationshipDataDocument from a JSON string
artists_videos_multi_relationship_data_document_instance = ArtistsVideosMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistsVideosMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artists_videos_multi_relationship_data_document_dict = artists_videos_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtistsVideosMultiRelationshipDataDocument from a dict
artists_videos_multi_relationship_data_document_from_dict = ArtistsVideosMultiRelationshipDataDocument.from_dict(artists_videos_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


