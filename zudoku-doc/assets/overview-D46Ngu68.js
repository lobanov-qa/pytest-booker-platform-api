import{J as t,j as e}from"./entry.client-DTYwzVsG.js";const d="Документ описывает требования к авторизации для каждого эндпоинта согласно анализу локально развернутых Swagger UI и официальной Postman-коллекции к restful-booker-platform.",s=[{depth:1,value:"Матрица доступа к API Restful-Booker-Platform",id:"матрица-доступа-к-api-restful-booker-platform",children:[{depth:2,value:"Важные замечания по авторизации",id:"важные-замечания-по-авторизации"},{depth:2,value:"Сервис: Auth (Аутентификация)",id:"сервис-auth-аутентификация"},{depth:2,value:"Сервис: Booking (Бронирования)",id:"сервис-booking-бронирования"},{depth:2,value:"Сервис: Room (Комнаты)",id:"сервис-room-комнаты"},{depth:2,value:"Сервис: Message (Сообщения)",id:"сервис-message-сообщения"},{depth:2,value:"Сервис: Branding (Брендирование)",id:"сервис-branding-брендирование"},{depth:2,value:"Сервис: Report (Отчёты)",id:"сервис-report-отчёты"}]}],c={lastModifiedTime:"2026-02-02T06:02:46.000Z"},h="pages/overview.mdx";function r(i){const n={a:"a",blockquote:"blockquote",code:"code",h1:"h1",h2:"h2",hr:"hr",li:"li",p:"p",strong:"strong",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",ul:"ul",...t(),...i.components};return e.jsxs(e.Fragment,{children:[e.jsx("script",{dangerouslySetInnerHTML:{__html:`
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

function goToHome() {
  window.location.href = "/pytest-booker-platform-api/";
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
`}}),`
`,e.jsxs("div",{className:"language-switcher",children:[e.jsx("button",{onClick:()=>goToHome(),"data-lang":"home",title:"Go to Test Reports Dashboard",className:"btn-home",children:e.jsx(n.p,{children:"🏠"})}),e.jsx("button",{onClick:()=>switchLanguage("ru"),"data-lang":"ru",children:e.jsx(n.p,{children:"🇷🇺"})}),e.jsx("button",{onClick:()=>switchLanguage("en"),"data-lang":"en",children:e.jsx(n.p,{children:"🇬🇧"})})]}),`
`,e.jsx("style",{jsx:!0,children:`
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
  font-size: 1.4rem;
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

`}),`
`,e.jsx(n.h1,{id:"матрица-доступа-к-api-restful-booker-platform",children:"Матрица доступа к API Restful-Booker-Platform"}),`
`,e.jsxs("div",{className:"service-buttons",children:[e.jsx("a",{href:"/pytest-booker-platform-api/zudoku-doc/api/auth",className:"service-button auth",children:"🔐 Auth"}),e.jsx("a",{href:"/pytest-booker-platform-api/zudoku-doc/api/booking",className:"service-button booking",children:"📅 Booking"}),e.jsx("a",{href:"/pytest-booker-platform-api/zudoku-doc/api/room",className:"service-button room",children:" 🛏️ Room"}),e.jsx("a",{href:"/pytest-booker-platform-api/zudoku-doc/api/message",className:"service-button message",children:"💬 Message"}),e.jsx("a",{href:"/pytest-booker-platform-api/zudoku-doc/api/branding",className:"service-button branding",children:"🎨 Branding"}),e.jsx("a",{href:"/pytest-booker-platform-api/zudoku-doc/api/report",className:"service-button report",children:"📊 Report"})]}),`
`,e.jsx("style",{children:`
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
`}),`
`,e.jsxs(n.p,{children:["Документ описывает требования к авторизации для каждого эндпоинта согласно анализу ",e.jsx(n.strong,{children:"локально развернутых Swagger UI"})," и ",e.jsx(n.strong,{children:"официальной Postman-коллекции"})," к ",e.jsx(n.a,{href:"https://github.com/mwinteringham/restful-booker-platform",children:"restful-booker-platform"}),"."]}),`
`,e.jsxs(n.blockquote,{children:[`
`,e.jsxs(n.p,{children:["🔍 ",e.jsx(n.strong,{children:"Важно о документации"}),":"]}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:["Swagger UI доступен ",e.jsx(n.strong,{children:"только локально"})," после запуска сервисов через Docker."]}),`
`,e.jsx(n.li,{children:"Эндпоинты и схемы проверены по OpenAPI, генерируемому каждым микросервисом."}),`
`,e.jsx(n.li,{children:"Дополнительно сверено с Postman-коллекцией."}),`
`]}),`
`]}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"важные-замечания-по-авторизации",children:"Важные замечания по авторизации"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Формат токена"}),": строка (например, ",e.jsx(n.code,{inline:"true",children:"abc123"}),")."]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Получение токена"}),":",`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.code,{inline:"true",children:"POST /auth/login"})," с телом ",e.jsx(n.code,{inline:"true",children:'{"username": "admin", "password": "password"}'}),"."]}),`
`,e.jsxs(n.li,{children:[e.jsxs(n.strong,{children:["Токен возвращается в ",e.jsx(n.code,{inline:"true",children:"Set-Cookie"})]}),", а не в теле (несмотря на OpenAPI)."]}),`
`,e.jsx(n.li,{children:"Тело ответа — пустое."}),`
`]}),`
`]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Передача токена"}),":",`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:["Для всех последующих запросов: в заголовке ",e.jsx(n.code,{inline:"true",children:"Cookie: token=<значение>"}),"."]}),`
`,e.jsxs(n.li,{children:["Для ",e.jsx(n.code,{inline:"true",children:"/auth/validate"})," и ",e.jsx(n.code,{inline:"true",children:"/auth/logout"}),": токен отправляется в теле: ",e.jsx(n.code,{inline:"true",children:'{"token": "..."}'}),"."]}),`
`]}),`
`]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Жизненный цикл токена"}),": На удалённом сервере токен сбрасывается каждые 10 минут."]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Примечание по клиентам"}),": ",e.jsx(n.code,{inline:"true",children:"*"})," — клиент ещё не реализован."]}),`
`]}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"сервис-auth-аутентификация",children:"Сервис: Auth (Аутентификация)"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Базовый URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3004"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger UI"}),": ",e.jsx(n.a,{href:"http://localhost:3004/auth/swagger-ui/index.html",children:"http://localhost:3004/auth/swagger-ui/index.html"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Проверка здоровья сервиса"}),": ",e.jsx(n.a,{href:"http://localhost:3004/auth/actuator/health",children:"http://localhost:3004/auth/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Метод"}),e.jsx(n.th,{children:"Путь"}),e.jsx(n.th,{children:"Назначение"}),e.jsx(n.th,{children:"Клиент"}),e.jsx(n.th,{children:"Примечания"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/auth/login"})}),e.jsx(n.td,{children:"Создание токена"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"AuthClient"})}),e.jsxs(n.td,{children:["Токен в ",e.jsx(n.code,{inline:"true",children:"Set-Cookie"}),". Тело пустое."]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/auth/validate"})}),e.jsx(n.td,{children:"Валидация токена"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"AuthClient"})}),e.jsxs(n.td,{children:["Токен в теле: ",e.jsx(n.code,{inline:"true",children:'{"token": "abc123"}'})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/auth/logout"})}),e.jsx(n.td,{children:"Уничтожение токена"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"AuthClient"})}),e.jsxs(n.td,{children:["Токен в теле: ",e.jsx(n.code,{inline:"true",children:'{"token": "abc123"}'})]})]})]})]})}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"сервис-booking-бронирования",children:"Сервис: Booking (Бронирования)"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Базовый URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3000"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger UI"}),": ",e.jsx(n.a,{href:"http://localhost:3000/booking/swagger-ui/index.html",children:"http://localhost:3000/booking/swagger-ui/index.html"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Проверка здоровья сервиса"}),": ",e.jsx(n.a,{href:"http://localhost:3000/booking/actuator/health",children:"http://localhost:3000/booking/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Метод"}),e.jsx(n.th,{children:"Путь"}),e.jsx(n.th,{children:"Назначение"}),e.jsx(n.th,{children:"Клиент"}),e.jsx(n.th,{children:"Требует аутентификации"}),e.jsx(n.th,{children:"Примечания"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/unavailable"})}),e.jsx(n.td,{children:"Проверка доступности комнат"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicBookingClient"})}),e.jsx(n.td,{children:"❌ Нет"}),e.jsxs(n.td,{children:["Обязательные параметры: ",e.jsx(n.code,{inline:"true",children:"checkin"}),", ",e.jsx(n.code,{inline:"true",children:"checkout"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/"})}),e.jsx(n.td,{children:"Создание бронирования"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicBookingClient"})}),e.jsx(n.td,{children:"❌ Нет"}),e.jsx(n.td,{children:"OpenAPI не требует токен"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/summary"})}),e.jsx(n.td,{children:"Сводка по броням"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicBookingClient"})}),e.jsx(n.td,{children:"❌ Нет"}),e.jsxs(n.td,{children:["Обязательный параметр: ",e.jsx(n.code,{inline:"true",children:"roomid"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/{id}"})}),e.jsx(n.td,{children:"Детали бронирования"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateBookingClient"})}),e.jsx(n.td,{children:"✅ Да"}),e.jsxs(n.td,{children:["Токен в ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/"})}),e.jsx(n.td,{children:"Все бронирования"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateBookingClient"})}),e.jsx(n.td,{children:"✅ Да"}),e.jsxs(n.td,{children:["Опциональный параметр: ",e.jsx(n.code,{inline:"true",children:"roomid"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"PUT"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/{id}"})}),e.jsx(n.td,{children:"Обновление бронирования"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateBookingClient"})}),e.jsx(n.td,{children:"✅ Да"}),e.jsxs(n.td,{children:["Токен в ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"DELETE"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/{id}"})}),e.jsx(n.td,{children:"Удаление бронирования"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateBookingClient"})}),e.jsx(n.td,{children:"✅ Да"}),e.jsxs(n.td,{children:["Токен в ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]})]})]})}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"сервис-room-комнаты",children:"Сервис: Room (Комнаты)"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Базовый URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3001"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger UI"}),": ",e.jsx(n.a,{href:"http://localhost:3001/room/swagger-ui/index.html",children:"http://localhost:3001/room/swagger-ui/index.html"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Проверка здоровья сервиса"}),": ",e.jsx(n.a,{href:"http://localhost:3001/room/actuator/health",children:"http://localhost:3001/room/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Метод"}),e.jsx(n.th,{children:"Путь"}),e.jsx(n.th,{children:"Назначение"}),e.jsx(n.th,{children:"Клиент"}),e.jsx(n.th,{children:"Примечания"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/room/"})}),e.jsx(n.td,{children:"Все комнаты"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicRoomClient*"})}),e.jsxs(n.td,{children:["Опциональные: ",e.jsx(n.code,{inline:"true",children:"checkin"}),", ",e.jsx(n.code,{inline:"true",children:"checkout"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/room/{id}"})}),e.jsx(n.td,{children:"Детали комнаты"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicRoomClient*"})}),e.jsx(n.td,{children:"–"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/room/"})}),e.jsx(n.td,{children:"Создание комнаты"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateRoomClient*"})}),e.jsxs(n.td,{children:["Токен в ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"PUT"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/room/{id}"})}),e.jsx(n.td,{children:"Обновление комнаты"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateRoomClient*"})}),e.jsxs(n.td,{children:["Токен в ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"DELETE"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/room/{id}"})}),e.jsx(n.td,{children:"Удаление комнаты"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateRoomClient*"})}),e.jsxs(n.td,{children:["Токен в ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]})]})]})}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"сервис-message-сообщения",children:"Сервис: Message (Сообщения)"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Базовый URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3006"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger UI"}),": ",e.jsx(n.a,{href:"http://localhost:3006/message/swagger-ui/index.html",children:"http://localhost:3006/message/swagger-ui/index.html"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Проверка здоровья сервиса"}),": ",e.jsx(n.a,{href:"http://localhost:3006/message/actuator/health",children:"http://localhost:3006/message/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Метод"}),e.jsx(n.th,{children:"Путь"}),e.jsx(n.th,{children:"Назначение"}),e.jsx(n.th,{children:"Клиент"}),e.jsx(n.th,{children:"Примечания"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/"})}),e.jsx(n.td,{children:"Все сообщения"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicMessageClient*"})}),e.jsx(n.td,{children:"–"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/count"})}),e.jsx(n.td,{children:"Кол-во непрочитанных"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicMessageClient*"})}),e.jsx(n.td,{children:"–"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/"})}),e.jsx(n.td,{children:"Создание сообщения"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicMessageClient*"})}),e.jsx(n.td,{children:"–"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/{id}"})}),e.jsx(n.td,{children:"Детали сообщения"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateMessageClient*"})}),e.jsxs(n.td,{children:["Токен в ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"PUT"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/{id}/read"})}),e.jsx(n.td,{children:"Пометить как прочитанное"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateMessageClient*"})}),e.jsxs(n.td,{children:["Токен в ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"DELETE"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/{id}"})}),e.jsx(n.td,{children:"Удаление сообщения"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateMessageClient*"})}),e.jsxs(n.td,{children:["Токен в ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]})]})]})}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"сервис-branding-брендирование",children:"Сервис: Branding (Брендирование)"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Базовый URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3002"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger UI"}),": ",e.jsx(n.a,{href:"http://localhost:3002/branding/swagger-ui/index.html",children:"http://localhost:3002/branding/swagger-ui/index.html"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Проверка здоровья сервиса"}),": ",e.jsx(n.a,{href:"http://localhost:3002/branding/actuator/health",children:"http://localhost:3002/branding/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Метод"}),e.jsx(n.th,{children:"Путь"}),e.jsx(n.th,{children:"Назначение"}),e.jsx(n.th,{children:"Клиент"}),e.jsx(n.th,{children:"Примечания"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/branding/"})}),e.jsx(n.td,{children:"Данные брендинга"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicBrandingClient*"})}),e.jsx(n.td,{children:"–"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"PUT"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/branding/"})}),e.jsx(n.td,{children:"Обновление брендинга"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateBrandingClient*"})}),e.jsxs(n.td,{children:["Токен в ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]})]})]})}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"сервис-report-отчёты",children:"Сервис: Report (Отчёты)"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Базовый URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3005"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger UI"}),": ",e.jsx(n.a,{href:"http://localhost:3005/report/swagger-ui/index.html",children:"http://localhost:3005/report/swagger-ui/index.html"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Проверка здоровья сервиса"}),": ",e.jsx(n.a,{href:"http://localhost:3005/report/actuator/health",children:"http://localhost:3005/report/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Метод"}),e.jsx(n.th,{children:"Путь"}),e.jsx(n.th,{children:"Назначение"}),e.jsx(n.th,{children:"Клиент"}),e.jsx(n.th,{children:"Примечания"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/report/room/{id}"})}),e.jsx(n.td,{children:"Отчёт по комнате"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicReportClient*"})}),e.jsx(n.td,{children:"–"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/report/"})}),e.jsx(n.td,{children:"Отчёт по всем комнатам"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateReportClient*"})}),e.jsxs(n.td,{children:["Токен в ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]})]})]})}),`
`,e.jsx(n.hr,{}),`
`,e.jsx("style",{jsx:!0,children:`

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
`})]})}function o(i={}){const{wrapper:n}={...t(),...i.components};return n?e.jsx(n,{...i,children:e.jsx(r,{...i})}):r(i)}export{h as __filepath,o as default,d as excerpt,c as frontmatter,s as tableOfContents};
//# sourceMappingURL=overview-D46Ngu68.js.map
