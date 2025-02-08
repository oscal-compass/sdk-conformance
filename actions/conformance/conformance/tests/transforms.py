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

"""Example test."""

import pathlib

from trestle.common.model_utils import ModelUtils
from trestle.oscal.assessment_plan import AssessmentPlan

from conformance.tests.test_runner import ConformanceTestRunner  # type: ignore

parent_path = pathlib.Path(__file__).parent.resolve()
input_component_path = parent_path / "data/component-definitions/example/component-definition.json"
expected_plan_path = parent_path / "data/assessment-plans/example/assessment-plan.json"

def test_component_definition_to_ap(runner: ConformanceTestRunner, tmp_dir: str) -> None:
    """This is an testing example."""
    tmp_dir_path = pathlib.Path(tmp_dir)
    runner.invoke_command(
        ["cd-to-app", "--compdef", input_component_path, "--output", "assessment-plan.json"],
        tmp_dir_path
    )

    # Load expected
    expected_plan = AssessmentPlan.oscal_read(expected_plan_path)
    # Load got
    output_plan_path = tmp_dir_path.joinpath("assessment-plan.json")
    got_plan = AssessmentPlan.oscal_read(output_plan_path)

    assert ModelUtils.models_are_equivalent(
                expected_plan,
                output_plan_path,
                ignore_all_uuid=True,
    )
