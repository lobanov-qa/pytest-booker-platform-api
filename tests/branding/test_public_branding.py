from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.branding.branding_schema import BrandingSchema
from clients.branding.public_branding_client import PublicBrandingClient
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.assertions.base import assert_status_code, assert_is_instance
from utils.assertions.schema import validate_json_schema


@pytest.mark.branding
@pytest.mark.regression
@allure.tag(AllureTag.BRANDING)
@allure.epic(AllureEpic.BRANDING)
@allure.feature(AllureFeature.BRANDING_CONFIG)
class TestPublicBrandingAPI:
    """Test suite for public Branding endpoints — GET /branding/."""

    @pytest.mark.smoke
    @allure.story(AllureStory.BRANDING_GET)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("GET /branding – Retrieve branding information (200)")
    @allure.severity(Severity.BLOCKER)
    def test_get_branding_returns_200(self, public_branding_client: PublicBrandingClient):
        """Positive test: Retrieve current branding via raw API method and validate JSON schema."""
        response = public_branding_client.get_branding_api()
        assert_status_code(response.status_code, HTTPStatus.OK)
        response_data = BrandingSchema.model_validate_json(response.text)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @pytest.mark.smoke
    @allure.story(AllureStory.BRANDING_GET)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("GET /branding – High-level method returns parsed model")
    @allure.severity(Severity.NORMAL)
    def test_get_branding_high_level(self, public_branding_client: PublicBrandingClient):
        """Positive test: Use convenience method get_branding() and verify returned Pydantic model type."""
        branding = public_branding_client.get_branding()
        assert_is_instance(branding, BrandingSchema, "branding")
