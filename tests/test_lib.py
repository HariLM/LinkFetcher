from app.lib import getAllLinks

def test_valid_url():
    data,error = getAllLinks("https://www.google.com")
    assert len(data) > 0
    assert error == ""

def test_empty_url_string():
    data,error = getAllLinks("")
    assert error == "URL_EMPTY"

def test_invalid_url():
    data,error = getAllLinks("htts://www.google.com")
    assert error == "URL_INVALID"

def test_connection_error():
    data,error = getAllLinks("https://www.asdaskdljasldk.com")
    assert error == "CONNECTION_ERROR"
