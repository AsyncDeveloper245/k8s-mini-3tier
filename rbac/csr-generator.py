from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.x509.oid import NameOID
from cryptography.x509 import (
    Name,
    CertificateSigningRequestBuilder,
    NameAttribute
)

# Generate a new private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

name = input("Enter Email Address: ")
user = input("Enter User: ")

# Generate a CSR
csr = (
    CertificateSigningRequestBuilder()
    .subject_name(
        Name([
            # Specify the details of the entity for which the certificate is being generated
            NameAttribute(NameOID.COUNTRY_NAME, "US"),
            NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
            NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
            NameAttribute(NameOID.ORGANIZATION_NAME, "GeekOps"),
            NameAttribute(NameOID.COMMON_NAME, user),
        ])
    )
    .sign(private_key, hashes.SHA256())
)

# Serialize the CSR and private key to PEM format
csr_pem = csr.public_bytes(serialization.Encoding.PEM)
private_key_pem = private_key.private_bytes(
    serialization.Encoding.PEM,
    serialization.PrivateFormat.PKCS8,
    serialization.NoEncryption(),
)


with open(name+'.csr', "w") as f:
    f.write(csr_pem.decode("utf-8"))

with open(name+'.pem', 'w') as f:
    f.write(private_key_pem.decode("utf-8"))
