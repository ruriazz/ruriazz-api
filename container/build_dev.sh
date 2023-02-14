docker login ghcr.io
docker buildx build \
  --push -t ghcr.io/ruriazz/ruriazz-api:dev \
  --platform=linux/amd64 \
  -f container/backend/Dockerfile .