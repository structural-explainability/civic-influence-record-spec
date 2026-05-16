"""Tests for specification configuration."""

from civic_influence_record.spec_config import SPEC_CONFIG


def test_spec_config_has_export_schemas() -> None:
    """Spec config exposes export schema identifiers."""
    assert SPEC_CONFIG.requirements_schema
    assert SPEC_CONFIG.scope_exclusions_schema
    assert SPEC_CONFIG.conformance_schema


def test_spec_config_has_markdown_file_names() -> None:
    """Spec config exposes expected Markdown source files."""
    assert SPEC_CONFIG.identifiers_file_name == "IDENTIFIERS.md"
    assert SPEC_CONFIG.spec_file_name == "SPEC.md"
    assert SPEC_CONFIG.conformance_file_name == "CONFORMANCE.md"
    assert SPEC_CONFIG.normative_source_file_name == "SPEC.md"
