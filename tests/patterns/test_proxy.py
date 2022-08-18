from algorithms_cheat_sheet.patterns.structural import (
    AbstractSubject,
    Proxy,
)

from base64 import b64decode
from typing import Optional


class TestProxy:

    """
    Tests for Proxy pattern.
    """

    TEST_SUBJECT: str = "Test Value"

    proxy: Proxy = Proxy(subject_title=TEST_SUBJECT)

    def test_interface(self) -> None:
        """
        Test proxy is inherited from AbstractSubject.
        """

        assert isinstance(self.proxy, AbstractSubject)

    def test_asbtract_subject_inheritance(self) -> None:
        """
        Test that controled object doesn't initialized yet.
        """
        assert isinstance(self.proxy, AbstractSubject)

    def test_real_object_not_initialized(self) -> None:
        """
        Test that controled object doesn't initialized yet.
        """
        assert self.proxy._real_subject is None

    def test_expensive_action_and_data(self) -> None:
        """
        Test that controled object initialized after
        calling proxy expensive_action method.
        """
        proxy_data: Optional[bytes] = self.proxy.data()
        assert proxy_data is None
        self.proxy.expensive_action()
        assert self.proxy._real_subject is not None
        assert isinstance(self.proxy._real_subject, AbstractSubject)
        proxy_data = self.proxy.data()
        if isinstance(proxy_data, bytes):
            bytes_decoded: bytes = b64decode(proxy_data)
            assert bytes_decoded.decode() == self.TEST_SUBJECT

    def test_no_data(self) -> None:
        """
        Test that there's no data without calling expensive_action.
        """
        another_proxy: Proxy = Proxy(subject_title=self.TEST_SUBJECT)

        assert another_proxy._real_subject is None

        another_proxy_data: Optional[bytes] = another_proxy.data()
        assert another_proxy_data is None
