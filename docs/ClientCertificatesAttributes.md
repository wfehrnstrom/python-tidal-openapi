# ClientCertificatesAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_expires_at** | **datetime** | Time when the issued certificate expires | [optional] 
**certificate_status** | **str** | Current lifecycle status of the certificate | 
**created_at** | **datetime** | Time when the certificate request was created | 
**last_modified_at** | **datetime** | Time when the certificate request was last modified | 
**package_download_link** | [**LinkObject**](LinkObject.md) |  | [optional] 
**package_expires_at** | **datetime** | Time until which the certificate package can be downloaded | [optional] 
**provisioning_status** | **str** | Status of certificate and package provisioning | 

## Example

```python
from tidal.models.client_certificates_attributes import ClientCertificatesAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCertificatesAttributes from a JSON string
client_certificates_attributes_instance = ClientCertificatesAttributes.from_json(json)
# print the JSON string representation of the object
print(ClientCertificatesAttributes.to_json())

# convert the object into a dict
client_certificates_attributes_dict = client_certificates_attributes_instance.to_dict()
# create an instance of ClientCertificatesAttributes from a dict
client_certificates_attributes_from_dict = ClientCertificatesAttributes.from_dict(client_certificates_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


