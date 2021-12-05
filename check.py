import ssl, socket
from prettytable import PrettyTable
import argparse
import time, json
import streamlit as st

# def check_ssl():
parser = argparse.ArgumentParser(description = 'Check and print SSL certiicate details')
parser.add_argument('--link', type=str)
args = parser.parse_args()
hostname = args.link.split('://')[1]

# print('Verifying SSL certificate details........\n')
# time.sleep(2)

def check_ssl(hostname):
    ctx = ssl.create_default_context()
    with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
        
        try:
            s.connect((hostname, 443))
            cert = s.getpeercert()

            data = json.dumps(cert, indent=2)
            # print(data)

            subject = dict(x[0] for x in cert['subject'])
            issued_to = subject['commonName']
            issuer = dict(x[0] for x in cert['issuer'])
            issued_by = issuer['commonName']

            subject = list(cert["subjectAltName"])
            dns=[]
            for i in range(len(subject)):
                index = subject[i]
                dns.append(index[1])

            st.write('----------------SSL Certificate Details-------------------')
            table  = PrettyTable(['Fields', 'Values'])
            table.add_row(["version", cert["version"]])
            table.add_row(["commonName", issued_to])
            for key in issuer.keys():
                info = [key, issuer[key]]
                table.add_row(info)
            table.add_row(["serialNumber", cert["serialNumber"]])
            table.add_row(["notBefore", cert["notBefore"]])
            table.add_row(["notAfter", cert["notAfter"]])

            table.add_row(["OCSP", cert["OCSP"][0]])
            table.add_row(["caIssuers", cert["caIssuers"][0]])
            table.add_row(["crlDistributionPoints", cert["crlDistributionPoints"][0]])
            table.add_row(["DNS", [dns][0][1:4]])
            st.json(data)
            
        except:
            st.write('no SSL certificate enabled for this URL!!')

# check_ssl(hostname)
