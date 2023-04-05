import pytest

from pybites_246 import print_workout_days


def test_print_workout_days_no_workout(capsys: pytest.CaptureFixture[str]):
    
    print_workout_days('no workout')
    captured = capsys.readouterr()
    assert captured.out.strip() == "No matching workout"

@pytest.mark.parametrize("workout, expected_print", [
    ("upper", "Mon, Thu"),
    ("lower", "Tue, Fri"),
    ("cardio", "Wed"),
])
def test_print_workout_days_when_workout_is_fount(workout: str, expected_print: str, capsys: pytest.CaptureFixture[str]):

    print_workout_days(workout)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_print