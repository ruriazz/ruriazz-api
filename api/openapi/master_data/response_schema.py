from drf_yasg import openapi


class ResponseSchema:
    idn_province_collections = {
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

    idn_district_collections = {
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
                            "code": "31.73",
                            "slug": "kota-jakarta-barat",
                            "provinceName": "DKI Jakarta",
                            "datiName": "Kota",
                            "name": "Jakarta Barat",
                            "alias": None
                        },
                        {
                            "code": "31.71",
                            "slug": "kota-jakarta-pusat",
                            "provinceName": "DKI Jakarta",
                            "datiName": "Kota",
                            "name": "Jakarta Pusat",
                            "alias": None
                        },
                        {
                            "code": "31.74",
                            "slug": "kota-jakarta-selatan",
                            "provinceName": "DKI Jakarta",
                            "datiName": "Kota",
                            "name": "Jakarta Selatan",
                            "alias": None
                        },
                        {
                            "code": "31.75",
                            "slug": "kota-jakarta-timur",
                            "provinceName": "DKI Jakarta",
                            "datiName": "Kota",
                            "name": "Jakarta Timur",
                            "alias": None
                        },
                        {
                            "code": "31.72",
                            "slug": "kota-jakarta-utara",
                            "provinceName": "DKI Jakarta",
                            "datiName": "Kota",
                            "name": "Jakarta Utara",
                            "alias": None
                        }
                    ],
                    "pagination": {
                        "page": 1,
                        "limit": 100,
                        "totalPage": 1,
                        "totalRows": 5
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

    idn_district_collection_by_province = {
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
                            "code": "31.73",
                            "slug": "kota-jakarta-barat",
                            "provinceName": "DKI Jakarta",
                            "datiName": "Kota",
                            "name": "Jakarta Barat",
                            "alias": None
                        },
                        {
                            "code": "31.71",
                            "slug": "kota-jakarta-pusat",
                            "provinceName": "DKI Jakarta",
                            "datiName": "Kota",
                            "name": "Jakarta Pusat",
                            "alias": None
                        },
                        {
                            "code": "31.74",
                            "slug": "kota-jakarta-selatan",
                            "provinceName": "DKI Jakarta",
                            "datiName": "Kota",
                            "name": "Jakarta Selatan",
                            "alias": None
                        },
                        {
                            "code": "31.75",
                            "slug": "kota-jakarta-timur",
                            "provinceName": "DKI Jakarta",
                            "datiName": "Kota",
                            "name": "Jakarta Timur",
                            "alias": None
                        },
                        {
                            "code": "31.72",
                            "slug": "kota-jakarta-utara",
                            "provinceName": "DKI Jakarta",
                            "datiName": "Kota",
                            "name": "Jakarta Utara",
                            "alias": None
                        }
                    ],
                    "pagination": {
                        "page": 1,
                        "limit": 100,
                        "totalPage": 1,
                        "totalRows": 5
                    }
                }
            }
        ),
        "400": openapi.Response(
            description="Data Not Found",
            examples={
                "application/json": {
                    "meta": {
                        "success": False,
                        "code": 7011,
                        "httpCode": 400,
                        "message": "Data Not Found"
                    },
                    "message": "No Indonesian Province found with slug 'random-slug'"
                }
            }
        ),
    }