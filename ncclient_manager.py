from ncclient import manager

conn = manager.connect(
        host='sandbox-nxos-1.cisco.com', 
        port=22, 
        username='admin', 
        password='Admin_1234!', 
        hostkey_verify=False, 
        device_params={'name': 'nexus'}, 
        look_for_keys=False)

for value in conn.server_capabilities:
    print(value)

conn.close_session()
