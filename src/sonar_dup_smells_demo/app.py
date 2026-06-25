from .module_01 import Processor01
from .module_02 import Processor02


def run_demo():
    processor = Processor01()
    other = Processor02()
    rows = [{"name": "a", "amount": 10, "status": "new"}]
    return processor.build_report(rows) + other.normalize_status("open")
