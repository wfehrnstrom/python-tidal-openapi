# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, field_validator  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from tidal.models.albums_album_statistics_single_relationship_data_document import AlbumsAlbumStatisticsSingleRelationshipDataDocument  # noqa: F401
from tidal.models.albums_artists_multi_relationship_data_document import AlbumsArtistsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.albums_artists_relationship_update_operation_payload import AlbumsArtistsRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.albums_cover_art_multi_relationship_data_document import AlbumsCoverArtMultiRelationshipDataDocument  # noqa: F401
from tidal.models.albums_cover_art_relationship_update_operation_payload import AlbumsCoverArtRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.albums_create_operation_payload import AlbumsCreateOperationPayload  # noqa: F401
from tidal.models.albums_create_single_resource_data_document import AlbumsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.albums_genres_multi_relationship_data_document import AlbumsGenresMultiRelationshipDataDocument  # noqa: F401
from tidal.models.albums_items_multi_relationship_data_document import AlbumsItemsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.albums_items_relationship_update_operation_payload import AlbumsItemsRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.albums_multi_resource_data_document import AlbumsMultiResourceDataDocument  # noqa: F401
from tidal.models.albums_owners_multi_relationship_data_document import AlbumsOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.albums_price_config_single_relationship_data_document import AlbumsPriceConfigSingleRelationshipDataDocument  # noqa: F401
from tidal.models.albums_providers_multi_relationship_data_document import AlbumsProvidersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.albums_replacement_single_relationship_data_document import AlbumsReplacementSingleRelationshipDataDocument  # noqa: F401
from tidal.models.albums_shares_multi_relationship_data_document import AlbumsSharesMultiRelationshipDataDocument  # noqa: F401
from tidal.models.albums_similar_albums_multi_relationship_data_document import AlbumsSimilarAlbumsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.albums_single_resource_data_document import AlbumsSingleResourceDataDocument  # noqa: F401
from tidal.models.albums_suggested_cover_arts_multi_relationship_data_document import AlbumsSuggestedCoverArtsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.albums_update_operation_payload import AlbumsUpdateOperationPayload  # noqa: F401
from tidal.models.albums_usage_rules_single_relationship_data_document import AlbumsUsageRulesSingleRelationshipDataDocument  # noqa: F401
from tidal.models.default400_response_body import Default400ResponseBody  # noqa: F401
from tidal.models.default404_response_body import Default404ResponseBody  # noqa: F401
from tidal.models.default405_response_body import Default405ResponseBody  # noqa: F401
from tidal.models.default406_response_body import Default406ResponseBody  # noqa: F401
from tidal.models.default415_response_body import Default415ResponseBody  # noqa: F401
from tidal.models.default429_response_body import Default429ResponseBody  # noqa: F401
from tidal.models.default500_response_body import Default500ResponseBody  # noqa: F401
from tidal.models.default503_response_body import Default503ResponseBody  # noqa: F401
from tidal.models.idempotency409_response_body import Idempotency409ResponseBody  # noqa: F401
from tidal.models.idempotency422_response_body import Idempotency422ResponseBody  # noqa: F401
from tidal.models.mutation_response_document import MutationResponseDocument  # noqa: F401


def test_albums_get(client: TestClient):
    """Test case for albums_get

    Get multiple albums.
    """
    params = [("country_code", 'US'),     ("filter_barcode_id", ['filter_barcode_id_example']),     ("filter_id", ['filter_id_example']),     ("filter_owners_id", ['filter_owners_id_example']),     ("include", ['artists.albums']),     ("include_linkage", ['include_linkage_example']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'artists.albums'),     ("share_code", 'xyz'),     ("sort", ['sort_example'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/albums",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_post(client: TestClient):
    """Test case for albums_post

    Create single album.
    """
    albums_create_operation_payload = tidal.AlbumsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/albums",
    #    headers=headers,
    #    json=albums_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_get(client: TestClient):
    """Test case for albums_id_get

    Get single album.
    """
    params = [("country_code", 'US'),     ("include", ['artists.albums']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'artists.albums'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/albums/{id}".format(id='251380836'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_delete(client: TestClient):
    """Test case for albums_id_delete

    Delete single album.
    """
    params = [("share_code", 'xyz')]
    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/albums/{id}".format(id='251380836'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_patch(client: TestClient):
    """Test case for albums_id_patch

    Update single album.
    """
    albums_update_operation_payload = tidal.AlbumsUpdateOperationPayload()
    params = [("share_code", 'xyz')]
    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/albums/{id}".format(id='251380836'),
    #    headers=headers,
    #    json=albums_update_operation_payload,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_relationships_album_statistics_get(client: TestClient):
    """Test case for albums_id_relationships_album_statistics_get

    Get albumStatistics relationship (\"to-one\").
    """
    params = [("include", ['albumStatistics']),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/albums/{id}/relationships/albumStatistics".format(id='251380836'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_relationships_artists_get(client: TestClient):
    """Test case for albums_id_relationships_artists_get

    Get artists relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['artists.albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'artists.albums'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/albums/{id}/relationships/artists".format(id='251380836'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_relationships_artists_patch(client: TestClient):
    """Test case for albums_id_relationships_artists_patch

    Update artists relationship (\"to-many\").
    """
    albums_artists_relationship_update_operation_payload = tidal.AlbumsArtistsRelationshipUpdateOperationPayload()
    params = [("share_code", 'xyz')]
    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/albums/{id}/relationships/artists".format(id='251380836'),
    #    headers=headers,
    #    json=albums_artists_relationship_update_operation_payload,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_relationships_cover_art_get(client: TestClient):
    """Test case for albums_id_relationships_cover_art_get

    Get coverArt relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['coverArt']),     ("page_cursor", 'page_cursor_example'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/albums/{id}/relationships/coverArt".format(id='251380836'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_relationships_cover_art_patch(client: TestClient):
    """Test case for albums_id_relationships_cover_art_patch

    Update coverArt relationship (\"to-many\").
    """
    albums_cover_art_relationship_update_operation_payload = tidal.AlbumsCoverArtRelationshipUpdateOperationPayload()
    params = [("share_code", 'xyz')]
    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/albums/{id}/relationships/coverArt".format(id='251380836'),
    #    headers=headers,
    #    json=albums_cover_art_relationship_update_operation_payload,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_relationships_genres_get(client: TestClient):
    """Test case for albums_id_relationships_genres_get

    Get genres relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['genres']),     ("page_cursor", 'page_cursor_example'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/albums/{id}/relationships/genres".format(id='251380836'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_relationships_items_get(client: TestClient):
    """Test case for albums_id_relationships_items_get

    Get items relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['items']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'items'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/albums/{id}/relationships/items".format(id='251380836'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_relationships_items_patch(client: TestClient):
    """Test case for albums_id_relationships_items_patch

    Update items relationship (\"to-many\").
    """
    albums_items_relationship_update_operation_payload = tidal.AlbumsItemsRelationshipUpdateOperationPayload()
    params = [("share_code", 'xyz')]
    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/albums/{id}/relationships/items".format(id='251380836'),
    #    headers=headers,
    #    json=albums_items_relationship_update_operation_payload,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_relationships_owners_get(client: TestClient):
    """Test case for albums_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/albums/{id}/relationships/owners".format(id='251380836'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_relationships_price_config_get(client: TestClient):
    """Test case for albums_id_relationships_price_config_get

    Get priceConfig relationship (\"to-one\").
    """
    params = [("country_code", 'US'),     ("include", ['priceConfig']),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/albums/{id}/relationships/priceConfig".format(id='251380836'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_relationships_providers_get(client: TestClient):
    """Test case for albums_id_relationships_providers_get

    Get providers relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['providers']),     ("page_cursor", 'page_cursor_example'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/albums/{id}/relationships/providers".format(id='251380836'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_relationships_replacement_get(client: TestClient):
    """Test case for albums_id_relationships_replacement_get

    Get replacement relationship (\"to-one\").
    """
    params = [("country_code", 'US'),     ("include", ['replacement']),     ("replace_media", 'replacement'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/albums/{id}/relationships/replacement".format(id='251380836'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_relationships_shares_get(client: TestClient):
    """Test case for albums_id_relationships_shares_get

    Get shares relationship (\"to-many\").
    """
    params = [("include", ['shares.sharedResources']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'shares.sharedResources'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/albums/{id}/relationships/shares".format(id='251380836'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_relationships_similar_albums_get(client: TestClient):
    """Test case for albums_id_relationships_similar_albums_get

    Get similarAlbums relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['similarAlbums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'similarAlbums'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/albums/{id}/relationships/similarAlbums".format(id='251380836'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_relationships_suggested_cover_arts_get(client: TestClient):
    """Test case for albums_id_relationships_suggested_cover_arts_get

    Get suggestedCoverArts relationship (\"to-many\").
    """
    params = [("include", ['suggestedCoverArts']),     ("page_cursor", 'page_cursor_example'),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/albums/{id}/relationships/suggestedCoverArts".format(id='251380836'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_albums_id_relationships_usage_rules_get(client: TestClient):
    """Test case for albums_id_relationships_usage_rules_get

    Get usageRules relationship (\"to-one\").
    """
    params = [("country_code", 'US'),     ("include", ['usageRules']),     ("share_code", 'xyz')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/albums/{id}/relationships/usageRules".format(id='251380836'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

