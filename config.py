# addresses hard coded in sig_proxy.js

client_service_address = ('localhost', 8080)
sig_service_address = ('localhost', 3495)
signature_service_url = f'http://{sig_service_address[0]}:{sig_service_address[1]}/http-security-layer-request'

# Debug helper
# mitmweb --listen-port 8080 --mode reverse:http://127.0.0.1:18080 --listen-host 127.0.0.1 --web-port 8081
# mitmweb --listen-port 13495 --mode reverse:http://127.0.0.1:3495 --listen-host 127.0.0.1 --web-port 8082