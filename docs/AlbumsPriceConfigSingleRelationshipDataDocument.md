# AlbumsPriceConfigSingleRelationshipDataDocument

Target resource types: `priceConfigurations`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResourceIdentifier**](ResourceIdentifier.md) |  | [optional] 
**included** | [**List[IncludedInner]**](IncludedInner.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from tidal.models.albums_price_config_single_relationship_data_document import AlbumsPriceConfigSingleRelationshipDataDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AlbumsPriceConfigSingleRelationshipDataDocument from a JSON string
albums_price_config_single_relationship_data_document_instance = AlbumsPriceConfigSingleRelationshipDataDocument.from_json(json)
# print the JSON string representation of the object
print(AlbumsPriceConfigSingleRelationshipDataDocument.to_json())

# convert the object into a dict
albums_price_config_single_relationship_data_document_dict = albums_price_config_single_relationship_data_document_instance.to_dict()
# create an instance of AlbumsPriceConfigSingleRelationshipDataDocument from a dict
albums_price_config_single_relationship_data_document_from_dict = AlbumsPriceConfigSingleRelationshipDataDocument.from_dict(albums_price_config_single_relationship_data_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


