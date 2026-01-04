import{h as g,S as N,i as y,a as e,_ as c,B as o,m as v,l,k as m,C as b,o as w,p as d,s as S,u as C,w as z,x as $}from"./entry.client-CgeIDkET.js";import{z as h}from"./index-1TbL0HXQ-6tBEOBeo.js";import{R as A}from"./Toc-D_Rj4jVx-s5MM83pY.js";import{S as P,x as R}from"./SchemaView-G-SVXxAG-Ad8mVIET.js";import"./circular-BxODTa7z-BrAwo8Un.js";const I=$(`
  query GetSchemas($input: JSON!, $type: SchemaType!) {
    schema(input: $input, type: $type) {
      title
      description
      summary
      components {
        schemas {
          name
          schema
          extensions
        }
      }
    }
  }
`);function V(){const{input:p,type:x,versions:u,version:t,options:r}=g(),j=N(I,{input:p,type:x}),{data:a}=y(j),i=a.schema.components?.schemas??[],f=Object.entries(u).length>1,n=r?.showVersionSelect==="always"||f&&r?.showVersionSelect!=="hide";return i.length?e.jsxs("div",{className:"grid grid-cols-(--sidecar-grid-cols) gap-8 justify-between","data-pagefind-filter":"section:openapi","data-pagefind-meta":"section:openapi",children:[e.jsx(P,{name:"category",children:a.schema.title}),e.jsxs(c,{children:[e.jsxs("title",{children:["Schemas ",n?t:""]}),e.jsx("meta",{name:"description",content:"List of schemas used by the API."})]}),e.jsxs("div",{className:"pt-(--padding-content-top) pb-(--padding-content-bottom)",children:[e.jsxs(o,{className:"w-full",children:[e.jsxs("div",{className:"flex flex-col gap-y-4 sm:flex-row justify-around items-start sm:items-end",children:[e.jsxs("div",{className:"flex-1",children:[e.jsx(v,{children:a.schema.title}),e.jsxs(l,{level:1,id:"schemas",registerNavigationAnchor:!0,className:"mb-0",children:["Schemas",n&&e.jsxs("span",{className:"text-xl text-muted-foreground ms-1.5",children:["(",t,")"]})]})]}),a.schema.description&&e.jsxs(m,{className:"flex items-center gap-1 text-sm font-medium text-muted-foreground group",children:[e.jsx("span",{children:"API information"}),e.jsx(b,{className:"group-data-[state=open]:hidden translate-y-px",size:14}),e.jsx(w,{className:"group-data-[state=closed]:hidden translate-y-px",size:13})]})]}),a.schema.description&&e.jsx(d,{className:"CollapsibleContent",children:e.jsx("div",{className:"mt-4 max-w-full border rounded-sm bg-muted/25",children:e.jsx(S,{className:"max-w-full prose-img:max-w-prose border-border p-3 lg:p-5",content:a.schema.description})})})]}),e.jsx("hr",{className:"my-8"}),e.jsx("div",{className:"flex flex-col gap-y-5",children:i.map(s=>e.jsxs(o,{className:"group",defaultOpen:!0,children:[e.jsxs(l,{registerNavigationAnchor:!0,level:2,className:"flex items-center gap-1 justify-between w-fit",id:h(s.name),children:[s.name," ",e.jsx(m,{asChild:!0,children:e.jsx(C,{variant:"ghost",size:"icon",className:"size-6",children:e.jsx(z,{size:16,className:"group-data-[state=open]:rotate-90 transition cursor-pointer"})})})]}),e.jsx(d,{className:"mt-4 CollapsibleContent",children:e.jsx(R,{schema:s.schema})})]},s.name))})]}),e.jsx(A,{entries:i.map(s=>({id:h(s.name),value:s.name,depth:1}))})]}):e.jsxs("div",{children:[e.jsxs(c,{children:[e.jsxs("title",{children:["Schemas ",n?t:""]}),e.jsx("meta",{name:"description",content:"List of schemas used by the API."})]}),"No schemas found"]})}export{V as SchemaList};
//# sourceMappingURL=SchemaList-DtyuDrQA-m5YIOmi3.js.map
