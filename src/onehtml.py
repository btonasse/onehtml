import base64
from pathlib import Path
import re
from typing import Set, Dict, List


class onehtml:
    @staticmethod
    def get_all_images_in_folder(folder: Path | str) -> Dict[Set[Path], Set[Path]]:
        """
        Return a dictionary containing two lists of paths: one for png files and one for jpg/jpeg.
        """
        if isinstance(folder, str):
            folder = Path(folder)

        if not folder.is_dir():
            raise TypeError(f"{folder.as_posix()} is not a directory.")

        return_dict = {"png": set(), "jpg": set()}

        for item in folder.iterdir():
            if item.suffix == ".png":
                return_dict["png"].add(item)
            elif item.suffix in (".jpg", ".jpeg"):
                return_dict["jpg"].add(item)

        return return_dict

    @staticmethod
    def find_all_img_paths_in_html(file_path: Path | str) -> List[str]:
        if isinstance(file_path, str):
            file_path = Path(file_path)
        if not file_path.suffix in (".html", ".htm"):
            raise TypeError(f"{file_path.as_posix()} is not a HTML file.")

        img_tax_regex = re.compile(r"<img[^>]*src=\"([^\"]+)\"[^>]*>")
        with file_path.open(encoding="utf-8") as html:
            return re.findall(img_tax_regex, html.read())

    @staticmethod
    def get_dict_of_img_paths(
        img_paths: List[str], base_path: Path
    ) -> Dict[Set[Path], Set[Path]]:
        return_dict = {"png": set(), "jpg": set()}

        for item in img_paths:
            if not item.startswith("http"):
                if item.startswith("/"):
                    raise NotImplementedError("Need to implement domain-relative path")
                else:
                    if item.endswith(".png"):
                        return_dict["png"].add(Path(base_path) / Path(item))
                    elif item.endswith(".jpg") or item.endswith(".jpeg"):
                        return_dict["jpg"].add(Path(base_path) / Path(item))
            else:
                raise NotImplementedError("Need to implement http paths")
        return return_dict

    @classmethod
    def get_all_images_from_html(
        cls, file_path: Path | str
    ) -> Dict[Set[Path], Set[Path]]:
        matches: List[str] = cls.find_all_img_paths_in_html(file_path)
        return_dict = cls.get_dict_of_img_paths(matches, file_path.parent.resolve())
        return return_dict
