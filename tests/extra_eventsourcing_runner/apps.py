# -*- coding: utf-8 -*-
import eventsourcing.system
from django.apps import AppConfig
from eventsourcing.tests.application import BankAccounts

from tests.emails.application import FormalEmailProcess, InformalEmailProcess


class ExtraEventSourcingSystemRunnerConfig(AppConfig):
    name = "tests.extra_eventsourcing_runner"
    the_runner: eventsourcing.system.Runner

    def ready(self) -> None:
        self.make_runner()

    def make_runner(self) -> eventsourcing.system.Runner:
        self.the_runner = eventsourcing.system.SingleThreadedRunner(
            eventsourcing.system.System(
                [
                    [BankAccounts, FormalEmailProcess],
                    [BankAccounts, InformalEmailProcess],
                ]
            )
        )
        return self.the_runner
