const __refs = Array.from({ length: 2 }, () => ({}));
const __refMap = {
  "#/components/schemas/Room": __refs[0],
  "#/components/schemas/Rooms": __refs[1]
};
const __refMapPaths = Object.keys(__refMap);
Object.assign(__refs[0], {
  "type": "object",
  "properties": {
    "roomid": {
      "type": "integer",
      "format": "int32"
    },
    "roomName": {
      "type": "string",
      "minLength": 1
    },
    "type": {
      "type": "string",
      "pattern": "Single|Double|Twin|Family|Suite"
    },
    "accessible": {
      "type": "boolean"
    },
    "image": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "features": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "roomPrice": {
      "type": "integer",
      "format": "int32",
      "maximum": 999,
      "minimum": 1
    }
  },
  "required": [
    "roomName",
    "type"
  ]
});
Object.defineProperty(__refs[0], "__$ref", { value: __refMapPaths[0], enumerable: false });
Object.assign(__refs[1], {
  "type": "object",
  "properties": {
    "rooms": {
      "type": "array",
      "items": __refMap["#/components/schemas/Room"]
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
      "url": "http://localhost:3001",
      "description": "Room Service"
    }
  ],
  "paths": {
    "/{id}": {
      "get": {
        "tags": [
          "room-controller"
        ],
        "operationId": "getRoom",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "*/*": {
                "schema": __refMap["#/components/schemas/Room"]
              }
            }
          }
        }
      },
      "put": {
        "tags": [
          "room-controller"
        ],
        "operationId": "updateRoom",
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
              "schema": __refMap["#/components/schemas/Room"]
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "*/*": {
                "schema": __refMap["#/components/schemas/Room"]
              }
            }
          }
        }
      },
      "delete": {
        "tags": [
          "room-controller"
        ],
        "operationId": "deleteRoom",
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
          "room-controller"
        ],
        "operationId": "getRooms",
        "parameters": [
          {
            "name": "checkin",
            "in": "query",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "checkout",
            "in": "query",
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
                "schema": __refMap["#/components/schemas/Rooms"]
              }
            }
          }
        }
      },
      "post": {
        "tags": [
          "room-controller"
        ],
        "operationId": "createRoom",
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
              "schema": __refMap["#/components/schemas/Room"]
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "*/*": {
                "schema": __refMap["#/components/schemas/Room"]
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Room": {
        "type": "object",
        "properties": {
          "roomid": {
            "type": "integer",
            "format": "int32"
          },
          "roomName": {
            "type": "string",
            "minLength": 1
          },
          "type": {
            "type": "string",
            "pattern": "Single|Double|Twin|Family|Suite"
          },
          "accessible": {
            "type": "boolean"
          },
          "image": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "features": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "roomPrice": {
            "type": "integer",
            "format": "int32",
            "maximum": 999,
            "minimum": 1
          }
        },
        "required": [
          "roomName",
          "type"
        ]
      },
      "Rooms": {
        "type": "object",
        "properties": {
          "rooms": {
            "type": "array",
            "items": __refMap["#/components/schemas/Room"]
          }
        }
      }
    }
  }
};
const slugs = {
  operations: { "/{id}-get-getRoom": "get-room", "/{id}-put-updateRoom": "update-room", "/{id}-delete-deleteRoom": "delete-room", "/-get-getRooms": "get-rooms", "/-post-createRoom": "create-room" },
  tags: { "room-controller": "room-controller" }
};
export {
  schema,
  slugs
};
//# sourceMappingURL=api_room-room.json-DYDZYagI.js.map
