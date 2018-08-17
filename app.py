import ElvantoAPIExtensions
import propresenter.files as propresenter

if __name__ == "__main__":
    class settings:
        import configparser
        import os
        import sys

        _configFilePath = "config.ini"
        _config = configparser.ConfigParser()

        if not os.path.exists(_configFilePath):
            _config.add_section("config")
            _config.set("config", "api_key", "")
            with open(_configFilePath, "w") as _configFile:
                _config.write(_configFile)
            print("Created '%s'. Please enter in your API key to continue. Exiting" % _configFilePath)
            sys.exit()
        elif not os.path.isfile(_configFilePath):
            raise Exception(_configFilePath + " is not a file! Aborting")
        _config.read(_configFilePath)
        api_key = _config.get("config", "api_key")
    api = ElvantoAPIExtensions.ElvantoAPI.Connection(APIKey=settings.api_key)

def connect(apiKey):
    global api
    api = ElvantoAPIExtensions.ElvantoAPI.Connection(APIKey=apiKey)

# TODO check for valid auth

# Elvanto API access: read only
# ProPresenter access: read write
# connect("B9ZUjAhyquWEqtbPVfDmS8amltDTItnzV")
print('print(api.servicesUpcoming(locationName="Kingsgrove"))')
print(api.servicesUpcoming(locationName="Kingsgrove"))
print('print(propresenter.playlist.children)')
print(propresenter.playlist.children)

