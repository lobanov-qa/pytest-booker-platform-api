import allure

from clients.report.report_schema import ReportSchema, EntrySchema
from utils.assertions.base import assert_is_instance, assert_equal, assert_positive
from utils.logger import get_logger

logger = get_logger("REPORT_ASSERTIONS")


@allure.step("Check report")
def assert_report(actual: ReportSchema, expected: ReportSchema):
    """
    Checks that the actual report matches the expected one.

    :param actual: Actual report data.
    :param expected: Expected report data.
    :raises AssertionError: If any field does not match.
    """
    logger.info("Check report")
    assert_is_instance(actual.report, list, "report")
    assert_equal(len(actual.report), len(expected.report), "report length")

    for i, (actual_entry, expected_entry) in enumerate(zip(actual.report, expected.report)):
        assert_entry_equal(actual_entry, expected_entry, index=i)


@allure.step("Check report entry at index {index}")
def assert_entry_equal(actual: EntrySchema, expected: EntrySchema, index: int = 0):
    """
    Checks that the actual entry matches the expected one.

    :param actual: Actual entry data.
    :param expected: Expected entry data.
    :param index: Index of the entry in the report (for logging).
    """
    logger.info(f"Check report entry at index {index}")
    assert_equal(actual.start, expected.start, f"entry[{index}].start")
    assert_equal(actual.end, expected.end, f"entry[{index}].end")
    assert_equal(actual.title, expected.title, f"entry[{index}].title")


@allure.step("Check report not empty")
def assert_report_not_empty(report: ReportSchema):
    """
    Checks that the report is not empty (has at least one entry).

    :param report: Report data.
    :raises AssertionError: If report is empty.
    """
    logger.info("Check report not empty")
    assert_is_instance(report.report, list, "report")
    assert_positive(len(report.report), "report length")