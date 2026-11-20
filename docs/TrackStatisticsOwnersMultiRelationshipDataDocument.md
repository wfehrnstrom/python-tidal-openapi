# TrackStatisticsOwnersMultiRelationshipDataDocument

Target resource types: `users`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceIdentifier]**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.track_statistics_owners_multi_relationship_data_document import TrackStatisticsOwnersMultiRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of TrackStatisticsOwnersMultiRelationshipDataDocument from a JSON string
track_statistics_owners_multi_relationship_data_document_instance = TrackStatisticsOwnersMultiRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(TrackStatisticsOwnersMultiRelationshipDataDocument.to_json())

# convert the object into a dict
track_statistics_owners_multi_relationship_data_document_dict = track_statistics_owners_multi_relationship_data_document_instance.to_dict()
# create an instance of TrackStatisticsOwnersMultiRelationshipDataDocument from a dict
track_statistics_owners_multi_relationship_data_document_from_dict = TrackStatisticsOwnersMultiRelationshipDataDocument.from_dict(track_statistics_owners_multi_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


