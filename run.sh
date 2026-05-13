docker build -t test .
docker run --rm \-v data\public_input.csv \-v data\output\output.ndjson \
test