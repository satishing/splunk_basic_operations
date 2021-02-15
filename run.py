import os
import sys
import pprint as pprint
from splunklib.binding import HTTPError, AuthenticationError

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
import splunklib.client as client


def _get_credentials():
    return {
        "host": os.getenv("SPLUNK_HOST", "localhost"),
        "port": int(os.getenv("SPLUNK_PORT", 8089)),
        "username": os.getenv("SPLUNK_USER", "admin"),
        "password": os.getenv("SPLUNK_PASSWORD", ""),
    }


def create_service():
    try:
        credentials = _get_credentials()
        service = client.connect(
            host=credentials.get("host"),
            port=credentials.get("port"),
            username=credentials.get("username"),
            password=credentials.get("password"),
            scheme="https", )
        return service
    except AuthenticationError as e:
        print("Login failed")
        raise e


def list_apps():
    service = create_service()
    print("List of available apps")
    for app in service.apps:
        print(app.name)
    service.logout()


def create_app(app_name):
    service = create_service()
    try:
        print(f"Creating app {app_name}")
        service.apps.create(app_name)
    except HTTPError as e:
        print(e)
    service.logout()


def delete_app(app_name):
    service = create_service()
    try:
        print(f"Deleting app {app_name}")
        service.apps.delete(app_name)
    except KeyError as e:
        print(e)
    service.logout()


def list_indexes():
    service = create_service()
    try:
        print("List of indexes")
        for index in service.indexes:
            print(index.name)
    except Exception as e:
        print(e)

    service.logout()


def create_index(index_name):
    service = create_service()
    try:
        print(f"Creating index {index_name}")
        service.indexes.create(index_name)
    except HTTPError as e:
        print(e)
    service.logout()


def delete_index(index_name):
    service = create_service()
    try:
        print(f"Deleting index {index_name}")
        service.indexes.delete(index_name)
    except HTTPError as e:
        print(e)
    service.logout()


def get_all_index_content():
    service = create_service()
    indexes = service.indexes
    for index in indexes:
        print (f"\n ------- {index.name} --------")
        print(index.content)
    service.logout()


def get_index_content(index_name):
    service = create_service()
    indexes = service.indexes
    for index in indexes:
        if index.name == index_name:
            print (f"\n ------- {index.name} --------")
            pprint.pprint(index.content)
    service.logout()


if __name__ == "__main__":
    print("\n")
    create_app("abc")

    print("\n")
    list_apps()

    print("\n")
    delete_app("abc")

    print("\n")
    create_index("xyz")

    print("\n")
    list_indexes()

    print("\n")
    delete_index("xyz")

    print("\n")
    get_all_index_content()

    print("\n")
    get_index_content("main")

