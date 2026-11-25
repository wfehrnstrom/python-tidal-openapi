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
from tidal.models.playlists_collaborator_profiles_multi_relationship_data_document import PlaylistsCollaboratorProfilesMultiRelationshipDataDocument  # noqa: F401
from tidal.models.playlists_collaborator_profiles_relationship_remove_operation_payload import PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayload  # noqa: F401
from tidal.models.playlists_collaborators_multi_relationship_data_document import PlaylistsCollaboratorsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.playlists_cover_art_multi_relationship_data_document import PlaylistsCoverArtMultiRelationshipDataDocument  # noqa: F401
from tidal.models.playlists_cover_art_relationship_update_operation_payload import PlaylistsCoverArtRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.playlists_create_operation_payload import PlaylistsCreateOperationPayload  # noqa: F401
from tidal.models.playlists_create_single_resource_data_document import PlaylistsCreateSingleResourceDataDocument  # noqa: F401
from tidal.models.playlists_curators_multi_relationship_data_document import PlaylistsCuratorsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.playlists_items_add_multi_data_relationship_with_response409_response_body import PlaylistsItemsAddMultiDataRelationshipWithResponse409ResponseBody  # noqa: F401
from tidal.models.playlists_items_add_multi_relationship_data_document import PlaylistsItemsAddMultiRelationshipDataDocument  # noqa: F401
from tidal.models.playlists_items_multi_relationship_data_document import PlaylistsItemsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.playlists_items_relationship_add_operation_payload import PlaylistsItemsRelationshipAddOperationPayload  # noqa: F401
from tidal.models.playlists_items_relationship_remove_operation_payload import PlaylistsItemsRelationshipRemoveOperationPayload  # noqa: F401
from tidal.models.playlists_items_relationship_update_operation_payload import PlaylistsItemsRelationshipUpdateOperationPayload  # noqa: F401
from tidal.models.playlists_multi_resource_data_document import PlaylistsMultiResourceDataDocument  # noqa: F401
from tidal.models.playlists_owner_profiles_multi_relationship_data_document import PlaylistsOwnerProfilesMultiRelationshipDataDocument  # noqa: F401
from tidal.models.playlists_owners_multi_relationship_data_document import PlaylistsOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.playlists_single_resource_data_document import PlaylistsSingleResourceDataDocument  # noqa: F401
from tidal.models.playlists_suggested_cover_arts_multi_relationship_data_document import PlaylistsSuggestedCoverArtsMultiRelationshipDataDocument  # noqa: F401
from tidal.models.playlists_update_operation_payload import PlaylistsUpdateOperationPayload  # noqa: F401
from tidal.models.playlists_update_single_resource_data_document import PlaylistsUpdateSingleResourceDataDocument  # noqa: F401


def test_playlists_get(client: TestClient):
    """Test case for playlists_get

    Get multiple playlists.
    """
    params = [("country_code", 'US'),     ("filter_collaborators_id", ['filter_collaborators_id_example']),     ("filter_id", ['filter_id_example']),     ("filter_owners_id", ['filter_owners_id_example']),     ("include", ['curators.albums']),     ("include_linkage", ['include_linkage_example']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'curators.albums'),     ("sort", ['sort_example'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlists",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlists_post(client: TestClient):
    """Test case for playlists_post

    Create single playlist.
    """
    playlists_create_operation_payload = tidal.PlaylistsCreateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/playlists",
    #    headers=headers,
    #    json=playlists_create_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlists_id_get(client: TestClient):
    """Test case for playlists_id_get

    Get single playlist.
    """
    params = [("country_code", 'US'),     ("include", ['curators.albums']),     ("include_linkage", ['include_linkage_example']),     ("replace_media", 'curators.albums')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlists/{id}".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlists_id_delete(client: TestClient):
    """Test case for playlists_id_delete

    Delete single playlist.
    """

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/playlists/{id}".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlists_id_patch(client: TestClient):
    """Test case for playlists_id_patch

    Update single playlist.
    """
    playlists_update_operation_payload = tidal.PlaylistsUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/playlists/{id}".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    json=playlists_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlists_id_relationships_collaborator_profiles_get(client: TestClient):
    """Test case for playlists_id_relationships_collaborator_profiles_get

    Get collaboratorProfiles relationship (\"to-many\").
    """
    params = [("include", ['collaboratorProfiles']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlists/{id}/relationships/collaboratorProfiles".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlists_id_relationships_collaborator_profiles_delete(client: TestClient):
    """Test case for playlists_id_relationships_collaborator_profiles_delete

    Delete from collaboratorProfiles relationship (\"to-many\").
    """
    playlists_collaborator_profiles_relationship_remove_operation_payload = tidal.PlaylistsCollaboratorProfilesRelationshipRemoveOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/playlists/{id}/relationships/collaboratorProfiles".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    json=playlists_collaborator_profiles_relationship_remove_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlists_id_relationships_collaborators_get(client: TestClient):
    """Test case for playlists_id_relationships_collaborators_get

    Get collaborators relationship (\"to-many\").
    """
    params = [("include", ['collaborators']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlists/{id}/relationships/collaborators".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlists_id_relationships_cover_art_get(client: TestClient):
    """Test case for playlists_id_relationships_cover_art_get

    Get coverArt relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("include", ['coverArt']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlists/{id}/relationships/coverArt".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlists_id_relationships_cover_art_patch(client: TestClient):
    """Test case for playlists_id_relationships_cover_art_patch

    Update coverArt relationship (\"to-many\").
    """
    playlists_cover_art_relationship_update_operation_payload = tidal.PlaylistsCoverArtRelationshipUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/playlists/{id}/relationships/coverArt".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    json=playlists_cover_art_relationship_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlists_id_relationships_curators_get(client: TestClient):
    """Test case for playlists_id_relationships_curators_get

    Get curators relationship (\"to-many\").
    """
    params = [("include", ['curators.albums']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'curators.albums')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlists/{id}/relationships/curators".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlists_id_relationships_items_get(client: TestClient):
    """Test case for playlists_id_relationships_items_get

    Get items relationship (\"to-many\").
    """
    params = [("country_code", 'US'),     ("filter_self_matches_query", 'filter_self_matches_query_example'),     ("include", ['items']),     ("page_cursor", 'page_cursor_example'),     ("replace_media", 'items'),     ("sort", ['sort_example'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlists/{id}/relationships/items".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlists_id_relationships_items_post(client: TestClient):
    """Test case for playlists_id_relationships_items_post

    Add to items relationship (\"to-many\").
    """
    playlists_items_relationship_add_operation_payload = tidal.PlaylistsItemsRelationshipAddOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/playlists/{id}/relationships/items".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    json=playlists_items_relationship_add_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlists_id_relationships_items_delete(client: TestClient):
    """Test case for playlists_id_relationships_items_delete

    Delete from items relationship (\"to-many\").
    """
    playlists_items_relationship_remove_operation_payload = tidal.PlaylistsItemsRelationshipRemoveOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/playlists/{id}/relationships/items".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    json=playlists_items_relationship_remove_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlists_id_relationships_items_patch(client: TestClient):
    """Test case for playlists_id_relationships_items_patch

    Update items relationship (\"to-many\").
    """
    playlists_items_relationship_update_operation_payload = tidal.PlaylistsItemsRelationshipUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/playlists/{id}/relationships/items".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    json=playlists_items_relationship_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlists_id_relationships_owner_profiles_get(client: TestClient):
    """Test case for playlists_id_relationships_owner_profiles_get

    Get ownerProfiles relationship (\"to-many\").
    """
    params = [("include", ['ownerProfiles']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlists/{id}/relationships/ownerProfiles".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlists_id_relationships_owners_get(client: TestClient):
    """Test case for playlists_id_relationships_owners_get

    Get owners relationship (\"to-many\").
    """
    params = [("include", ['owners']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlists/{id}/relationships/owners".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_playlists_id_relationships_suggested_cover_arts_get(client: TestClient):
    """Test case for playlists_id_relationships_suggested_cover_arts_get

    Get suggestedCoverArts relationship (\"to-many\").
    """
    params = [("include", ['suggestedCoverArts']),     ("page_cursor", 'page_cursor_example')]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/playlists/{id}/relationships/suggestedCoverArts".format(id='550e8400-e29b-41d4-a716-446655440000'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

