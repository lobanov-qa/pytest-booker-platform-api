import { jsx, jsxs } from "react/jsx-runtime";
import { Transform } from "node:stream";
import { QueryClient, dehydrate } from "@tanstack/react-query";
import "loglevel";
import { renderToPipeableStream, renderToStaticMarkup } from "react-dom/server";
import { createStaticHandler, isRouteErrorResponse, createStaticRouter } from "react-router";
import { RouterError, Meta, RouteGuard, BuildCheck, StatusPage, Layout, ServerError, BootstrapStatic } from "zudoku/__internal";
import "react";
import config from "./zudoku.config.js";
import { openApiPlugin } from "zudoku/plugins/openapi";
import { customPagesPlugin } from "zudoku/plugins/custom-pages";
import { markdownPlugin } from "zudoku/plugins/markdown";
import { Key, Calendar, Home, MessageSquare, Palette, BarChart, Server } from "zudoku/icons";
import { redirectPlugin } from "zudoku/plugins/redirect";
import { pagefindSearchPlugin } from "zudoku/plugins/search-pagefind";
import { Zudoku } from "zudoku/components";
import { Outlet } from "zudoku/router";
import { transformerMetaHighlight, transformerMetaWordHighlight } from "@shikijs/transformers";
import { createHighlighterCore } from "shiki/core";
import { createJavaScriptRegexEngine } from "shiki/engine/javascript";
import "clsx";
import { z } from "zod";
import "zudoku";
const NO_DEHYDRATE = "no-dehydrate";
const configuredApiPlugins = [];
const configuredApiCatalogPlugins = [];
const apis = Array.isArray(config.apis) ? config.apis : [config.apis];
configuredApiPlugins.push(openApiPlugin({
  type: "file",
  input: [{ "path": "v0", "label": "v0", "input": "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/auth.json" }],
  path: "/api/auth",
  tagPages: ["auth-controller"],
  options: {
    examplesLanguage: config.defaults?.apis?.examplesLanguage ?? config.defaults?.examplesLanguage,
    supportedLanguages: config.defaults?.apis?.supportedLanguages,
    disablePlayground: config.defaults?.apis?.disablePlayground,
    disableSidecar: config.defaults?.apis?.disableSidecar,
    showVersionSelect: config.defaults?.apis?.showVersionSelect ?? "if-available",
    expandAllTags: config.defaults?.apis?.expandAllTags ?? true,
    expandApiInformation: config.defaults?.apis?.expandApiInformation ?? false,
    schemaDownload: config.defaults?.apis?.schemaDownload,
    transformExamples: config.defaults?.apis?.transformExamples,
    generateCodeSnippet: config.defaults?.apis?.generateCodeSnippet,
    ...apis[0].options ?? {}
  },
  schemaImports: {
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/auth.json": () => import("./assets/api_auth-auth.json-DMyuoHSx.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/booking.json": () => import("./assets/api_booking-booking.json-AUzkorEj.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/room.json": () => import("./assets/api_room-room.json-DYDZYagI.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/message.json": () => import("./assets/api_message-message.json-_vBQBkWT.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/branding.json": () => import("./assets/api_branding-branding.json-C4lP229q.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/report.json": () => import("./assets/api_report-report.json-D-WT2iIa.js")
  }
}));
configuredApiPlugins.push(openApiPlugin({
  type: "file",
  input: [{ "path": "v0", "label": "v0", "input": "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/booking.json" }],
  path: "/api/booking",
  tagPages: ["booking-controller"],
  options: {
    examplesLanguage: config.defaults?.apis?.examplesLanguage ?? config.defaults?.examplesLanguage,
    supportedLanguages: config.defaults?.apis?.supportedLanguages,
    disablePlayground: config.defaults?.apis?.disablePlayground,
    disableSidecar: config.defaults?.apis?.disableSidecar,
    showVersionSelect: config.defaults?.apis?.showVersionSelect ?? "if-available",
    expandAllTags: config.defaults?.apis?.expandAllTags ?? true,
    expandApiInformation: config.defaults?.apis?.expandApiInformation ?? false,
    schemaDownload: config.defaults?.apis?.schemaDownload,
    transformExamples: config.defaults?.apis?.transformExamples,
    generateCodeSnippet: config.defaults?.apis?.generateCodeSnippet,
    ...apis[1].options ?? {}
  },
  schemaImports: {
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/auth.json": () => import("./assets/api_auth-auth.json-DMyuoHSx.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/booking.json": () => import("./assets/api_booking-booking.json-AUzkorEj.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/room.json": () => import("./assets/api_room-room.json-DYDZYagI.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/message.json": () => import("./assets/api_message-message.json-_vBQBkWT.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/branding.json": () => import("./assets/api_branding-branding.json-C4lP229q.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/report.json": () => import("./assets/api_report-report.json-D-WT2iIa.js")
  }
}));
configuredApiPlugins.push(openApiPlugin({
  type: "file",
  input: [{ "path": "v0", "label": "v0", "input": "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/room.json" }],
  path: "/api/room",
  tagPages: ["room-controller"],
  options: {
    examplesLanguage: config.defaults?.apis?.examplesLanguage ?? config.defaults?.examplesLanguage,
    supportedLanguages: config.defaults?.apis?.supportedLanguages,
    disablePlayground: config.defaults?.apis?.disablePlayground,
    disableSidecar: config.defaults?.apis?.disableSidecar,
    showVersionSelect: config.defaults?.apis?.showVersionSelect ?? "if-available",
    expandAllTags: config.defaults?.apis?.expandAllTags ?? true,
    expandApiInformation: config.defaults?.apis?.expandApiInformation ?? false,
    schemaDownload: config.defaults?.apis?.schemaDownload,
    transformExamples: config.defaults?.apis?.transformExamples,
    generateCodeSnippet: config.defaults?.apis?.generateCodeSnippet,
    ...apis[2].options ?? {}
  },
  schemaImports: {
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/auth.json": () => import("./assets/api_auth-auth.json-DMyuoHSx.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/booking.json": () => import("./assets/api_booking-booking.json-AUzkorEj.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/room.json": () => import("./assets/api_room-room.json-DYDZYagI.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/message.json": () => import("./assets/api_message-message.json-_vBQBkWT.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/branding.json": () => import("./assets/api_branding-branding.json-C4lP229q.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/report.json": () => import("./assets/api_report-report.json-D-WT2iIa.js")
  }
}));
configuredApiPlugins.push(openApiPlugin({
  type: "file",
  input: [{ "path": "v0", "label": "v0", "input": "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/message.json" }],
  path: "/api/message",
  tagPages: ["message-controller"],
  options: {
    examplesLanguage: config.defaults?.apis?.examplesLanguage ?? config.defaults?.examplesLanguage,
    supportedLanguages: config.defaults?.apis?.supportedLanguages,
    disablePlayground: config.defaults?.apis?.disablePlayground,
    disableSidecar: config.defaults?.apis?.disableSidecar,
    showVersionSelect: config.defaults?.apis?.showVersionSelect ?? "if-available",
    expandAllTags: config.defaults?.apis?.expandAllTags ?? true,
    expandApiInformation: config.defaults?.apis?.expandApiInformation ?? false,
    schemaDownload: config.defaults?.apis?.schemaDownload,
    transformExamples: config.defaults?.apis?.transformExamples,
    generateCodeSnippet: config.defaults?.apis?.generateCodeSnippet,
    ...apis[3].options ?? {}
  },
  schemaImports: {
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/auth.json": () => import("./assets/api_auth-auth.json-DMyuoHSx.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/booking.json": () => import("./assets/api_booking-booking.json-AUzkorEj.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/room.json": () => import("./assets/api_room-room.json-DYDZYagI.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/message.json": () => import("./assets/api_message-message.json-_vBQBkWT.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/branding.json": () => import("./assets/api_branding-branding.json-C4lP229q.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/report.json": () => import("./assets/api_report-report.json-D-WT2iIa.js")
  }
}));
configuredApiPlugins.push(openApiPlugin({
  type: "file",
  input: [{ "path": "v0", "label": "v0", "input": "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/branding.json" }],
  path: "/api/branding",
  tagPages: ["branding-controller"],
  options: {
    examplesLanguage: config.defaults?.apis?.examplesLanguage ?? config.defaults?.examplesLanguage,
    supportedLanguages: config.defaults?.apis?.supportedLanguages,
    disablePlayground: config.defaults?.apis?.disablePlayground,
    disableSidecar: config.defaults?.apis?.disableSidecar,
    showVersionSelect: config.defaults?.apis?.showVersionSelect ?? "if-available",
    expandAllTags: config.defaults?.apis?.expandAllTags ?? true,
    expandApiInformation: config.defaults?.apis?.expandApiInformation ?? false,
    schemaDownload: config.defaults?.apis?.schemaDownload,
    transformExamples: config.defaults?.apis?.transformExamples,
    generateCodeSnippet: config.defaults?.apis?.generateCodeSnippet,
    ...apis[4].options ?? {}
  },
  schemaImports: {
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/auth.json": () => import("./assets/api_auth-auth.json-DMyuoHSx.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/booking.json": () => import("./assets/api_booking-booking.json-AUzkorEj.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/room.json": () => import("./assets/api_room-room.json-DYDZYagI.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/message.json": () => import("./assets/api_message-message.json-_vBQBkWT.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/branding.json": () => import("./assets/api_branding-branding.json-C4lP229q.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/report.json": () => import("./assets/api_report-report.json-D-WT2iIa.js")
  }
}));
configuredApiPlugins.push(openApiPlugin({
  type: "file",
  input: [{ "path": "v0", "label": "v0", "input": "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/report.json" }],
  path: "/api/report",
  tagPages: ["report-controller"],
  options: {
    examplesLanguage: config.defaults?.apis?.examplesLanguage ?? config.defaults?.examplesLanguage,
    supportedLanguages: config.defaults?.apis?.supportedLanguages,
    disablePlayground: config.defaults?.apis?.disablePlayground,
    disableSidecar: config.defaults?.apis?.disableSidecar,
    showVersionSelect: config.defaults?.apis?.showVersionSelect ?? "if-available",
    expandAllTags: config.defaults?.apis?.expandAllTags ?? true,
    expandApiInformation: config.defaults?.apis?.expandApiInformation ?? false,
    schemaDownload: config.defaults?.apis?.schemaDownload,
    transformExamples: config.defaults?.apis?.transformExamples,
    generateCodeSnippet: config.defaults?.apis?.generateCodeSnippet,
    ...apis[5].options ?? {}
  },
  schemaImports: {
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/auth.json": () => import("./assets/api_auth-auth.json-DMyuoHSx.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/booking.json": () => import("./assets/api_booking-booking.json-AUzkorEj.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/room.json": () => import("./assets/api_room-room.json-DYDZYagI.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/message.json": () => import("./assets/api_message-message.json-_vBQBkWT.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/branding.json": () => import("./assets/api_branding-branding.json-C4lP229q.js"),
    "/home/runner/work/pytest-booker-platform-api/pytest-booker-platform-api/docs/zudoku/apis/report.json": () => import("./assets/api_report-report.json-D-WT2iIa.js")
  }
}));
const configuredCustomPagesPlugin = customPagesPlugin(config.navigation);
const fileImports = {
  "/overview": () => import("./assets/overview-DnCQPls6.js"),
  "/overview.en": () => import("./assets/overview.en-Bvkx9evZ.js")
};
const configuredDocsPlugin = markdownPlugin({
  basePath: "/pytest-booker-platform-api/zudoku-doc",
  fileImports,
  defaultOptions: void 0
});
const configuredNavigation = [
  {
    type: "category",
    label: "Microservices APIs",
    link: {
      type: "doc",
      file: "overview",
      label: "Матрица доступа к API Restful-Booker-Platform",
      icon: void 0,
      path: "overview"
    },
    items: [
      {
        type: "category",
        label: "Microservices",
        description: "Independent services running on different ports",
        collapsible: false,
        icon: Server,
        items: [
          {
            type: "link",
            label: "Auth Service",
            description: "Port 3004 - Authentication & Authorization",
            to: "/api/auth",
            icon: Key
          },
          {
            type: "link",
            label: "Booking Service",
            description: "Port 3000 - Booking Management",
            to: "/api/booking",
            icon: Calendar
          },
          {
            type: "link",
            label: "Room Service",
            description: "Port 3001 - Room Management",
            to: "/api/room",
            icon: Home
          },
          {
            type: "link",
            label: "Message Service",
            description: "Port 3006 - Message Management",
            to: "/api/message",
            icon: MessageSquare
          },
          {
            type: "link",
            label: "Branding Service",
            description: "Port 3002 - Branding & Settings",
            to: "/api/branding",
            icon: Palette
          },
          {
            type: "link",
            label: "Report Service",
            description: "Port 3005 - Reporting & Analytics",
            to: "/api/report",
            icon: BarChart
          }
        ],
        link: void 0
      }
    ]
  }
];
const redirects = [
  {
    "from": "/",
    "to": "/overview"
  },
  {
    "from": "/api",
    "to": "/overview"
  }
];
const configuredRedirectPlugin = redirectPlugin({ redirects });
const configuredSearchPlugin = pagefindSearchPlugin(config.search);
const registerShiki = async (highlighter2) => {
  await Promise.all([
    highlighter2.loadTheme(
      import("zudoku/shiki/themes/github-light"),
      import("zudoku/shiki/themes/github-dark")
    ),
    highlighter2.loadLanguage(
      import("zudoku/shiki/langs/shellscript"),
      import("zudoku/shiki/langs/javascript"),
      import("zudoku/shiki/langs/jsx"),
      import("zudoku/shiki/langs/typescript"),
      import("zudoku/shiki/langs/tsx"),
      import("zudoku/shiki/langs/graphql"),
      import("zudoku/shiki/langs/jsonc"),
      import("zudoku/shiki/langs/json"),
      import("zudoku/shiki/langs/python"),
      import("zudoku/shiki/langs/java"),
      import("zudoku/shiki/langs/go"),
      import("zudoku/shiki/langs/csharp"),
      import("zudoku/shiki/langs/kotlin"),
      import("zudoku/shiki/langs/objective-c"),
      import("zudoku/shiki/langs/php"),
      import("zudoku/shiki/langs/ruby"),
      import("zudoku/shiki/langs/swift"),
      import("zudoku/shiki/langs/css"),
      import("zudoku/shiki/langs/html"),
      import("zudoku/shiki/langs/xml"),
      import("zudoku/shiki/langs/yaml"),
      import("zudoku/shiki/langs/toml"),
      import("zudoku/shiki/langs/rust"),
      import("zudoku/shiki/langs/markdown"),
      import("zudoku/shiki/langs/mdx"),
      import("zudoku/shiki/langs/zig"),
      import("zudoku/shiki/langs/scala"),
      import("zudoku/shiki/langs/dart"),
      import("zudoku/shiki/langs/ocaml"),
      import("zudoku/shiki/langs/c"),
      import("zudoku/shiki/langs/cpp"),
      import("zudoku/shiki/langs/common-lisp"),
      import("zudoku/shiki/langs/elixir"),
      import("zudoku/shiki/langs/powershell"),
      import("zudoku/shiki/langs/csv")
    )
  ]);
};
const isNavigationPlugin = (obj) => "getRoutes" in obj && typeof obj.getRoutes === "function";
const engine = createJavaScriptRegexEngine({ forgiving: true });
const shikiPromise = createHighlighterCore({
  engine,
  langAlias: {
    markup: "html",
    svg: "xml",
    mathml: "xml",
    atom: "xml",
    ssml: "xml",
    rss: "xml",
    webmanifest: "json"
  }
});
const highlighter = await shikiPromise;
({
  transformers: [transformerMetaHighlight(), transformerMetaWordHighlight()]
});
const EntitlementsSchema = z.object({
  devPortalZuploBranding: z.boolean(),
  numberOfProjects: z.number(),
  numberOfUsers: z.number(),
  egressGbPerMonth: z.number(),
  requestsPerMonth: z.number(),
  numberOfApiKeys: z.number(),
  customDomains: z.number(),
  advancedAnalyticsEnabled: z.boolean(),
  devPortalAnalyticsEnabled: z.boolean(),
  premiumSupport: z.boolean(),
  emergencyPhoneSupport: z.boolean(),
  rbacEnabled: z.boolean(),
  onPremEnabled: z.boolean(),
  largeBuildRunners: z.boolean()
});
z.object({
  entitlements: EntitlementsSchema,
  environmentType: z.string().optional(),
  deploymentName: z.string(),
  deploymentUrl: z.string().optional(),
  projectId: z.string().optional(),
  projectType: z.string().optional(),
  sourceType: z.string().optional(),
  accountName: z.string().optional(),
  projectName: z.string().optional()
});
const getZuploBuildConfig = () => {
  return void 0;
};
const ZuploEnv = {
  buildConfig: getZuploBuildConfig()
};
await registerShiki(highlighter);
const convertZudokuConfigToOptions = (config2) => {
  return {
    basePath: config2.basePath,
    canonicalUrlOrigin: config2.canonicalUrlOrigin,
    protectedRoutes: config2.protectedRoutes,
    site: {
      ...config2.site,
      showPoweredBy: ZuploEnv.buildConfig?.entitlements.devPortalZuploBranding ?? config2.site?.showPoweredBy,
      logo: config2.site?.logo
    },
    slots: config2.slots,
    metadata: {
      favicon: "https://cdn.zudoku.dev/logos/favicon.svg",
      title: "%s - Zudoku",
      ...config2.metadata
    },
    navigation: configuredNavigation,
    mdx: config2.mdx,
    plugins: [
      ...[],
      ...configuredDocsPlugin ? [configuredDocsPlugin] : [],
      ...configuredApiPlugins,
      ...configuredSearchPlugin ? [configuredSearchPlugin] : [],
      ...configuredRedirectPlugin ? [configuredRedirectPlugin] : [],
      ...[],
      ...configuredCustomPagesPlugin ? [configuredCustomPagesPlugin] : [],
      ...configuredApiCatalogPlugins,
      ...config2.plugins ?? []
    ],
    syntaxHighlighting: {
      highlighter,
      themes: config2.syntaxHighlighting?.themes
    }
  };
};
const getRoutesByOptions = (options, enableStatusPages = true) => {
  const allPlugins = [
    ...options.plugins ?? [],
    ...options.authentication ? [options.authentication] : []
  ];
  const routes = allPlugins.flatMap((plugin) => isNavigationPlugin(plugin) ? plugin.getRoutes() : []).concat(
    enableStatusPages ? [400, 404, 500].map((statusCode) => ({
      path: `/${statusCode}`,
      element: /* @__PURE__ */ jsx(StatusPage, { statusCode })
    })) : []
  ).concat([{ path: "*", element: /* @__PURE__ */ jsx(StatusPage, { statusCode: 404 }) }]).map((route) => ({
    ...route,
    errorElement: /* @__PURE__ */ jsx(RouterError, { className: "w-full m-0" })
  }));
  return routes;
};
const getRoutesByConfig = (config2) => {
  const options = convertZudokuConfigToOptions(config2);
  const routes = getRoutesByOptions(
    options,
    config2.enableStatusPages
  );
  return [
    {
      element: /* @__PURE__ */ jsxs(Zudoku, { ...options, children: [
        /* @__PURE__ */ jsx(
          BuildCheck,
          {
            buildId: void 0,
            environmentType: void 0
          }
        ),
        /* @__PURE__ */ jsx(Outlet, {})
      ] }),
      hydrateFallbackElement: /* @__PURE__ */ jsx("div", { children: "Loading..." }),
      children: [
        {
          element: /* @__PURE__ */ jsx(Meta, { children: /* @__PURE__ */ jsx(RouteGuard, {}) }),
          errorElement: /* @__PURE__ */ jsx(RouterError, {}),
          children: routes.map(
            (r) => r.handle?.layout === "none" ? r : wrapWithLayout(r)
          )
        }
      ]
    }
  ];
};
const wrapWithLayout = (route) => {
  return {
    element: /* @__PURE__ */ jsx(Layout, {}),
    children: [route]
  };
};
const render = async ({
  template,
  request: baseRequest,
  response,
  routes,
  basePath,
  bypassProtection
}) => {
  const { query, dataRoutes } = createStaticHandler(routes, {
    basename: basePath
  });
  const queryClient = new QueryClient();
  const request = baseRequest instanceof Request ? baseRequest : createFetchRequest(baseRequest, response);
  const context = await query(request);
  let status = 200;
  if (context instanceof Response) {
    if ([301, 302, 303, 307, 308].includes(context.status)) {
      return response.redirect(
        context.status,
        context.headers.get("Location") ?? ""
      );
    }
    throw context;
  } else if (context.errors) {
    const firstError = Object.values(context.errors).find(isRouteErrorResponse);
    if (firstError?.status) {
      status = firstError.status;
    }
  }
  const router = createStaticRouter(dataRoutes, context);
  const helmetContext = {};
  const App = /* @__PURE__ */ jsx(
    BootstrapStatic,
    {
      router,
      context,
      queryClient,
      helmetContext,
      bypassProtection
    }
  );
  const { pipe } = renderToPipeableStream(App, {
    onShellError(error) {
      response.status(500);
      response.set({ "Content-Type": "text/html" });
      const html = renderToStaticMarkup(/* @__PURE__ */ jsx(ServerError, { error }));
      response.send(html);
    },
    onAllReady() {
      response.set({ "Content-Type": "text/html" });
      response.status(status);
      const transformStream = new Transform({
        transform(chunk, encoding, callback) {
          response.write(chunk, encoding);
          callback();
        }
      });
      const [htmlStart, htmlEnd] = template.split("<!--app-html-->");
      if (!htmlStart) {
        throw new Error("No <!--app-html--> found in template");
      }
      response.write(
        htmlStart.replace(
          "<!--app-helmet-->",
          [
            helmetContext.helmet.title.toString(),
            helmetContext.helmet.meta.toString(),
            helmetContext.helmet.link.toString(),
            helmetContext.helmet.style.toString(),
            helmetContext.helmet.script.toString()
          ].join("\n")
        )
      );
      transformStream.on("finish", () => {
        const dehydrated = dehydrate(queryClient, {
          shouldDehydrateQuery: (query2) => !query2.queryKey.includes(NO_DEHYDRATE)
        });
        if (!htmlEnd) return response.end();
        const closingTag = "</body>";
        const idx = htmlEnd.lastIndexOf(closingTag);
        if (idx === -1) return response.end(htmlEnd);
        const serialized = JSON.stringify(dehydrated).replace(/</g, "\\u003c").replace(/>/g, "\\u003e");
        response.write(htmlEnd.slice(0, idx));
        response.write("<script>window.DATA=");
        response.write(serialized);
        response.write("<\/script>");
        response.end(htmlEnd.slice(idx));
      });
      pipe(transformStream);
    },
    onError(error) {
      status = 500;
      {
        throw error;
      }
    }
  });
};
function createFetchRequest(req, res) {
  const origin = `${req.protocol}://${req.get("host")}`;
  const url = new URL(req.originalUrl || req.url, origin);
  const controller = new AbortController();
  res.on("close", () => controller.abort());
  const headers = new Headers();
  for (const [key, values] of Object.entries(req.headers)) {
    if (values) {
      if (Array.isArray(values)) {
        for (const value of values) {
          headers.append(key, value);
        }
      } else {
        headers.set(key, values);
      }
    }
  }
  const init = {
    method: req.method,
    headers,
    signal: controller.signal
  };
  if (req.method !== "GET" && req.method !== "HEAD") {
    init.body = req.body;
  }
  return new Request(url.href, init);
}
export {
  createFetchRequest,
  getRoutesByConfig,
  render
};
//# sourceMappingURL=entry.server.js.map
