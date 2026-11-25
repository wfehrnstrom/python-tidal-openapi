# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, field_validator  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
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
from tidal.models.user_collection_artists_items_add_multi_data_relationship_with_response409_response_body import UserCollectionArtistsItemsAddMultiDataRelationshipWithResponse409ResponseBody  # noqa: F401
from tidal.models.user_collection_artists_items_add_multi_relationship_data_document import UserCollectionArtistsItemsAddMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_collection_artists_items_multi_relationship_data_document import UserCollectionArtistsItemsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_collection_artists_items_read_multi_data_relationship403_response_body import UserCollectionArtistsItemsReadMultiDataRelationship403ResponseBody  # noqa: F401
from tidal.models.user_collection_artists_items_relationship_add_operation_payload import UserCollectionArtistsItemsRelationshipAddOperationPayload  # noqa: F401
from tidal.models.user_collection_artists_items_relationship_remove_operation_payload import UserCollectionArtistsItemsRelationshipRemoveOperationPayload  # noqa: F401
from tidal.models.user_collection_artists_owners_multi_relationship_data_document import UserCollectionArtistsOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.user_collection_artists_single_resource_data_document import UserCollectionArtistsSingleResourceDataDocument  # noqa: F401


def test_user_collection_artists_id_get(client: TestClient):
    """Test case for user_collection_artists_id_get

    Get single userCollectionArtist.
    """
    params = [("include", ['items.albums']),     ("include_linkage", ['include_linkage_example']),     ("locale", 'en-US'),     ("replace_media", 'items.albums')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userCollectionArtists/{id}".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_collection_artists_id_relationships_items_get(client: TestClient):
    """Test case for user_collection_artists_id_relationships_items_get

    Get items relationship (\"to-many\").
    """
    params = [("filter_self_matches_query", 'filter_self_matches_query_example'),     ("include", ['items.albums']),     ("locale", 'en-US'),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'items.albums'),     ("sort", ['sort_example'])]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userCollectionArtists/{id}/relationships/items".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_collection_artists_id_relationships_items_post(client: TestClient):
    """Test case for user_collection_artists_id_relationships_items_post

    Add to items relationship (\"to-many\").
    """
    user_collection_artists_items_relationship_add_operation_payload = tidal.UserCollectionArtistsItemsRelationshipAddOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/userCollectionArtists/{id}/relationships/items".format(id='me'),
    #    headers=headers,
    #    json=user_collection_artists_items_relationship_add_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_collection_artists_id_relationships_items_delete(client: TestClient):
    """Test case for user_collection_artists_id_relationships_items_delete

    Delete from items relationship (\"to-many\").
    """
    user_collection_artists_items_relationship_remove_operation_payload = tidal.UserCollectionArtistsItemsRelationshipRemoveOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/userCollectionArtists/{id}/relationships/items".format(id='me'),
    #    headers=headers,
    #    json=user_collection_artists_items_relationship_remove_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_collection_artists_id_relationships_owners_get(client: TestClient):
    """Test case for user_collection_artists_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/userCollectionArtists/{id}/relationships/owners".format(id='me'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

