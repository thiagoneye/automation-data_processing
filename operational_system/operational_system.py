"""
Operational System

This class allows performing operations on the operating system.
"""

# Imports

import os


# Classes

class OperationalSystem:
    """
    Operational System
    """

    def __init__(self, path):
        self._data_files = []

        self.file_mapping(path)

    def file_mapping(self, path):
        """
        Mapping of files in a directory.
        """
        for directory, _, files in os.walk(path):
            for file in files:
                self._data_files.append(directory + '\\' + file)
                