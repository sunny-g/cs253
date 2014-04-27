# unit 01
# the web
#### THE CLASS IS FRAMEWORK-AGNOSTIC!!!
'''
# the world wide web
# collection of html documents, the basis of the web

# your browser uses the internet to send http requests to servers
# http is a simple protocol for browser-server communication

# html is made of:
#   text content (what you see)
#   markup (what it looks like)
#   references to other docs (images, videos, links)

# html markup
# <name> contents </name>
all of the above is referred to as an element with opening and closing tags

tags:
    <b> bold text </b>
    <em> emphasized (italics) text </em>

    <TAG ATTR="value"> contents </TAG> 
    ex:
        <a href="www.reddit.com"> derp </a>
        <img src="url" alt="text displayed when img doesnt load"> ## NO END TAG
            // imgs appear inline with text

# whitespace
    use <br> break (void tag) to force newlines // ignores whitespace between
        words and sentences
        <br> is an inline tag; it just renders individual lines (rather than blocks)
        <em>, <img> etc are all inline tags
    <p> this renders as a paragraph (auto newlines) </p> 
        <p> renders blocks around the text (even with height and width)
    
<span attr=""> text </span>         inline; will keep all text inline
<div attr=""> text </div>           block; will block the text

#### the html document
begins with the doctype and html tags
<!DOCTYPE HTML>         // specifies the kind of html being used
  <html>            // surrounds the entire html document
    <head>              //  has metadata and other; css, JS and titles are here
    </head>
      <body>
head, body, contents of the doc (stuff you see on the screen)
      </body>
  </html>

#### urls
uniform resource locator
contains protocol (http, ftp), host (domain name/ip address), path
(...com/cs253/blah.html)
    #### Query parameters (GET parameters)  name=value
    they can do a lot of different things
    example.com/foo?p=1&g=neat      // ?p=1&g=neat are 2 parameters, & separates
    example.com/foo#fragment        // used to reference a part of the page you
        are looking at, like the second part of a wiki; can have other uses w/JS
        fragments are never sent to the server
    combo:  example.com/foo?p=1#fragment    // follows query parameters
    
    localhost:8000/     // port: default is 80, goes between host and path

#### http
hypertext transfer protocol
ex:     http://www.example.com/foo
request from browser: 
    GET /foo HTTP/1.1   // request line (sent human-readable to the server, just
                        like this
                        3 parts: method (GET), path (/foo) and version (HTTP/1.1)
                        path is the document you are requesting from the server
                        version (most use 1.1, there is also 1.0)
    ex: example.com/foo/logo.png?p=1#tricky
    request line: GET /foo/logo.png?p=1 HTTP/1.1    // no fragment is sent

requests include request line AND headers
headers:        name: value
    Host: www.example.com       // host is required for http1.1
    User-Agent: Chrome v.17     // can be used to semi-identify users
                                // values can be anything

HTTP responses:
    HTTP/1.1 200 OK     // status line
                        // 3 parts: version (same as request)
                            status code (200, 302 = found, 404 = not found, 500
                            = server error, etc)
                            2** = success, 3** = try again differently, 
                            4** = error browser-side, 5** = error server-side
                            reason phrase (OK, not found, server error, etc)
headers with HTTP responses:
    Date: Tue Mar 2012 04:04:03 GMT
    Server: Apache /2.2.4       // DONT SHOW THIS UNLESS YOU WANT TO BE HACKED
    Content-type: text/html
    Content-length: 1539        // length of html document, not required

#### servers
purpose: respond to http requests
2 types of responses:
    static:     pre-written files (images, videos, stuff of the 90's)
    dynamic:    response is built on the fly by WEB APPLICATIONS

web apps:       lives on the server, speaks http, generates content that browser
                requests

################################################################
OFFICE HOURS

google app engine

    used to get a site up and running (easily)
    you write python files
        launcher:   lets you start the app on the google's servers
                    requires python installed on the machine
                    can be used to then move your local code to the server
            app config update:      console way of uploading code to server
    large-scale projects on GAE?
        free at small scale
        pay for bandwidth, data store, etc
        udacity runs on GAE, other also use it for production

front end development:
    JS and CSS are whats needed
    JS can be served like HTML and can be used to modify CSS on the fly
    CSS controls font sizes, colors, etc

challenges when developing reddit and hipmunk?
    thats what the class is all about (unit 7: how do build in the real world)



    
    
    






















