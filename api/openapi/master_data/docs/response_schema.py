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
                            "code": "19",
                            "slug": "bangka-belitung",
                            "isoCode": "ID-BB",
                            "name": "Bangka Belitung"
                        }
                    ],
                    "pagination": {
                        "page": 1,
                        "limit": 2,
                        "totalPage": 17,
                        "totalRows": 34
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
                            "code": "12.76",
                            "slug": "kota-tebing-tinggi",
                            "provinceName": "Sumatera Utara",
                            "datiName": "Kota",
                            "name": "Tebing Tinggi",
                            "alias": None
                        },
                        {
                            "code": "15.09",
                            "slug": "kabupaten-tebo",
                            "provinceName": "Jambi",
                            "datiName": "Kabupaten",
                            "name": "Tebo",
                            "alias": None
                        }
                    ],
                    "pagination": {
                        "page": 1,
                        "limit": 2,
                        "totalPage": 15,
                        "totalRows": 29
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
                        }
                    ],
                    "pagination": {
                        "page": 1,
                        "limit": 2,
                        "totalPage": 3,
                        "totalRows": 6
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

    idn_subdistrict_collections = {
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
                            "code": "31.75.03",
                            "slug": "jatinegara",
                            "provinceName": "DKI Jakarta",
                            "districtName": "Kota Jakarta Timur",
                            "name": "Jatinegara",
                            "alias": None
                        },
                        {
                            "code": "33.28.07",
                            "slug": "jatinegara-kabupaten-tegal",
                            "provinceName": "Jawa Tengah",
                            "districtName": "Kabupaten Tegal",
                            "name": "Jatinegara",
                            "alias": None
                        }
                    ],
                    "pagination": {
                        "page": 1,
                        "limit": 100,
                        "totalPage": 1,
                        "totalRows": 2
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

    idn_subdistrict_collection_by_district = {
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
                            "code": "31.72.04",
                            "slug": "cilincing",
                            "provinceName": "DKI Jakarta",
                            "districtName": "Kota Jakarta Utara",
                            "name": "Cilincing",
                            "alias": None
                        },
                        {
                            "code": "31.72.06",
                            "slug": "kelapa-gading",
                            "provinceName": "DKI Jakarta",
                            "districtName": "Kota Jakarta Utara",
                            "name": "Kelapa Gading",
                            "alias": None
                        }
                    ],
                    "pagination": {
                        "page": 1,
                        "limit": 2,
                        "totalPage": 3,
                        "totalRows": 6
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
                    "message": "No Indonesian District found with slug 'kabupaten-jakarta-utara'"
                }
            }
        ),
    }

    idn_urban_village_collections = {
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
                            "code": "31.71.06.1002",
                            "slug": "pegangsaan",
                            "provinceName": "DKI Jakarta",
                            "districtName": "Kota Jakarta Pusat",
                            "subdistrictName": "Menteng",
                            "name": "Pegangsaan",
                            "alias": None,
                            "postalCode": "10320"
                        },
                        {
                            "code": "31.72.06.1002",
                            "slug": "pegangsaan-dua",
                            "provinceName": "DKI Jakarta",
                            "districtName": "Kota Jakarta Utara",
                            "subdistrictName": "Kelapa Gading",
                            "name": "Pegangsaan Dua",
                            "alias": None,
                            "postalCode": "14250"
                        }
                    ],
                    "pagination": {
                        "page": 1,
                        "limit": 2,
                        "totalPage": 1,
                        "totalRows": 2
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

    idn_urban_village_collection_by_subdistrict = {
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
                            "code": "31.75.03.1003",
                            "slug": "bali-mester",
                            "provinceName": "DKI Jakarta",
                            "districtName": "Kota Jakarta Timur",
                            "subdistrictName": "Jatinegara",
                            "name": "Bali Mester",
                            "alias": None,
                            "postalCode": "13310"
                        },
                        {
                            "code": "31.75.03.1002",
                            "slug": "bidara-cina",
                            "provinceName": "DKI Jakarta",
                            "districtName": "Kota Jakarta Timur",
                            "subdistrictName": "Jatinegara",
                            "name": "Bidara Cina",
                            "alias": "Bidaracina",
                            "postalCode": "13330"
                        }
                    ],
                    "pagination": {
                        "page": 1,
                        "limit": 2,
                        "totalPage": 4,
                        "totalRows": 8
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
                    "message": "No Indonesian Subdistrict found with slug 'kota-jatinegara'"
                }
            }
        ),
    }

    idn_subdistrict_collection_by_province = {
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
                            "code": "31.75.06",
                            "slug": "cakung",
                            "provinceName": "DKI Jakarta",
                            "districtName": "Kota Jakarta Timur",
                            "name": "Cakung",
                            "alias": None
                        },
                        {
                            "code": "31.71.05",
                            "slug": "cempaka-putih",
                            "provinceName": "DKI Jakarta",
                            "districtName": "Kota Jakarta Pusat",
                            "name": "Cempaka Putih",
                            "alias": None
                        }
                    ],
                    "pagination": {
                        "page": 1,
                        "limit": 2,
                        "totalPage": 22,
                        "totalRows": 44
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
                    "message": "No Indonesian Province found with slug 'jakarta-timur'"
                }
            }
        ),
    }

    idn_urban_village_collection_by_district = {
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
                            "code": "31.72.05.1003",
                            "slug": "ancol-pademangan",
                            "provinceName": "DKI Jakarta",
                            "districtName": "Kota Jakarta Utara",
                            "subdistrictName": "Pademangan",
                            "name": "Ancol",
                            "alias": None,
                            "postalCode": "14430"
                        },
                        {
                            "code": "31.72.04.1001",
                            "slug": "cilincing",
                            "provinceName": "DKI Jakarta",
                            "districtName": "Kota Jakarta Utara",
                            "subdistrictName": "Cilincing",
                            "name": "Cilincing",
                            "alias": None,
                            "postalCode": "14120"
                        }
                    ],
                    "pagination": {
                        "page": 1,
                        "limit": 2,
                        "totalPage": 16,
                        "totalRows": 31
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
                    "message": "No Indonesian District found with slug 'jatinegara'"
                }
            }
        ),
    }

    idn_urban_village_collection_by_province = {
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
                            "code": "31.72.05.1003",
                            "slug": "ancol-pademangan",
                            "provinceName": "DKI Jakarta",
                            "districtName": "Kota Jakarta Utara",
                            "subdistrictName": "Pademangan",
                            "name": "Ancol",
                            "alias": None,
                            "postalCode": "14430"
                        },
                        {
                            "code": "31.73.04.1007",
                            "slug": "angke",
                            "provinceName": "DKI Jakarta",
                            "districtName": "Kota Jakarta Barat",
                            "subdistrictName": "Tambora",
                            "name": "Angke",
                            "alias": None,
                            "postalCode": "11330"
                        }
                    ],
                    "pagination": {
                        "page": 1,
                        "limit": 2,
                        "totalPage": 134,
                        "totalRows": 267
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
                    "message": "No Indonesian Province found with slug 'jakarta-timur'"
                }
            }
        ),
    }