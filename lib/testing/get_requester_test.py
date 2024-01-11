from GetRequester import GetRequester


class GetRequesterTest:
    '''Class {Classname} in {modulename}.py'''


URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
JSON_STRING = b"[\n  {\n    \"name\": \"Daniel\",\n    \"occupation\": \"LG Fridge Salesman\"\n  },\n  {\n    \"name\": \"Joe\",\n    \"occupation\": \"WiFi Fixer\"\n  },\n  {\n    \"name\": \"Avi\",\n    \"occupation\": \"DJ\"\n  },\n  {\n    \"name\": \"Howard\",\n    \"occupation\": \"Mountain Legend\"\n  }\n]\n"
CONVERTED_DATA = [{'name': 'Daniel', 'occupation': 'LG Fridge Salesman'}, {'name': 'Joe', 'occupation': 'WiFi Fixer'}, {
    'name': 'Avi', 'occupation': 'DJ'}, {'name': 'Howard', 'occupation': 'Mountain Legend'}]


def test_get_response():
    '''get_response_body function returns response.'''
    requester = GetRequester(URL)
    expected_response = JSON_STRING.decode('utf-8')  # Decode bytes to string
    actual_response = requester.get_response_body()
    assert actual_response == expected_response


def test_load_json():
    '''load_json function returns response.'''
    requester = GetRequester(URL)
    assert (requester.load_json() == CONVERTED_DATA)
