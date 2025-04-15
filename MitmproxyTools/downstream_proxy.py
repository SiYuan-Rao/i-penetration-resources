import logging
import mitmproxy
import warnings
from des_tool import des_decrypt
from des_tool import des_encrypt
from http_extractor_tool import get_request_host_header
from filter import filter_request
from shared_config import config

warnings.filterwarnings("ignore", category=UserWarning)

def request(flow: mitmproxy.http.HTTPFlow) -> None:
    host_header = get_request_host_header(flow)
    if host_header != config["host_header"]:
        return

    if not filter_request(flow, config["base_url"]):
        return
    
    body_message = flow.request.get_text()
    if body_message != "":
        logging.info(f"下游代理获取到Request密文: {flow.request.get_text()}")
        decrypt_body_message = des_decrypt(body_message)
        logging.info(f"下游代理解密Request密文（Request明文）: {decrypt_body_message}")
        flow.request.set_text(decrypt_body_message)

def response(flow: mitmproxy.http.HTTPFlow) -> None:
    host_header = get_request_host_header(flow)
    if host_header != config["host_header"]:
        return
    
    if not filter_request(flow, config["base_url"]):
        return
    
    logging.info(f"下游代理获取到Response明文: {flow.response.get_text()}")
    body_message = flow.response.get_text()
    encrypt_body_message = des_encrypt(body_message)
    logging.info(f"下游代理加密Response明文（Response密文）: {encrypt_body_message}")
    flow.response.set_text(encrypt_body_message)