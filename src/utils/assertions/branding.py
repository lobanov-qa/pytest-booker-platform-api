import allure

from clients.branding.branding_schema import BrandingSchema
from utils.assertions.base import assert_equal
from utils.logger import get_logger

logger = get_logger("BRANDING_ASSERTIONS")


@allure.step("Check branding")
def assert_branding(actual: BrandingSchema, expected: BrandingSchema):
    """
    Checks that the actual branding data matches the expected one.

    :param actual: Actual branding data.
    :param expected: Expected branding data.
    :raises AssertionError: If at least one field does not match.
    """
    logger.info("Check branding")
    assert_equal(actual.name, expected.name, "name")
    assert_equal(actual.logo_url, expected.logo_url, "logo_url")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.directions, expected.directions, "directions")

    if expected.map is not None:
        assert actual.map is not None, "Expected map to be present but got None"
        assert_equal(actual.map.latitude, expected.map.latitude, "map.latitude")
        assert_equal(actual.map.longitude, expected.map.longitude, "map.longitude")
    if expected.contact is not None:
        assert actual.contact is not None, "Expected contact to be present but got None"
        assert_equal(actual.contact.name, expected.contact.name, "contact.name")
        assert_equal(actual.contact.phone, expected.contact.phone, "contact.phone")
        assert_equal(str(actual.contact.email), str(expected.contact.email), "contact.email")
    if expected.address is not None:
        assert actual.address is not None, "Expected address to be present but got None"
        assert_equal(actual.address.line1, expected.address.line1, "address.line1")
        assert_equal(actual.address.line2, expected.address.line2, "address.line2")
        assert_equal(actual.address.post_town, expected.address.post_town, "address.post_town")
        assert_equal(actual.address.county, expected.address.county, "address.county")
        assert_equal(actual.address.post_code, expected.address.post_code, "address.post_code")


@allure.step("Check update branding response")
def assert_update_branding_response(
    updated: BrandingSchema,
    update_request: BrandingSchema
):
    """
    Checks that updated branding fields match the update request.
    Compares all fields from update_request against updated response.

    :param updated: Branding data after update.
    :param update_request: The update request that was sent (full Branding object).
    :raises AssertionError: If fields do not match expectations.
    """
    logger.info("Check update branding response")

    assert_equal(updated.name, update_request.name, "name")
    assert_equal(updated.logo_url, update_request.logo_url, "logo_url")
    assert_equal(updated.description, update_request.description, "description")
    assert_equal(updated.directions, update_request.directions, "directions")

    assert updated.map is not None, "Expected updated map but got None"
    assert_equal(updated.map.latitude, update_request.map.latitude, "map.latitude")
    assert_equal(updated.map.longitude, update_request.map.longitude, "map.longitude")

    assert updated.contact is not None, "Expected updated contact but got None"
    assert_equal(updated.contact.name, update_request.contact.name, "contact.name")
    assert_equal(updated.contact.phone, update_request.contact.phone, "contact.phone")
    assert_equal(str(updated.contact.email), str(update_request.contact.email), "contact.email")

    assert updated.address is not None, "Expected updated address but got None"
    assert_equal(updated.address.line1, update_request.address.line1, "address.line1")
    assert_equal(updated.address.line2, update_request.address.line2, "address.line2")
    assert_equal(updated.address.post_town, update_request.address.post_town, "address.post_town")
    assert_equal(updated.address.county, update_request.address.county, "address.county")
    assert_equal(updated.address.post_code, update_request.address.post_code, "address.post_code")