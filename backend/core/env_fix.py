import os

def disable_proxies():
    proxy_vars = [
        "HTTP_PROXY", "HTTPS_PROXY",
        "http_proxy", "https_proxy",
        "ALL_PROXY"
    ]

    for var in proxy_vars:
        os.environ.pop(var, None)
