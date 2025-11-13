def build_url(base, **params):
    """
    Builds a URL with query parameters using **kwargs.
    """
    if not params:
        return base  # No params, just return base URL

    # Convert dictionary to query string
    query_string = "&".join([f"{key}={value}" for key, value in params.items()])
    return f"{base}?{query_string}"


# Example usage:
url = build_url(
    "https://api.example.com/search",
    q="python",
    page=2,
    sort="recent"
)

print(url)
