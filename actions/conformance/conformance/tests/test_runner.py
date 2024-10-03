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

"""Test runners for test suite"""

import pathlib
import subprocess
from typing import List, Optional, Tuple


class ConformanceTestRunner:
    """Class to run test suite."""

    def __init__(self, root_cmd: str) -> None:
        """Initialize the class."""
        self.root_cmd = root_cmd

    def invoke_command(
        self, args: List[str], working_dir: Optional[pathlib.Path] = None
    ) -> Tuple[int, str, str]:
        """
        Invoke a command for test

        Args:
            args List(str): Arguments to run with root command in the shell

        Returns:
            Tuple[int, str]: Return code, stdout, stderr of the command
        """
        command: List[str] = [self.root_cmd]
        command.extend(args)
        result = subprocess.run(
            command,
            cwd=working_dir,
            capture_output=True
        )
        return (
            result.returncode,
            result.stdout.decode("utf-8"),
            result.stderr.decode("utf-8"),
        )
