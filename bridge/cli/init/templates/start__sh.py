template = """#!/usr/bin/env bash
gunicorn {app_path} -w "${{WEB_CONCURRENCY:-4}}"
"""


def start_sh_template(app_path: str) -> str:
    return template.format(app_path=app_path)
