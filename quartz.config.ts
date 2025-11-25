import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "PicoCTF Write-ups",
    // pageTitleSuffix: "| Sarmatae685",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl: "sarmatae685.github.io/picoctf",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "created", // буде показувати дату, коли я вирішив завдання (бере з тегу created). Якщо created-тегу немає, то Quartz використає modified (дата останньої зміни)
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        /*
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
        */
        header: "JetBrains Mono",      // Моноширинний для tech-look
        body: "Inter",                  // Сучасний, читабельний
        code: "Fira Code",              // З лігатурами для коду
      },
      colors: {
        lightMode: {
          /*
          light: "#faf8f8",
          lightgray: "#e5e5e5",
          gray: "#b8b8b8",
          darkgray: "#4e4e4e",
          dark: "#2b2b2b",
          secondary: "#284b63",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#fff23688",
          */
          light: "#fafafa",
          lightgray: "#e7e7e7",
          gray: "#9f9f9f",
          darkgray: "#4a4a4a",
          dark: "#1a1a1a",
          secondary: "#8b5cf6",         // Фіолетовий (cyber)
          tertiary: "#ec4899",          // Рожевий (акцент)
          highlight: "rgba(139, 92, 246, 0.1)",
          textHighlight: "#fde68a88",
        },
        darkMode: {
          /*
          light: "#161618",
          lightgray: "#393639",
          gray: "#646464",
          darkgray: "#d4d4d4",
          dark: "#ebebec",
          secondary: "#7b97aa",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#b3aa0288",
          */
          light: "#0a0a0f",
          lightgray: "#1a1a24",
          gray: "#6b7280",
          darkgray: "#d1d5db",
          dark: "#f3f4f6",
          secondary: "#a78bfa",         // Світло-фіолетовий
          tertiary: "#f472b6",          // Світло-рожевий
          highlight: "rgba(167, 139, 250, 0.15)",
          textHighlight: "#fbbf2488",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      // Plugin.CustomOgImages(),
    ],
  },
}

export default config
