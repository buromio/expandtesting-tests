from jsonschema import validate


def assert_matches_schema(instance: dict, schema: dict) -> None:
    validate(instance=instance, schema=schema)
