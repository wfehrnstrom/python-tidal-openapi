# ArtistsUpdateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_color** | **str** | Background colour override. | [optional] 
**contributions_enabled** | **bool** |  | [optional] 
**contributions_sales_pitch** | **str** |  | [optional] 
**external_links** | [**List[ExternalLinkPayload]**](ExternalLinkPayload.md) |  | [optional] 
**foreground_color** | **str** | Foreground colour override. | [optional] 
**handle** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from tidal.models.artists_update_operation_payload_data_attributes import ArtistsUpdateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsUpdateOperationPayloadDataAttributes from a JSON string
artists_update_operation_payload_data_attributes_instance = ArtistsUpdateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ArtistsUpdateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
artists_update_operation_payload_data_attributes_dict = artists_update_operation_payload_data_attributes_instance.to_dict()
# create an instance of ArtistsUpdateOperationPayloadDataAttributes from a dict
artists_update_operation_payload_data_attributes_from_dict = ArtistsUpdateOperationPayloadDataAttributes.from_dict(artists_update_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


