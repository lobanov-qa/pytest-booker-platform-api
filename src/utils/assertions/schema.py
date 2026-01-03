from typing import Any

import allure

from jsonschema import validate
from jsonschema.validators import Draft202012Validator

from utils.logger import get_logger

logger = get_logger("SCHEMA_ASSERTIONS")


@allure.step("Validate JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Checks whether a JSON object (instance) matches the given JSON schema (schema).

    :param instance: JSON data to be validated.
    :param schema: Expected JSON-schema.
    :raises jsonschema.exceptions.ValidationError: If instance does not match schema.
    """
    logger.info("Validating JSON schema")

    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )