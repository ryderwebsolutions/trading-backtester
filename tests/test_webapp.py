import importlib
import pytest

def test_webapp_import():
    # ensure the webapp script can be imported without errors if streamlit
    # is present; otherwise skip.
    try:
        import streamlit  # type: ignore
    except ImportError:
        pytest.skip("streamlit not installed, skipping webapp import test")

    spec = importlib.util.spec_from_file_location("webapp.app", "webapp/app.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert hasattr(module, 'st')  # streamlit should be imported
