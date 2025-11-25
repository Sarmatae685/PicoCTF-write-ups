import { FullSlug, resolveRelative } from "../util/path"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

const TagList: QuartzComponent = ({ fileData, displayClass }: QuartzComponentProps) => {
  const tags = fileData.frontmatter?.tags
  if (tags && tags.length > 0) {
    return (
      <ul class={classNames(displayClass, "tags")}>
        {tags.map((tag) => {
          const linkDest = resolveRelative(fileData.slug!, `tags/${tag}` as FullSlug)
          return (
            <li>
              <a href={linkDest} class="internal tag-link">
                {tag}
              </a>
            </li>
          )
        })}
      </ul>
    )
  } else {
    return null
  }
}

/* default
TagList.css = `
.tags {
  list-style: none;
  display: flex;
  padding-left: 0;
  gap: 0.4rem;
  margin: 1rem 0;
  flex-wrap: wrap;
}

.section-li > .section > .tags {
  justify-content: flex-end;
}
  
.tags > li {
  display: inline-block;
  white-space: nowrap;
  margin: 0;
  overflow-wrap: normal;
}

a.internal.tag-link {
  border-radius: 8px;
  background-color: var(--highlight);
  padding: 0.2rem 0.4rem;
  margin: 0 0.1rem;
}
`
*/

TagList.css = `
.tags {
  list-style: none;
  display: flex;
  padding-left: 0;
  gap: 0.4rem;
  margin: 1rem 0;
  flex-wrap: wrap;
}

.section-li > .section > .tags {
  justify-content: flex-end;
}
  
.tags > li {
  display: inline-block;
  white-space: nowrap;
  margin: 0;
  overflow-wrap: normal;
}

a.internal.tag-link {
  border-radius: 8px;
  /* За замовчуванням */
  color: var(--secondary);
  background-color: color-mix(in srgb, var(--secondary) 14%, transparent);
  border: 1px solid var(--secondary);
  padding: 0.2rem 0.4rem;
  margin: 0 0.1rem;
  text-decoration: none;
  transition: all 0.2s ease;
  font-weight: 500;

  
  white-space: nowrap;   /* Не переносити текст всередині тегу */
  display: inline-block; /* щоб тег поводився як один блок */
}



/* Категорії - Forensics */
a.internal.tag-link[href*="forensics"] {
  color: #ef4444;
  background-color: rgba(239, 68, 68, 0.14);
  border-color: #ef4444;
}

/* Cryptography */
a.internal.tag-link[href*="cryptography"] {
  color: #8b5cf6;
  background-color: rgba(139, 92, 246, 0.14);
  border-color: #8b5cf6;
}

/* Reverse Engineering */
a.internal.tag-link[href*="reverse-engineering"] {
  color: #ec4899;
  background-color: rgba(236, 72, 153, 0.14);
  border-color: #ec4899;
}

/* Web Exploitation */
a.internal.tag-link[href*="web-exploitation"] {
  color: #3b82f6;
  background-color: rgba(59, 130, 246, 0.14);
  border-color: #3b82f6;
}

/* Binary Exploitation */
a.internal.tag-link[href*="binary-exploitation"] {
  color: #f59e0b;
  background-color: rgba(245, 158, 11, 0.14);
  border-color: #f59e0b;
}

/* Складність - Easy */
a.internal.tag-link[href*="easy"] {
  color: #10b981;
  background-color: rgba(16, 185, 129, 0.14);
  border-color: #10b981;
}

/* Medium */
a.internal.tag-link[href*="medium"] {
  color: #f59e0b;
  background-color: rgba(245, 158, 11, 0.14);
  border-color: #f59e0b;
}

/* Hard */
a.internal.tag-link[href*="hard"] {
  color: #ef4444;
  background-color: rgba(239, 68, 68, 0.14);
  border-color: #ef4444;
}

/* Інструменти */
a.internal.tag-link[href*="sleuthkit"],
a.internal.tag-link[href*="wireshark"],
a.internal.tag-link[href*="ghidra"] {
  color: #6366f1;
  background-color: rgba(99, 102, 241, 0.14);
  border-color: #6366f1;
}

/* Hover - текст стає яскравішим, фон трохи темніший */
a.internal.tag-link:hover {
  background-color: color-mix(in srgb, currentColor 20%, transparent);
  transform: translateY(-1px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.15);
}
`

export default (() => TagList) satisfies QuartzComponentConstructor
