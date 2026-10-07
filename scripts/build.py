"""Build the committed static HTML pages. Requires only Python 3."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHOLARSHIP_URL = "https://bold.org/scholarships/cooper-congress-scholarship/"
SITE_URL = "https://coopercongress.com/"

NAV = [
    ("index.html", "Home"),
    ("mission.html", "Mission"),
    ("values.html", "Values"),
    ("people.html", "People"),
    ("scholarship.html", "Scholarship"),
]


def link(url, label, css="", external=False):
    extra = ' target="_blank" rel="noopener noreferrer"' if external else ""
    cl = f' class="{css}"' if css else ""
    return f'<a href="{url}"{cl}{extra}>{label}</a>'


def layout(page, title, description, body):
    canonical = SITE_URL if page == "index.html" else SITE_URL + page
    robots = '  <meta name="robots" content="noindex">\n' if page == "404.html" else ""
    nav = "".join(
        f'<a href="./{url}"{current}>{label}</a>'
        for url, label in NAV
        for current in [' aria-current="page"' if page == url else ""]
    )
    document = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#142b35">
  <meta name="description" content="{escape(description, quote=True)}">
  <title>{escape(title)} | Cooper Congress</title>
{robots}  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(title, quote=True)} | Cooper Congress">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta property="og:url" content="{canonical}">
  <link rel="icon" type="image/svg+xml" href="./assets/images/favicon.svg">
  <link rel="stylesheet" href="./assets/css/styles.css">
  <script defer src="./assets/js/main.js"></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="header-inner shell">
      <a class="brand" href="./index.html" aria-label="Cooper Congress home">
        <span class="brand-mark" aria-hidden="true"><span>C</span><span>C</span></span>
        <span class="brand-name">Cooper<br>Congress</span>
      </a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open navigation">
        <span></span><span></span><span></span>
      </button>
      <nav id="site-nav" class="site-nav" aria-label="Main navigation">{nav}</nav>
    </div>
  </header>
  <main id="main">{body}</main>
  <footer class="site-footer">
    <div class="shell footer-main">
      <div>
        <a class="footer-brand" href="./index.html">Cooper Congress<span class="brand-dot">.</span></a>
        <p>A place for serious ideas and open minds.</p>
      </div>
      <nav aria-label="Footer navigation">
        <a href="./mission.html">Mission</a>
        <a href="./values.html">Values</a>
        <a href="./people.html">People</a>
        <a href="./scholarship.html">Scholarship</a>
      </nav>
      <div class="footer-action">
        <span class="eyebrow">The scholarship</span>
        {link(SCHOLARSHIP_URL, 'View on Bold.org <span aria-hidden="true">↗</span>', external=True)}
      </div>
    </div>
    <div class="shell footer-bottom"><span>© <span id="year">2026</span> Cooper Congress</span><span>Founded by Matthew Cooper</span></div>
  </footer>
</body>
</html>
"""
    (ROOT / page).write_text(document, encoding="utf-8")


def section_intro(number, kicker, title, text):
    return f"""<div class="section-heading">
      <div class="section-index"><span>{number}</span><span>{kicker}</span></div>
      <div><h2>{title}</h2><p>{text}</p></div>
    </div>"""


home = f"""
<section class="hero home-hero">
  <div class="shell hero-grid">
    <div class="hero-copy">
      <div class="eyebrow"><span class="eyebrow-line"></span> Ideas across differences</div>
      <h1>Better policy begins with <em>better listening.</em></h1>
      <p class="lead">Cooper Congress brings people across differences to listen carefully, question respectfully, and advance policies that move society forward.</p>
      <div class="button-row">
        {link('./mission.html', 'Explore our mission <span aria-hidden="true">↗</span>', 'button button-dark')}
        {link('./values.html', 'What we believe <span aria-hidden="true">→</span>', 'text-link')}
      </div>
      <div class="hero-caption"><span class="tiny-rule"></span> Founded by Matthew Cooper <span class="caption-divider">/</span> Open to every perspective</div>
    </div>
    <div class="hero-art" role="img" aria-label="Abstract lines converging on common ground: listen, examine, advance">
      <div class="art-orbit art-orbit-one"></div>
      <div class="art-orbit art-orbit-two"></div>
      <div class="art-orbit art-orbit-three"></div>
      <div class="art-center"><span>COMMON<br>GROUND</span><i></i></div>
      <div class="art-label art-label-left">01 / Listen</div>
      <div class="art-label art-label-middle">02 / Examine</div>
      <div class="art-label art-label-right">03 / Advance</div>
    </div>
  </div>
</section>

<section class="statement-band">
  <div class="shell statement-inner">
    <span class="eyebrow light">Our principle</span>
    <p>Good ideas can come from <em>any perspective.</em> Their value lies in the future they help build.</p>
    <a href="./mission.html" aria-label="Read the Cooper Congress mission">Read the mission <span aria-hidden="true">↗</span></a>
  </div>
</section>

<section class="section section-outcomes">
  <div class="shell">
    {section_intro('01', 'The direction', 'What does “forward” mean?', 'We look toward outcomes that matter in everyday life, in the United States and around the world.')}
    <div class="outcome-grid">
      <article class="outcome-card"><span class="card-number">01</span><svg class="outcome-symbol" viewBox="0 0 48 48" aria-hidden="true" focusable="false"><path d="M7 40C4 22 16 8 42 7c-1 25-15 38-35 33Z"/><path d="M9 39c8-13 17-21 29-28"/></svg><h3>More sustainable</h3><p>Use resources responsibly and protect the conditions that future generations will depend on.</p></article>
      <article class="outcome-card"><span class="card-number">02</span><svg class="outcome-symbol" viewBox="0 0 48 48" aria-hidden="true" focusable="false"><path d="M24 5 41 11v13c0 10-6.5 17.5-17 21C13.5 41.5 7 34 7 24V11L24 5Z"/><path d="m16 25 6 6 11-12"/></svg><h3>More resilient</h3><p>Build communities and systems that can adapt, recover, and keep serving people through change.</p></article>
      <article class="outcome-card"><span class="card-number">03</span><svg class="outcome-symbol" viewBox="0 0 48 48" aria-hidden="true" focusable="false"><circle cx="24" cy="24" r="19"/><path d="M24 12v12l9 6"/></svg><h3>More efficient</h3><p>Make better use of time, public resources, and human effort to solve real problems.</p></article>
      <article class="outcome-card"><span class="card-number">04</span><svg class="outcome-symbol" viewBox="0 0 48 48" aria-hidden="true" focusable="false"><path d="M24 42 8.3 27.3C1 20.3 5.2 8 14.3 8c4.2 0 7.6 2.3 9.7 5.4C26.1 10.3 29.5 8 33.7 8c9.1 0 13.3 12.3 6 19.3L24 42Z"/></svg><h3>Higher quality of life</h3><p>Measure progress by whether people can live healthier, safer, freer, and more fulfilling lives.</p></article>
    </div>
  </div>
</section>

<section class="section values-preview">
  <div class="shell two-column">
    <div class="sticky-heading"><span class="eyebrow">The way we work</span><h2>Conviction and curiosity belong together.</h2><p>Our values ask us to stay open to people, rigorous about ideas, and focused on useful change.</p>{link('./values.html', 'Read all three values <span aria-hidden="true">↗</span>', 'text-link')}</div>
    <div class="value-list">
      <a href="./values.html#listen"><span>01</span><div><h3>Listen to other perspectives.</h3><p>Go beyond the circles where agreement comes easily.</p></div><b aria-hidden="true">↗</b></a>
      <a href="./values.html#skeptical"><span>02</span><div><h3>Be skeptical, but respectful.</h3><p>Ask hard questions while honoring the people answering them.</p></div><b aria-hidden="true">↗</b></a>
      <a href="./values.html#advocate"><span>03</span><div><h3>Advocate for policies that move society forward.</h3><p>Let evidence and outcomes guide the work.</p></div><b aria-hidden="true">↗</b></a>
    </div>
  </div>
</section>

<section class="section winner-preview">
  <div class="shell">
    {section_intro('02', 'People in action', 'The next generation is already leading.', 'Our scholarship recognizes students who turn civic commitment into practical work.')}
    <div class="winner-grid">
      <article class="winner-card">
        <div class="winner-card-top"><span class="portrait-initials">LR</span><span class="year-tag">2026 winner</span></div>
        <div class="winner-card-body"><span class="eyebrow">Public health & policy</span><h3>Lauryn Russell</h3><p>From patient advocacy to Illinois legislation, Lauryn has worked across local, state, and federal policy to improve responses to tick-borne disease.</p>{link('./people.html#lauryn', 'Meet Lauryn <span aria-hidden="true">↗</span>', 'text-link')}</div>
      </article>
      <article class="winner-card">
        <div class="winner-card-top alt"><span class="portrait-initials">FR</span><span class="year-tag">2025 winner</span></div>
        <div class="winner-card-body"><span class="eyebrow">Youth voice & service</span><h3>Finlay Ross</h3><p>Finlay founded the Santa Monica Youth Advisory Council and helped young people take part in civic decisions and community service.</p>{link('./people.html#finlay', 'Meet Finlay <span aria-hidden="true">↗</span>', 'text-link')}</div>
      </article>
    </div>
  </div>
</section>

<section class="scholarship-banner">
  <div class="shell banner-inner"><div><span class="eyebrow light">Cooper Congress Scholarship</span><h2>Support for people who bring us together.</h2><p>The next application deadline is planned for August 20, 2027. Learn about the award and apply through Bold.org when the next cycle opens.</p></div><a class="button button-light" href="./scholarship.html">About the scholarship <span aria-hidden="true">↗</span></a></div>
</section>
"""

mission = f"""
<section class="page-hero shell">
  <div class="eyebrow"><span class="eyebrow-line"></span> Our mission</div>
  <h1>Progress is a <em>shared project.</em></h1>
  <p class="lead">Cooper Congress brings people across differences to listen carefully, question respectfully, and advance policies that make the United States and the world more sustainable, resilient, efficient, and livable.</p>
</section>
<section class="section mission-intro"><div class="shell split-prose"><span class="section-index"><span>01</span><span>Why we exist</span></span><div class="prose"><h2>A broader table. A clearer destination.</h2><p>We believe a proposal deserves consideration because of what it can accomplish, regardless of the perspective it comes from. A useful idea can emerge from a neighbor, a student, a public servant, a skeptic, or someone whose experience differs sharply from our own.</p><p>Openness is only a starting point. The next step is to ask what a policy would do, who it would affect, what it would cost, and whether it would leave people better equipped for the future. Listening across difference helps us see consequences that any one group might miss.</p></div></div></section>
<section class="section mission-outcomes"><div class="shell">
  {section_intro('02', 'The destination', 'Four tests for moving forward.', 'These outcomes give Cooper Congress a direction, not a partisan label. Strong proposals may advance several at once; tradeoffs deserve honest discussion.')}
  <div class="mission-grid">
    <article><span>01 / SUSTAINABILITY</span><h3>Can it last?</h3><p>Protect the environment and steward resources so tomorrow’s opportunities are not consumed today.</p></article>
    <article><span>02 / RESILIENCE</span><h3>Can it withstand change?</h3><p>Help people, institutions, and essential systems prepare for disruption and recover when it comes.</p></article>
    <article><span>03 / EFFICIENCY</span><h3>Does it use resources well?</h3><p>Reduce waste and friction so public effort reaches the people and problems it is meant to serve.</p></article>
    <article><span>04 / QUALITY OF LIFE</span><h3>Does life get better?</h3><p>Look beyond a single metric to health, safety, opportunity, freedom, connection, and everyday well-being.</p></article>
  </div>
</div></section>
<section class="section"><div class="shell split-prose"><span class="section-index"><span>03</span><span>Our approach</span></span><div class="prose"><h2>Make room for disagreement. Make demands of the idea.</h2><p>Respectful discussion does not require automatic agreement. It asks us to understand the people affected, test assumptions, examine evidence, and speak plainly about costs and tradeoffs.</p><p>Cooper Congress welcomes proposals from any perspective that can help move society forward. As the initiative grows, these principles can guide future conversations, resources, and civic work. Today, the scholarship is a concrete investment in people already practicing them.</p><a class="button button-dark" href="./scholarship.html">Explore the scholarship <span aria-hidden="true">↗</span></a></div></div></section>
<section class="quote-band"><div class="shell"><span class="eyebrow light">A guiding thought</span><blockquote>“The better we understand one another, the better we can understand the policy in front of us.”</blockquote><span>Cooper Congress</span></div></section>
"""

values = f"""
<section class="page-hero shell"><div class="eyebrow"><span class="eyebrow-line"></span> Our values</div><h1>How we <em>show up.</em></h1><p class="lead">A shared direction matters. So does the way we get there. These three commitments guide the conversations and policy thinking we hope to encourage.</p></section>
<section id="listen" class="value-detail section"><div class="shell value-detail-grid"><div class="value-detail-title"><span class="value-numeral">01</span><h2>Listen to other perspectives.</h2><p>Curiosity is a civic practice.</p></div><div class="prose"><p>Listening means more than waiting for a turn to reply. It means seeking out people beyond the groups where we feel most comfortable, asking what experiences shape their views, and checking whether we understood them correctly.</p><p>A policy can look elegant from a distance and fail in the life of someone it affects. Listening widens the evidence we have before we decide.</p><div class="practice"><span>Put it into practice</span><p>Join a conversation outside your usual circle. Ask a clarifying question. Summarize the other person’s concern before offering your answer.</p></div></div></div></section>
<section id="skeptical" class="value-detail section alternate"><div class="shell value-detail-grid"><div class="value-detail-title"><span class="value-numeral">02</span><h2>Be skeptical, but respectful.</h2><p>Take ideas seriously enough to test them.</p></div><div class="prose"><p>Respect for a person does not require agreement with a claim. We should ask for evidence, look for unintended consequences, and remain willing to change our minds when facts change.</p><p>Skepticism is most useful when it is applied to our own assumptions as well as to someone else’s. Disagreement can sharpen a proposal without diminishing the people who brought it forward.</p><div class="practice"><span>Put it into practice</span><p>Challenge the reasoning, name the tradeoff, and invite a response. Avoid reducing a person to a label or motive.</p></div></div></div></section>
<section id="advocate" class="value-detail section"><div class="shell value-detail-grid"><div class="value-detail-title"><span class="value-numeral">03</span><h2>Advocate for policies that move society forward.</h2><p>Keep outcomes in view.</p></div><div class="prose"><p>Dialogue should lead somewhere. We support the search for policies that make the United States and the world more sustainable, resilient, and efficient, while improving quality of life.</p><p>That means looking at who benefits, who bears a cost, whether a proposal can work in practice, and how we would know if it succeeds. Good intentions deserve a plan that can meet reality.</p><div class="practice"><span>Put it into practice</span><p>Describe the change you want, the people affected, the evidence behind it, and the result you would measure.</p></div></div></div></section>
<section class="section values-end"><div class="shell"><div class="end-card"><span class="eyebrow">Our standard</span><h2>Open to any perspective.<br><em>Accountable to the future.</em></h2><a class="button button-dark" href="./mission.html">See the mission <span aria-hidden="true">↗</span></a></div></div></section>
"""

people = f"""
<section class="page-hero shell"><div class="eyebrow"><span class="eyebrow-line"></span> The people</div><h1>Ideas become real through <em>people.</em></h1><p class="lead">Meet the founder of Cooper Congress and the first two recipients of the Cooper Congress Scholarship.</p></section>
<section id="matthew" class="section founder-section"><div class="shell person-layout"><div class="person-panel"><span class="person-monogram">MC</span><span class="panel-caption">Founder / Matthew Cooper</span></div><div class="person-copy"><span class="eyebrow">The founder</span><h2>Matthew Cooper</h2><p class="person-intro">A commitment to good ideas, wherever they come from.</p><p>Matthew Cooper founded Cooper Congress and funds the Cooper Congress Scholarship. A former Congressional fellow and federal employee, he is committed to public service that values listening, civil discourse, and practical progress.</p><p>Through the scholarship, Matthew supports students who bridge divides and use policy and civic leadership to help others be heard.</p><a class="text-link" href="https://bold.org/donor/matthew-cooper/" target="_blank" rel="noopener noreferrer">Matthew’s Bold.org profile <span aria-hidden="true">↗</span></a></div></div></section>
<section class="section winners-section"><div class="shell">{section_intro('01', 'Scholarship recipients', 'Leadership already in motion.', 'The following profiles summarize the recipients’ winning applications on Bold.org.')}
  <article id="lauryn" class="recipient">
    <div class="recipient-sidebar"><div class="recipient-mark">LR</div><span>2026 recipient</span><span>Illinois / public health</span></div>
    <div class="recipient-main"><span class="eyebrow">Policy shaped by lived experience</span><h3>Lauryn Russell</h3><p>Lauryn’s experience with Lyme disease led her into legislative advocacy in Illinois. She connected with lawmakers, testified, and helped turn firsthand experience into policy. Illinois law recognizes the Lyme Disease Prevention and Protection Act by her name.</p><p>Her application describes ongoing work with the Illinois Lyme Association, the Illinois Tick Policy Coalition, and the Center for Lyme Action. She aims to shape tick-borne disease and rural health policy across levels of government.</p><div class="recipient-note"><span>What her work shows</span><p>Policy improves when decision makers listen to the people who live with its consequences.</p></div><div class="recipient-links"><a href="{SCHOLARSHIP_URL}" target="_blank" rel="noopener noreferrer">Read her winning application on Bold.org <span aria-hidden="true">↗</span></a><a href="https://www.ilga.gov/Legislation/ILCS/Articles?ActID=3919&amp;ChapterID=35" target="_blank" rel="noopener noreferrer">View the Illinois law <span aria-hidden="true">↗</span></a></div></div>
  </article>
  <article id="finlay" class="recipient">
    <div class="recipient-sidebar alt"><div class="recipient-mark">FR</div><span>2025 recipient</span><span>California / youth leadership</span></div>
    <div class="recipient-main"><span class="eyebrow">A voice for younger citizens</span><h3>Finlay Ross</h3><p>Finlay founded the Santa Monica Youth Advisory Council to create a lasting way for young people to participate in local government. Their application also describes founding a letter-writing club that helps students speak to elected leaders before they can vote.</p><p>Finlay has helped lead a school effort that distributes meals to food-insecure families, served on Congressman Ted Lieu’s Youth Advisory Council, and taken part in other civic and service programs. Across these roles, the common thread is making participation practical.</p><div class="recipient-note"><span>What their work shows</span><p>People are more likely to be heard when someone builds a place for them at the table.</p></div><div class="recipient-links"><a href="{SCHOLARSHIP_URL}" target="_blank" rel="noopener noreferrer">Read the winning application on Bold.org <span aria-hidden="true">↗</span></a></div></div>
  </article>
</div></section>
<section class="scholarship-banner"><div class="shell banner-inner"><div><span class="eyebrow light">The scholarship</span><h2>Know someone building bridges?</h2><p>The next deadline is planned for August 20, 2027. Learn about the award and its application.</p></div><a class="button button-light" href="./scholarship.html">Scholarship details <span aria-hidden="true">↗</span></a></div></section>
"""

scholarship = f"""
<section class="page-hero shell scholarship-hero"><div class="eyebrow"><span class="eyebrow-line"></span> Cooper Congress Scholarship</div><h1>Investing in <em>people who connect us.</em></h1><p class="lead">The Cooper Congress Scholarship recognizes students who bring people together through civil discourse, public service, and a commitment to policy change.</p><div class="button-row">{link(SCHOLARSHIP_URL, 'View scholarship on Bold.org <span aria-hidden="true">↗</span>', 'button button-dark', True)}</div></section>
<section class="award-strip"><div class="shell award-grid"><div><span>Most recent award</span><strong>$1,000</strong></div><div><span>Recipients</span><strong>One per cycle</strong></div><div><span>2027 deadline</span><strong>August 20</strong></div><div><span>2027 award date</span><strong>September 21</strong></div></div></section>
<section class="section"><div class="shell">{section_intro('01', '2027 requirements', 'Who can apply?', 'Founder Matthew Cooper confirms the 2027 application will use the same qualifications as the 2026 cycle. Applications are submitted on Bold.org.')}<div class="eligibility-grid"><div class="eligibility-card"><span>01</span><h3>Education</h3><p>High school senior or undergraduate student.</p></div><div class="eligibility-card"><span>02</span><h3>Citizenship</h3><p>U.S. citizen.</p></div><div class="eligibility-card"><span>03</span><h3>Field of study</h3><p>Law, legislation, political science, public policy, government, or a related field.</p></div></div><p class="eligibility-footnote">Applicants should advocate for policy change. Volunteer experience is strongly preferred. The scholarship also looks for interest or experience in conflict resolution, peacebuilding, or mediation; commitment to public service; and inclusive civic leadership.</p></div></section>
<section class="section application-section"><div class="shell split-prose"><span class="section-index"><span>02</span><span>How to apply</span></span><div class="prose"><h2>Tell the story behind your civic work.</h2><p>The 2027 application is planned to use the same prompts and materials as the 2026 cycle. Submit through Bold.org. Write a 400–600 word essay answering one of three themes:</p><ol class="prompt-list"><li><strong>Mediation and peacebuilding.</strong> Describe resolving a disagreement across opposing views.</li><li><strong>Policy and government aspirations.</strong> Explain the policy issue and level of government you hope to work in, and the role of civil discourse.</li><li><strong>Values and impact.</strong> Explain what it means to ensure everyone has a voice.</li></ol><p>Also list relevant civic, leadership, mediation, or policy roles with dates and verification contacts, and upload one to five photos reflecting connection, listening, vision, or inspiration. The official Bold.org listing has the full prompts and instructions.</p><a class="button button-dark" href="{SCHOLARSHIP_URL}" target="_blank" rel="noopener noreferrer">Read the official instructions <span aria-hidden="true">↗</span></a></div></div></section>
<section class="section cycle-section"><div class="shell cycle-card"><div><span class="eyebrow">2027 cycle</span><h2>Mark your calendar.</h2><p>The next application deadline is August 20, 2027, with the award scheduled for September 21, 2027, according to founder Matthew Cooper. The 2026 award is complete. Apply through Bold.org when its next cycle opens and use its listing to confirm live application status.</p><span class="checked-date">Bold.org’s 2026 listing checked October 7, 2026; 2027 dates provided by the founder.</span></div><a class="button button-light" href="{SCHOLARSHIP_URL}" target="_blank" rel="noopener noreferrer">Check Bold.org <span aria-hidden="true">↗</span></a></div></section>
<section class="section"><div class="shell">{section_intro('03', 'The recipients', 'Meet the first two winners.', 'Their work shows how listening and civic action can reinforce each other.')}<div class="simple-winners"><a href="./people.html#lauryn"><span>2026</span><strong>Lauryn Russell</strong><em>Public health & policy</em><b aria-hidden="true">↗</b></a><a href="./people.html#finlay"><span>2025</span><strong>Finlay Ross</strong><em>Youth voice & service</em><b aria-hidden="true">↗</b></a></div></div></section>
"""

not_found = f"""
<section class="page-hero shell not-found"><div class="eyebrow"><span class="eyebrow-line"></span> Page not found</div><h1>Let’s find a <em>better path.</em></h1><p class="lead">That page may have moved or may no longer be available. Start with the Cooper Congress home page.</p><a class="button button-dark" href="./index.html">Back to home <span aria-hidden="true">↗</span></a></section>
"""

layout("index.html", "Ideas across differences", "Cooper Congress welcomes good ideas from every perspective and advances policies for a more sustainable, resilient, efficient, and livable future.", home)
layout("mission.html", "Our mission", "The Cooper Congress mission: listen across differences and advance policies that move society forward.", mission)
layout("values.html", "Our values", "Listen to other perspectives. Be skeptical but respectful. Advocate for policies that move society forward.", values)
layout("people.html", "Our people", "Meet Cooper Congress founder Matthew Cooper and scholarship winners Lauryn Russell and Finlay Ross.", people)
layout("scholarship.html", "The scholarship", "Learn about the Cooper Congress Scholarship, its planned 2027 deadline, eligibility and application requirements, and its winners.", scholarship)
layout("404.html", "Page not found", "Find your way back to Cooper Congress.", not_found)

sitemap_pages = [url for url, _ in NAV]
(ROOT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(
        f"  <url><loc>{SITE_URL if page == 'index.html' else SITE_URL + page}</loc></url>\n"
        for page in sitemap_pages
    )
    + "</urlset>\n",
    encoding="utf-8",
)
(ROOT / "robots.txt").write_text(
    "User-agent: *\nAllow: /\nSitemap: " + SITE_URL + "sitemap.xml\n",
    encoding="utf-8",
)
