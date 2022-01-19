import sys

import retroarcher
paths = retroarcher.get_paths()
sys.path.append(paths['retroarcherModulesDir'])

# xbox-smartglass-core cannot bind the socket on Windows at this point https://github.com/OpenXbox/xbox-smartglass-core-python/blob/96e1e0a45db347f66101c3df5eec3f7cb92d1236/xbox/sg/console.py#L165
# The smartglass rest server could be used alternatively, but requires many more dependencies https://github.com/OpenXbox/xbox-smartglass-core-python/blob/master/xbox/scripts/rest_server.py
# Thanks unknownskl for providing this workaround https://gist.github.com/unknownskl/501630df1ac4ff7a480fa765d913d052
import socket
import struct
from cryptography import x509
from cryptography.x509.oid import NameOID


class XboxDiscovery(object):

    def discover(self, addr='', server_addr='0.0.0.0', server_port=8080):
        _consoles = []

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            server_address = (server_addr, server_port)
            s.bind(server_address)

            discovery_packet = bytes.fromhex("dd00000a000000000000000800000002")
            s.sendto(discovery_packet, (addr, 5050))
            s.settimeout(1)

            while True:
                data, address = s.recvfrom(4096)
                response = XboxDiscovery().unpack_discovery(data, address)
                if response:
                    _consoles.append(response)

            s.close()

        except socket.timeout:
            s.close()
            return _consoles

    def unpack_discovery(self, data, address):
        if (data[:2] != b'\xdd\x01'):
            return False

        name_length = struct.unpack('>h', data[12:14])[0]
        offset = 14

        name = data[offset:offset + name_length].decode()
        offset += name_length + 1

        uuid_length = struct.unpack('>h', data[offset:offset + 2])[0]
        uuid = data[offset + 2:offset + uuid_length].decode()
        offset += uuid_length + 3

        offset += 4  # Skip error status
        cert_length = struct.unpack('>h', data[offset:offset + 2])[0]
        cert = data[offset + 2:].hex()

        # Read certificate
        cert_data = x509.load_der_x509_certificate(bytes.fromhex(cert))
        live_id = cert_data.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value

        return {
            'name': name,
            'uuid': uuid,
            'liveid': live_id,
            'address': address[0],
            'port': address[1]
        }
