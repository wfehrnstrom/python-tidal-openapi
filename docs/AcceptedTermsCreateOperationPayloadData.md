# AcceptedTermsCreateOperationPayloadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationships** | [**AcceptedTermsCreateOperationPayloadDataRelationships**](AcceptedTermsCreateOperationPayloadDataRelationships.md) |  | 
**type** | **str** |  | 

## Example

```python
from tidal.models.accepted_terms_create_operation_payload_data import AcceptedTermsCreateOperationPayloadData

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptedTermsCreateOperationPayloadData from a JSON string
accepted_terms_create_operation_payload_data_instance = AcceptedTermsCreateOperationPayloadData.from_json(json)
# print the JSON string representation of the object
print(AcceptedTermsCreateOperationPayloadData.to_json())

# convert the object into a dict
accepted_terms_create_operation_payload_data_dict = accepted_terms_create_operation_payload_data_instance.to_dict()
# create an instance of AcceptedTermsCreateOperationPayloadData from a dict
accepted_terms_create_operation_payload_data_from_dict = AcceptedTermsCreateOperationPayloadData.from_dict(accepted_terms_create_operation_payload_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


