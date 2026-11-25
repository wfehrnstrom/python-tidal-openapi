# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, field_validator  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from tidal.models.artist_biographies_owners_multi_relationship_data_document import ArtistBiographiesOwnersMultiRelationshipDataDocument  # noqa: F401
from tidal.models.artist_biographies_single_resource_data_document import ArtistBiographiesSingleResourceDataDocument  # noqa: F401
from tidal.models.artist_biographies_update_operation_payload import ArtistBiographiesUpdateOperationPayload  # noqa: F401
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


def test_artist_biographies_id_get(client: TestClient):
    """Test case for artist_biographies_id_get

    Get single artistBiographie.
    """
    params = [("country_code", 'US'),     ("include", ['include_example']),     ("include_linkage", ['include_linkage_example'])]
    headers = {
        "Authorization": "Bearer special-key",
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/artistBiographies/{id}".format(id='123456'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artist_biographies_id_patch(client: TestClient):
    """Test case for artist_biographies_id_patch

    Update single artistBiographie.
    """
    artist_biographies_update_operation_payload = tidal.ArtistBiographiesUpdateOperationPayload()

    headers = {
        "idempotency_key": '79e1f37e-3e84-4c51-b5e2-7d9e1a2b3c4d',
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/artistBiographies/{id}".format(id='123456'),
    #    headers=headers,
    #    json=artist_biographies_update_operation_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_artist_biographies_id_relationships_owners_get(client: TestClient):
    """Test case for artist_biographies_id_relationships_owners_get

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
    #    "/artistBiographies/{id}/relationships/owners".format(id='123456'),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

