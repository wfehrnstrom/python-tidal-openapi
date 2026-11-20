# ClientsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_tier** | **str** |  | 
**client_preset** | **str** | Client preset defining default OAuth settings and supported audio formats. | 
**client_secret** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | 
**redirect_uris** | **List[str]** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from tidal.models.clients_attributes import ClientsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ClientsAttributes from a JSON string
clients_attributes_instance = ClientsAttributes.from_json(json)
# print the JSON string representation of the object
print(ClientsAttributes.to_json())

# convert the object into a dict
clients_attributes_dict = clients_attributes_instance.to_dict()
# create an instance of ClientsAttributes from a dict
clients_attributes_from_dict = ClientsAttributes.from_dict(clients_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


