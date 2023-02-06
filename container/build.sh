docker login ghcr.io
docker buildx create --name foRceTYl
docker buildx use foRceTYl
docker buildx build \
    --platform linux/arm64,linux/amd64,linux/arm/v7 \
    -t ghcr.io/ruriazz/ruriazz-api:latest \
    -f container/Dockerfile \
    --push .