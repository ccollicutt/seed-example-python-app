start:
    python app/echo_server.py

curl:
    curl -X POST -H "Content-Type: application/json" -d '{"message":"hello Flask"}' http://localhost:5000/echo

test:
    cd app && python -m unittest discover -s tests

push:
    git add . && git commit -m "update" && git push origin main