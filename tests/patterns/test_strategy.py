from algorithms_cheat_sheet.patterns.behavioral import (
    AbstractContext,
    AbstractStrategy,
)


class ConcreteContext(AbstractContext):
    pass


class ConcreteStrategyA(AbstractStrategy):
    pass


class ConcreteStrategyB(AbstractStrategy):
    pass


class ConcreteStrategyC(AbstractStrategy):
    pass


class TestStrategy:

    """
    Tests for Strategy pattern.
    """

    context: ConcreteContext = ConcreteContext()

    def test_context_inheritance(self) -> None:
        """
        Test context is inherited from AbstractContext.
        """
        assert isinstance(self.context, AbstractContext)

    def test_strategy_inheritance(self) -> None:
        """
        Test strategy is inherited from AbstractStrategy.
        """
        assert isinstance(ConcreteStrategyA(), AbstractStrategy)
        assert isinstance(ConcreteStrategyB(), AbstractStrategy)
        assert isinstance(ConcreteStrategyC(), AbstractStrategy)

    def test_context_actions(self) -> None:
        """
        Test strategy is called and has correct output.
        """
        assert self.context.action(ConcreteStrategyA()) \
            == ConcreteStrategyA.__name__
        assert self.context.action(ConcreteStrategyB()) \
            == ConcreteStrategyB.__name__
        assert self.context.action(ConcreteStrategyC()) \
            == ConcreteStrategyC.__name__
