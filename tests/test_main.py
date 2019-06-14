import os
import tempfile
import sys
import pytest

#sys.path.append('../')
import ec2.main

@pytest.fixture
def client():
    main.app.config['TESTING'] = True
    client = main.app.test_client()
    yield client
