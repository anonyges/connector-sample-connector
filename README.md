# connector-sample-connector

FortiSOAR sample connector
Sample connector to provide developer tutorials.

## Changelog

### Version 1.0.0

Something here!

## Regex for validations

### HTTP/HTTPS Full URL

Regex

```regex
^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)$
```

Matching cases

```text
https://www.test.com
https://test.com

http://www.test.com
http://test.com

https://test.com/123
https://test.com/123/456
http://username:password@example.com
```

References

- <https://stackoverflow.com/questions/3809401/what-is-a-good-regular-expression-to-match-a-url>

### HTTP/HTTPS Domain URL

Regex

```regex
^https?:\/\/(?:(?:(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9])|(?:(?:(?:(?!25?[6-9])[12]\d|[1-9])?\d\.?\b){4})|(?:(?:[a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*(?:[A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9]))(?::\d+)?$
```

Matching cases

```text
https://www.test.com
https://test.com
https://localhost

http://www.test.com
http://test.com
http://localhost


https://www.test.com:123
https://test.com:123
https://localhost:123

```

Not matching cases

```text
https://test.com/123
https://test.com/123/456
```

References

- <https://stackoverflow.com/questions/3809401/what-is-a-good-regular-expression-to-match-a-url>

### IPv4

Regex

```regex
^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$
```

Matching cases

```text
1.1.1.1
8.8.8.8
0.0.0.0
255.255.255.255
```

Not matching cases

```text
1111.1111.111.11
111.111.111.256
```

References

- <https://stackoverflow.com/questions/5284147/validating-ipv4-addresses-with-regexp>

## Tutorial for developing a sample connector

The connector essential needs the following files.

```text
connector-org-name/
├─ connector.py
├─ info.json
```

As for the connector.py needs the following class.

``` python
from connectors.core.connector import Connector

class BaseConnector(Connector):
    def execute(self, config: dict, operation: str, params: dict, *args, **kwargs):
        pass
    def check_health(self, config: dict=None, *args, **kwargs):
        pass
```

As for the info.py needs the following information.

```json
{
    "name": "sample-connector",
    "version": "1.0.0",
    "label": "Sample Connector",
    ...
}
```

info.json contains the configuration and operations(actions).

When FortiSOAR executes the connector,

1. Integration(Playbook) Engine collects info.json data for connector.
2. Loads the configuration(credentials) from DB
3. Loads the operations by the name, inputs the fields
4. Gets the config, params from the info
5. Use the info.

```mermaid
zenuml
  title Get Connector Information

  @Actor User
  @ECS FortiSOAR
  group Connector {
    @Entity "info.json"
    @Entity "connector.py"
  }

  @Starter(User)
  // `GET /get_connector_info`
  FortiSOAR.get(config, params) {
    // `GET /get_info
    "info.json".get(config, params) {
      return "config, params"
    }
    return "data"
  }
```

```mermaid
zenuml
  title Connector Execute UML

  @Actor User
  @ECS FortiSOAR
  group Connector {
    @Entity <<Connector>> "info.json"
    @Entity <<Connector>> "connector.py"
  }
  
  @Starter(User)
  // `POST /api/integration/execute/?format=json`
  FortiSOAR.execute(config, operation, params) {
    "connector.py".execute(config, operation, params, params) {
      supported_operations(operation) {
        return result
      }
      return result
    }
    return result
  }
```

The connector.py must have Connector as a class and under Connector must have 2 functions which is as below.

- execute
- check_health