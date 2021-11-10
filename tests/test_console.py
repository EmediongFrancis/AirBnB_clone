#!/usr/bin/python3
"""
    Unit tests for console.py
"""
import unittest
from console import HBNBCommand
import io
from datetime import datetime
from os import path, remove
from models.base_model import BaseModel
from unittest.mock import patch
