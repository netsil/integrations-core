# (C) Datadog, Inc. 2010-2016
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

# stdlib
import os
from nose.plugins.attrib import attr

# 3p

# project
from tests.checks.common import AgentCheckTest, Fixtures

FIXTURE_DIR = os.path.join(os.path.dirname(__file__), 'ci')

instance = {
    'host': 'localhost',
    'port': 26379,
    'password': 'datadog-is-devops-best-friend'
}


# NOTE: Feel free to declare multiple test classes if needed

@attr(requires='ecs')
class TestEcs(AgentCheckTest):
    """Basic Test for ecs integration."""
    CHECK_NAME = 'ecs'

    def test_check(self):
        """
        Testing Ecs check.
        """
        self.load_check({}, {})

        # run your actual tests...

        self.assertTrue(True)
        # Raises when COVERAGE=true and coverage < 100%
        self.coverage_report()
