from pathlib import Path
import subprocess
import os


scripts_dir = Path(__file__).parent.resolve() / "scripts"


def test_run_save_stage():
    env = os.environ
    env["LAMIN_TESTING"] = "true"

    filepath = scripts_dir / "initialized.py"
    # attempt to save the script without it yet being run
    # lamin save sub/lamin-cli/tests/scripts/initialized.py
    result = subprocess.run(
        f"lamin save {str(filepath)}",
        shell=True,
        capture_output=True,
    )
    print(result.stdout.decode())
    assert result.returncode == 1
    assert "Did you run ln.track()" in result.stdout.decode()

    # python sub/lamin-cli/tests/scripts/initialized.py
    result = subprocess.run(
        f"python {str(filepath)}",
        shell=True,
        capture_output=True,
    )
    print(result.stdout.decode())
    assert result.returncode == 0
    assert "saved: Transform" in result.stdout.decode()

    # save the script
    # lamin save sub/lamin-cli/tests/scripts/initialized.py
    result = subprocess.run(
        f"lamin save {str(filepath)}",
        shell=True,
        capture_output=True,
    )
    print(result.stdout.decode())
    assert result.returncode == 0
    assert "saved transform" in result.stdout.decode()
    assert filepath.exists()  # test that it's not cleaned out!

    # python sub/lamin-cli/tests/scripts/initialized.py
    # now, trying to run the same thing again will error
    result = subprocess.run(
        f"python {str(filepath)}",
        shell=True,
        capture_output=True,
        env=env,
    )
    print(result.stdout.decode())
    assert result.returncode == 1
    assert "Please update your transform settings as follows" in result.stdout.decode()

    result = subprocess.run(
        "lamin stage 'transform m5uCHTTpJnjQ5zKv'",
        shell=True,
        capture_output=True,
    )
    assert result.returncode == 0
