# LyricsUpdateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lrc_text** | **str** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from tidal.models.lyrics_update_operation_payload_data_attributes import LyricsUpdateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of LyricsUpdateOperationPayloadDataAttributes from a JSON string
lyrics_update_operation_payload_data_attributes_instance = LyricsUpdateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(LyricsUpdateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
lyrics_update_operation_payload_data_attributes_dict = lyrics_update_operation_payload_data_attributes_instance.to_dict()
# create an instance of LyricsUpdateOperationPayloadDataAttributes from a dict
lyrics_update_operation_payload_data_attributes_from_dict = LyricsUpdateOperationPayloadDataAttributes.from_dict(lyrics_update_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


