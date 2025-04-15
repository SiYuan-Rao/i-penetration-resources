import mitmproxy

def filter_request(flow: mitmproxy.http.HTTPFlow, base_url: list) -> bool:
    path = flow.request.path
    return path.startswith(tuple(base_url))