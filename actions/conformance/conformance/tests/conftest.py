# Copyright (c) 2024 The OSCAL Compass Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Test fixtures."""

import os
import pytest  # type: ignore
import shutil
import tempfile
from typing import Generator, TypeVar

from conformance.tests.test_runner import ConformanceTestRunner  # type: ignore

T = TypeVar("T")
YieldFixture = Generator[T, None, None]

@pytest.fixture(scope="module")
def runner() -> ConformanceTestRunner:
    """Create a test runner."""
    root_cmd = os.getenv("CONFORMANCE_ENTRYPOINT")
    if not root_cmd:
        raise RuntimeError("CONFORMANCE_ENTRYPOINT environment variable is not set.")
    return ConformanceTestRunner(root_cmd)

@pytest.fixture(scope="function")
def tmp_dir() -> YieldFixture[str]:
    tmpdir = tempfile.mkdtemp(prefix="runner-test")
    yield tmpdir
    shutil.rmtree(tmpdir)
