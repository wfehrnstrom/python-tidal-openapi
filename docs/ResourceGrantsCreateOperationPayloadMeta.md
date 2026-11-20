# ResourceGrantsCreateOperationPayloadMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password of a password-protected invitation. Ignored for other invitations. | [optional] 

## Example

```python
from tidal.models.resource_grants_create_operation_payload_meta import ResourceGrantsCreateOperationPayloadMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceGrantsCreateOperationPayloadMeta from a JSON string
resource_grants_create_operation_payload_meta_instance = ResourceGrantsCreateOperationPayloadMeta.from_json(json)
# print the JSON string representation of the object
print(ResourceGrantsCreateOperationPayloadMeta.to_json())

# convert the object into a dict
resource_grants_create_operation_payload_meta_dict = resource_grants_create_operation_payload_meta_instance.to_dict()
# create an instance of ResourceGrantsCreateOperationPayloadMeta from a dict
resource_grants_create_operation_payload_meta_from_dict = ResourceGrantsCreateOperationPayloadMeta.from_dict(resource_grants_create_operation_payload_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


