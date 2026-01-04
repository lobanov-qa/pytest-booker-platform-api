import{J as t,j as e}from"./entry.client-172Ys3p0.js";const l="This document describes authorization requirements for each endpoint, based on analysis of locally deployed Swagger UI and the official Postman collection for restful-booker-platform.",d=[{depth:1,value:"API Access Matrix for Restful-Booker-Platform",id:"api-access-matrix-for-restful-booker-platform",children:[{depth:2,value:"Authorization Notes",id:"authorization-notes"},{depth:2,value:"Service: Auth (Authentication)",id:"service-auth-authentication"},{depth:2,value:"Service: Booking",id:"service-booking"},{depth:2,value:"Service: Room",id:"service-room"},{depth:2,value:"Service: Message",id:"service-message"},{depth:2,value:"Service: Branding",id:"service-branding"},{depth:2,value:"Service: Report",id:"service-report"}]}],c={lastModifiedTime:"2026-01-04T15:51:41.000Z"},o="pages/overview.en.mdx";function r(i){const n={a:"a",blockquote:"blockquote",code:"code",h1:"h1",h2:"h2",hr:"hr",li:"li",p:"p",strong:"strong",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",ul:"ul",...t(),...i.components};return e.jsxs(e.Fragment,{children:[e.jsx("script",{dangerouslySetInnerHTML:{__html:`
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

  // Сохраняем текущий язык (на случай, если localStorage пуст)
  if (savedLang !== activeLang) {
    localStorage.setItem("preferred-language", activeLang);
  }

  // Подсвечиваем активную кнопку
  const buttons = document.querySelectorAll(".language-switcher button");
  buttons.forEach((btn) => {
    if (btn.dataset.lang === activeLang) {
      btn.classList.add("active");
    }
  });
});
`}}),`
`,e.jsxs("div",{className:"language-switcher",children:[e.jsx("button",{onClick:()=>switchLanguage("ru"),children:e.jsx(n.p,{children:"🇷🇺"})}),e.jsx("button",{onClick:()=>switchLanguage("en"),children:e.jsx(n.p,{children:"🇬🇧"})})]}),`
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
`}),`
`,e.jsx(n.h1,{id:"api-access-matrix-for-restful-booker-platform",children:"API Access Matrix for Restful-Booker-Platform"}),`
`,e.jsxs("div",{className:"service-buttons",children:[e.jsx("a",{href:"/api/auth",className:"service-button auth",children:"🔐 Auth"}),e.jsx("a",{href:"/api/booking",className:"service-button booking",children:"📅 Booking"}),e.jsx("a",{href:"/api/room",className:"service-button room",children:"🏠 Room"}),e.jsx("a",{href:"/api/message",className:"service-button message",children:"💬 Message"}),e.jsx("a",{href:"/api/branding",className:"service-button branding",children:"🎨 Branding"}),e.jsx("a",{href:"/api/report",className:"service-button report",children:"📊 Report"})]}),`
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
`,e.jsxs(n.p,{children:["This document describes authorization requirements for each endpoint, based on analysis of ",e.jsx(n.strong,{children:"locally deployed Swagger UI"})," and the ",e.jsx(n.strong,{children:"official Postman collection"})," for ",e.jsx(n.a,{href:"https://github.com/mwinteringham/restful-booker-platform",children:"restful-booker-platform"}),"."]}),`
`,e.jsxs(n.blockquote,{children:[`
`,e.jsxs(n.p,{children:["🔍 ",e.jsx(n.strong,{children:"About the documentation"}),":"]}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:["Swagger UI is available ",e.jsx(n.strong,{children:"locally only"}),", after launching services via Docker."]}),`
`,e.jsx(n.li,{children:"Endpoints and schemas are verified against OpenAPI generated by each microservice."}),`
`,e.jsx(n.li,{children:"Cross-checked with the Postman collection."}),`
`]}),`
`]}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"authorization-notes",children:"Authorization Notes"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Token format"}),": string (e.g., ",e.jsx(n.code,{inline:"true",children:"abc123"}),")."]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Obtaining a token"}),":",`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.code,{inline:"true",children:"POST /auth/login"})," with body ",e.jsx(n.code,{inline:"true",children:'{"username": "admin", "password": "password"}'}),"."]}),`
`,e.jsxs(n.li,{children:[e.jsxs(n.strong,{children:["Token is returned in ",e.jsx(n.code,{inline:"true",children:"Set-Cookie"})]}),", not in the response body (despite OpenAPI)."]}),`
`,e.jsx(n.li,{children:"Response body is empty."}),`
`]}),`
`]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Sending the token"}),":",`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:["For all subsequent requests: in header ",e.jsx(n.code,{inline:"true",children:"Cookie: token=<value>"}),"."]}),`
`,e.jsxs(n.li,{children:["For ",e.jsx(n.code,{inline:"true",children:"/auth/validate"})," and ",e.jsx(n.code,{inline:"true",children:"/auth/logout"}),": token is sent in body: ",e.jsx(n.code,{inline:"true",children:'{"token": "..."}'}),"."]}),`
`]}),`
`]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Token lifetime"}),": reset every 10 minutes on the remote instance."]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Client note"}),": ",e.jsx(n.code,{inline:"true",children:"*"})," — client not yet implemented."]}),`
`]}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"service-auth-authentication",children:"Service: Auth (Authentication)"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Base URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3004"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger UI"}),": ",e.jsx(n.a,{href:"http://localhost:3004/auth/swagger-ui/index.html",children:"http://localhost:3004/auth/swagger-ui/index.html"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Health check"}),": ",e.jsx(n.a,{href:"http://localhost:3004/auth/actuator/health",children:"http://localhost:3004/auth/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Method"}),e.jsx(n.th,{children:"Path"}),e.jsx(n.th,{children:"Purpose"}),e.jsx(n.th,{children:"Client"}),e.jsx(n.th,{children:"Notes"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/auth/login"})}),e.jsx(n.td,{children:"Create token"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"AuthClient"})}),e.jsxs(n.td,{children:["Token in ",e.jsx(n.code,{inline:"true",children:"Set-Cookie"}),". Body is empty."]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/auth/validate"})}),e.jsx(n.td,{children:"Validate token"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"AuthClient"})}),e.jsxs(n.td,{children:["Token in body: ",e.jsx(n.code,{inline:"true",children:'{"token": "abc123"}'})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/auth/logout"})}),e.jsx(n.td,{children:"Destroy token"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"AuthClient"})}),e.jsxs(n.td,{children:["Token in body: ",e.jsx(n.code,{inline:"true",children:'{"token": "abc123"}'})]})]})]})]})}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"service-booking",children:"Service: Booking"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Base URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3000"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger UI"}),": ",e.jsx(n.a,{href:"http://localhost:3000/booking/swagger-ui/index.html",children:"http://localhost:3000/booking/swagger-ui/index.html"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Health check"}),": ",e.jsx(n.a,{href:"http://localhost:3000/booking/actuator/health",children:"http://localhost:3000/booking/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Method"}),e.jsx(n.th,{children:"Path"}),e.jsx(n.th,{children:"Purpose"}),e.jsx(n.th,{children:"Client"}),e.jsx(n.th,{children:"Notes"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/unavailable"})}),e.jsx(n.td,{children:"Check room availability"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicBookingClient*"})}),e.jsxs(n.td,{children:["Required: ",e.jsx("wbr",{}),e.jsx(n.code,{inline:"true",children:"checkin"}),", ",e.jsx("wbr",{}),e.jsx(n.code,{inline:"true",children:"checkout"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/"})}),e.jsx(n.td,{children:"Create booking"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicBookingClient*"})}),e.jsx(n.td,{children:"OpenAPI does not require token"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/{id}"})}),e.jsx(n.td,{children:"Get booking details"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateBookingClient*"})}),e.jsxs(n.td,{children:["Token in ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/"})}),e.jsx(n.td,{children:"Get all bookings"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateBookingClient*"})}),e.jsxs(n.td,{children:["Optional ",e.jsx(n.code,{inline:"true",children:"roomid"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/summary"})}),e.jsx(n.td,{children:"Booking summary"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateBookingClient*"})}),e.jsxs(n.td,{children:["Required ",e.jsx(n.code,{inline:"true",children:"roomid"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"PUT"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/{id}"})}),e.jsx(n.td,{children:"Update booking"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateBookingClient*"})}),e.jsxs(n.td,{children:["Token in ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"DELETE"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/{id}"})}),e.jsx(n.td,{children:"Delete booking"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateBookingClient*"})}),e.jsxs(n.td,{children:["Token in ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]})]})]})}),`
`,e.jsxs(n.blockquote,{children:[`
`,e.jsxs(n.p,{children:["⚠️ ",e.jsx(n.strong,{children:"Discrepancy"}),`:
Postman documentation claims `,e.jsx(n.code,{inline:"true",children:"POST /booking"}),` requires a token.
`,e.jsx(n.strong,{children:"In fact — it does not"}),". OpenAPI and actual service behavior take precedence."]}),`
`]}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"service-room",children:"Service: Room"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Base URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3001"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger UI"}),": ",e.jsx(n.a,{href:"http://localhost:3001/room/swagger-ui/index.html",children:"http://localhost:3001/room/swagger-ui/index.html"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Health check"}),": ",e.jsx(n.a,{href:"http://localhost:3001/room/actuator/health",children:"http://localhost:3001/room/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Method"}),e.jsx(n.th,{children:"Path"}),e.jsx(n.th,{children:"Purpose"}),e.jsx(n.th,{children:"Client"}),e.jsx(n.th,{children:"Notes"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/room/"})}),e.jsx(n.td,{children:"Get all rooms"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicRoomClient*"})}),e.jsxs(n.td,{children:["Optional: ",e.jsx(n.code,{inline:"true",children:"checkin"}),", ",e.jsx(n.code,{inline:"true",children:"checkout"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/room/{id}"})}),e.jsx(n.td,{children:"Get room details"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicRoomClient*"})}),e.jsx(n.td,{children:"–"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/room/"})}),e.jsx(n.td,{children:"Create room"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateRoomClient*"})}),e.jsxs(n.td,{children:["Token in ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"PUT"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/room/{id}"})}),e.jsx(n.td,{children:"Update room"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateRoomClient*"})}),e.jsxs(n.td,{children:["Token in ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"DELETE"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/room/{id}"})}),e.jsx(n.td,{children:"Delete room"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateRoomClient*"})}),e.jsxs(n.td,{children:["Token in ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]})]})]})}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"service-message",children:"Service: Message"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Base URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3006"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger UI"}),": ",e.jsx(n.a,{href:"http://localhost:3006/message/swagger-ui/index.html",children:"http://localhost:3006/message/swagger-ui/index.html"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Health check"}),": ",e.jsx(n.a,{href:"http://localhost:3006/message/actuator/health",children:"http://localhost:3006/message/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Method"}),e.jsx(n.th,{children:"Path"}),e.jsx(n.th,{children:"Purpose"}),e.jsx(n.th,{children:"Client"}),e.jsx(n.th,{children:"Notes"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/"})}),e.jsx(n.td,{children:"Get all messages"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicMessageClient*"})}),e.jsx(n.td,{children:"–"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/count"})}),e.jsx(n.td,{children:"Unread messages count"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicMessageClient*"})}),e.jsx(n.td,{children:"–"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/"})}),e.jsx(n.td,{children:"Create message"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicMessageClient*"})}),e.jsx(n.td,{children:"–"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/{id}"})}),e.jsx(n.td,{children:"Get message details"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateMessageClient*"})}),e.jsxs(n.td,{children:["Token in ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"PUT"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/{id}/read"})}),e.jsx(n.td,{children:"Mark as read"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateMessageClient*"})}),e.jsxs(n.td,{children:["Token in ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"DELETE"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/{id}"})}),e.jsx(n.td,{children:"Delete message"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateMessageClient*"})}),e.jsxs(n.td,{children:["Token in ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]})]})]})}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"service-branding",children:"Service: Branding"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Base URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3002"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger UI"}),": ",e.jsx(n.a,{href:"http://localhost:3002/branding/swagger-ui/index.html",children:"http://localhost:3002/branding/swagger-ui/index.html"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Health check"}),": ",e.jsx(n.a,{href:"http://localhost:3002/branding/actuator/health",children:"http://localhost:3002/branding/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Method"}),e.jsx(n.th,{children:"Path"}),e.jsx(n.th,{children:"Purpose"}),e.jsx(n.th,{children:"Client"}),e.jsx(n.th,{children:"Notes"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/branding/"})}),e.jsx(n.td,{children:"Get branding data"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicBrandingClient*"})}),e.jsx(n.td,{children:"–"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"PUT"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/branding/"})}),e.jsx(n.td,{children:"Update branding"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateBrandingClient*"})}),e.jsxs(n.td,{children:["Token in ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]})]})]})}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"service-report",children:"Service: Report"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Base URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3005"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger UI"}),": ",e.jsx(n.a,{href:"http://localhost:3005/report/swagger-ui/index.html",children:"http://localhost:3005/report/swagger-ui/index.html"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Health check"}),": ",e.jsx(n.a,{href:"http://localhost:3005/report/actuator/health",children:"http://localhost:3005/report/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Method"}),e.jsx(n.th,{children:"Path"}),e.jsx(n.th,{children:"Purpose"}),e.jsx(n.th,{children:"Client"}),e.jsx(n.th,{children:"Notes"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/report/room/{id}"})}),e.jsx(n.td,{children:"Report for a room"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicReportClient*"})}),e.jsx(n.td,{children:"–"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/report/"})}),e.jsx(n.td,{children:"Report for all rooms"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateReportClient*"})}),e.jsxs(n.td,{children:["Token in ",e.jsx(n.code,{inline:"true",children:"Cookie"})]})]})]})]})}),`
`,e.jsx(n.hr,{}),`
`,e.jsx("style",{jsx:!0,children:`


/* Responsive table */
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
  table-layout: auto;
}

.table-container th,
.table-container td {
  padding: 0.4rem 0.6rem;
  text-align: left;
  border-bottom: 1px solid var(--zuplo-border-color);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  min-width: 100px;
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
`})]})}function h(i={}){const{wrapper:n}={...t(),...i.components};return n?e.jsx(n,{...i,children:e.jsx(r,{...i})}):r(i)}export{o as __filepath,h as default,l as excerpt,c as frontmatter,d as tableOfContents};
//# sourceMappingURL=overview.en-IL2fSRz3.js.map
