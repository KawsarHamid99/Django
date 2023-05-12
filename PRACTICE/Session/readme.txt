



** Session Method

* get_session_cookie_age() return session cookeie age in second. default to SESSION_COOKIE_AGE.
* set_expiry():
     ex:request.session.set_expiry(300) it will set the session expiry date 300 second.
* get_expiry_age() -> It returns the number of session until the session expire.
    this function accepts two optional keyword arguments:
        modification: last modification of the session as a datetime object. Default to the current time.
        expiry: expiry information for the session,as a datetime object an int(in second) or None.Defaults 
        to the value stored in the session bu set_expiry(),if there is one or None.
* get_expiry_date() -> it returns the date this session will expire. this function accepts same keyword 
                       arguments as get_expiry_age()

* get_expire_at_browser_close() -> It returns either true or false,
  depending on weather the user's session cookies will expire when the user's web browser is closed.

* clear_expired() - It removes expired session from the session store.this class method is called by clearsession. 


* set_test_cookie() -> it set's a test coookie to determine weather the user's browser cookies.
* test_cookie_worked() -> it return either True or False.depending on the other user's browser acceptes 
                          the test cookies.you wil have to call set_test_cookie() before use test_cookie_worked().
* delete_test_cookie() ->it deletes the test cookie.Use this to clean up after yourself.


** Session settings

SESSION_CACHE_ALIAS

SESSION_COOKIE_AGE

SESSION_COOKIE_DOMAIN

SESSION_COOKIE_HTTPONLY

SESSION_COOKIE_NAME

SESSION_COOKIE_PATH

SESSION_COOKIE_SAMESITE

SESSION_COOKIE_SECURE

SESSION_EXPIRE_AT_BROWSER_CLOSE

SESSION_FILE_PATH

SESSION_SAVE_EVERY_REQUEST