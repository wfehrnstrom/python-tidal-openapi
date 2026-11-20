# ClientsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**ClientsAttributes**](ClientsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**ClientsRelationships**](ClientsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.clients_resource_object import ClientsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ClientsResourceObject from a JSON string
clients_resource_object_instance = ClientsResourceObject.from_json(json)
# print the JSON string representation of the object
print(ClientsResourceObject.to_json())

# convert the object into a dict
clients_resource_object_dict = clients_resource_object_instance.to_dict()
# create an instance of ClientsResourceObject from a dict
clients_resource_object_from_dict = ClientsResourceObject.from_dict(clients_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


