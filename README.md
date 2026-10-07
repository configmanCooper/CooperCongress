# Cooper Congress

A static, responsive website for Cooper Congress, founded by Matthew Cooper. The site introduces its mission and values, the founder and first two scholarship recipients, and the Cooper Congress Scholarship.

**Site:** https://coopercongress.com/

**GitHub repository:** https://github.com/configmanCooper/CooperCongress

## Pages

- `index.html` — home
- `mission.html` — mission and definition of moving society forward
- `values.html` — the three values
- `people.html` — founder and 2025/2026 scholarship recipients
- `scholarship.html` — eligibility, application, and planned 2027 dates
- `404.html` — custom not-found page

All pages are committed as plain HTML. GitHub Pages can serve them without a build step, package manager, or backend. The small `scripts/build.py` script keeps the shared header, footer, and page copy in one place. Edit that script and run `python scripts/build.py` to regenerate all HTML before committing.

## Preview

From this folder:

```powershell
python -m http.server 8000
```

Open `http://localhost:8000/`.

Run `python scripts/check.py` to validate the generated pages and local links.

## GitHub Pages

Pages publishes the `main` branch from `/(root)` with `coopercongress.com` as its custom domain. Pushes to `main` deploy automatically. All internal links and asset paths are document relative, so they work at the custom domain root. `.nojekyll` tells Pages to serve the files directly. The build script generates canonical metadata, `robots.txt`, and `sitemap.xml` for the custom domain.

## Updating the scholarship

The 2027 application and dates in this site were supplied by Matthew Cooper: August 20, 2027 application deadline and September 21, 2027 award date. The currently published [Bold.org listing](https://bold.org/scholarships/cooper-congress-scholarship/) still describes the completed 2026 cycle as of October 7, 2026. Before opening the next cycle, compare the live listing with this site's eligibility, essay prompts, photos, award amount, and dates. Edit the `scholarship` section in `scripts/build.py`, regenerate the HTML, and commit the changes.

Scholarship applications are handled on Bold.org. The site does not collect personal data.

## Content sources

- [Official Cooper Congress Scholarship listing](https://bold.org/scholarships/cooper-congress-scholarship/) — award, criteria, application instructions, and winning applications.
- [Matthew Cooper's Bold.org profile](https://bold.org/donor/matthew-cooper/) — founder background and scholarship purpose.
- [Illinois Lyme Disease Prevention and Protection Act](https://www.ilga.gov/Legislation/ILCS/Articles?ActID=3919&ChapterID=35) — name of the Lauryn Russell law.
- [National Institute for Civil Discourse: Engaging Differences](https://nicd.arizona.edu/wp-content/uploads/2025/04/Engaging-Differences-Core-Principles-and-Best-Practices-KA.pdf) — background on listening, empathy, and intellectual humility.
- [GitHub Pages publishing documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

Winner profiles are original summaries of their public scholarship applications. Verification contacts from the applications are intentionally omitted. The site uses typographic monograms rather than portraits pending image permission and suitable files.

## Future growth

The current site has no account system, calendar, or apps. Shared styles and page templates make it straightforward to add new static pages or downloadable files now. A calendar or authenticated features can later be deployed separately or introduced with a new hosting architecture while retaining these public URLs.
