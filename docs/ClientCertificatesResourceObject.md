# ClientCertificatesResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ClientCertificatesAttributes**](ClientCertificatesAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ClientCertificatesRelationships**](ClientCertificatesRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.client_certificates_resource_object import ClientCertificatesResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCertificatesResourceObject from a JSON string
client_certificates_resource_object_instance = ClientCertificatesResourceObject.from_json(json)
# print the JSON string representation of the object
print(ClientCertificatesResourceObject.to_json())

# convert the object into a dict
client_certificates_resource_object_dict = client_certificates_resource_object_instance.to_dict()
# create an instance of ClientCertificatesResourceObject from a dict
client_certificates_resource_object_from_dict = ClientCertificatesResourceObject.from_dict(client_certificates_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


