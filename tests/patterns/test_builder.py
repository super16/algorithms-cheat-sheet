from typing import Any

from algorithms_cheat_sheet.patterns.creational import (
    Builder,
    ComplexObject,
    PartObject,
)


class TestBuilder:

    """
    Tests for Builder pattern.
    """

    builder: Builder = Builder() \
        .modify_object_with_foo_part() \
        .modify_object_with_bar_part()

    built_object: ComplexObject = builder.get_result()

    def test_result(self) -> None:
        """
        Test result of built complex object.
        """

        assert isinstance(self.built_object, ComplexObject)

    def test_parts_of_object(self) -> None:
        """
        Test parts of built object.
        """

        assert len(self.built_object.parts) == 2

        part: Any
        for part in self.built_object.parts:
            assert isinstance(part, PartObject)

    def test_parts_description(self) -> None:
        """
        Test description of built object parts.
        """
        assert self.built_object.parts[0].__str__() == "foo"
        assert self.built_object.parts[1].__str__() == "bar"

    def test_modified_built_object(self) -> None:
        """
        Modify and test again built object.
        """
        self.builder.modify_object_with_bar_part()
        modified_build_object: ComplexObject = self.builder.get_result()

        assert len(modified_build_object.parts) == 3
        assert isinstance(modified_build_object.parts[2], PartObject)
        assert modified_build_object.parts[2].__str__() == "bar"
