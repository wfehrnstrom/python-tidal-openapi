# ArtistsTrackProvidersMultiRelationshipDataDocument

Target resource types: `providers`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ArtistsTrackProvidersResourceIdentifier]**](ArtistsTrackProvidersResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artists_track_providers_multi_relationship_data_document import ArtistsTrackProvidersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsTrackProvidersMultiRelationshipDataDocument from a JSON string
artists_track_providers_multi_relationship_data_document_instance = ArtistsTrackProvidersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistsTrackProvidersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artists_track_providers_multi_relationship_data_document_dict = artists_track_providers_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtistsTrackProvidersMultiRelationshipDataDocument from a dict
artists_track_providers_multi_relationship_data_document_from_dict = ArtistsTrackProvidersMultiRelationshipDataDocument.from_dict(artists_track_providers_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


