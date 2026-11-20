# ProviderProductInfosAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode_id** | **str** |  | [optional] 
**broken** | **bool** |  | [optional] 
**broken_code** | **int** |  | [optional] 
**grid** | **str** |  | [optional] 
**tracks** | [**List[TrackInfo]**](TrackInfo.md) |  | [optional] 

## Example

```python
from tidal.models.provider_product_infos_attributes import ProviderProductInfosAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderProductInfosAttributes from a JSON string
provider_product_infos_attributes_instance = ProviderProductInfosAttributes.from_json(json)
# print the JSON string representation of the object
print(ProviderProductInfosAttributes.to_json())

# convert the object into a dict
provider_product_infos_attributes_dict = provider_product_infos_attributes_instance.to_dict()
# create an instance of ProviderProductInfosAttributes from a dict
provider_product_infos_attributes_from_dict = ProviderProductInfosAttributes.from_dict(provider_product_infos_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


