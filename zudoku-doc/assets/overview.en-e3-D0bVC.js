import{J as t,j as e}from"./entry.client-Dy4XF2Tl.js";const d="This document describes the real behavior of each microservice API in restful-booker-platform. All status codes and response formats are verified via direct curl requests.",l=[{depth:1,value:"API Access Matrix for Restful-Booker-Platform",id:"api-access-matrix-for-restful-booker-platform",children:[{depth:2,value:"Authorization Notes",id:"authorization-notes"},{depth:2,value:"Service: Auth",id:"service-auth"},{depth:2,value:"Service: Booking",id:"service-booking",children:[{depth:3,value:"Spec Deviations",id:"spec-deviations"}]},{depth:2,value:"Service: Room",id:"service-room",children:[{depth:3,value:"Spec Deviations",id:"spec-deviations-1"},{depth:3,value:"Serialization",id:"serialization"}]},{depth:2,value:"Service: Message",id:"service-message",children:[{depth:3,value:"Spec Deviations",id:"spec-deviations-2"},{depth:3,value:"Schemas",id:"schemas"}]},{depth:2,value:"Service: Branding",id:"service-branding",children:[{depth:3,value:"Spec Deviations",id:"spec-deviations-3"},{depth:3,value:"Serialization",id:"serialization-1"}]},{depth:2,value:"Service: Report",id:"service-report"}]}],c={lastModifiedTime:"2026-06-04T05:17:13.000Z"},h="pages/overview.en.mdx";function r(i){const n={a:"a",blockquote:"blockquote",code:"code",h1:"h1",h2:"h2",h3:"h3",hr:"hr",li:"li",p:"p",strong:"strong",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",ul:"ul",...t(),...i.components};return e.jsxs(e.Fragment,{children:[e.jsx("script",{dangerouslySetInnerHTML:{__html:`
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
  const savedLang = localStorage.getItem("preferred-language") || "en";
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
`,e.jsx(n.h1,{id:"api-access-matrix-for-restful-booker-platform",children:"API Access Matrix for Restful-Booker-Platform"}),`
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
`,e.jsxs(n.p,{children:["This document describes the ",e.jsx(n.strong,{children:"real behavior"})," of each microservice API in ",e.jsx(n.a,{href:"https://github.com/mwinteringham/restful-booker-platform",children:"restful-booker-platform"}),". All status codes and response formats are verified via direct curl requests."]}),`
`,e.jsxs(n.blockquote,{children:[`
`,e.jsxs(n.p,{children:["🔍 ",e.jsx(n.strong,{children:"API verification"}),":"]}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:["Swagger/OpenAPI: ",e.jsx(n.code,{inline:"true",children:"http://localhost:<port>/<service>/v3/api-docs"})]}),`
`,e.jsxs(n.li,{children:["Health: ",e.jsx(n.code,{inline:"true",children:"http://localhost:<port>/<service>/actuator/health"})]}),`
`,e.jsx(n.li,{children:"Status: ✅ matches OpenAPI spec, ⚠️ differs from spec"}),`
`]}),`
`]}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"authorization-notes",children:"Authorization Notes"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Token format"}),": string (e.g., ",e.jsx(n.code,{inline:"true",children:"abc123"}),")."]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Obtaining"}),": ",e.jsx(n.code,{inline:"true",children:"POST /auth/login"})," with body ",e.jsx(n.code,{inline:"true",children:'{"username": "admin", "password": "password"}'}),"."]}),`
`,e.jsxs(n.li,{children:[e.jsxs(n.strong,{children:["Token is returned in ",e.jsx(n.code,{inline:"true",children:"Set-Cookie"})]}),", not in the response body."]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Sending"}),": in header ",e.jsx(n.code,{inline:"true",children:"Cookie: token=<value>"}),"."]}),`
`]}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"service-auth",children:"Service: Auth"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Base URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3004"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3004/auth/v3/api-docs"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Health"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3004/auth/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Method"}),e.jsx(n.th,{children:"Path"}),e.jsx(n.th,{children:"Purpose"}),e.jsx(n.th,{children:"Client"}),e.jsx(n.th,{children:"Status"}),e.jsx(n.th,{children:"Notes"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/auth/login"})}),e.jsx(n.td,{children:"Login"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"AuthClient"})}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"200"})," ✅"]}),e.jsxs(n.td,{children:["Token in ",e.jsx(n.code,{inline:"true",children:"Set-Cookie"}),". Empty body"]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/auth/validate"})}),e.jsx(n.td,{children:"Validate"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"AuthClient"})}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"200"})," ✅"]}),e.jsxs(n.td,{children:["Token in body: ",e.jsx(n.code,{inline:"true",children:'{"token": "..."}'})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/auth/logout"})}),e.jsx(n.td,{children:"Logout"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"AuthClient"})}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"200"})," ✅"]}),e.jsxs(n.td,{children:["Token in body: ",e.jsx(n.code,{inline:"true",children:'{"token": "..."}'})]})]})]})]})}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"service-booking",children:"Service: Booking"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Base URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3000"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3000/booking/v3/api-docs"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Health"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3000/booking/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Method"}),e.jsx(n.th,{children:"Path"}),e.jsx(n.th,{children:"Purpose"}),e.jsx(n.th,{children:"Client"}),e.jsx(n.th,{style:{textAlign:"center"},children:"Auth?"}),e.jsx(n.th,{children:"Status"}),e.jsx(n.th,{children:"Notes"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/unavailable"})}),e.jsx(n.td,{children:"Availability"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicBookingClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"❌"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"200"})," ✅"]}),e.jsxs(n.td,{children:["Params: ",e.jsx(n.code,{inline:"true",children:"checkin"}),", ",e.jsx(n.code,{inline:"true",children:"checkout"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/"})}),e.jsx(n.td,{children:"Create"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicBookingClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"❌"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"201"})," ⚠️"]}),e.jsx(n.td,{children:"Spec: 200. Real: 201 Created"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/summary"})}),e.jsx(n.td,{children:"Summary"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicBookingClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"❌"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"200"})," ✅"]}),e.jsxs(n.td,{children:["Param: ",e.jsx(n.code,{inline:"true",children:"roomid"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/{id}"})}),e.jsx(n.td,{children:"Details"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateBookingClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"✅"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"200"})," ✅"]}),e.jsx(n.td,{children:"—"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/"})}),e.jsx(n.td,{children:"List all"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateBookingClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"✅"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"200"})," ✅"]}),e.jsxs(n.td,{children:["Optional: ",e.jsx(n.code,{inline:"true",children:"roomid"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"PUT"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/{id}"})}),e.jsx(n.td,{children:"Update"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateBookingClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"✅"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"200"})," ✅"]}),e.jsx(n.td,{children:"—"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"DELETE"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/booking/{id}"})}),e.jsx(n.td,{children:"Delete"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateBookingClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"✅"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"202"})," ⚠️"]}),e.jsx(n.td,{children:"Spec: 200. Real: 202 Accepted"})]})]})]})}),`
`,e.jsx(n.h3,{id:"spec-deviations",children:"Spec Deviations"}),`
`,e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Endpoint"}),e.jsx(n.th,{children:"Expected"}),e.jsx(n.th,{children:"Actual"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"POST /booking/"})}),e.jsx(n.td,{children:"200 OK"}),e.jsx(n.td,{children:e.jsx(n.strong,{children:"201 Created"})})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"DELETE /booking/{id}"})}),e.jsx(n.td,{children:"200 OK"}),e.jsx(n.td,{children:e.jsx(n.strong,{children:"202 Accepted"})})]}),e.jsxs(n.tr,{children:[e.jsxs(n.td,{children:[e.jsx(n.code,{inline:"true",children:"GET /booking/-1"})," (negative ID)"]}),e.jsx(n.td,{children:"400 Bad Request"}),e.jsx(n.td,{children:e.jsx(n.strong,{children:"404 Not Found"})})]})]})]}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"service-room",children:"Service: Room"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Base URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3001"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3001/room/v3/api-docs"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Health"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3001/room/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Method"}),e.jsx(n.th,{children:"Path"}),e.jsx(n.th,{children:"Purpose"}),e.jsx(n.th,{children:"Client"}),e.jsx(n.th,{style:{textAlign:"center"},children:"Auth?"}),e.jsx(n.th,{children:"Status"}),e.jsx(n.th,{children:"Notes"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/room/"})}),e.jsx(n.td,{children:"List all"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicRoomClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"❌"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"200"})," ✅"]}),e.jsxs(n.td,{children:["Optional: ",e.jsx(n.code,{inline:"true",children:"checkin"}),", ",e.jsx(n.code,{inline:"true",children:"checkout"})]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/room/{id}"})}),e.jsx(n.td,{children:"Details"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicRoomClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"❌"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"200"})," ✅"]}),e.jsx(n.td,{children:"—"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/room/"})}),e.jsx(n.td,{children:"Create"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateRoomClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"✅"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"201"})," ✅"]}),e.jsxs(n.td,{children:["Requires ",e.jsx(n.code,{inline:"true",children:"roomPrice"})," >= 1"]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"PUT"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/room/{id}"})}),e.jsx(n.td,{children:"Update"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateRoomClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"✅"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"202"})," ⚠️"]}),e.jsx(n.td,{children:"Spec: 200. Real: 202 Accepted"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"DELETE"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/room/{id}"})}),e.jsx(n.td,{children:"Delete"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateRoomClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"✅"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"202"})," ⚠️"]}),e.jsx(n.td,{children:"Spec: 200. Real: 202 Accepted"})]})]})]})}),`
`,e.jsx(n.h3,{id:"spec-deviations-1",children:"Spec Deviations"}),`
`,e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Endpoint"}),e.jsx(n.th,{children:"Expected"}),e.jsx(n.th,{children:"Actual"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsxs(n.td,{children:[e.jsx(n.code,{inline:"true",children:"GET /room/9999"})," (not found)"]}),e.jsx(n.td,{children:"404"}),e.jsx(n.td,{children:e.jsx(n.strong,{children:"500 Internal Server Error"})})]}),e.jsxs(n.tr,{children:[e.jsxs(n.td,{children:[e.jsx(n.code,{inline:"true",children:"GET /room/0"})," (invalid ID)"]}),e.jsx(n.td,{children:"400"}),e.jsx(n.td,{children:e.jsx(n.strong,{children:"500 Internal Server Error"})})]}),e.jsxs(n.tr,{children:[e.jsxs(n.td,{children:[e.jsx(n.code,{inline:"true",children:"GET /room/-1"})," (negative ID)"]}),e.jsx(n.td,{children:"400"}),e.jsx(n.td,{children:e.jsx(n.strong,{children:"404 Not Found"})})]}),e.jsxs(n.tr,{children:[e.jsxs(n.td,{children:[e.jsx(n.code,{inline:"true",children:"POST /room/"})," field ",e.jsx(n.code,{inline:"true",children:"roomPrice"})]}),e.jsx(n.td,{children:"optional"}),e.jsx(n.td,{children:e.jsx(n.strong,{children:"Required >= 1"})})]})]})]}),`
`,e.jsx(n.h3,{id:"serialization",children:"Serialization"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:["All fields in ",e.jsx(n.strong,{children:"camelCase"})," (roomName, type, roomPrice, roomid)"]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.code,{inline:"true",children:"null"})," values for optional fields → 400. Uses ",e.jsx(n.code,{inline:"true",children:"exclude_none=True"})]}),`
`]}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"service-message",children:"Service: Message"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Base URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3006"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3006/message/v3/api-docs"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Health"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3006/message/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Method"}),e.jsx(n.th,{children:"Path"}),e.jsx(n.th,{children:"Purpose"}),e.jsx(n.th,{children:"Client"}),e.jsx(n.th,{style:{textAlign:"center"},children:"Auth?"}),e.jsx(n.th,{children:"Status"}),e.jsx(n.th,{children:"Notes"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/"})}),e.jsx(n.td,{children:"List all"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicMessageClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"❌"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"200"})," ✅"]}),e.jsx(n.td,{children:"—"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/count"})}),e.jsx(n.td,{children:"Count"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicMessageClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"❌"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"200"})," ✅"]}),e.jsx(n.td,{children:"—"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"POST"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/"})}),e.jsx(n.td,{children:"Create"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicMessageClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"❌"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"201"})," ⚠️"]}),e.jsx(n.td,{children:"Spec: 200. Real: 201 Created"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/{id}"})}),e.jsx(n.td,{children:"Details"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicMessageClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"❌"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"200"})," ✅"]}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"Public"}),", no token needed"]})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"PUT"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/{id}/read"})}),e.jsx(n.td,{children:"Mark read"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateMessageClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"✅"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"202"})," ⚠️"]}),e.jsx(n.td,{children:"Spec: 200. Real: 202 Accepted"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"DELETE"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/message/{id}"})}),e.jsx(n.td,{children:"Delete"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateMessageClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"✅"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"202"})," ⚠️"]}),e.jsx(n.td,{children:"Spec: 200. Real: 202 Accepted"})]})]})]})}),`
`,e.jsx(n.h3,{id:"spec-deviations-2",children:"Spec Deviations"}),`
`,e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Endpoint"}),e.jsx(n.th,{children:"Expected"}),e.jsx(n.th,{children:"Actual"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"GET /message/{id}"})}),e.jsx(n.td,{children:"requires token"}),e.jsx(n.td,{children:e.jsx(n.strong,{children:"Public"})})]}),e.jsxs(n.tr,{children:[e.jsxs(n.td,{children:[e.jsx(n.code,{inline:"true",children:"GET /message/9999"})," (not found)"]}),e.jsx(n.td,{children:"404"}),e.jsx(n.td,{children:e.jsx(n.strong,{children:"500 Internal Server Error"})})]})]})]}),`
`,e.jsx(n.h3,{id:"schemas",children:"Schemas"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.code,{inline:"true",children:"MessageSchema"})," (full): messageid, name, email, phone, subject, description"]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.code,{inline:"true",children:"MessageSummarySchema"})," (list): id, name, subject, read — field is ",e.jsx(n.code,{inline:"true",children:"id"}),", not ",e.jsx(n.code,{inline:"true",children:"messageid"})]}),`
`]}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"service-branding",children:"Service: Branding"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Base URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3002"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3002/branding/v3/api-docs"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Health"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3002/branding/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Method"}),e.jsx(n.th,{children:"Path"}),e.jsx(n.th,{children:"Purpose"}),e.jsx(n.th,{children:"Client"}),e.jsx(n.th,{style:{textAlign:"center"},children:"Auth?"}),e.jsx(n.th,{children:"Status"}),e.jsx(n.th,{children:"Notes"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/branding/"})}),e.jsx(n.td,{children:"Get data"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicBrandingClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"❌"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"200"})," ✅"]}),e.jsx(n.td,{children:"—"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"PUT"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/branding/"})}),e.jsx(n.td,{children:"Update"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateBrandingClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"✅"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"202"})," ⚠️"]}),e.jsx(n.td,{children:"Spec: 200. Real: 202 Accepted"})]})]})]})}),`
`,e.jsx(n.h3,{id:"spec-deviations-3",children:"Spec Deviations"}),`
`,e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Endpoint"}),e.jsx(n.th,{children:"Expected"}),e.jsx(n.th,{children:"Actual"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsxs(n.td,{children:[e.jsx(n.code,{inline:"true",children:"PUT /branding/"})," without nested objects"]}),e.jsx(n.td,{children:"—"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"500"})," (NullPointerException on ",e.jsx(n.code,{inline:"true",children:"map"}),")"]})]}),e.jsxs(n.tr,{children:[e.jsxs(n.td,{children:[e.jsx(n.code,{inline:"true",children:"contact.phone"})," in DB"]}),e.jsx(n.td,{children:"VARCHAR(15)"}),e.jsxs(n.td,{children:["Phone > 15 chars → ",e.jsx(n.strong,{children:"500"})]})]})]})]}),`
`,e.jsx(n.h3,{id:"serialization-1",children:"Serialization"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:["All fields in ",e.jsx(n.strong,{children:"camelCase"})," (logoUrl, postTown, postCode)"]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.code,{inline:"true",children:"phone"}),": digits only, optional ",e.jsx(n.code,{inline:"true",children:"+"}),", max 15 chars"]}),`
`]}),`
`,e.jsx(n.hr,{}),`
`,e.jsx(n.h2,{id:"service-report",children:"Service: Report"}),`
`,e.jsxs(n.ul,{children:[`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Base URL"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3005"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Swagger"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3005/report/v3/api-docs"})]}),`
`,e.jsxs(n.li,{children:[e.jsx(n.strong,{children:"Health"}),": ",e.jsx(n.code,{inline:"true",children:"http://localhost:3005/report/actuator/health"})]}),`
`]}),`
`,e.jsx("div",{class:"table-container",children:e.jsxs(n.table,{children:[e.jsx(n.thead,{children:e.jsxs(n.tr,{children:[e.jsx(n.th,{children:"Method"}),e.jsx(n.th,{children:"Path"}),e.jsx(n.th,{children:"Purpose"}),e.jsx(n.th,{children:"Client"}),e.jsx(n.th,{style:{textAlign:"center"},children:"Auth?"}),e.jsx(n.th,{children:"Status"}),e.jsx(n.th,{children:"Notes"})]})}),e.jsxs(n.tbody,{children:[e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/report/room/{id}"})}),e.jsx(n.td,{children:"Room report"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PublicReportClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"❌"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"200"})," ✅"]}),e.jsx(n.td,{children:"Non-existent IDs → 200 with empty list"})]}),e.jsxs(n.tr,{children:[e.jsx(n.td,{children:"GET"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"/report/"})}),e.jsx(n.td,{children:"All reports"}),e.jsx(n.td,{children:e.jsx(n.code,{inline:"true",children:"PrivateReportClient"})}),e.jsx(n.td,{style:{textAlign:"center"},children:"✅"}),e.jsxs(n.td,{children:[e.jsx(n.strong,{children:"200"})," ✅"]}),e.jsx(n.td,{children:"—"})]})]})]})}),`
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
`})]})}function o(i={}){const{wrapper:n}={...t(),...i.components};return n?e.jsx(n,{...i,children:e.jsx(r,{...i})}):r(i)}export{h as __filepath,o as default,d as excerpt,c as frontmatter,l as tableOfContents};
//# sourceMappingURL=overview.en-e3-D0bVC.js.map
