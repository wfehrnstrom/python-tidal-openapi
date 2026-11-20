# ExternalLinkPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**meta** | [**ExternalLinkMeta**](ExternalLinkMeta.md) |  | 

## Example

```python
from tidal.models.external_link_payload import ExternalLinkPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalLinkPayload from a JSON string
external_link_payload_instance = ExternalLinkPayload.from_json(json)
# print the JSON string representation of the object
print(ExternalLinkPayload.to_json())

# convert the object into a dict
external_link_payload_dict = external_link_payload_instance.to_dict()
# create an instance of ExternalLinkPayload from a dict
external_link_payload_from_dict = ExternalLinkPayload.from_dict(external_link_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


