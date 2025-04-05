# connector-sample-connector

FortiSOAR sample connector
Sample connector to provide developer tutorials.

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
^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b$
```

Matching cases

```text
https://www.test.com
https://test.com

http://www.test.com
http://test.com
http://username:password@example.com
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
