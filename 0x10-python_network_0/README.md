# 0x10. Python - Network #0

## Table of Contents
- [URL (Uniform Resource Locator)](#url)
- [HTTP (HyperText Transfer Protocol)](#http)
- [Reading a URL](#reading-a-url)
- [HTTP URL Scheme](#http-url-scheme)
- [Domain Name](#domain-name)
- [Sub-Domain](#sub-domain)
- [Port Number in a URL](#port-number-in-url)
- [Query String](#query-string)
- [HTTP Request](#http-request)
- [HTTP Response](#http-response)
- [HTTP Headers](#http-headers)
- [HTTP Message Body](#http-message-body)
- [HTTP Request Method](#http-request-method)
- [HTTP Response Status Code](#http-response-status-code)
- [HTTP Cookie](#http-cookie)
- [Making a Request with cURL](#making-a-request-with-curl)
- [Process behind typing google.com in a Browser](#process-behind-typing-googlecom-in-a-browser)

## URL
A **Uniform Resource Locator (URL)** acts as a web address, allowing us to access resources on the Internet. It uniquely identifies where a particular resource is and how to retrieve it.

**Example:** `https://www.example.com/pages/sample`

## HTTP
The **HyperText Transfer Protocol (HTTP)** is the underlying protocol of the World Wide Web. It facilitates the communication between web browsers and servers, allowing for the transfer of web pages to the user's computer.

## Reading a URL
To read a URL, one should understand its typical structure: `protocol://subdomain.domain:port/path?query#fragment`. Each part has a distinct role in directing browsers to the correct resource.

## HTTP URL Scheme
The URL scheme indicates the protocol being used. For HTTP, the schemes are `http://` for unsecured connections and `https://` for secured connections using SSL/TLS.

## Domain Name
A **Domain Name** represents the human-readable web address that we type into our browsers to visit a website. It's the recognizable "name" of a website.

**Example:** In the URL `https://www.google.com`, `google.com` is the domain name.

## Sub-Domain
A **Sub-Domain** is a subset or a lower-level component of the primary domain. It allows organizations to organize content or services under the same primary domain.

**Example:** `blog.example.com` is a sub-domain of `example.com`.

## Port Number in URL
Every server application listens on a specific port number on the server. By default, HTTP uses port 80, and HTTPS uses port 443. However, custom ports can be specified in the URL.

**Example:** `http://example.com:8080/` - Here, the server is listening on port 8080.

## Query String
A **Query String** is a part of a URL that provides additional data to the server. It usually starts with a `?` and contains key-value pairs separated by `&`.

**Example:** `example.com/search?q=query&sort=date` - This searches for the term "query" and sorts the results by date.

## HTTP Request
An **HTTP Request** is a message sent from the browser to a server. It's the way we ask servers to serve us a webpage or other resources.

## HTTP Response
An **HTTP Response** is what the server sends back after processing an HTTP request. It contains the content we requested, such as a web page, image, or video.

## HTTP Headers
**HTTP Headers** are used in both requests and responses. They provide essential metadata about the communication, like specifying content type, setting cookies, or indicating caching behaviors.

## HTTP Message Body
The **HTTP Message Body** is the part of the request or response that contains the actual data. For instance, when you submit a form, the data goes in the request message body. When you receive a webpage, the HTML content comes in the response message body.

## HTTP Request Method
The **HTTP Request Method** indicates the desired action on the resource. Common methods include:
- **GET**: Retrieve data.
- **POST**: Submit data.
- **PUT**: Update existing data.
- **DELETE**: Remove data.

## HTTP Response Status Code
The **HTTP Response Status Code** tells the client about the result of the request. For example:
- `200`: OK - The request was successful.
- `404`: Not Found - The requested resource is not available.
- `500`: Internal Server Error - The server failed to process a valid request.

## HTTP Cookie
An **HTTP Cookie** is a small piece of data that the server sends to the user's browser. The browser stores the cookie and sends it back with subsequent requests to the same domain. This mechanism allows for things like user sessions and preferences.

## Making a Request with cURL
**cURL** is a command-line tool used to send or receive data using various protocols. To make an HTTP request:

**Example:** 
```
curl https://www.example.com
```

## Process behind typing google.com in a Browser
1. **DNS Lookup**: The browser checks its cache to see if it knows the IP address for `google.com`. If not, it queries a DNS server.
2. **Establishing Connection**: The browser establishes a connection to the server using the retrieved IP address.
3. **Sending Request**: The browser sends an HTTP request to the server.
4. **Receiving Response**: The server processes the request and sends back an HTTP response.
5. **Rendering**: The browser processes the response and displays the content.
