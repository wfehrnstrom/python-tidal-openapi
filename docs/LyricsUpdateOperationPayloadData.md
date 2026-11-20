# LyricsUpdateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**LyricsUpdateOperationPayloadDataAttributes**](LyricsUpdateOperationPayloadDataAttributes.md) |  | 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.lyrics_update_operation_payload_data import LyricsUpdateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of LyricsUpdateOperationPayloadData from a JSON string
lyrics_update_operation_payload_data_instance = LyricsUpdateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(LyricsUpdateOperationPayloadData.to_json())

# convert the object into a dict
lyrics_update_operation_payload_data_dict = lyrics_update_operation_payload_data_instance.to_dict()
# create an instance of LyricsUpdateOperationPayloadData from a dict
lyrics_update_operation_payload_data_from_dict = LyricsUpdateOperationPayloadData.from_dict(lyrics_update_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


