import unittest
from pathlib import Path
import sys
try:
    from onehtml import onehtml
except ImportError:
    sys.path.append(Path(__file__).parent.parent.as_posix())
    from onehtml import onehtml

class TestOneHTML(unittest.TestCase):
    def setUp(self) -> None:
        self.sample_base_path = Path(__file__).parent / 'sample'
        self.target_html = Path(__file__).parent / 'sample/notes.html'

