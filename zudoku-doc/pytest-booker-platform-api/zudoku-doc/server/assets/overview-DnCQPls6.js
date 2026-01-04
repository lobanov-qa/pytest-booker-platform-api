import { jsx, jsxs, Fragment } from "react/jsx-runtime";
import { useMDXComponents } from "zudoku/components";
const excerpt = "Документ описывает требования к авторизации для каждого эндпоинта согласно анализу локально развернутых Swagger UI и официальной Postman-коллекции к restful-booker-platform.";
const tableOfContents = [{
  "depth": 1,
  "value": "Матрица доступа к API Restful-Booker-Platform",
  "id": "матрица-доступа-к-api-restful-booker-platform",
  "children": [{
    "depth": 2,
    "value": "Важные замечания по авторизации",
    "id": "важные-замечания-по-авторизации"
  }, {
    "depth": 2,
    "value": "Сервис: Auth (Аутентификация)",
    "id": "сервис-auth-аутентификация"
  }, {
    "depth": 2,
    "value": "Сервис: Booking (Бронирования)",
    "id": "сервис-booking-бронирования"
  }, {
    "depth": 2,
    "value": "Сервис: Room (Комнаты)",
    "id": "сервис-room-комнаты"
  }, {
    "depth": 2,
    "value": "Сервис: Message (Сообщения)",
    "id": "сервис-message-сообщения"
  }, {
    "depth": 2,
    "value": "Сервис: Branding (Брендирование)",
    "id": "сервис-branding-брендирование"
  }, {
    "depth": 2,
    "value": "Сервис: Report (Отчёты)",
    "id": "сервис-report-отчёты"
  }]
}];
const frontmatter = {
  "lastModifiedTime": "2026-01-04T17:05:27.000Z"
};
const __filepath = "pages/overview.mdx";
function _createMdxContent(props) {
  const _components = {
    a: "a",
    blockquote: "blockquote",
    br: "br",
    code: "code",
    h1: "h1",
    h2: "h2",
    hr: "hr",
    li: "li",
    p: "p",
    strong: "strong",
    table: "table",
    tbody: "tbody",
    td: "td",
    th: "th",
    thead: "thead",
    tr: "tr",
    ul: "ul",
    ...useMDXComponents(),
    ...props.components
  };
  return jsxs(Fragment, {
    children: [jsx("script", {
      dangerouslySetInnerHTML: {
        __html: `
function switchLanguage(lang) {
  localStorage.setItem("preferred-language", lang);

  const currentPath = window.location.pathname;
  let newPath;

  if (lang === "en") {
    newPath = currentPath.replace(/\\/overview(\\.(ru|en))?$/, "/overview.en");
  } else {
    newPath = currentPath.replace(/\\/overview(\\.(ru|en))?$/, "/overview");
  }

  if (currentPath === newPath) return;

  window.location.href = newPath;
}

document.addEventListener("DOMContentLoaded", () => {
  const savedLang = localStorage.getItem("preferred-language") || "ru";
  const currentPath = window.location.pathname;
  const isEnglish = currentPath.includes("/overview.en");
  const activeLang = isEnglish ? "en" : "ru";

  if (savedLang !== activeLang) {
    localStorage.setItem("preferred-language", activeLang);
  }

  const buttons = document.querySelectorAll(".language-switcher button");
  buttons.forEach((btn) => {
    if (btn.dataset.lang === activeLang) {
      btn.classList.add("active");
    }
  });
});
`
      }
    }), "\n", jsxs("div", {
      className: "language-switcher",
      children: [jsx("a", {
        href: "/pytest-booker-platform-api/",
        target: "_blank",
        title: "Go to Test Reports Dashboard",
        style: "\ndisplay: flex;\nalign-items: center;\njustify-content: center;\nwidth: 40px;\nheight: 40px;\nborder: 1px solid var(--zuplo-border-color);\nbackground: var(--zuplo-background-secondary);\nborder-radius: 6px;\ncursor: pointer;\ntransition: all 0.2s ease;\ntext-decoration: none;\nmargin-right: 8px;\n",
        children: jsx(_components.p, {
          children: "🏠"
        })
      }), jsx("button", {
        onClick: () => switchLanguage("ru"),
        children: jsx(_components.p, {
          children: "🇷🇺"
        })
      }), jsx("button", {
        onClick: () => switchLanguage("en"),
        children: jsx(_components.p, {
          children: "🇬🇧"
        })
      })]
    }), "\n", jsx("style", {
      jsx: true,
      children: `
.language-switcher {
  display: flex;
  gap: 8px;
  margin: 0 0 20px 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.language-switcher button {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--zuplo-border-color);
  background: var(--zuplo-background-secondary);
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 1.2rem;
  padding: 0;
}

.language-switcher button:hover {
  background: var(--zuplo-color-primary);
  transform: scale(1.05);
}

.language-switcher button.active {
  background: var(--zuplo-color-primary);
  color: white;
  border-color: var(--zuplo-color-primary);
  font-weight: 600;
}
`
    }), "\n", jsx(_components.h1, {
      id: "матрица-доступа-к-api-restful-booker-platform",
      children: "Матрица доступа к API Restful-Booker-Platform"
    }), "\n", jsxs("div", {
      className: "service-buttons",
      children: [jsx("a", {
        href: "/pytest-booker-platform-api/zudoku-doc/api/auth",
        className: "service-button auth",
        children: "🔐 Auth"
      }), jsx("a", {
        href: "/pytest-booker-platform-api/zudoku-doc/api/booking",
        className: "service-button booking",
        children: "📅 Booking"
      }), jsx("a", {
        href: "/pytest-booker-platform-api/zudoku-doc/api/room",
        className: "service-button room",
        children: " 🛏️ Room"
      }), jsx("a", {
        href: "/pytest-booker-platform-api/zudoku-doc/api/message",
        className: "service-button message",
        children: "💬 Message"
      }), jsx("a", {
        href: "/pytest-booker-platform-api/zudoku-doc/api/branding",
        className: "service-button branding",
        children: "🎨 Branding"
      }), jsx("a", {
        href: "/pytest-booker-platform-api/zudoku-doc/api/report",
        className: "service-button report",
        children: "📊 Report"
      })]
    }), "\n", jsx("style", {
      children: `
.service-buttons {
display: flex;
gap: 10px;
flex-wrap: wrap;
margin: 20px 0;
}

.service-button {
padding: 10px 20px;
color: white;
border-radius: 5px;
text-decoration: none;
font-weight: bold;
font-size: 0.875rem;
}

.service-button.auth { background: #3b82f6; }
.service-button.booking { background: #10b981; }
.service-button.room { background: #8b5cf6; }
.service-button.message { background: #f97316; }
.service-button.branding { background: #ec4899; }
.service-button.report { background: #ef4444; }

.service-button:hover {
opacity: 0.9;
transform: translateY(-2px);
transition: all 0.2s;
}
`
    }), "\n", jsxs(_components.p, {
      children: ["Документ описывает требования к авторизации для каждого эндпоинта согласно анализу ", jsx(_components.strong, {
        children: "локально развернутых Swagger UI"
      }), " и ", jsx(_components.strong, {
        children: "официальной Postman-коллекции"
      }), " к ", jsx(_components.a, {
        href: "https://github.com/mwinteringham/restful-booker-platform",
        children: "restful-booker-platform"
      }), "."]
    }), "\n", jsxs(_components.blockquote, {
      children: ["\n", jsxs(_components.p, {
        children: ["🔍 ", jsx(_components.strong, {
          children: "Важно о документации"
        }), ":"]
      }), "\n", jsxs(_components.ul, {
        children: ["\n", jsxs(_components.li, {
          children: ["Swagger UI доступен ", jsx(_components.strong, {
            children: "только локально"
          }), " после запуска сервисов через Docker."]
        }), "\n", jsx(_components.li, {
          children: "Эндпоинты и схемы проверены по OpenAPI, генерируемому каждым микросервисом."
        }), "\n", jsx(_components.li, {
          children: "Дополнительно сверено с Postman-коллекцией."
        }), "\n"]
      }), "\n"]
    }), "\n", jsx(_components.hr, {}), "\n", jsx(_components.h2, {
      id: "важные-замечания-по-авторизации",
      children: "Важные замечания по авторизации"
    }), "\n", jsxs(_components.ul, {
      children: ["\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Формат токена"
        }), ": строка (например, ", jsx(_components.code, {
          inline: "true",
          children: "abc123"
        }), ")."]
      }), "\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Получение токена"
        }), ":", "\n", jsxs(_components.ul, {
          children: ["\n", jsxs(_components.li, {
            children: [jsx(_components.code, {
              inline: "true",
              children: "POST /auth/login"
            }), " с телом ", jsx(_components.code, {
              inline: "true",
              children: '{"username": "admin", "password": "password"}'
            }), "."]
          }), "\n", jsxs(_components.li, {
            children: [jsxs(_components.strong, {
              children: ["Токен возвращается в ", jsx(_components.code, {
                inline: "true",
                children: "Set-Cookie"
              })]
            }), ", а не в теле (несмотря на OpenAPI)."]
          }), "\n", jsx(_components.li, {
            children: "Тело ответа — пустое."
          }), "\n"]
        }), "\n"]
      }), "\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Передача токена"
        }), ":", "\n", jsxs(_components.ul, {
          children: ["\n", jsxs(_components.li, {
            children: ["Для всех последующих запросов: в заголовке ", jsx(_components.code, {
              inline: "true",
              children: "Cookie: token=<значение>"
            }), "."]
          }), "\n", jsxs(_components.li, {
            children: ["Для ", jsx(_components.code, {
              inline: "true",
              children: "/auth/validate"
            }), " и ", jsx(_components.code, {
              inline: "true",
              children: "/auth/logout"
            }), ": токен отправляется в теле: ", jsx(_components.code, {
              inline: "true",
              children: '{"token": "..."}'
            }), "."]
          }), "\n"]
        }), "\n"]
      }), "\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Жизненный цикл токена"
        }), ": На удалённом сервере токен сбрасывается каждые 10 минут."]
      }), "\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Примечание по клиентам"
        }), ": ", jsx(_components.code, {
          inline: "true",
          children: "*"
        }), " — клиент ещё не реализован."]
      }), "\n"]
    }), "\n", jsx(_components.hr, {}), "\n", jsx(_components.h2, {
      id: "сервис-auth-аутентификация",
      children: "Сервис: Auth (Аутентификация)"
    }), "\n", jsxs(_components.ul, {
      children: ["\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Базовый URL"
        }), ": ", jsx(_components.code, {
          inline: "true",
          children: "http://localhost:3004"
        })]
      }), "\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Swagger UI"
        }), ": ", jsx(_components.a, {
          href: "http://localhost:3004/auth/swagger-ui/index.html",
          children: "http://localhost:3004/auth/swagger-ui/index.html"
        })]
      }), "\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Проверка здоровья сервиса"
        }), ": ", jsx(_components.a, {
          href: "http://localhost:3004/auth/actuator/health",
          children: "http://localhost:3004/auth/actuator/health"
        })]
      }), "\n"]
    }), "\n", jsx("div", {
      class: "table-container",
      children: jsxs(_components.table, {
        children: [jsx(_components.thead, {
          children: jsxs(_components.tr, {
            children: [jsx(_components.th, {
              children: "Метод"
            }), jsx(_components.th, {
              children: "Путь"
            }), jsx(_components.th, {
              children: "Назначение"
            }), jsx(_components.th, {
              children: "Клиент"
            }), jsx(_components.th, {
              children: "Примечания"
            })]
          })
        }), jsxs(_components.tbody, {
          children: [jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "POST"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/auth/login"
              })
            }), jsx(_components.td, {
              children: "Создание токена"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "AuthClient"
              })
            }), jsxs(_components.td, {
              children: ["Токен в ", jsx(_components.code, {
                inline: "true",
                children: "Set-Cookie"
              }), ". Тело пустое."]
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "POST"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/auth/validate"
              })
            }), jsx(_components.td, {
              children: "Валидация токена"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "AuthClient"
              })
            }), jsxs(_components.td, {
              children: ["Токен в теле: ", jsx(_components.code, {
                inline: "true",
                children: '{"token": "abc123"}'
              })]
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "POST"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/auth/logout"
              })
            }), jsx(_components.td, {
              children: "Уничтожение токена"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "AuthClient"
              })
            }), jsxs(_components.td, {
              children: ["Токен в теле: ", jsx(_components.code, {
                inline: "true",
                children: '{"token": "abc123"}'
              })]
            })]
          })]
        })]
      })
    }), "\n", jsx(_components.hr, {}), "\n", jsx(_components.h2, {
      id: "сервис-booking-бронирования",
      children: "Сервис: Booking (Бронирования)"
    }), "\n", jsxs(_components.ul, {
      children: ["\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Базовый URL"
        }), ": ", jsx(_components.code, {
          inline: "true",
          children: "http://localhost:3000"
        })]
      }), "\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Swagger UI"
        }), ": ", jsx(_components.a, {
          href: "http://localhost:3000/booking/swagger-ui/index.html",
          children: "http://localhost:3000/booking/swagger-ui/index.html"
        })]
      }), "\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Проверка здоровья сервиса"
        }), ": ", jsx(_components.a, {
          href: "http://localhost:3000/booking/actuator/health",
          children: "http://localhost:3000/booking/actuator/health"
        })]
      }), "\n"]
    }), "\n", jsx("div", {
      class: "table-container",
      children: jsxs(_components.table, {
        children: [jsx(_components.thead, {
          children: jsxs(_components.tr, {
            children: [jsx(_components.th, {
              children: "Метод"
            }), jsx(_components.th, {
              children: "Путь"
            }), jsx(_components.th, {
              children: "Назначение"
            }), jsx(_components.th, {
              children: "Клиент"
            }), jsx(_components.th, {
              children: "Примечания"
            })]
          })
        }), jsxs(_components.tbody, {
          children: [jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "GET"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/booking/unavailable"
              })
            }), jsx(_components.td, {
              children: "Проверка доступности комнат"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PublicBookingClient*"
              })
            }), jsxs(_components.td, {
              children: ["Обязательные: ", jsx("wbr", {}), jsx(_components.code, {
                inline: "true",
                children: "checkin"
              }), ", ", jsx("wbr", {}), jsx(_components.code, {
                inline: "true",
                children: "checkout"
              })]
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "POST"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/booking/"
              })
            }), jsx(_components.td, {
              children: "Создание бронирования"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PublicBookingClient*"
              })
            }), jsx(_components.td, {
              children: "OpenAPI не требует токен"
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "GET"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/booking/{id}"
              })
            }), jsx(_components.td, {
              children: "Детали бронирования"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PrivateBookingClient*"
              })
            }), jsxs(_components.td, {
              children: ["Токен в ", jsx(_components.code, {
                inline: "true",
                children: "Cookie"
              })]
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "GET"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/booking/"
              })
            }), jsx(_components.td, {
              children: "Все бронирования"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PrivateBookingClient*"
              })
            }), jsxs(_components.td, {
              children: ["Опциональный ", jsx(_components.code, {
                inline: "true",
                children: "roomid"
              })]
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "GET"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/booking/summary"
              })
            }), jsx(_components.td, {
              children: "Сводка по броням"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PrivateBookingClient*"
              })
            }), jsxs(_components.td, {
              children: ["Обязательный ", jsx(_components.code, {
                inline: "true",
                children: "roomid"
              })]
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "PUT"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/booking/{id}"
              })
            }), jsx(_components.td, {
              children: "Обновление бронирования"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PrivateBookingClient*"
              })
            }), jsxs(_components.td, {
              children: ["Токен в ", jsx(_components.code, {
                inline: "true",
                children: "Cookie"
              })]
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "DELETE"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/booking/{id}"
              })
            }), jsx(_components.td, {
              children: "Удаление бронирования"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PrivateBookingClient*"
              })
            }), jsxs(_components.td, {
              children: ["Токен в ", jsx(_components.code, {
                inline: "true",
                children: "Cookie"
              })]
            })]
          })]
        })]
      })
    }), "\n", jsxs(_components.blockquote, {
      children: ["\n", jsxs(_components.p, {
        children: ["⚠️ ", jsx(_components.strong, {
          children: "Расхождение"
        }), ":", jsx(_components.br, {}), "\n", "Postman-документация утверждает, что ", jsx(_components.code, {
          inline: "true",
          children: "POST /booking"
        }), " требует токен.", jsx(_components.br, {}), "\n", jsx(_components.strong, {
          children: "Фактически — не требует"
        }), ". Приоритет у OpenAPI и поведения сервиса."]
      }), "\n"]
    }), "\n", jsx(_components.hr, {}), "\n", jsx(_components.h2, {
      id: "сервис-room-комнаты",
      children: "Сервис: Room (Комнаты)"
    }), "\n", jsxs(_components.ul, {
      children: ["\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Базовый URL"
        }), ": ", jsx(_components.code, {
          inline: "true",
          children: "http://localhost:3001"
        })]
      }), "\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Swagger UI"
        }), ": ", jsx(_components.a, {
          href: "http://localhost:3001/room/swagger-ui/index.html",
          children: "http://localhost:3001/room/swagger-ui/index.html"
        })]
      }), "\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Проверка здоровья сервиса"
        }), ": ", jsx(_components.a, {
          href: "http://localhost:3001/room/actuator/health",
          children: "http://localhost:3001/room/actuator/health"
        })]
      }), "\n"]
    }), "\n", jsx("div", {
      class: "table-container",
      children: jsxs(_components.table, {
        children: [jsx(_components.thead, {
          children: jsxs(_components.tr, {
            children: [jsx(_components.th, {
              children: "Метод"
            }), jsx(_components.th, {
              children: "Путь"
            }), jsx(_components.th, {
              children: "Назначение"
            }), jsx(_components.th, {
              children: "Клиент"
            }), jsx(_components.th, {
              children: "Примечания"
            })]
          })
        }), jsxs(_components.tbody, {
          children: [jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "GET"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/room/"
              })
            }), jsx(_components.td, {
              children: "Все комнаты"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PublicRoomClient*"
              })
            }), jsxs(_components.td, {
              children: ["Опциональные: ", jsx(_components.code, {
                inline: "true",
                children: "checkin"
              }), ", ", jsx(_components.code, {
                inline: "true",
                children: "checkout"
              })]
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "GET"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/room/{id}"
              })
            }), jsx(_components.td, {
              children: "Детали комнаты"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PublicRoomClient*"
              })
            }), jsx(_components.td, {
              children: "–"
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "POST"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/room/"
              })
            }), jsx(_components.td, {
              children: "Создание комнаты"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PrivateRoomClient*"
              })
            }), jsxs(_components.td, {
              children: ["Токен в ", jsx(_components.code, {
                inline: "true",
                children: "Cookie"
              })]
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "PUT"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/room/{id}"
              })
            }), jsx(_components.td, {
              children: "Обновление комнаты"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PrivateRoomClient*"
              })
            }), jsxs(_components.td, {
              children: ["Токен в ", jsx(_components.code, {
                inline: "true",
                children: "Cookie"
              })]
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "DELETE"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/room/{id}"
              })
            }), jsx(_components.td, {
              children: "Удаление комнаты"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PrivateRoomClient*"
              })
            }), jsxs(_components.td, {
              children: ["Токен в ", jsx(_components.code, {
                inline: "true",
                children: "Cookie"
              })]
            })]
          })]
        })]
      })
    }), "\n", jsx(_components.hr, {}), "\n", jsx(_components.h2, {
      id: "сервис-message-сообщения",
      children: "Сервис: Message (Сообщения)"
    }), "\n", jsxs(_components.ul, {
      children: ["\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Базовый URL"
        }), ": ", jsx(_components.code, {
          inline: "true",
          children: "http://localhost:3006"
        })]
      }), "\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Swagger UI"
        }), ": ", jsx(_components.a, {
          href: "http://localhost:3006/message/swagger-ui/index.html",
          children: "http://localhost:3006/message/swagger-ui/index.html"
        })]
      }), "\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Проверка здоровья сервиса"
        }), ": ", jsx(_components.a, {
          href: "http://localhost:3006/message/actuator/health",
          children: "http://localhost:3006/message/actuator/health"
        })]
      }), "\n"]
    }), "\n", jsx("div", {
      class: "table-container",
      children: jsxs(_components.table, {
        children: [jsx(_components.thead, {
          children: jsxs(_components.tr, {
            children: [jsx(_components.th, {
              children: "Метод"
            }), jsx(_components.th, {
              children: "Путь"
            }), jsx(_components.th, {
              children: "Назначение"
            }), jsx(_components.th, {
              children: "Клиент"
            }), jsx(_components.th, {
              children: "Примечания"
            })]
          })
        }), jsxs(_components.tbody, {
          children: [jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "GET"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/message/"
              })
            }), jsx(_components.td, {
              children: "Все сообщения"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PublicMessageClient*"
              })
            }), jsx(_components.td, {
              children: "–"
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "GET"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/message/count"
              })
            }), jsx(_components.td, {
              children: "Кол-во непрочитанных"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PublicMessageClient*"
              })
            }), jsx(_components.td, {
              children: "–"
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "POST"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/message/"
              })
            }), jsx(_components.td, {
              children: "Создание сообщения"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PublicMessageClient*"
              })
            }), jsx(_components.td, {
              children: "–"
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "GET"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/message/{id}"
              })
            }), jsx(_components.td, {
              children: "Детали сообщения"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PrivateMessageClient*"
              })
            }), jsxs(_components.td, {
              children: ["Токен в ", jsx(_components.code, {
                inline: "true",
                children: "Cookie"
              })]
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "PUT"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/message/{id}/read"
              })
            }), jsx(_components.td, {
              children: "Пометить как прочитанное"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PrivateMessageClient*"
              })
            }), jsxs(_components.td, {
              children: ["Токен в ", jsx(_components.code, {
                inline: "true",
                children: "Cookie"
              })]
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "DELETE"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/message/{id}"
              })
            }), jsx(_components.td, {
              children: "Удаление сообщения"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PrivateMessageClient*"
              })
            }), jsxs(_components.td, {
              children: ["Токен в ", jsx(_components.code, {
                inline: "true",
                children: "Cookie"
              })]
            })]
          })]
        })]
      })
    }), "\n", jsx(_components.hr, {}), "\n", jsx(_components.h2, {
      id: "сервис-branding-брендирование",
      children: "Сервис: Branding (Брендирование)"
    }), "\n", jsxs(_components.ul, {
      children: ["\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Базовый URL"
        }), ": ", jsx(_components.code, {
          inline: "true",
          children: "http://localhost:3002"
        })]
      }), "\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Swagger UI"
        }), ": ", jsx(_components.a, {
          href: "http://localhost:3002/branding/swagger-ui/index.html",
          children: "http://localhost:3002/branding/swagger-ui/index.html"
        })]
      }), "\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Проверка здоровья сервиса"
        }), ": ", jsx(_components.a, {
          href: "http://localhost:3002/branding/actuator/health",
          children: "http://localhost:3002/branding/actuator/health"
        })]
      }), "\n"]
    }), "\n", jsx("div", {
      class: "table-container",
      children: jsxs(_components.table, {
        children: [jsx(_components.thead, {
          children: jsxs(_components.tr, {
            children: [jsx(_components.th, {
              children: "Метод"
            }), jsx(_components.th, {
              children: "Путь"
            }), jsx(_components.th, {
              children: "Назначение"
            }), jsx(_components.th, {
              children: "Клиент"
            }), jsx(_components.th, {
              children: "Примечания"
            })]
          })
        }), jsxs(_components.tbody, {
          children: [jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "GET"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/branding/"
              })
            }), jsx(_components.td, {
              children: "Данные брендинга"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PublicBrandingClient*"
              })
            }), jsx(_components.td, {
              children: "–"
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "PUT"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/branding/"
              })
            }), jsx(_components.td, {
              children: "Обновление брендинга"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PrivateBrandingClient*"
              })
            }), jsxs(_components.td, {
              children: ["Токен в ", jsx(_components.code, {
                inline: "true",
                children: "Cookie"
              })]
            })]
          })]
        })]
      })
    }), "\n", jsx(_components.hr, {}), "\n", jsx(_components.h2, {
      id: "сервис-report-отчёты",
      children: "Сервис: Report (Отчёты)"
    }), "\n", jsxs(_components.ul, {
      children: ["\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Базовый URL"
        }), ": ", jsx(_components.code, {
          inline: "true",
          children: "http://localhost:3005"
        })]
      }), "\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Swagger UI"
        }), ": ", jsx(_components.a, {
          href: "http://localhost:3005/report/swagger-ui/index.html",
          children: "http://localhost:3005/report/swagger-ui/index.html"
        })]
      }), "\n", jsxs(_components.li, {
        children: [jsx(_components.strong, {
          children: "Проверка здоровья сервиса"
        }), ": ", jsx(_components.a, {
          href: "http://localhost:3005/report/actuator/health",
          children: "http://localhost:3005/report/actuator/health"
        })]
      }), "\n"]
    }), "\n", jsx("div", {
      class: "table-container",
      children: jsxs(_components.table, {
        children: [jsx(_components.thead, {
          children: jsxs(_components.tr, {
            children: [jsx(_components.th, {
              children: "Метод"
            }), jsx(_components.th, {
              children: "Путь"
            }), jsx(_components.th, {
              children: "Назначение"
            }), jsx(_components.th, {
              children: "Клиент"
            }), jsx(_components.th, {
              children: "Примечания"
            })]
          })
        }), jsxs(_components.tbody, {
          children: [jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "GET"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/report/room/{id}"
              })
            }), jsx(_components.td, {
              children: "Отчёт по комнате"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PublicReportClient*"
              })
            }), jsx(_components.td, {
              children: "–"
            })]
          }), jsxs(_components.tr, {
            children: [jsx(_components.td, {
              children: "GET"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "/report/"
              })
            }), jsx(_components.td, {
              children: "Отчёт по всем комнатам"
            }), jsx(_components.td, {
              children: jsx(_components.code, {
                inline: "true",
                children: "PrivateReportClient*"
              })
            }), jsxs(_components.td, {
              children: ["Токен в ", jsx(_components.code, {
                inline: "true",
                children: "Cookie"
              })]
            })]
          })]
        })]
      })
    }), "\n", jsx(_components.hr, {}), "\n", jsx("style", {
      jsx: true,
      children: `

/* Адаптивная таблица */
.table-container th:first-child,
.table-container td:first-child {
  width: 50px;
  min-width: 60px;
  max-width: 65px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding: 0.4rem 0.5rem;
}
.table-container {
  overflow-x: auto;
  margin: 1rem 0;
  -webkit-overflow-scrolling: touch;
  border-radius: 0.5rem;
  background: var(--zuplo-code-background);
}

.table-container table {
  width: 100%;
  min-width: 600px;
  border-collapse: collapse;
  font-size: 0.85rem;
  table-layout: auto; /* Позволяет ячейкам адаптироваться */
}

.table-container th,
.table-container td {
  padding: 0.4rem 0.6rem;
  text-align: left;
  border-bottom: 1px solid var(--zuplo-border-color);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  min-width: 100px; /* Минимальная ширина столбца */
}

.table-container th {
  font-weight: 600;
  background: var(--zuplo-background-secondary);
}

.table-container code {
  font-size: 0.90em;
  padding: 0.15em 0.4em;
  background: var(--zuplo-code-background);
  border: 1px solid var(--zuplo-border-color);
  border-radius: 6px;
  color: var(--zuplo-code-color);
}

/* Адаптация под мобильные */
@media (max-width: 768px) {
  .table-container {
    margin: 0.75rem 0;
  }

  .table-container table {
    font-size: 0.8rem;
  }

  .table-container th,
  .table-container td {
    padding: 0.3rem 0.4rem;
    min-width: 80px;
  }

  .service-button {
    padding: 8px 12px;
    font-size: 0.8rem;
  }
}

@media (max-width: 480px) {
  .table-container table {
    font-size: 0.75rem;
  }

  .table-container th,
  .table-container td {
    padding: 0.25rem 0.3rem;
    min-width: 60px;
  }

  .service-button {
    font-size: 0.75rem;
    padding: 6px 10px;
  }
}
`
    })]
  });
}
function MDXContent(props = {}) {
  const { wrapper: MDXLayout } = {
    ...useMDXComponents(),
    ...props.components
  };
  return MDXLayout ? jsx(MDXLayout, {
    ...props,
    children: jsx(_createMdxContent, {
      ...props
    })
  }) : _createMdxContent(props);
}
export {
  __filepath,
  MDXContent as default,
  excerpt,
  frontmatter,
  tableOfContents
};
//# sourceMappingURL=overview-DnCQPls6.js.map
