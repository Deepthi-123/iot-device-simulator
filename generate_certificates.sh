#!/bin/bash

DEVICE_ID="$1"

log() {
    echo "$(date --iso-8601=seconds): $*" >> /tmp/crt.log
}

cleanup() {
    rm -f certs/device.*
}

mkdir -p certs/

# create device private key
wait < <(openssl genrsa -out client.key 2048)

# create CSR
wait< <(openssl req -new -key device.key -out device.csr \
  -subj "CN=simulator-$DEVICE_ID")


exit_code="$?"

if [[ "$exit_code" != 0 ]];then
    log "failed to create certificate signing request."
    exit "$exit_code"
fi

# create device certificates
wait < <(openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out certs/client.crt -days 365 -sha256)

exit_code="$?"

if [[ "$exit_code" != 0 ]];then
    log "failed to create device certificates."
    exit "$exit_code"
fi

trap cleanup EXIT