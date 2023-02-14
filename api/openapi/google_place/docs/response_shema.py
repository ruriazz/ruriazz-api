from drf_yasg import openapi


class ResponseSchema:
    gmap_link_info = {
        "200": openapi.Response(
            description="OK",
            examples={
                "application/json": {
                    "meta": {
                        "success": True,
                        "code": 1000,
                        "httpCode": 200,
                        "message": "OK"
                    },
                    "data": [
                        {
                            "code": "51",
                            "slug": "bali",
                            "isoCode": "ID-BA",
                            "name": "Bali"
                        },
                        {
                            "code": "36",
                            "slug": "banten",
                            "isoCode": "ID-BT",
                            "name": "Banten"
                        },
                        {
                            "code": "19",
                            "slug": "bangka-belitung",
                            "isoCode": "ID-BB",
                            "name": "Bangka Belitung"
                        },
                        {
                            "code": "32",
                            "slug": "jawa-barat",
                            "isoCode": "ID-JB",
                            "name": "Jawa Barat"
                        },
                        {
                            "code": "61",
                            "slug": "kalimantan-barat",
                            "isoCode": "ID-KB",
                            "name": "Kalimantan Barat"
                        },
                        {
                            "code": "52",
                            "slug": "nusa-tenggara-barat",
                            "isoCode": "ID-NB",
                            "name": "Nusa Tenggara Barat"
                        },
                        {
                            "code": "92",
                            "slug": "papua-barat",
                            "isoCode": "ID-PB",
                            "name": "Papua Barat"
                        },
                        {
                            "code": "76",
                            "slug": "sulawesi-barat",
                            "isoCode": "ID-SR",
                            "name": "Sulawesi Barat"
                        },
                        {
                            "code": "13",
                            "slug": "sumatera-barat",
                            "isoCode": "ID-SB",
                            "name": "Sumatera Barat"
                        }
                    ],
                    "pagination": {
                        "page": 1,
                        "limit": 1000,
                        "totalPage": 1,
                        "totalRows": 9
                    }
                }
            }
        ),
        "400": openapi.Response(
            description="Parameter validation error",
            examples={
                "application/json": {
                    "meta": {
                        "success": False,
                        "code": 7001,
                        "httpCode": 400,
                        "message": "Parameter validation error"
                    },
                    "message": {
                        "limit": [
                            "Ensure this value is greater than or equal to 1."
                        ],
                        "page": [
                            "Ensure this value is greater than or equal to 1."
                        ]
                    }
                }
            }
        ),
    }