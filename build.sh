echo "Building container"
echo ""
docker build -t pythonapp .
sleep 1
docker run --rm pythonapp
sleep 1
echo "Size"
docker image ls