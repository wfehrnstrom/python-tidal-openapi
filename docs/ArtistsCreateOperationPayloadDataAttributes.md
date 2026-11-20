# ArtistsCreateOperationPayloadDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handle** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from tidal.models.artists_create_operation_payload_data_attributes import ArtistsCreateOperationPayloadDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistsCreateOperationPayloadDataAttributes from a JSON string
artists_create_operation_payload_data_attributes_instance = ArtistsCreateOperationPayloadDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ArtistsCreateOperationPayloadDataAttributes.to_json())

# convert the object into a dict
artists_create_operation_payload_data_attributes_dict = artists_create_operation_payload_data_attributes_instance.to_dict()
# create an instance of ArtistsCreateOperationPayloadDataAttributes from a dict
artists_create_operation_payload_data_attributes_from_dict = ArtistsCreateOperationPayloadDataAttributes.from_dict(artists_create_operation_payload_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


