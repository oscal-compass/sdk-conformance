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

import os
import sys
from pathlib import Path

import pytest  # type: ignore


def main() -> None:
    """Run tests"""
    workspace = os.getenv("GITHUB_ACTION_PATH")
    if not workspace:
        raise RuntimeError("GITHUB_ACTION_PATH environment variable is not set.")

    test_dir = Path(workspace).joinpath("conformance/tests")
    exit_code = pytest.main([str(test_dir)])

    if exit_code == 0:
        print("All tests passed!")
    else:
        print("One or more failures were found.")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
