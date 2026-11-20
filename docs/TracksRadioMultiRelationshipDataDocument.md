# TracksRadioMultiRelationshipDataDocument

Target resource types: `playlists`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.tracks_radio_multi_relationship_data_document import TracksRadioMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TracksRadioMultiRelationshipDataDocument from a JSON string
tracks_radio_multi_relationship_data_document_instance = TracksRadioMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(TracksRadioMultiRelationshipDataDocument.to_json())

# convert the object into a dict
tracks_radio_multi_relationship_data_document_dict = tracks_radio_multi_relationship_data_document_instance.to_dict()
# create an instance of TracksRadioMultiRelationshipDataDocument from a dict
tracks_radio_multi_relationship_data_document_from_dict = TracksRadioMultiRelationshipDataDocument.from_dict(tracks_radio_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


