# LyricsUpdateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LyricsUpdateOperationPayloadData**](LyricsUpdateOperationPayloadData.md) |  | 

## Example

```python
from tidal.models.lyrics_update_operation_payload import LyricsUpdateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of LyricsUpdateOperationPayload from a JSON string
lyrics_update_operation_payload_instance = LyricsUpdateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(LyricsUpdateOperationPayload.to_json())

# convert the object into a dict
lyrics_update_operation_payload_dict = lyrics_update_operation_payload_instance.to_dict()
# create an instance of LyricsUpdateOperationPayload from a dict
lyrics_update_operation_payload_from_dict = LyricsUpdateOperationPayload.from_dict(lyrics_update_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


