def build(base, **params):
    """ Builds a url with query parameters using **kwargs"""
    if not params:
        return base # no params, just return base URL
    query_string = "&".join()