# Copyright (c) 2024 Braid Technologies Ltd

# Standard Library Imports
import pytest
import os
import shutil
import sys
import logging

test_root = os.path.dirname(__file__)
parent= os.path.abspath(os.path.join(test_root, '..'))
src_dir = os.path.join(parent, 'src')
sys.path.extend([parent, src_dir])

# Set up logging to display information about the execution of the script
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.DEBUG)
from src.embedder import Embedder
from src.html_file_downloader import HtmlFileDownloader

# Fixture to create a temporary directory for test output
@pytest.fixture
def test_output_dir(tmpdir):
    dir_path = tmpdir.mkdir("test_output")
    logger.info(f"Created temporary test output directory: {dir_path}")
    yield str(dir_path)
    # Clean up after the test
    logger.info(f"Cleaning up test output directory: {dir_path}")
    shutil.rmtree(str(dir_path))

def test_basic ():
    test_path = 'test'
    test_output_location = 'test_output'
    test_text = "This is some text"

    embedder = Embedder (test_path, test_text, test_output_location)
    assert embedder.path == test_path  
    assert embedder.text == test_text 

def test_with_output (test_output_dir):
    test_root = os.path.dirname(__file__)
    os.chdir (test_root)
    test_path = 'simple_test.html'
    test_output_location = 'test_output'
    downloader = HtmlFileDownloader (test_path, test_output_location)
    text = downloader.download () 

    embedder = Embedder (test_path, text, test_output_location)
    embedding = embedder.embed ()    
    assert len(embedding) > 0