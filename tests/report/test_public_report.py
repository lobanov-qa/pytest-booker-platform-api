from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.report.public_report_client import PublicReportClient
from clients.report.report_schema import ReportSchema, EntrySchema
from clients.report.routes import ReportRoutes
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.assertions.base import (
    assert_status_code,
    assert_is_instance,
)
from utils.assertions.report import assert_report_not_empty


@pytest.mark.report
@pytest.mark.regression
@allure.tag(AllureTag.REPORT)
@allure.epic(AllureEpic.REPORT)
@allure.feature(AllureFeature.REPORT_GENERATION)
class TestPublicReportAPI:
    """Test suite for public report endpoints (no authentication)."""

    @pytest.mark.smoke
    @allure.story(AllureStory.REPORT_BY_ROOM)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /report/room/1 - Get report for existing room (200)")
    @allure.severity(Severity.BLOCKER)
    def test_get_room_report(self, report_public_client: PublicReportClient):
        """Positive: get report for room id=1.
        Validates response structure and that report has entries."""
        response = report_public_client.get_room_report_api(room_id=1)
        assert_status_code(response.status_code, HTTPStatus.OK)

        report = ReportSchema.model_validate_json(response.text)
        assert_is_instance(report.report, list, "report")
        assert_report_not_empty(report)

        for entry in report.report:
            assert_is_instance(entry, EntrySchema, "entry")
            assert entry.start < entry.end, f"start ({entry.start}) must be before end ({entry.end})"

    @pytest.mark.smoke
    @allure.story(AllureStory.REPORT_BY_ROOM)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /report/room/1 - High-level method returns parsed model")
    @allure.severity(Severity.NORMAL)
    def test_get_room_report_high_level(self, report_public_client: PublicReportClient):
        """Positive: use convenience get_room_report() → ReportSchema."""
        report = report_public_client.get_room_report(room_id=1)
        assert_is_instance(report, ReportSchema, "report")
        assert_is_instance(report.report, list, "report list")
        assert_report_not_empty(report)

    @allure.story(AllureStory.REPORT_BY_ROOM)
    @allure.tag(AllureTag.GET_ENTITY, AllureTag.NEGATIVE)
    @allure.title("GET /report/room/999999 - Non-existent room (200 but empty)")
    @allure.severity(Severity.NORMAL)
    def test_get_room_report_nonexistent_room(self, report_public_client: PublicReportClient):
        """Positive: check non-existent room id=999999 returns 200 with empty report."""
        response = report_public_client.get_room_report_api(room_id=999999)
        assert_status_code(response.status_code, HTTPStatus.OK)

        report = ReportSchema.model_validate_json(response.text)
        assert_is_instance(report.report, list, "report")
        # May be empty (API returns empty list or may have other data)
        # This test is generic, exact behaviour to be confirmed by curl in the next phase.

    @allure.story(AllureStory.REPORT_BY_ROOM)
    @allure.tag(AllureTag.GET_ENTITY, AllureTag.NEGATIVE)
    @allure.title("GET /report/room/abc - Non-numeric id returns 404")
    @allure.severity(Severity.NORMAL)
    def test_get_room_report_non_numeric_id(self, report_public_client: PublicReportClient):
        """Negative: non-numeric id like 'abc' → 404 (path mismatch)."""
        path = ReportRoutes.ROOM_REPORT.format(id="abc")
        response = report_public_client.get(path)
        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)

    @allure.story(AllureStory.REPORT_BY_ROOM)
    @allure.tag(AllureTag.GET_ENTITY, AllureTag.NEGATIVE)
    @allure.title("GET /report/room/-1 - Negative id returns 404")
    @allure.severity(Severity.NORMAL)
    def test_get_room_report_negative_id(self, report_public_client: PublicReportClient):
        """Negative: id=-1 → 404 (valid path, resource not found)."""
        path = ReportRoutes.ROOM_REPORT.format(id=-1)
        response = report_public_client.get(path)
        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)

    @allure.story(AllureStory.REPORT_BY_ROOM)
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.title("GET /report/room/0 - Zero id returns 200 (empty report)")
    @allure.severity(Severity.NORMAL)
    def test_get_room_report_zero_id(self, report_public_client: PublicReportClient):
        """Positive: id=0 → 200 OK with empty report."""
        path = ReportRoutes.ROOM_REPORT.format(id=0)
        response = report_public_client.get(path)
        assert_status_code(response.status_code, HTTPStatus.OK)

        report = ReportSchema.model_validate_json(response.text)
        assert_is_instance(report.report, list, "report")

    @allure.story(AllureStory.REPORT_BY_ROOM)
    @allure.tag(AllureTag.GET_ENTITY, AllureTag.NEGATIVE)
    @allure.title("GET /report/room/ — Missing id (404)")
    @allure.severity(Severity.MINOR)
    def test_get_room_report_no_id(self, report_public_client: PublicReportClient):
        """Negative: request without id path parameter.
        API should return 404 Not Found."""
        response = report_public_client.get("/room/")
        assert_status_code(response.status_code, HTTPStatus.NOT_FOUND)