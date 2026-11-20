# SquareConnectionsResourceObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**SquareConnectionsAttributes**](SquareConnectionsAttributes.md) |  | [optional] 
**id** | **str** | Resource id | 
**relationships** | [**SquareConnectionsRelationships**](SquareConnectionsRelationships.md) |  | [optional] 
**type** | **str** | Resource type | 

## Example

```python
from tidal.models.square_connections_resource_object import SquareConnectionsResourceObject

# TODO update the JSON string below
json = "{}"
# create an instance of SquareConnectionsResourceObject from a JSON string
square_connections_resource_object_instance = SquareConnectionsResourceObject.from_json(json)
# print the JSON string representation of the object
print(SquareConnectionsResourceObject.to_json())

# convert the object into a dict
square_connections_resource_object_dict = square_connections_resource_object_instance.to_dict()
# create an instance of SquareConnectionsResourceObject from a dict
square_connections_resource_object_from_dict = SquareConnectionsResourceObject.from_dict(square_connections_resource_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


