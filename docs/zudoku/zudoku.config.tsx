// zudoku.config.ts
import type { Navigation, ZudokuConfig } from "zudoku";
import { defaultLanguages } from "zudoku";
import apis from "./apis/_apis.json";
import navigation from "./apis/_navigation.json";

const config: ZudokuConfig = {
  basePath: "/pytest-booker-platform-api/zudoku-doc",
  site: {
    title: "Restful Booker Platform Documentation",
    description: "Microservices API Documentation",
  },
  

  theme: {
    noDefaultTheme: true,
    light: {
      "background": "#f1f5f7",
      "foreground": "#010a18d4",
      "card": "#ffffff",
      "cardForeground": "#010a18d4",
      "popover": "#ffffff",
      "popoverForeground": "#010a18d4",
      "primary": "#2c67e8",
      "primaryForeground": "#ffffff",
      "secondary": "#eef2f6",
      "secondaryForeground": "#010a18d4",
      "muted": "#f1f5f7",
      "mutedForeground": "#0316308f",
      "accent": "#eef2f6",
      "accentForeground": "#010a18d4",
      "destructive": "#e8392c",
      "destructiveForeground": "#ffffff",
      "border": "#0b376a29",
      "input": "#e3e8ef",
      "ring": "#2c67e8",
      "radius": "1rem"
    },
    dark: {
      "background": "#2a2f38",
      "foreground": "#fcfcfd",
      "card": "#1e2229",
      "cardForeground": "#fcfcfd",
      "popover": "#1e2229",
      "popoverForeground": "#fcfcfd",
      "primary": "#7aa8ff",
      "primaryForeground": "#fcfcfd",
      "secondary": "#2a2f38",
      "secondaryForeground": "#cedff84d",
      "muted": "#282B34",
      "mutedForeground": "#bed7f836",
      "accent": "#363c47",
      "accentForeground": "#fcfcfd",
      "destructive": "#ff584d",
      "destructiveForeground": "#fcfcfd",
      "border": "#3d4450",
      "input": "#364152",
      "ring": "#7aa8ff",
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
