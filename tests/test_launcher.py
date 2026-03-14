from pathlib import Path

import launcher


def test_load_config_missing_file(tmp_path: Path) -> None:
    missing = tmp_path / "does_not_exist.json"
    try:
        launcher.load_config(missing)
    except launcher.ConfigError as error:
        assert "launcher_config.json" in str(error)
    else:
        raise AssertionError("Expected ConfigError")


def test_build_launch_command_with_direct_path(tmp_path: Path) -> None:
    fake_exec = tmp_path / "prismlauncher"
    fake_exec.write_text("#!/bin/sh\n", encoding="utf-8")

    config = {
        "launcher_command": str(fake_exec),
        "instance_name": "PackPrivado",
        "window_title": "Demo",
    }

    cmd = launcher.build_launch_command(config)
    assert cmd == [str(fake_exec), "--launch", "PackPrivado"]
