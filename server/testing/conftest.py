#!/usr/bin/env python3
import pytest
from app import app
from models import db

def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))

@pytest.fixture(autouse=True, scope='function')
def setup_and_teardown():
    with app.app_context():
        db.create_all()
        yield
        db.session.remove()
        db.drop_all()
