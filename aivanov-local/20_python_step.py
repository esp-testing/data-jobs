# Copyright 2021 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0
import logging

from vdk.api.job_input import IJobInput

log = logging.getLogger(__name__)


def run(job_input: IJobInput):
    """
    Function named `run` is required in order for a python script to be recognized as a Data Job Python step and executed.

    VDK provides to every python step an object - job_input - that has methods for:

    * executing queries to OLAP Database;
    * ingesting data into a database;
    * processing data into a database.
    See IJobInput documentation for more details.
    """
    log.info(f"Starting job step {__name__}")
    import time
    sleep_seconds = job_input.get_arguments().get("sleep", 100)
    for i in range(sleep_seconds // 10):
        time.sleep(10)
        log.info("Slept for 10 seconds")
    log.info("Done")