const __refs = Array.from({ length: 4 }, () => ({}));
const __refMap = {
  "#/components/schemas/Branding": __refs[0],
  "#/components/schemas/Map": __refs[1],
  "#/components/schemas/Contact": __refs[2],
  "#/components/schemas/Address": __refs[3]
};
const __refMapPaths = Object.keys(__refMap);
Object.assign(__refs[0], {
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "maxLength": 100,
      "minLength": 3,
      "pattern": "[A-Za-z& ]*"
    },
    "map": __refMap["#/components/schemas/Map"],
    "logoUrl": {
      "type": "string",
      "minLength": 1
    },
    "description": {
      "type": "string",
      "maxLength": 500,
      "minLength": 3,
      "pattern": "[a-zA-Z,&. ]*"
    },
    "directions": {
      "type": "string",
      "minLength": 1
    },
    "contact": __refMap["#/components/schemas/Contact"],
    "address": __refMap["#/components/schemas/Address"]
  },
  "required": [
    "description",
    "directions",
    "logoUrl",
    "name"
  ]
});
Object.defineProperty(__refs[0], "__$ref", { value: __refMapPaths[0], enumerable: false });
Object.assign(__refs[1], {
  "type": "object",
  "properties": {
    "latitude": {
      "type": "number",
      "format": "double"
    },
    "longitude": {
      "type": "number",
      "format": "double"
    }
  },
  "required": [
    "latitude",
    "longitude"
  ]
});
Object.defineProperty(__refs[1], "__$ref", { value: __refMapPaths[1], enumerable: false });
Object.assign(__refs[2], {
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "maxLength": 40,
      "minLength": 3,
      "pattern": "[A-Za-z& ]*"
    },
    "phone": {
      "type": "string",
      "minLength": 1
    },
    "email": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "email",
    "name",
    "phone"
  ]
});
Object.defineProperty(__refs[2], "__$ref", { value: __refMapPaths[2], enumerable: false });
Object.assign(__refs[3], {
  "type": "object",
  "properties": {
    "line1": {
      "type": "string",
      "minLength": 1
    },
    "line2": {
      "type": "string",
      "minLength": 1
    },
    "postTown": {
      "type": "string",
      "minLength": 1
    },
    "county": {
      "type": "string",
      "minLength": 1
    },
    "postCode": {
      "type": "string",
      "minLength": 1
    }
  },
  "required": [
    "county",
    "line1",
    "line2",
    "postCode",
    "postTown"
  ]
});
Object.defineProperty(__refs[3], "__$ref", { value: __refMapPaths[3], enumerable: false });
const schema = {
  "openapi": "3.1.0",
  "info": {
    "title": "OpenAPI definition",
    "version": "v0"
  },
  "servers": [
    {
      "url": "http://localhost:3002",
      "description": "Branding Service"
    }
  ],
  "paths": {
    "/": {
      "get": {
        "tags": [
          "branding-controller"
        ],
        "operationId": "getBranding",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "*/*": {
                "schema": __refMap["#/components/schemas/Branding"]
              }
            }
          }
        }
      },
      "put": {
        "tags": [
          "branding-controller"
        ],
        "operationId": "updateBranding",
        "parameters": [
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
              "schema": __refMap["#/components/schemas/Branding"]
            }
          },
          "required": true
        },
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
    }
  },
  "components": {
    "schemas": {
      "Address": {
        "type": "object",
        "properties": {
          "line1": {
            "type": "string",
            "minLength": 1
          },
          "line2": {
            "type": "string",
            "minLength": 1
          },
          "postTown": {
            "type": "string",
            "minLength": 1
          },
          "county": {
            "type": "string",
            "minLength": 1
          },
          "postCode": {
            "type": "string",
            "minLength": 1
          }
        },
        "required": [
          "county",
          "line1",
          "line2",
          "postCode",
          "postTown"
        ]
      },
      "Branding": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "maxLength": 100,
            "minLength": 3,
            "pattern": "[A-Za-z& ]*"
          },
          "map": __refMap["#/components/schemas/Map"],
          "logoUrl": {
            "type": "string",
            "minLength": 1
          },
          "description": {
            "type": "string",
            "maxLength": 500,
            "minLength": 3,
            "pattern": "[a-zA-Z,&. ]*"
          },
          "directions": {
            "type": "string",
            "minLength": 1
          },
          "contact": __refMap["#/components/schemas/Contact"],
          "address": __refMap["#/components/schemas/Address"]
        },
        "required": [
          "description",
          "directions",
          "logoUrl",
          "name"
        ]
      },
      "Contact": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "maxLength": 40,
            "minLength": 3,
            "pattern": "[A-Za-z& ]*"
          },
          "phone": {
            "type": "string",
            "minLength": 1
          },
          "email": {
            "type": "string",
            "minLength": 1
          }
        },
        "required": [
          "email",
          "name",
          "phone"
        ]
      },
      "Map": {
        "type": "object",
        "properties": {
          "latitude": {
            "type": "number",
            "format": "double"
          },
          "longitude": {
            "type": "number",
            "format": "double"
          }
        },
        "required": [
          "latitude",
          "longitude"
        ]
      }
    }
  }
};
const slugs = {
  operations: { "/-get-getBranding": "get-branding", "/-put-updateBranding": "update-branding" },
  tags: { "branding-controller": "branding-controller" }
};
export {
  schema,
  slugs
};
//# sourceMappingURL=api_branding-branding.json-C4lP229q.js.map
