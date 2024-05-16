import unittest
from retailtree.retailtree import Annotation, RetailTree
import json


class TestAnnotation(unittest.TestCase):

    def setUp(self):
        # Build tree before every test case
        file_path = './tests/test_data/test_data.json'
        file_path_output = './tests/test_data/tblr_output.json'
        # Annotations data2
        with open(file_path, 'r') as file:
            self.annotation_data_json = json.load(file)

        with open(file_path_output, 'r') as file:
            self.annotation_output_data = json.load(file)

        self.RT = RetailTree()
        for data in self.annotation_data_json:
            ann = Annotation(data['id'], data['x_min'],
                             data['y_min'], data['x_max'], data['y_max'])
            self.RT.add_annotation(ann)

        self.RT.build_tree()
        self.assertIsNotNone(self.RT.tree)

    def test_tblr_0(self):
        self.assertEqual(self.RT.TBLR(
            id=0, radius=2), self.annotation_output_data[0])

    def test_tblr_1(self):
        self.assertEqual(self.RT.TBLR(
            id=1, radius=2), self.annotation_output_data[1])

    def test_tblr_2(self):
        self.assertEqual(self.RT.TBLR(
            id=2, radius=2), self.annotation_output_data[2])

    def test_tblr_3(self):
        self.assertEqual(self.RT.TBLR(
            id=3, radius=2), self.annotation_output_data[3])

    def test_tblr_4(self):
        self.assertEqual(self.RT.TBLR(
            id=4, radius=2), self.annotation_output_data[4])

    def test_tblr_5(self):
        self.assertEqual(self.RT.TBLR(
            id=5, radius=2), self.annotation_output_data[5])

    def test_tblr_6(self):
        self.assertEqual(self.RT.TBLR(
            id=6, radius=2), self.annotation_output_data[6])

    def test_tblr_7(self):
        self.assertEqual(self.RT.TBLR(
            id=7, radius=2), self.annotation_output_data[7])

    def test_tblr_8(self):
        self.assertEqual(self.RT.TBLR(
            id=8, radius=2), self.annotation_output_data[8])

    def test_tblr_9(self):
        self.assertEqual(self.RT.TBLR(
            id=9, radius=2), self.annotation_output_data[9])


if __name__ == '__main__':
    unittest.main()
