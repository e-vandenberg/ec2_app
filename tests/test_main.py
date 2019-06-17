import os
import tempfile
import sys
import pytest

sys.path.append('../')
from ec2 import main

@pytest.fixture
def client():
    main.app.config['TESTING'] = True
    client = main.app.test_client()
    yield client

@pytest.mark.parametrize(
        'num', [
            (2014),
            (-14),
            (3)
        ],
    )
def test_math(client, num):
    t = client.post('/math', data=dict(
        num=num
    ), follow_redirects=True)

    assert str(num * 10 + 3) in t.data
