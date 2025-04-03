import mitmproxy

def get_request_host_header(flow: mitmproxy.http.HTTPFlow) -> str | None:
    return flow.request.host_header

def get_request_header_by_key(flow: mitmproxy.http.HTTPFlow, key: str) -> str:
    return flow.request.headers.get(key, f"Header '{key}' Not Found")