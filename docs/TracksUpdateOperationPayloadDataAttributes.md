# TracksUpdateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | **str** | Access type | [optional] 
**bpm** | **float** |  | [optional] 
**explicit** | **bool** | Explicit content | [optional] 
**isrc** | **str** | An ISRC the rights holder already owns: the 12 characters ISO 3901 defines, without the hyphens of the display form. An ISRC set here can be replaced until the track is first sold, and null resets it to the default value. An empty string is also accepted as a reset for now, for compatibility. After the first sale both are rejected. The ISRC TIDAL assigns at the track&#39;s first sale is permanent. Omit the field to leave the ISRC unchanged. Only the track&#39;s owners can set it. | [optional] 
**key** | **str** |  | [optional] 
**key_scale** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**tone_tags** | **List[str]** |  | [optional] 

## Example

```python
from tidal.models.tracks_update_operation_payload_data_attributes import TracksUpdateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TracksUpdateOperationPayloadDataAttributes from a JSON string
tracks_update_operation_payload_data_attributes_instance = TracksUpdateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(TracksUpdateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
tracks_update_operation_payload_data_attributes_dict = tracks_update_operation_payload_data_attributes_instance.to_dict()
# create an instance of TracksUpdateOperationPayloadDataAttributes from a dict
tracks_update_operation_payload_data_attributes_from_dict = TracksUpdateOperationPayloadDataAttributes.from_dict(tracks_update_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


