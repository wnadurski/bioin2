import unittest

import mock as mock

import handlers


class SomeTests(unittest.TestCase):
    def test_global_with_inputs(self):
        with mock.patch('handlers.get_command') as fake_get_command:
            fake_get_command.return_value = "1"

            with mock.patch('handlers.get_input') as fake_get_input:
                fake_get_input.side_effect = ["inputs/lilium.fna",
                                              "inputs/thalian.fna",
                                              "inputs/matrix1.txt"]

                handlers.global_alignment()

    def test_local_with_inputs(self):
        with mock.patch('handlers.get_command') as fake_get_command:
            fake_get_command.return_value = "1"

            with mock.patch('handlers.get_input') as fake_get_input:
                fake_get_input.side_effect = ["inputs/lilium.fna",
                                              "inputs/thalian.fna",
                                              "inputs/matrix1.txt"]

                handlers.local_alignment()

    def test_global_with_mrna(self):
        with mock.patch('handlers.get_command') as fake_get_command:
            fake_get_command.return_value = "2"

            with mock.patch('handlers.get_input') as fake_get_input:
                fake_get_input.side_effect = ["inputs/lilium.fna",
                                              "inputs/thalian.fna",
                                              "inputs/blosum.txt"]

                handlers.global_alignment()
