# LyricsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**LyricsCreateOperationPayloadDataAttributes**](LyricsCreateOperationPayloadDataAttributes.md) |  | [optional] 
**relationships** | [**LyricsCreateOperationPayloadDataRelationships**](LyricsCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.lyrics_create_operation_payload_data import LyricsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of LyricsCreateOperationPayloadData from a JSON string
lyrics_create_operation_payload_data_instance = LyricsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(LyricsCreateOperationPayloadData.to_json())

# convert the object into a dict
lyrics_create_operation_payload_data_dict = lyrics_create_operation_payload_data_instance.to_dict()
# create an instance of LyricsCreateOperationPayloadData from a dict
lyrics_create_operation_payload_data_from_dict = LyricsCreateOperationPayloadData.from_dict(lyrics_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


