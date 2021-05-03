from flask import request, jsonify
import index


def test_api_sample():
    with index.app.test_client() as c:
        print("Start Test")
        rv = c.get('/api/sample', json={
            'hey': 'dummy request body'
        })
        json_data = rv.get_json()
        assert 'day_of_year' in json_data
        assert json_data['day_of_year'] > 0


