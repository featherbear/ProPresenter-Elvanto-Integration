import ElvantoAPIExtensions

class settings:
    import configparser
    import os
    import sys

    _configFilePath = "config.ini"
    _config = configparser.ConfigParser()

    if not os.path.exists(_configFilePath):
        _config.add_section("config")
        _config.set("config","api_key", "")
        with open(_configFilePath, "w") as _configFile:
            _config.write(_configFile)
        print("Created '%s'. Please enter in your API key to continue. Exiting" % _configFilePath)
        sys.exit()
    elif not os.path.isfile(_configFilePath):
        raise Exception(_configFilePath + " is not a file! Aborting")
    _config.read(_configFilePath)
    api_key = _config.get("config","api_key")

api = ElvantoAPIExtensions.ElvantoAPI.Connection(APIKey = settings.api_key)

import datetime
date_today = datetime.date.today()
date_service = date_today + datetime.timedelta( (6 - date_today.weekday()) % 7 )

"""
API Request :: services/getAll
start | YYYY-MM-DD
end   | YYYY-MM-DD
page_size | int | minimum page size is 10
"""
services = api._Post("services/getAll", page_size = 10, start = str(date_service-datetime.timedelta(1)), end = str(date_service+datetime.timedelta(1)), fields = ["plans", "volunteers", "songs"])
"""
songs | only useful if songs are attached
can extract songs from plans item
"""

if services["status"] == "fail":
    raise Exception("Could not retrieve any details for the upcoming Sunday service")
services = services["services"]["service"]

for service in services:
    print("ID", service["id"])
    print("Name", service["name"])
    print("Date", service["date"])
    print("Type", service["service_type"]["id"], service["service_type"]["name"])
    print("Location", service["location"]["id"], service["location"]["name"])

    print("Songs", service["songs"])

    roles = service["volunteers"]["plan"][0]["positions"]["position"]
    for role in roles:
        """
        department_name
        sub_department_name
        position_name
        volunteers["volunteer"] {
          "person" | (firstname || preferred_name), lastname
          "status" | str
        }
        """

    plan = service["plans"]["plan"][0]
    planItems = plan["items"]["item"]
    for item in planItems:
        """
        id
        heading
        duration
        title
        song
        description
        """
        # Item is a header if (item["heading"] == 1)
        pass

    print()

    # service_length; service_length_formatted
    # total_length; total_length_formatted ????

    # id, name, date, service_type[id,name], location[id,name]
