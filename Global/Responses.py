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



getBlogResp = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "example": {
                        "value": {
                            "statusCode": 200,
                            "message": "Success",
                            "data": {
                                "blogs": [
                                    {
                                        "id": "657ee30d3ec905367fe9b52b",
                                        "postCode": "pt_6GKRW1",
                                        "title": "Fitness Journey",
                                        "content": "Documenting my fitness transformation",
                                        "author": "FitLife",
                                        "creation_date": "2023-12-17T08:09:20.498000"
                                    },
                                    {
                                        "id": "657fdac78adaa93bc444d9c6",
                                        "postCode": "pt_AHD8DR",
                                        "title": "Recipe Corner",
                                        "content": "Delicious recipes for food enthusiasts.",
                                        "author": "ChefCook",
                                        "creation_date": "2023-12-18T05:38:15.436000"
                                    }]}}}}}}}}


# searchPostResp = {
#     200: {
#         "description": "Success",
#         "content": {"application/json": {
#                     "examples": {"example": {
#                                 "value": {
#                                     "statusCode": 200,
#                                     "message": "Success",
#                                     "data": {[{"id": "657ee30d3ec905367fe9b52b",
#                                                 "postCode": "pt_6GKRW1",
#                                                 "title": "Fitness Journey",
#                                                 "content": "Documenting my fitness transformation",
#                                                 "author": "FitLife",
#                                                 "creation_date": "2023-12-17T08:09:20.498000"
#                                             },
#                                             {
#                                                 "id": "657fe4a83d3ea16b397410d1",
#                                                 "postCode": "pt_ME2V23",
#                                                 "title": "Photography Showcase",
#                                                 "content": "Capturing moments through the lens",
#                                                 "author": "PhotoEnthusiast",
#                                                 "creation_date": "2023-12-18T06:20:24.366000"
#                                             }]}}}}}}}}


createResp = {
    201 : {
        "description": "Resource created successfully",
        "content": {
            "application/json": {
                "examples": {"example" : {"value" :
                    {
                        "statusCode": 201,
                        "message" : "Resource created successfully"
                }}}}}}}

updateResp = {
    200 : {
        "description": "Request successful",
        "content": {
            "application/json": {
                "examples": {"example" : {"value" :
                    {
                        "statusCode": 200,
                        "message" : "Request successful"
                }}}}}}}

deleteResp = {
    200 : {
        "description": "Request successful",
        "content": {
            "application/json": {
                "examples": {"example" : {"value" :
                    {
                        "statusCode": 200,
                        "message" : "Request successful"
                }}}}}}}