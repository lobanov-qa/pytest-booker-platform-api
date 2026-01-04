const __refs = Array.from({ length: 2 }, () => ({}));
const __refMap = {
  "#/components/schemas/Report": __refs[0],
  "#/components/schemas/Entry": __refs[1]
};
const __refMapPaths = Object.keys(__refMap);
Object.assign(__refs[0], {
  "type": "object",
  "properties": {
    "report": {
      "type": "array",
      "items": __refMap["#/components/schemas/Entry"]
    }
  }
});
Object.defineProperty(__refs[0], "__$ref", { value: __refMapPaths[0], enumerable: false });
Object.assign(__refs[1], {
  "type": "object",
  "properties": {
    "start": {
      "type": "string",
      "format": "date-time"
    },
    "end": {
      "type": "string",
      "format": "date-time"
    },
    "title": {
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
      "url": "http://localhost:3005",
      "description": "Report Service"
    }
  ],
  "paths": {
    "/room/{id}": {
      "get": {
        "tags": [
          "report-controller"
        ],
        "operationId": "getSpecificRoomReport",
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
                "schema": __refMap["#/components/schemas/Report"]
              }
            }
          }
        }
      }
    },
    "/": {
      "get": {
        "tags": [
          "report-controller"
        ],
        "operationId": "getAllRoomReports",
        "parameters": [
          {
            "name": "token",
            "in": "cookie",
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
                "schema": __refMap["#/components/schemas/Report"]
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Entry": {
        "type": "object",
        "properties": {
          "start": {
            "type": "string",
            "format": "date-time"
          },
          "end": {
            "type": "string",
            "format": "date-time"
          },
          "title": {
            "type": "string"
          }
        }
      },
      "Report": {
        "type": "object",
        "properties": {
          "report": {
            "type": "array",
            "items": __refMap["#/components/schemas/Entry"]
          }
        }
      }
    }
  }
};
const slugs = {
  operations: { "/room/{id}-get-getSpecificRoomReport": "get-specific-room-report", "/-get-getAllRoomReports": "get-all-room-reports" },
  tags: { "report-controller": "report-controller" }
};
export {
  schema,
  slugs
};
//# sourceMappingURL=api_report-report.json-D-WT2iIa.js.map
