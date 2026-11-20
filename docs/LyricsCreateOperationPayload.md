# LyricsCreateOperationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LyricsCreateOperationPayloadData**](LyricsCreateOperationPayloadData.md) |  | 
**meta** | [**LyricsCreateOperationPayloadMeta**](LyricsCreateOperationPayloadMeta.md) |  | [optional] 

## Example

```python
from tidal.models.lyrics_create_operation_payload import LyricsCreateOperationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of LyricsCreateOperationPayload from a JSON string
lyrics_create_operation_payload_instance = LyricsCreateOperationPayload.from_json(json)
# print the JSON string representation of the object
print(LyricsCreateOperationPayload.to_json())

# convert the object into a dict
lyrics_create_operation_payload_dict = lyrics_create_operation_payload_instance.to_dict()
# create an instance of LyricsCreateOperationPayload from a dict
lyrics_create_operation_payload_from_dict = LyricsCreateOperationPayload.from_dict(lyrics_create_operation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


