# UserCollectionSaveForLatersSingleResourceDataDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserCollectionSaveForLatersResourceObject**](UserCollectionSaveForLatersResourceObject.md) |  | 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.user_collection_save_for_laters_single_resource_data_document import UserCollectionSaveForLatersSingleResourceDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UserCollectionSaveForLatersSingleResourceDataDocument from a JSON string
user_collection_save_for_laters_single_resource_data_document_instance = UserCollectionSaveForLatersSingleResourceDataDocument.from_json(json)
# print the JSON string representation of the object
print(UserCollectionSaveForLatersSingleResourceDataDocument.to_json())

# convert the object into a dict
user_collection_save_for_laters_single_resource_data_document_dict = user_collection_save_for_laters_single_resource_data_document_instance.to_dict()
# create an instance of UserCollectionSaveForLatersSingleResourceDataDocument from a dict
user_collection_save_for_laters_single_resource_data_document_from_dict = UserCollectionSaveForLatersSingleResourceDataDocument.from_dict(user_collection_save_for_laters_single_resource_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


