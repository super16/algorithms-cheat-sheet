from algorithms_cheat_sheet.patterns.creational import (
    AbstractProduct,
    AbstractFactory,
)


CONCRETE_PRODUCT = "Concrete product"

FACTORY_A_PRODUCT = "Concrete product from factory A"
FACTORY_B_PRODUCT = "Concrete product from factory B"

FACTORY_A_ANOTHER_PRODUCT = "Concrete product from factory A"
FACTORY_B_ANOTHER_PRODUCT = "Concrete product from factory B"


class ConcreteProduct(AbstractProduct):

    """Concrete product class."""

    pass


class AnotherConcreteProductA(AbstractProduct):

    """Another concrete product class."""

    pass


class AnotherConcreteProductB(AbstractProduct):

    """Another concrete product class."""

    pass


class ConcreteFactoryA(AbstractFactory):

    """
    Concrete factory that creates concrete product.
    """

    def create_product(self) -> ConcreteProduct:
        """
        Create concrete product.

        Returns:
            Concrete product from factory A.
        """
        return ConcreteProduct(title=FACTORY_A_PRODUCT)

    def create_another_product(self) -> AnotherConcreteProductA:
        """
        Create another concrete product A.

        Returns:
            Concrete another product from factory A.
        """
        return AnotherConcreteProductA(title=FACTORY_A_ANOTHER_PRODUCT)


class ConcreteFactoryB(AbstractFactory):

    def create_product(self) -> ConcreteProduct:
        """
        Create concrete product.

        Returns:
            Concrete product from factory B.
        """
        return ConcreteProduct(title=FACTORY_B_PRODUCT)

    def create_another_product(self) -> AnotherConcreteProductB:
        """
        Create another concrete product B.

        Returns:
            Concrete another product from factory B.
        """
        return AnotherConcreteProductB(title=FACTORY_B_ANOTHER_PRODUCT)


class TestAbstractFactory:

    """
    Tests for Abstract factory pattern.
    """

    concrete_factory_a: ConcreteFactoryA = ConcreteFactoryA()
    concrete_factory_b: ConcreteFactoryB = ConcreteFactoryB()

    concrete_product: ConcreteProduct = ConcreteProduct(
        title=CONCRETE_PRODUCT
    )

    def test_factories_inheritance(self) -> None:
        """
        Test factories is subclass of AbstractFactory.
        """
        assert isinstance(self.concrete_factory_a, AbstractFactory)
        assert isinstance(self.concrete_factory_b, AbstractFactory)

    def test_product_inheritance(self) -> None:
        """
        Test concrete_product is subclass of AbstractProduct.
        """
        assert isinstance(self.concrete_product, AbstractProduct)

    def test_output_product_type(self) -> None:
        """
        Test create_product method for returning AbstractProduct
        subclass.
        """
        assert isinstance(
            self.concrete_factory_a.create_product(),
            AbstractProduct,
        )
        assert isinstance(
            self.concrete_factory_b.create_product(),
            AbstractProduct,
        )

    def test_factories_products(self) -> None:
        """
        Test create_product method for returning correct products.
        """
        assert self.concrete_factory_a.create_product().__str__() \
            == FACTORY_A_PRODUCT
        assert self.concrete_factory_b.create_product().__str__() \
            == FACTORY_B_PRODUCT

    def test_factories_another_products(self) -> None:
        """
        Test create_another_product methods with different products.
        """
        assert self.concrete_factory_a.create_another_product().__str__() \
            == FACTORY_A_ANOTHER_PRODUCT
        assert self.concrete_factory_b.create_another_product().__str__() \
            == FACTORY_B_ANOTHER_PRODUCT

    def test_factories_another_products_types(self) -> None:
        """
        Test create_another_product methods returning type of product.
        """
        assert isinstance(
            self.concrete_factory_a.create_another_product(),
            AnotherConcreteProductA
        )
        assert isinstance(
            self.concrete_factory_b.create_another_product(),
            AnotherConcreteProductB
        )
        assert not isinstance(
            self.concrete_factory_a.create_another_product(),
            AnotherConcreteProductB
        )
        assert not isinstance(
            self.concrete_factory_b.create_another_product(),
            AnotherConcreteProductA
        )
