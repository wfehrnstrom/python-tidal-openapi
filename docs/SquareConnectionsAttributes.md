# SquareConnectionsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**List[SquareConnectionsCapability]**](SquareConnectionsCapability.md) | Per-feature capability statuses for this Square connection. Every capability the connection offers is listed with a status carrying more than mere presence: SITES is GRANTED when the Square Online sites scopes are granted, or REQUIRES_REAUTH when the connection exists but its credential lacks them (the seller must reconnect Square via POST /squareConnections). Because a connection always offers the sites feature, SITES is always present here. Extensible — only SITES is defined today. Absent only when the connection has no sites state (e.g. no approved Square credential). Client rule: if SITES !&#x3D; GRANTED prompt reconnect; else if selectedSite.data is null show the site picker; else the selected site is shown to buyers. | [optional] 
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


