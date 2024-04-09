docker build -t iris:0.1 .
docker run -it iris:0.1 /bin/bash

docker run -v "$(pwd)/data:/tmp/data" -it iris:0.1 /bin/bash

docker logs iris0:0.1
