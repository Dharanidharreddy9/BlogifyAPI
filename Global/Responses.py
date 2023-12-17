from fastapi.responses import JSONResponse


# Error Messages
no_response = JSONResponse(content={"error": "Server Not responding"}, status_code=500)
no_data = JSONResponse(content={"error": "Data not found", "status_code": 404}, status_code=404)
invalid_input = JSONResponse(content={"error": "Invalid input", "status_code": 400}, status_code=400)
user_exists = JSONResponse(content={"error": "EmailId or Username already exists", "status_code": 400}, status_code=400)
code_exists = JSONResponse(content={"error": "This code already exists", "status_code": 400}, status_code=400)
unprocessable_entity = JSONResponse(content={"error": "Unprocessable entity", "status_code": 422}, status_code=422)
authentication_failed = JSONResponse(content={"error": "Authentication failed", "status_code": 401}, status_code=401)
permission_denied = JSONResponse(content={"error": "Permission denied", "status_code": 403}, status_code=403)
required_fields = JSONResponse(content={"error": "Required fields are missing", "status_code": 400},status_code=400)


# Success messages
success_created = JSONResponse(content={"message": "Resource created successfully", "status_code": 201}, status_code=201)
success_ok = JSONResponse(content={"message": "Request successful", "status_code": 200}, status_code=200)
success_accepted = JSONResponse(content={"message": "Request accepted", "status_code": 202}, status_code=202)
