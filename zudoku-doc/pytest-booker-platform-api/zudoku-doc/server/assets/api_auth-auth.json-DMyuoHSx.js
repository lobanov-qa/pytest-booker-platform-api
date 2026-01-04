const __refs = Array.from({ length: 2 }, () => ({}));
const __refMap = {
  "#/components/schemas/Token": __refs[0],
  "#/components/schemas/Auth": __refs[1]
};
const __refMapPaths = Object.keys(__refMap);
Object.assign(__refs[0], {
  "type": "object",
  "properties": {
    "token": {
      "type": "string"
    }
  }
});
Object.defineProperty(__refs[0], "__$ref", { value: __refMapPaths[0], enumerable: false });
Object.assign(__refs[1], {
  "type": "object",
  "properties": {
    "username": {
      "type": "string"
    },
    "password": {
      "type": "string"
    }
  }
});
Object.defineProperty(__refs[1], "__$ref", { value: __refMapPaths[1], enumerable: false });
const schema = {
  "openapi": "3.1.0",
  "info": {
    "title": "OpenAPI definition",
    "version": "v0"
  },
  "servers": [
    {
      "url": "http://localhost:3004",
      "description": "Auth Service"
    }
  ],
  "paths": {
    "/validate": {
      "post": {
        "tags": [
          "auth-controller"
        ],
        "operationId": "validateToken",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": __refMap["#/components/schemas/Token"]
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "*/*": {
                "schema": __refMap["#/components/schemas/Token"]
              }
            }
          }
        }
      }
    },
    "/logout": {
      "post": {
        "tags": [
          "auth-controller"
        ],
        "operationId": "clearToken",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": __refMap["#/components/schemas/Token"]
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
    },
    "/login": {
      "post": {
        "tags": [
          "auth-controller"
        ],
        "operationId": "createToken",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": __refMap["#/components/schemas/Auth"]
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "*/*": {
                "schema": __refMap["#/components/schemas/Token"]
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Token": {
        "type": "object",
        "properties": {
          "token": {
            "type": "string"
          }
        }
      },
      "Auth": {
        "type": "object",
        "properties": {
          "username": {
            "type": "string"
          },
          "password": {
            "type": "string"
          }
        }
      }
    }
  }
};
const slugs = {
  operations: { "/validate-post-validateToken": "validate-token", "/logout-post-clearToken": "clear-token", "/login-post-createToken": "create-token" },
  tags: { "auth-controller": "auth-controller" }
};
export {
  schema,
  slugs
};
//# sourceMappingURL=api_auth-auth.json-DMyuoHSx.js.map
