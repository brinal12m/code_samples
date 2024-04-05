# Creating a Self-Signed Certificate

This guide'll walk us through the steps to create a self-signed SSL certificate using OpenSSL.

## Step 1: Generate a Private Key

Generate an RSA private key with 2048 bits:

```bash
openssl genrsa -out server.key 2048


## Step 2: Generate a Certificate Signing Request (CSR)

Generate a Certificate Signing Request (CSR) using the private key:

```bash
openssl req -new -key server.key -out server.csr

During the CSR generation, provide the required information such as Common Name (CN), Organization, etc.

## Step 3: Generate a Self-Signed Certificate

Sign the CSR using the private key to generate a self-signed certificate valid for 365 days:

```bash
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

## Summary
By following these steps, you'll have a self-signed SSL certificate (server.crt) along with its corresponding private key (server.key) ready for use.
