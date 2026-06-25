from sonar_dup_smells_demo.module_01 import Processor01


def test_normalize_status_open():
    assert Processor01().normalize_status("open") == "OPEN"


def test_build_report():
    assert "alice" in Processor01().build_report([{"name": "alice", "amount": 1, "status": "new"}])
