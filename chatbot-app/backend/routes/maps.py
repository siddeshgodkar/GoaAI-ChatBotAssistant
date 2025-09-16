# from flask import Blueprint, request, jsonify
# from services.maps_services import search_location

# maps_bp = Blueprint("maps", __name__)

# @maps_bp.route("/map-search", methods=["GET"])
# def map_search():
#     query = request.args.get("query")
#     results = search_location(query)
#     return jsonify(results)
