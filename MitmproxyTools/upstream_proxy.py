import logging
import mitmproxy
from des_tool import des_decrypt
from des_tool import des_encrypt
from http_extractor_tool import get_request_host_header
from filter import filter_request
from shared_config import config

def request(flow: mitmproxy.http.HTTPFlow) -> None:
    host_header = get_request_host_header(flow)
    if host_header != config["host_header"]:
        return
    
    if not filter_request(flow, config["base_url"]):
        return
    
    logging.info(f"上游代理获取到Request明文: {flow.request.get_text()}")
    body_message = flow.request.get_text()
    encrypt_body_message = des_encrypt(body_message)
    logging.info(f"上游代理加密Request明文（密文）: {encrypt_body_message}")
    flow.request.set_text(encrypt_body_message)


def response(flow: mitmproxy.http.HTTPFlow) -> None:
    host_header = get_request_host_header(flow)
    if host_header != config["host_header"]:
        return
    
    if not filter_request(flow, config["base_url"]):
        return
    
    logging.info(f"上游代理获取到Response密文: {flow.response.get_text()}")
    body_message = flow.response.get_text()
    decrypt_body_message = des_decrypt(body_message)
    logging.info(f"上游代理解密Response密文（明文）: {decrypt_body_message}")
    flow.response.set_text(decrypt_body_message)