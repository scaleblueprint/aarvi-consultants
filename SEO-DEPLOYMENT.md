# AARVI SEO and GEO deployment

The static HTML site retains its existing Render setup. Dedicated programme pages contain visible text, metadata, FAQs and Service structured data. The homepage contains Organization, Person and WebSite structured data.

## Production domain required

The repository does not identify a verified production hostname. Do not guess it. Once confirmed, run `SITE_URL=https://YOUR-VERIFIED-DOMAIN python3 scripts/generate-sitemap.py`, then commit the resulting `sitemap.xml` and updated `robots.txt`. The sitemap generator deliberately requires a verified HTTPS origin. If Render runs a build command, configure SITE_URL and run the generator there; otherwise commit the generated files. Check that the nested programme URLs return HTTP 200 and that Render serves them rather than falling back to the homepage.

`seo.js` sets canonical and Open Graph URLs from the actual browser origin. For strongest crawler compatibility, replace these with absolute HTML canonical URLs after confirming the production domain.

## Google Search Console

Create or select the property for the real domain, use Google's DNS or HTML verification method, then submit `/sitemap.xml`. Inspect all five URLs. A verification token cannot be generated without the property owner completing Google's process.

## ChatGPT Search

The robots file explicitly allows OAI-SearchBot. Check any hosting firewall or CDN against OpenAI's published searchbot IP ranges. GPTBot is a separate training crawler; this change does not set a training-use preference.

## Content integrity

No programme duration, placement guarantee, performance statistics or unverified phone numbers were added. Confirm public contact details and participant photo permissions before publication. FAQ content is visible on each programme page; rich-result display is not guaranteed.
