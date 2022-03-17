import base64
from pathlib import Path
import re
from typing import Set, Dict, List, Iterator, Tuple

ImgPathDict = Dict[Set[Path], Set[Path]]

class onehtml:
    @staticmethod
    def get_all_images_in_folder(folder: Path | str) -> ImgPathDict:
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
    def convert_local_imgs_to_base64(image_paths: Set[Path]) -> Iterator[Tuple[Path, str]]:
        for image_path in image_paths:
            with image_path.open('rb') as image:
                image_data = image.read()
                base64_encoded_data = base64.b64encode(image_data)
                base64_string = base64_encoded_data.decode('utf-8')
                yield (image_path, base64_string)



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
    def get_dict_of_img_paths(img_paths: List[str], base_path: Path) -> ImgPathDict:
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
    def get_all_images_from_html(cls, file_path: Path | str) -> ImgPathDict:
        matches: List[str] = cls.find_all_img_paths_in_html(file_path)
        return_dict = cls.get_dict_of_img_paths(matches, file_path.parent.resolve())
        return return_dict


def main():
    x = onehtml.get_all_images_from_html(Path(__file__).parent / 'test/sample/notes.html')
    y = onehtml.convert_local_imgs_to_base64(x['png'])
    for item in y:
        print(item[0].name, len(item[1]))


if __name__ == '__main__':
    main()