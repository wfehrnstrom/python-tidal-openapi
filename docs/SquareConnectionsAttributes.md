# SquareConnectionsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**List[SquareConnectionsCapability]**](SquareConnectionsCapability.md) | Per-feature capability statuses for this Square connection: GRANTED when the feature&#39;s Square scopes are granted, or REQUIRES_REAUTH when the seller must reconnect Square to use it. | [optional] 
**created_at** | **datetime** | Timestamp when the connection was created | [optional] 
**external_links** | [**List[ExternalLink]**](ExternalLink.md) | External links for Square connection | [optional] 
**last_modified_at** | **datetime** | Timestamp when the connection was last modified | [optional] 
**status** | **str** | Current status of this Square connection | 

## Example

```python
from tidal.models.square_connections_attributes import SquareConnectionsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of SquareConnectionsAttributes from a JSON string
square_connections_attributes_instance = SquareConnectionsAttributes.from_json(json)
# print the JSON string representation of the object
print(SquareConnectionsAttributes.to_json())

# convert the object into a dict
square_connections_attributes_dict = square_connections_attributes_instance.to_dict()
# create an instance of SquareConnectionsAttributes from a dict
square_connections_attributes_from_dict = SquareConnectionsAttributes.from_dict(square_connections_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


