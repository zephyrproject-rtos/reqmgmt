# Invoke is broken on Python 3.11
# https://github.com/pyinvoke/invoke/issues/833#issuecomment-1293148106
import inspect
import os
import re
import sys
from enum import Enum
from typing import Optional

if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec

import invoke  # pylint: disable=wrong-import-position
from invoke import task  # pylint: disable=wrong-import-position

# Specifying encoding because Windows crashes otherwise when running Invoke
# tasks below:
# UnicodeEncodeError: 'charmap' codec can't encode character '\ufffd'
# in position 16: character maps to <undefined>
# People say, it might also be possible to export PYTHONIOENCODING=utf8 but this
# seems to work.
# FIXME: If you are a Windows user and expert, please advise on how to do this
# properly.
sys.stdout = open(  # pylint: disable=consider-using-with
    1, "w", encoding="utf-8", closefd=False, buffering=1
)


def run_invoke(
    context,
    cmd,
    environment: Optional[dict] = None,
    warn: bool = False,
) -> invoke.runners.Result:
    def one_line_command(string):
        return re.sub("\\s+", " ", string).strip()

    return context.run(
        one_line_command(cmd),
        env=environment,
        hide=False,
        warn=warn,
        pty=False,
        echo=True,
    )


@task()
def import_excel(context, path_to_excel):
    """
    This task calls into a Python script that was used to import the Zephyr
    requirements from the original Excel table.
    Keeping it around for some time in case if someone would want to
    reproduce the import.
    """
    assert os.path.isfile(path_to_excel)
    clean_command = f"""
        python tools/import_zephyr_from_excel.py "{path_to_excel}"
    """
    run_invoke(context, clean_command)


@task()
def html(context):
    """
    This task can be used as a simple shortcut to generate the static HTML export.
    """
    run_invoke(context, """
        strictdoc export .
    """)


@task()
def server(context):
    """
    This task can be used as a simple shortcut to start StrictDoc's web server.
    """
    run_invoke(context, """
        strictdoc server .
    """)
