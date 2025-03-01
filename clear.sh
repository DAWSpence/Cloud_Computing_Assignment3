echo "Restarting procedure"
echo ""
docker stop $(docker ps -aq) 2>/dev/null
docker rm $(docker ps -aq) 2>/dev/null
docker image rm $(docker image ls) 2>/dev/null

