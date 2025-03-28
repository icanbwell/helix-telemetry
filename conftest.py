from typing import Generator, Any

import pytest

from helixtelemetry.telemetry.register import register


@pytest.fixture(scope="session", autouse=True)
def run_before_each_test() -> Generator[None, Any, None]:
    # This code will run before every test
    # print("Setting up something before each test")
    # You can do setup operations here
    # For example, initializing databases, clearing caches, etc.
    register()

    # Optional: You can yield if you want to do tear down after the test
    yield

    # Optional teardown code here
    print("Cleaning up after each test")
