# unit 2: forms
# 
'''
#### HTML forms:
<form> content </form>
content:
    <input>     one of the possible elements which makes a box
                ## can take an attr:      name="qname"
                    qname is the input paramater for name
                    if the form is filled, url changes to
                    ?qname=forminput
                ## another attr:          type="submit"   // is only submit
                    creates a button with text "Submit"
                    same as clicking 'enter' within the form
                urls cant have spaces or 
    form attributes:
        action="/foo"
            determines url of where we want the form to submit to
            if you set this to google.com/search, it will send the form
                to google.com/search
        method='post'
            method defaults to get
        get vs post
            get
                includes params in the url
                used for fetching docs
                they have a maximum url length
                OK to cache inbetween you and the server
                shouldn't change the server
            post
                includes params/data in the body after the headers
                used for updating data
                have no max url length (though a servers configure for this)
                hardly ever cached since the updates will be on the server
                usually change the server
            what happens if you dont obey the rules
                37signals todo list with delete buttons on the side
                a google web accelerator would pre-cache links on the page by
                    invoking their GET requests
                so it would invoke the delete GET requests (and delete the
                    lists!)



