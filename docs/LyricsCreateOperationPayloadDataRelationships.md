# LyricsCreateOperationPayloadDataRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**track** | [**LyricsCreateOperationPayloadDataRelationshipsTrack**](LyricsCreateOperationPayloadDataRelationshipsTrack.md) |  | 

## Example

```python
from tidal.models.lyrics_create_operation_payload_data_relationships import LyricsCreateOperationPayloadDataRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of LyricsCreateOperationPayloadDataRelationships from a JSON string
lyrics_create_operation_payload_data_relationships_instance = LyricsCreateOperationPayloadDataRelationships.from_json(json)
# print the JSON string representation of the object
print(LyricsCreateOperationPayloadDataRelationships.to_json())

# convert the object into a dict
lyrics_create_operation_payload_data_relationships_dict = lyrics_create_operation_payload_data_relationships_instance.to_dict()
# create an instance of LyricsCreateOperationPayloadDataRelationships from a dict
lyrics_create_operation_payload_data_relationships_from_dict = LyricsCreateOperationPayloadDataRelationships.from_dict(lyrics_create_operation_payload_data_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


