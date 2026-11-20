# MutationResponseDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Links**](Links.md) |  | 
**meta** | **Dict[str, object]** | Non-standard meta information | [optional] 

## Example

```python
from tidal.models.mutation_response_document import MutationResponseDocument

# TODO update the JSON string below
json = "{}"
# create an instance of MutationResponseDocument from a JSON string
mutation_response_document_instance = MutationResponseDocument.from_json(json)
# print the JSON string representation of the object
print(MutationResponseDocument.to_json())

# convert the object into a dict
mutation_response_document_dict = mutation_response_document_instance.to_dict()
# create an instance of MutationResponseDocument from a dict
mutation_response_document_from_dict = MutationResponseDocument.from_dict(mutation_response_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


