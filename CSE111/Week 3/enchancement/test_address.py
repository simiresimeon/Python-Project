from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    #
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_city("123 Ocean View Dr, Los Angeles, CA 83460") == "CA"
    assert extract_city("789 Mountain Way, Denver, CO 80292") == "CO"

