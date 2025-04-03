import mitmproxy

def filter_request(flow: mitmproxy.http.HTTPFlow, base_url: str) -> bool:
    path = flow.request.path
    return path.startswith(base_url)