from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.report.private_report_client import PrivateReportClient
from clients.report.report_schema import ReportSchema, EntrySchema
from utils.allure.epics import AllureEpic
from utils.allure.features import AllureFeature
from utils.allure.stories import AllureStory
from utils.allure.tags import AllureTag
from utils.assertions.base import assert_status_code, assert_is_instance
from utils.assertions.report import assert_report_not_empty


@pytest.mark.report
@pytest.mark.regression
@allure.tag(AllureTag.REPORT)
@allure.epic(AllureEpic.REPORT)
@allure.feature(AllureFeature.REPORT_GENERATION)
class TestPrivateReportAPI:
    """Test suite for authenticated report endpoints."""

    @pytest.mark.smoke
    @allure.story(AllureStory.REPORT_ALL)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /report/ - Retrieve all reports successfully (200)")
    @allure.severity(Severity.BLOCKER)
    def test_get_all_reports(self, report_private_client: PrivateReportClient):
        """Positive: get all reports with valid auth -> 200 OK."""
        response = report_private_client.get_all_reports_api()
        assert_status_code(response.status_code, HTTPStatus.OK)

        report = ReportSchema.model_validate_json(response.text)
        assert_is_instance(report.report, list, "report")
        assert_report_not_empty(report)

        for entry in report.report:
            assert_is_instance(entry, EntrySchema, "entry")
            assert entry.start < entry.end, (
                f"start ({entry.start}) must be before end ({entry.end})"
            )

    @pytest.mark.smoke
    @allure.story(AllureStory.REPORT_ALL)
    @allure.tag(AllureTag.GET_ENTITIES)
    @allure.title("GET /report/ - High-level method returns parsed model")
    @allure.severity(Severity.NORMAL)
    def test_get_all_reports_high_level(self, report_private_client: PrivateReportClient):
        """Positive: convenience get_all_reports() -> ReportSchema."""
        report = report_private_client.get_all_reports()
        assert_is_instance(report, ReportSchema, "report")
        assert_is_instance(report.report, list, "report list")
        assert_report_not_empty(report)

    @allure.story(AllureStory.REPORT_ALL)
    @allure.tag(AllureTag.GET_ENTITIES, AllureTag.NEGATIVE)
    @allure.title("GET /report/ - Without authentication (403)")
    @allure.severity(Severity.CRITICAL)
    def test_get_all_reports_without_auth(
        self, report_private_client_invalid: PrivateReportClient
    ):
        """Negative: no valid cookies -> 500 Internal Server Error (API bug)."""
        response = report_private_client_invalid.get_all_reports_api()
        assert_status_code(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)