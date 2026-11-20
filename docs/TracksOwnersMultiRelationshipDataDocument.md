# TracksOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.tracks_owners_multi_relationship_data_document import TracksOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TracksOwnersMultiRelationshipDataDocument from a JSON string
tracks_owners_multi_relationship_data_document_instance = TracksOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(TracksOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
tracks_owners_multi_relationship_data_document_dict = tracks_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of TracksOwnersMultiRelationshipDataDocument from a dict
tracks_owners_multi_relationship_data_document_from_dict = TracksOwnersMultiRelationshipDataDocument.from_dict(tracks_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


