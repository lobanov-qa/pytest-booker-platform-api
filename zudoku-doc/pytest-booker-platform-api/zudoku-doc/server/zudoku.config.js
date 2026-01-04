import { defaultLanguages } from "zudoku";
const apis = [
  {
    type: "file",
    input: "./apis/auth.json",
    path: "/api/auth",
    name: "Auth Service",
    description: "Authentication & Authorization - Port 3004",
    options: {
      examplesLanguage: "shell",
      expandAllTags: false,
      schemaDownload: {
        enabled: true
      }
    }
  },
  {
    type: "file",
    input: "./apis/booking.json",
    path: "/api/booking",
    name: "Booking Service",
    description: "Booking Management - Port 3000",
    options: {
      examplesLanguage: "shell",
      expandAllTags: false,
      schemaDownload: {
        enabled: true
      }
    }
  },
  {
    type: "file",
    input: "./apis/room.json",
    path: "/api/room",
    name: "Room Service",
    description: "Room Management - Port 3001",
    options: {
      examplesLanguage: "shell",
      expandAllTags: false,
      schemaDownload: {
        enabled: true
      }
    }
  },
  {
    type: "file",
    input: "./apis/message.json",
    path: "/api/message",
    name: "Message Service",
    description: "Message Management - Port 3006",
    options: {
      examplesLanguage: "shell",
      expandAllTags: false,
      schemaDownload: {
        enabled: true
      }
    }
  },
  {
    type: "file",
    input: "./apis/branding.json",
    path: "/api/branding",
    name: "Branding Service",
    description: "Branding & Settings - Port 3002",
    options: {
      examplesLanguage: "shell",
      expandAllTags: false,
      schemaDownload: {
        enabled: true
      }
    }
  },
  {
    type: "file",
    input: "./apis/report.json",
    path: "/api/report",
    name: "Report Service",
    description: "Reporting & Analytics - Port 3005",
    options: {
      examplesLanguage: "shell",
      expandAllTags: false,
      schemaDownload: {
        enabled: true
      }
    }
  }
];
const navigation = [
  {
    type: "category",
    label: "Microservices",
    description: "Independent services running on different ports",
    collapsible: false,
    icon: "server",
    items: [
      {
        type: "link",
        label: "Auth Service",
        description: "Port 3004 - Authentication & Authorization",
        to: "/api/auth",
        icon: "key"
      },
      {
        type: "link",
        label: "Booking Service",
        description: "Port 3000 - Booking Management",
        to: "/api/booking",
        icon: "calendar"
      },
      {
        type: "link",
        label: "Room Service",
        description: "Port 3001 - Room Management",
        to: "/api/room",
        icon: "home"
      },
      {
        type: "link",
        label: "Message Service",
        description: "Port 3006 - Message Management",
        to: "/api/message",
        icon: "message-square"
      },
      {
        type: "link",
        label: "Branding Service",
        description: "Port 3002 - Branding & Settings",
        to: "/api/branding",
        icon: "palette"
      },
      {
        type: "link",
        label: "Report Service",
        description: "Port 3005 - Reporting & Analytics",
        to: "/api/report",
        icon: "bar-chart"
      }
    ]
  }
];
const config = {
  basePath: "/pytest-booker-platform-api/zudoku-doc",
  site: {
    title: "Restful Booker Platform",
    description: "Microservices API Documentation",
    header: {
      right: [
        {
          type: "html",
          html: `
<a href="/pytest-booker-platform-api/" 
   style="
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 0.9em;
    font-weight: 500;
    color: var(--zuplo-color-primary);
    text-decoration: none;
    padding: 0.25rem 0.75rem;
    border: 1px solid var(--zuplo-border-color);
    border-radius: 6px;
    transition: all 0.2s ease;
  "
   target="_blank"
   title="Go to Test Reports Dashboard">
  🏠 Home
</a>
          `
        }
      ]
    }
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
    }
  },
  navigation: [
    {
      type: "category",
      label: "Microservices APIs",
      link: "overview",
      items: navigation
    }
  ],
  syntaxHighlighting: {
    languages: [...defaultLanguages, "csv"]
  },
  search: {
    type: "pagefind"
  },
  redirects: [
    { from: "/", to: "/overview" },
    { from: "/api", to: "/overview" }
  ],
  apis,
  defaults: {
    apis: {
      expandAllTags: true,
      examplesLanguage: "shell",
      disablePlayground: true,
      showVersionSelect: "if-available"
    }
  },
  docs: {
    files: "/pages/**/*.{md,mdx}"
  }
};
export {
  config as default
};
//# sourceMappingURL=zudoku.config.js.map
