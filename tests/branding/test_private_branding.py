from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.branding.branding_schema import BrandingSchema
from clients.branding.private_branding_client import PrivateBrandingClient
from clients.branding.public_branding_client import PublicBrandingClient
from clients.branding.routes import BrandingRoutes
from data_factories.branding_factory import BrandingFactory
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.assertions.base import assert_status_code, assert_is_instance
from utils.assertions.branding import assert_branding, assert_update_branding_response
from utils.assertions.schema import validate_json_schema


@pytest.mark.branding
@pytest.mark.regression
@allure.tag(AllureTag.BRANDING)
@allure.epic(AllureEpic.BRANDING)
@allure.feature(AllureFeature.BRANDING_CONFIG)
class TestPrivateBrandingAPI:
    """Test suite for authenticated Branding endpoints — PUT /branding/."""

    @pytest.mark.smoke
    @allure.story(AllureStory.BRANDING_UPDATE)
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.title("PUT /branding – Update branding successfully (202)")
    @allure.severity(Severity.BLOCKER)
    def test_update_branding_returns_202(
        self,
        private_branding_client: PrivateBrandingClient,
        valid_branding_update: BrandingSchema
    ):
        """Positive test: Update branding via raw API method, validate status and JSON schema."""
        response = private_branding_client.update_branding_api(valid_branding_update)
        assert_status_code(response.status_code, HTTPStatus.ACCEPTED)
        response_data = BrandingSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.BRANDING_UPDATE)
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.title("PUT /branding – High-level method returns parsed model")
    @allure.severity(Severity.NORMAL)
    def test_update_branding_high_level(
        self,
        private_branding_client: PrivateBrandingClient,
        valid_branding_update: BrandingSchema
    ):
        """Positive test: Use convenience method update_branding() and validate response fields match request."""
        updated = private_branding_client.update_branding(valid_branding_update)
        assert_is_instance(updated, BrandingSchema, "updated")
        assert_update_branding_response(updated, valid_branding_update)

    @allure.story(AllureStory.BRANDING_UPDATE)
    @allure.tag(AllureTag.UPDATE_ENTITY)
    @allure.title("PUT /branding – Update and verify via GET")
    @allure.severity(Severity.NORMAL)
    def test_update_branding_verify_via_get(
        self,
        public_branding_client: PublicBrandingClient,
        private_branding_client: PrivateBrandingClient,
        valid_branding_update: BrandingSchema
    ):
        """Positive test: Update branding, then retrieve via GET and assert data persistence."""
        updated = private_branding_client.update_branding(valid_branding_update)
        assert_is_instance(updated, BrandingSchema, "updated")
        current = public_branding_client.get_branding()
        assert_branding(current, updated)

    @allure.story(AllureStory.BRANDING_UPDATE)
    @allure.tag(AllureTag.UPDATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("PUT /branding – Without authentication (403)")
    @allure.severity(Severity.CRITICAL)
    def test_update_branding_unauthorized_403(
        self,
        private_branding_client_invalid: PrivateBrandingClient
    ):
        """Negative test: Update branding with invalid cookies should return 403 Forbidden."""
        response = private_branding_client_invalid.put(
            BrandingRoutes.ROOT,
            json={"name": "Test Brand", "logoUrl": "http://x.com/l.png", "description": "Valid description", "directions": "Go straight ahead."}
        )
        assert_status_code(response.status_code, HTTPStatus.FORBIDDEN)

    @allure.story(AllureStory.BRANDING_UPDATE)
    @allure.tag(AllureTag.UPDATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("PUT /branding – Name too short (400)")
    @allure.severity(Severity.NORMAL)
    def test_update_branding_name_too_short_400(
        self,
        private_branding_client: PrivateBrandingClient
    ):
        """Negative test: Update branding with name shorter than minimum length (1 char)."""
        invalid_data = BrandingFactory.build().model_dump(mode="json")
        invalid_data["name"] = "A"

        response = private_branding_client.put(BrandingRoutes.ROOT, json=invalid_data)
        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)

    @allure.story(AllureStory.BRANDING_UPDATE)
    @allure.tag(AllureTag.UPDATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("PUT /branding – Invalid name pattern (digits, 400)")
    @allure.severity(Severity.NORMAL)
    def test_update_branding_invalid_pattern_400(
        self,
        private_branding_client: PrivateBrandingClient
    ):
        """Negative test: Update branding with digits in name — API rejects non-alpha characters."""
        invalid_data = BrandingFactory.build().model_dump(mode="json")
        invalid_data["name"] = "Hotel123"

        response = private_branding_client.put(BrandingRoutes.ROOT, json=invalid_data)
        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)

    @allure.story(AllureStory.BRANDING_UPDATE)
    @allure.tag(AllureTag.UPDATE_ENTITY, AllureTag.NEGATIVE)
    @allure.title("PUT /branding – Missing required field (description, 400)")
    @allure.severity(Severity.NORMAL)
    def test_update_branding_missing_required_field_400(
        self,
        private_branding_client: PrivateBrandingClient
    ):
        """Negative test: Update branding without required description field."""
        invalid_data = BrandingFactory.build().model_dump(mode="json")
        del invalid_data["description"]

        response = private_branding_client.put(BrandingRoutes.ROOT, json=invalid_data)
        assert_status_code(response.status_code, HTTPStatus.BAD_REQUEST)
