# unit 2: forms
# 
'''
#### HTML forms:
<form> content </form>
content:
    <input>
        one of the possible elements which allows for user input, either through text boxes or buttons
        ## can take an attr:      name="qname"
            qname is the input paramater for name
            if the form is filled, url changes to
            ?qname=forminput
        ## type="submit"
            creates a button with text "Submit"
            same as clicking 'enter' within the form
        ## type="text"
            tells you the type of the input
            text is default
        ## type="password"
            hides the text as it's being input
            should be used when typing in passwords
            NOT SENT SECURELY, ONLY PREVENTS OVER-SHOULDER-LOOKING
        ## type="checkbox"
            submits "on" when checked, is missing when unchecked
            design software to check for "on", everything else is off
        ## type="radio"
            individually, they behave exactly like checkboxes that can't be unchecked
            giving them the same name makes them behave as group
        ## value="someValue"
            if the checkbox or radio button for this tag is checked, the param is set to someValue
            someValue is also the default value in a textbox when the page is loaded
    <label>
        defines a label for an input element
    <select>
        creates a dropdown menu w/ the 1st option selected automatically
        <option>
            each option within a dropdown menu
            can also have a value= attr
            input's value defaults to text between <option> tags


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
        what happens when you dont obey the rules
            37signals todo list with delete buttons on the side
            a google web accelerator would pre-cache links on the page by
                invoking their GET requests
            so it would invoke the delete GET requests (and delete the list entries!)

STRING SUBSTITUTION
    '<b>sometext</b>'
        this is hardcoded, and doesnt allow us to change the string
    '<b>%s</b>' %variable
        this allows us to change %variable to change the string

INPUT VALIDATION
    malicious agents can send arbitrary data or junk
    so the server needs to deal w/ this w/o blindly operating on input
    ** EVEN IF YOU ONLY USE DROPDOWNS, malicious users can still modify the forms w/in the browsers and use the modified forms to post to any server they want
        SO YOU SERVER MUST ALWAYS VALIDATE INPUT, NO EXCEPTIONS

VALIDATION
    three steps
        1. verify user input
        2. on error, render form again
        3. when rendering the second time, include error message

ESCAPING
    if you're not careful, someone can include html or JS in an input
    which can completely fuck up your site, cause you to lose data, or worse, cause user data to be leaked
    ex
        all improper chars are converted:
            " --> &quot;
            > --> &gt;
            < --> &lt;
            & --> &amp;

RESUBMITTING THE FORM / REDIRECTION
    when you refresh a page generated from a POST request, your browser will ask you if you want to resend the posted info
    so instead of rendering the result in the POST,
        send them to a new page
        or send them to the page with the posted info
    so return a redirect to GET a success page, which will then be returned
        why not just send the success page after the POST?
            say the user can only request success.html after POSTing
            to get success.html again, the user will have to POST again
            instead, say the user gets a redirect link from the POST, which has them GET a success.html
            now, they can GET success.html without rePOSTing



'''