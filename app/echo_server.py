from flask import Flask, request, jsonify
from pydantic import BaseModel, ValidationError, constr, validator

app = Flask(__name__)


class EchoData(BaseModel):
    message: constr(strip_whitespace=True, min_length=1, max_length=1000)

    @validator("message")
    def check_regex(cls, value):
        import re

        if not re.match(r"^[a-zA-Z0-9\s]*$", value):
            raise ValueError("Invalid characters in message")
        return value


@app.route("/echo", methods=["POST"])
def echo():
    if request.method == "GET":
        return jsonify({"error": "only accepts POST"}), 405

    try:
        data = EchoData(**request.json)
        return jsonify(data.model_dump())
    except ValidationError as e:
        return jsonify("validation error"), 400
    except ValueError as ve:
        return jsonify("value error"), 400


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
