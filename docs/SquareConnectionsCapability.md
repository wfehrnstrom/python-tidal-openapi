# SquareConnectionsCapability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The capability name | 
**status** | **str** | The capability&#39;s current status | 

## Example

```python
from tidal.models.square_connections_capability import SquareConnectionsCapability

# TODO update the JSON string below
json = "{}"
# create an instance of SquareConnectionsCapability from a JSON string
square_connections_capability_instance = SquareConnectionsCapability.from_json(json)
# print the JSON string representation of the object
print(SquareConnectionsCapability.to_json())

# convert the object into a dict
square_connections_capability_dict = square_connections_capability_instance.to_dict()
# create an instance of SquareConnectionsCapability from a dict
square_connections_capability_from_dict = SquareConnectionsCapability.from_dict(square_connections_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


