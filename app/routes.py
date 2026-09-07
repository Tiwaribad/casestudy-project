import asyncio

from flask import Blueprint, jsonify, request

from app.services import (
    process_request,
    process_multiple_requests
)


main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Intucate API is running"
    })


@main.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    if not data or "userInput" not in data:
        return jsonify({
            "error": "userInput is required"
        }), 400

    user_input = data["userInput"]

    if not isinstance(user_input, str):
        return jsonify({
            "error": "userInput must be a string"
        }), 400

    if not user_input.strip():
        return jsonify({
            "error": "userInput cannot be empty"
        }), 400

    try:
        response = process_request(user_input)

        return jsonify({
            "response": response
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@main.route("/ask-multiple", methods=["POST"])
def ask_multiple():

    data = request.get_json()

    if not data or "userInput" not in data:
        return jsonify({
            "error": "userInput is required"
        }), 400

    user_inputs = data["userInput"]

    if not isinstance(user_inputs, list):
        return jsonify({
            "error": "userInput must be a list"
        }), 400

    if not user_inputs:
        return jsonify({
            "error": "userInput list cannot be empty"
        }), 400

    if not all(
        isinstance(item, str) and item.strip()
        for item in user_inputs
    ):
        return jsonify({
            "error": "All items must be non-empty strings"
        }), 400

    try:
        responses = asyncio.run(
            process_multiple_requests(user_inputs)
        )

        return jsonify({
            "responses": responses
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500