import base64
from pathlib import Path
import re
from typing import Dict

class onehtml:
    @staticmethod
    def get_all_images_in_folder(folder: Path) -> Dict[Path, Path]:
        """
        Return a dictionary containing two lists of paths: one for png files and one for jpg/jpeg.
        """
        raise NotImplementedError

