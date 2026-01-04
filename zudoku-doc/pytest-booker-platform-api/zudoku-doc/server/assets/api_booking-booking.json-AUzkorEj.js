const __refs = Array.from({ length: 7 }, () => ({}));
const __refMap = {
  "#/components/schemas/Booking": __refs[0],
  "#/components/schemas/CreatedBooking": __refs[1],
  "#/components/schemas/Bookings": __refs[2],
  "#/components/schemas/AvailableRoom": __refs[3],
  "#/components/schemas/BookingSummaries": __refs[4],
  "#/components/schemas/BookingDates": __refs[5],
  "#/components/schemas/BookingSummary": __refs[6]
};
const __refMapPaths = Object.keys(__refMap);
Object.assign(__refs[0], {
  "type": "object",
  "properties": {
    "bookingid": {
      "type": "integer",
      "format": "int32"
    },
    "roomid": {
      "type": "integer",
      "format": "int32",
      "minimum": 1
    },
    "firstname": {
      "type": "string",
      "maxLength": 18,
      "minLength": 3
    },
    "lastname": {
      "type": "string",
      "maxLength": 30,
      "minLength": 3
    },
    "depositpaid": {
      "type": "boolean"
    },
    "email": {
      "type": "string",
      "minLength": 1
    },
    "phone": {
      "type": "string",
      "maxLength": 21,
      "minLength": 11
    },
    "bookingdates": __refMap["#/components/schemas/BookingDates"]
  },
  "required": [
    "depositpaid"
  ]
});
Object.defineProperty(__refs[0], "__$ref", { value: __refMapPaths[0], enumerable: false });
Object.assign(__refs[1], {
  "type": "object",
  "properties": {
    "bookingid": {
      "type": "integer",
      "format": "int32"
    },
    "booking": __refMap["#/components/schemas/Booking"]
  }
});
Object.defineProperty(__refs[1], "__$ref", { value: __refMapPaths[1], enumerable: false });
Object.assign(__refs[2], {
  "type": "object",
  "properties": {
    "bookings": {
      "type": "array",
      "items": __refMap["#/components/schemas/Booking"]
    }
  }
});
Object.defineProperty(__refs[2], "__$ref", { value: __refMapPaths[2], enumerable: false });
Object.assign(__refs[3], {
  "type": "object",
  "properties": {
    "roomid": {
      "type": "integer",
      "format": "int32"
    }
  }
});
Object.defineProperty(__refs[3], "__$ref", { value: __refMapPaths[3], enumerable: false });
Object.assign(__refs[4], {
  "type": "object",
  "properties": {
    "bookings": {
      "type": "array",
      "items": __refMap["#/components/schemas/BookingSummary"]
    }
  }
});
Object.defineProperty(__refs[4], "__$ref", { value: __refMapPaths[4], enumerable: false });
Object.assign(__refs[5], {
  "type": "object",
  "properties": {
    "checkin": {
      "type": "string",
      "format": "date"
    },
    "checkout": {
      "type": "string",
      "format": "date"
    }
  },
  "required": [
    "checkin",
    "checkout"
  ]
});
Object.defineProperty(__refs[5], "__$ref", { value: __refMapPaths[5], enumerable: false });
Object.assign(__refs[6], {
  "type": "object",
  "properties": {
    "bookingDates": __refMap["#/components/schemas/BookingDates"]
  }
});
Object.defineProperty(__refs[6], "__$ref", { value: __refMapPaths[6], enumerable: false });
const schema = {
  "openapi": "3.1.0",
  "info": {
    "title": "OpenAPI definition",
    "version": "v0"
  },
  "servers": [
    {
      "url": "http://localhost:3000",
      "description": "Booking Service"
    }
  ],
  "paths": {
    "/{id}": {
      "get": {
        "tags": [
          "booking-controller"
        ],
        "operationId": "getBooking",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "token",
            "in": "cookie",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "*/*": {
                "schema": __refMap["#/components/schemas/Booking"]
              }
            }
          }
        }
      },
      "put": {
        "tags": [
          "booking-controller"
        ],
        "operationId": "updateBooking",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "token",
            "in": "cookie",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": __refMap["#/components/schemas/Booking"]
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "*/*": {
                "schema": __refMap["#/components/schemas/CreatedBooking"]
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "booking-controller"
        ],
        "operationId": "deleteBooking",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "token",
            "in": "cookie",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "*/*": {
                "schema": {
                  "type": "object"
                }
              }
            }
          }
        }
      }
    },
    "/": {
      "get": {
        "tags": [
          "booking-controller"
        ],
        "operationId": "getBookings",
        "parameters": [
          {
            "name": "roomid",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "token",
            "in": "cookie",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "*/*": {
                "schema": __refMap["#/components/schemas/Bookings"]
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "booking-controller"
        ],
        "operationId": "createBooking",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": __refMap["#/components/schemas/Booking"]
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "*/*": {
                "schema": __refMap["#/components/schemas/CreatedBooking"]
              }
            }
          }
        }
      }
    },
    "/unavailable": {
      "get": {
        "tags": [
          "booking-controller"
        ],
        "operationId": "checkUnavailability",
        "parameters": [
          {
            "name": "checkin",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "checkout",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "*/*": {
                "schema": {
                  "type": "array",
                  "items": __refMap["#/components/schemas/AvailableRoom"]
                }
              }
            }
          }
        }
      }
    },
    "/summary": {
      "get": {
        "tags": [
          "booking-controller"
        ],
        "operationId": "getSummaries",
        "parameters": [
          {
            "name": "roomid",
            "in": "query",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "*/*": {
                "schema": __refMap["#/components/schemas/BookingSummaries"]
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Booking": {
        "type": "object",
        "properties": {
          "bookingid": {
            "type": "integer",
            "format": "int32"
          },
          "roomid": {
            "type": "integer",
            "format": "int32",
            "minimum": 1
          },
          "firstname": {
            "type": "string",
            "maxLength": 18,
            "minLength": 3
          },
          "lastname": {
            "type": "string",
            "maxLength": 30,
            "minLength": 3
          },
          "depositpaid": {
            "type": "boolean"
          },
          "email": {
            "type": "string",
            "minLength": 1
          },
          "phone": {
            "type": "string",
            "maxLength": 21,
            "minLength": 11
          },
          "bookingdates": __refMap["#/components/schemas/BookingDates"]
        },
        "required": [
          "depositpaid"
        ]
      },
      "BookingDates": {
        "type": "object",
        "properties": {
          "checkin": {
            "type": "string",
            "format": "date"
          },
          "checkout": {
            "type": "string",
            "format": "date"
          }
        },
        "required": [
          "checkin",
          "checkout"
        ]
      },
      "CreatedBooking": {
        "type": "object",
        "properties": {
          "bookingid": {
            "type": "integer",
            "format": "int32"
          },
          "booking": __refMap["#/components/schemas/Booking"]
        }
      },
      "AvailableRoom": {
        "type": "object",
        "properties": {
          "roomid": {
            "type": "integer",
            "format": "int32"
          }
        }
      },
      "BookingSummaries": {
        "type": "object",
        "properties": {
          "bookings": {
            "type": "array",
            "items": __refMap["#/components/schemas/BookingSummary"]
          }
        }
      },
      "BookingSummary": {
        "type": "object",
        "properties": {
          "bookingDates": __refMap["#/components/schemas/BookingDates"]
        }
      },
      "Bookings": {
        "type": "object",
        "properties": {
          "bookings": {
            "type": "array",
            "items": __refMap["#/components/schemas/Booking"]
          }
        }
      }
    }
  }
};
const slugs = {
  operations: { "/{id}-get-getBooking": "get-booking", "/{id}-put-updateBooking": "update-booking", "/{id}-delete-deleteBooking": "delete-booking", "/-get-getBookings": "get-bookings", "/-post-createBooking": "create-booking", "/unavailable-get-checkUnavailability": "check-unavailability", "/summary-get-getSummaries": "get-summaries" },
  tags: { "booking-controller": "booking-controller" }
};
export {
  schema,
  slugs
};
//# sourceMappingURL=api_booking-booking.json-AUzkorEj.js.map
