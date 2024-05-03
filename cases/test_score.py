import pytest
from requests import request
from lxml import etree
from constants import Constants
import allure

''' positive test cases
    1. name is String and not empty/None
    2. email is String and format is correct
    3. role is in the enumeration range
    4. score is in [0,100]
'''


@allure.step("Positive test cases")
@pytest.mark.parametrize("name,email", [("Tom", "tom@gmail.com")])
@pytest.mark.parametrize("score,role", [(0, "Teacher"), (1, "Student"), (100, "Helper")])
def test_score_valid(name, email, score, role):
    url = Constants.Base_URL
    json = {
        "name": "",
        "email": "",
        "score": -1,
        "role": ""
    }

    resp = request(method="POST", url=url, json=json)
    assert resp.status_code == 200
    html = etree.HTML(resp.content.decode("utf-8"))
    h2 = html.xpath("//h2/text()")[0]
    assert h2 == Constants.HEAD_CONTENT
    # resp_name = html.xpath("//p[1]/text()")
    # assert resp_name == name
    # print(resp.content)


'''negative test cases: duplicate input
    send request with the same input twice
    
'''


@allure.step("Negative test cases: duplicate input")
@pytest.mark.parametrize("name,email,score,role", [("Tom", "tom@gmail.com", 0, "Helper"),
                                                   ("Tom", "tom@gmail.com", 0, "Helper")])
def test_score_valid(name, email, score, role):
    url = Constants.Base_URL
    json = {
        "name": "",
        "email": "",
        "score": -1,
        "role": ""
    }

    resp = request(method="POST", url=url, json=json)
    assert resp.status_code == 200
    html = etree.HTML(resp.content.decode("utf-8"))
    h2 = html.xpath("//h2/text()")[0]
    assert h2 == Constants.HEAD_CONTENT
    # resp_name = html.xpath("//p[1]/text()")
    # assert resp_name == name
    # print(resp.content)


'''negative test cases
   1. role is empty/None
   2. role is out of enumeration range 
   3. role is not a string:
        1. Number
        2. List
        3. Set
        4. Tuple
        5. Dictionary
'''


@allure.step("Negative test cases: invalid role")
@pytest.mark.parametrize("name,email,score", [("Tom", "tom@gmail.com", 100)])
@pytest.mark.parametrize("role", [None, "", "Professor", 12, [1, 2], (1, 2), {"name": 1}, {1, 2}])
def test_score_invalid_role(name, email, score, role):
    url = Constants.Base_URL
    json = {
        "name": name,
        "email": email,
        "score": score,
        "role": role
    }

    resp = request(method="POST", url=url, json=json)
    # print(resp.content)
    # assert resp.status_code == 404


'''negative test cases: invalid score
   1. score is None
   1. score is less than 0
   2. score is larger than 100
   3. score is not a Number(int):  
        1. Number(float)
        2. Number(bool)  
        3. String
        4. Set
        5. Dictionary
        6. Tuple
        7. List   
'''


@allure.step("Negative test cases: invalid score")
@pytest.mark.parametrize("name,email,role", [("Tom", "tom@gmail.com", "Teacher")])
@pytest.mark.parametrize("score", [None, -1, 101, 3.04, True, "12", {"score": 1}, (1, 2), [1, 2], {1, 2}])
def test_score_invalid_score(name, email, score, role):
    url = Constants.Base_URL
    json = {
        "name": name,
        "email": email,
        "score": score,
        "role": role
    }

    resp = request(method="POST", url=url, json=json)
    # print(resp.content)
    # assert resp.status_code == 404


''' negative test cases: invalid email
    1. email is empty/None
    2. email does not match format: one @ in the middle of a string
        1. starts with @
        2. ends with @
        3. 2 @ in the middle
    3. email is not a String:
        1. Number
        2. Set
        3. Dictionary
        4. Tuple
        5. List
'''


@allure.step("Negative test cases: invalid email")
@pytest.mark.parametrize("name,score,role", [("Tom", 99, "Teacher")])
@pytest.mark.parametrize("email", ["", None, "@123", "123@", "1@@3", 123, {"email": 1}, (1, 2), [1, 2], {1, 2}])
def test_score_invalid_email(name, email, score, role):
    url = Constants.Base_URL
    json = {
        "name": name,
        "email": email,
        "score": score,
        "role": role
    }

    resp = request(method="POST", url=url, json=json)
    # print(resp.content)
    # assert resp.status_code == 404


''' 
    negative test cases: name is invalid
    1. Name is empty/None
    1. Name is not a String:
        1. Number
        2. Tuple
        3. Set
        4. Dictionary
        5. List
'''


@allure.step("Negative test cases: invalid name")
@pytest.mark.parametrize("email,score,role", [("tom@gmail.com", 99, "Teacher")])
@pytest.mark.parametrize("name", ["", None, 123, (1, 2), {"key": 2}, [1, 2], {1, 2}])
def test_score_invalid_name(name, email, score, role):
    url = Constants.Base_URL
    json = {
        "name": name,
        "email": email,
        "score": score,
        "role": role
    }

    resp = request(method="POST", url=url, json=json)
    # print(resp.content)
    # assert resp.status_code == 404
