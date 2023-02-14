from drf_yasg import openapi


class ResponseSchema:
    create_short_url = {
        "200": openapi.Response(
            description="custom 200 description",
            examples={
                "application/json": {
                    "200_key1": "200_value_1",
                    "200_key2": "200_value_2",
                }
            }
        ),
        "205": openapi.Response(
            description="custom 205 description",
            examples={
                "application/json": {
                    "205_key1": "205_value_1",
                    "205_key2": "205_value_2",
                }
            }
        ),
    }