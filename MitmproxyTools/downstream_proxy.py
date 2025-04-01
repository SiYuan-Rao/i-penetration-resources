import logging
import mitmproxy
from des_tool import des_decrypt
from des_tool import des_encrypt

def request(flow: mitmproxy.http.HTTPFlow) -> None:
    logging.info(f"下游代理获取到Request密文: {flow.request.get_text()}")
    body_message = flow.request.get_text()
    decrypt_body_message = des_decrypt(body_message)
    logging.info(f"下游代理解密Request密文（Request明文）: {decrypt_body_message}")
    flow.request.set_text(decrypt_body_message)

def response(flow: mitmproxy.http.HTTPFlow) -> None:
    logging.info(f"下游代理获取到Response明文: {flow.response.get_text()}")
    body_message = flow.response.get_text()
    encrypt_body_message = des_encrypt(body_message)
    logging.info(f"下游代理加密Response明文（Response密文）: {encrypt_body_message}")
    flow.response.set_text(encrypt_body_message)