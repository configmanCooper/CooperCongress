# Cooper Congress website plan

## Purpose and voice

Create a polished public introduction to Cooper Congress: a civic initiative founded by Matthew Cooper that welcomes ideas from any perspective and judges them by their potential to move society forward. Define that as policies that help the United States and the world become more sustainable, resilient, and efficient, while improving quality of life. Use inviting, substantive language without implying formal nonprofit status, membership, policy endorsements, or programs that do not yet exist.

Proposed mission: **Cooper Congress brings people across differences to listen carefully, question respectfully, and advance policies that make the United States and the world more sustainable, resilient, efficient, and livable. Good ideas can come from any perspective; their value lies in the future they help build.**

## Information architecture

- Home: mission, definition of moving society forward, three values, both scholarship winners, clear navigation.
- Mission: fuller explanation of an open, outcome-focused civic approach; four outcomes and a practical framework for evaluating proposals.
- Values: (1) Listen to other perspectives: intentionally leave familiar groups and reflect back what was heard; (2) Be skeptical, but respectful: test claims and tradeoffs without attacking people; (3) Advocate for policies that move society forward: evaluate sustainability, resilience, efficiency, and quality of life. These are aspirations for the initiative, not a claim that a formal review program exists.
- People: Matthew Cooper founder profile; Lauryn Russell (2026) and Finlay Ross (2025) winner profiles. Summarize their publicly supplied work in original prose; link to the primary scholarship page for the full applications. Do not republish third-party verification phone numbers or emails.
- Scholarship: founder confirmed the 2027 cycle will use the same application, August 20 deadline, and September 21 award date. Present 2027 details as founder supplied while distinguishing them from the Bold.org 2026 listing. List eligibility and application steps, three essay prompt themes, 400–600 word essay, 1–5 photos, and link to official Bold.org page. No onsite application form.
- Keep future resources out of navigation until actual downloads exist.

## Research and accuracy

- Primary scholarship source: https://bold.org/scholarships/cooper-congress-scholarship/ — $1,000, one award; 2026 deadline Aug 20 and announcement Sep 21; listed high school seniors or undergraduates, U.S. citizens, fields of law/legislation/political science/public policy/government; volunteer experience preferred; 400–600 words, one of three prompts, 1–5 photos; 2026 winner Lauryn Russell and 2025 winner Finlay Ross.
- Founder information: https://bold.org/donor/matthew-cooper/ — prior Congressional fellow and federal employee; scholarship donor and civic mission. Keep biography concise and avoid unverified career detail.
- Illinois statute: https://www.ilga.gov/Legislation/ILCS/Articles?ActID=3919&ChapterID=35 — verifies the Lauryn Russell Lyme Disease Prevention and Protection Law name.
- Dialogue practices: National Institute for Civil Discourse, https://nicd.arizona.edu/wp-content/uploads/2025/04/Engaging-Differences-Core-Principles-and-Best-Practices-KA.pdf — listening for understanding, curiosity, humility, empathy. Adapt ideas in original wording.
- Hosting guidance: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site — publish a static site from repository root on a selected branch.

## Design and implementation

- Distinctive editorial civic design: warm ivory background, deep ink/navy, restrained copper accent, generous typography, custom geometric motif, crisp card layouts, subtle interaction. Avoid stock political imagery or partisan iconography.
- Responsive layout for phone, tablet, and desktop; readable line lengths and accessible contrast. Semantic HTML, skip link, one H1 per page, keyboard navigation, mobile menu with `aria-expanded`, `aria-current`, visible focus, reduced-motion support, descriptive links, and navigation available without JavaScript. Check 320px and 200% zoom.
- Plain static HTML/CSS with minimal JavaScript for mobile navigation and progressive enhancements. Root-relative independence via document-relative links so GitHub Pages works under a project subpath. No build service, account, analytics, or backend.
- Shared design tokens and components in `assets/css/styles.css`, small `assets/js/main.js`, pages at repository root. Add `.nojekyll`, favicon, README with GitHub Pages steps, and simple content editing guidance. Include room for later event/calendar and application routes without promising functionality now.
- Verify internal links, responsive presentation, accessibility basics, and static serving under a simulated repository subpath. Add unique titles/descriptions and 404 page. Do not publish to GitHub without repository/account details.

## Open editorial questions after implementation

- Matthew's preferred full biography, portrait, and contact channel.
- Whether the full winning essays/applications and portraits should appear on this site, with each winner's permission, or remain linked to Bold.org.
- Whether there is a preferred logo, domain, and GitHub repository name/owner.
