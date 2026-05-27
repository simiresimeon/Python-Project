from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    """Verify that the extract City function Works """
    # Test with standard adress
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    # Test with Double word city
    assert extract_city("123 Ocean View Dr, Los Angeles, CA 90001") == "Los Angeles"
    # Test with extra White space
    assert extract_city(" 789 Mountain Way, Denver, CO 80202 ") == "Denver"


def test_extract_state():
    """Verify that the extract_state function Works """
    #te
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("123 Ocean View Dr, Los Angeles, CA 90001") == "CA"
    assert extract_state("789 Mountain Way, Denver, CO 80202") == "CO"


def test_extract_zipcode():
    """Verify that the extract_zipcode function Works """
    #te
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("123 Ocean View Dr, Los Angeles, CA 90001") == "90001"
    assert extract_zipcode("789 Mountain Way, Denver, CO 80202") == "80202"


pytest.main(["-v", "--tb=line", "-rN", __file__])