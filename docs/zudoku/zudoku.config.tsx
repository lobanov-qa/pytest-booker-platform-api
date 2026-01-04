// zudoku.config.ts
import type { Navigation, ZudokuConfig } from "zudoku";
import { defaultLanguages } from "zudoku";
import apis from "./apis/_apis.json";
import navigation from "./apis/_navigation.json";

const config: ZudokuConfig = {
  basePath: "/pytest-booker-platform-api/zudoku-doc",
  site: {
    title: "Restful Booker Platform",
    description: "Microservices API Documentation",
  },
  

  theme: {
    noDefaultTheme: true,
    dark: {
      "background": "oklch(19.4% 0.046 244)",
      "foreground": "oklch(89.8% 0.02 260)",
      "muted": "oklch(26.8% 0.011 243)",
      "mutedForeground": "oklch(72.2% 0.019 243)",
      "popover": "oklch(15.6% 0.033 239)",
      "popoverForeground": "oklch(98.3% 0.003 260)",
      "card": "oklch(16.9% 0.037 241)",
      "cardForeground": "oklch(94.1% 0.011 260)",
      "border": "oklch(25.3% 0.06 247)",
      "input": "oklch(28.7% 0.07 248)",
      "primary": "oklch(57.6% 0.053 244)",
      "primaryForeground": "oklch(100% 0 none)",
      "secondary": "oklch(80.3% 0.015 242)",
      "secondaryForeground": "oklch(26.8% 0.011 243)",
      "accent": "oklch(36.7% 0.103 250)",
      "accentForeground": "oklch(86.2% 0.07 243)",
      "destructive": "oklch(58.7% 0.231 30.6)",
      "destructiveForeground": "oklch(100% 0 none)",
      "ring": "oklch(57.6% 0.053 244)",
      "radius": "1rem"
    },
    light: {
      "background": "oklch(98.5% 0 none)",
      "foreground": "oklch(38% 0.035 287)",
      "muted": "oklch(91.9% 0.007 17.3)",
      "mutedForeground": "oklch(40.4% 0.025 18.3)",
      "popover": "oklch(96.2% 0 none)",
      "popoverForeground": "oklch(29% 0.025 287)",
      "card": "oklch(97% 0 none)",
      "cardForeground": "oklch(33.6% 0.03 287)",
      "border": "oklch(94.7% 0 none)",
      "input": "oklch(92.3% 0 none)",
      "primary": "oklch(38% 0.035 287)",
      "primaryForeground": "oklch(90.6% 0.011 288)",
      "secondary": "oklch(79.9% 0.007 289)",
      "secondaryForeground": "oklch(26.5% 0.006 288)",
      "accent": "oklch(86.9% 0 none)",
      "accentForeground": "oklch(35.1% 0 none)",
      "destructive": "oklch(32.5% 0.118 32.1)",
      "destructiveForeground": "oklch(81.2% 0.101 29.1)",
      "ring": "oklch(38% 0.035 287)",
      "radius": "1rem"
    },
  },

  navigation: [
    {
      type: "category",
      label: "Microservices APIs",
      link: "overview",
      items: navigation as Navigation,
    },
  ],

  syntaxHighlighting: {
    languages: [...defaultLanguages, "csv"],
  },

  search: {
    type: "pagefind",
  },

  redirects: [
    { from: "/", to: "/overview" },
    { from: "/api", to: "/overview" },
  ],

  apis: apis as ZudokuConfig["apis"],

  defaults: {
    apis: {
      expandAllTags: true,
      examplesLanguage: "shell",
      disablePlayground: true,
      showVersionSelect: "if-available",
    },
  },

  docs: {
    files: "/pages/**/*.{md,mdx}",
  },

  
};

export default config;
