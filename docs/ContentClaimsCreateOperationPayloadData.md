# ContentClaimsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ContentClaimsCreateOperationPayloadDataAttributes**](ContentClaimsCreateOperationPayloadDataAttributes.md) |  | 
**relationships** | [**ContentClaimsCreateOperationPayloadDataRelationships**](ContentClaimsCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.content_claims_create_operation_payload_data import ContentClaimsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of ContentClaimsCreateOperationPayloadData from a JSON string
content_claims_create_operation_payload_data_instance = ContentClaimsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(ContentClaimsCreateOperationPayloadData.to_json())

# convert the object into a dict
content_claims_create_operation_payload_data_dict = content_claims_create_operation_payload_data_instance.to_dict()
# create an instance of ContentClaimsCreateOperationPayloadData from a dict
content_claims_create_operation_payload_data_from_dict = ContentClaimsCreateOperationPayloadData.from_dict(content_claims_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


