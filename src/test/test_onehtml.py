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
        self.img_srcs = [
            'responsesContactReport.png',
            'webNav.png',
            'createCMFClassic.png',
            'instructionsCreate.png',
            'noSubTabMAX.png',
            'createAsEdit.png',
            'editCMFClassic.png',
            'pageCrash.png',
            'makeFieldRequired.png',
            'correctEditForm.png'
        ]
        self.images = {
            'png': {
                Path(__file__).parent / 'sample/correctEditForm.png',
                Path(__file__).parent / 'sample/createAsEdit.png',
                Path(__file__).parent / 'sample/createCMFClassic.png',
                Path(__file__).parent / 'sample/editCMFClassic.png',
                Path(__file__).parent / 'sample/instructionsCreate.png',
                Path(__file__).parent / 'sample/makeFieldRequired.png',
                Path(__file__).parent / 'sample/noSubTabMAX.png',
                Path(__file__).parent / 'sample/pageCrash.png',
                Path(__file__).parent / 'sample/responsesContactReport.png',
                Path(__file__).parent / 'sample/webNav.png'
            },
            'jpg': set()
        }

    def test_get_all_imgs_from_folder(self):
        self.assertEqual(onehtml.get_all_images_in_folder(self.sample_base_path), self.images)
        self.assertEqual(onehtml.get_all_images_in_folder(self.sample_base_path.as_posix()), self.images)
        with self.assertRaises(TypeError):
            onehtml.get_all_images_in_folder(self.target_html)

    def test_find_all_img_paths(self):
        with self.assertRaises(TypeError):
            onehtml.find_all_img_paths_in_html(self.sample_base_path)
        self.assertEqual(onehtml.find_all_img_paths_in_html(self.target_html), self.img_srcs)

    def test_get_dict_from_img_paths(self):
        self.assertEqual(onehtml.get_dict_of_img_paths(self.img_srcs, self.sample_base_path), self.images)

    def test_get_all_imgs_from_html(self):
        with self.assertRaises(TypeError):
            onehtml.get_all_images_from_html(self.sample_base_path)
        self.assertEqual(onehtml.get_all_images_from_html(self.target_html), self.images)
        

if __name__ == '__main__':
    unittest.main()