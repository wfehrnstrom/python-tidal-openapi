# ArtistStreamsStatisticsCountryListeners


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | 
**listeners** | **int** |  | 

## Example

```python
from tidal.models.artist_streams_statistics_country_listeners import ArtistStreamsStatisticsCountryListeners

# TODO update the JSON string below
json = "{}"
# create an instance of ArtistStreamsStatisticsCountryListeners from a JSON string
artist_streams_statistics_country_listeners_instance = ArtistStreamsStatisticsCountryListeners.from_json(json)
# print the JSON string representation of the object
print(ArtistStreamsStatisticsCountryListeners.to_json())

# convert the object into a dict
artist_streams_statistics_country_listeners_dict = artist_streams_statistics_country_listeners_instance.to_dict()
# create an instance of ArtistStreamsStatisticsCountryListeners from a dict
artist_streams_statistics_country_listeners_from_dict = ArtistStreamsStatisticsCountryListeners.from_dict(artist_streams_statistics_country_listeners_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


