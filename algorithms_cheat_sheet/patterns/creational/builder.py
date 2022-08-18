from typing import List, TypeVar


class PartObject:

    """
    Part of complex object.
    """

    def __init__(self, description: str) -> None:

        """
        Part constructor.

        Args:
            description (str): Description to object.
        """

        self.description: str = description

    def __str__(self) -> str:
        """
        Description of part.

        Returns:
            Description of part object.
        """

        return self.description


class ComplexObject:

    """
    Complex object class.
    """

    def __init__(self) -> None:

        """
        Complex object constructor. Objects contains
        list of parts (PartObject instances).
        """

        self.parts: List[PartObject] = []


BuilderType = TypeVar("BuilderType", bound="Builder")


class Builder:

    """
    Builder pattern class.
    """

    def __init__(self: BuilderType) -> None:

        """
        Initialize builder with complex object.
        """

        self._complex_object: ComplexObject = ComplexObject()

    def modify_object_with_foo_part(self: BuilderType) -> BuilderType:

        """
        Add 'foo' part to complex object.

        Returns:
            Self object.
        """

        self._complex_object.parts.append(
            PartObject(description="foo")
        )
        return self

    def modify_object_with_bar_part(self: BuilderType) -> BuilderType:

        """
        Add 'bar' part to complex object.

        Returns:
            Self object.
        """

        self._complex_object.parts.append(
            PartObject(description="bar")
        )
        return self

    def get_result(self: BuilderType) -> ComplexObject:
        """
        Get result of building as complex object.

        Returns:
            Initialized and maybe modified ComplexObject class.
        """

        return self._complex_object
