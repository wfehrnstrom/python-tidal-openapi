# ArtistsRadioMultiRelationshipDataDocument

Target resource types: `playlists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.artists_radio_multi_relationship_data_document import ArtistsRadioMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsRadioMultiRelationshipDataDocument from a JSON string
artists_radio_multi_relationship_data_document_instance = ArtistsRadioMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(ArtistsRadioMultiRelationshipDataDocument.to_json())

# convert the object into a dict
artists_radio_multi_relationship_data_document_dict = artists_radio_multi_relationship_data_document_instance.to_dict()
# create an instance of ArtistsRadioMultiRelationshipDataDocument from a dict
artists_radio_multi_relationship_data_document_from_dict = ArtistsRadioMultiRelationshipDataDocument.from_dict(artists_radio_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


