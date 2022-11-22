# install json2xml:  pip install json2xml
# https://pypi.org/project/json2xml/

def json2xml(request):

    # get the xml from an URL that return json
    data = readfromurl("https://coderwall.com/vinitcool76.json")

    json_data = {
        "id": 26077,
        "username": "vinitcool76",
        "name": "Vinit Kumar",
        "location": "Pune, India",
        "karma": 1136,
        "accounts": {
            "github": "vinitkumar",
            "twitter": "vinitkme"
        }
    }

    print(json2xml.Json2xml(json_data).to_xml())

    # get the xml from a json string
    data = readfromstring(
        '{"login":"mojombo","id":1,"avatar_url":"https://avatars0.githubusercontent.com/u/1?v=4"}'
    )
    print(json2xml.Json2xml(data).to_xml())

    # get the data from an URL
    data = readfromjson("examples/licht.json")
    print(json2xml.Json2xml(data).to_xml())
    return HttpResponse('xml generated!')
