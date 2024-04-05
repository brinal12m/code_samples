# Creating a Self-Signed Certificate

In this guide, we'll walk through the steps to create a self-signed SSL certificate using OpenSSL.

## Step 1: Generate a Private Key

Generate an RSA private key with 2048 bits:

```bash
openssl genrsa -out server.key 2048
