# AARVI SEO and GEO deployment

The static HTML site retains its existing Render setup. Dedicated programme pages contain visible text, metadata, FAQs and Service structured data. The homepage contains Organization, Person and WebSite structured data.

## Production domain required

The confirmed production origin is `https://aarvi-consultants.onrender.com`. Its `sitemap.xml` and `robots.txt` are committed. When changing the production domain, run `SITE_URL=https://YOUR-NEW-VERIFIED-DOMAIN python3 scripts/generate-sitemap.py`, then commit the generated files. The sitemap generator deliberately requires a verified HTTPS origin. If Render runs a build command, configure SITE_URL and run the generator there; otherwise commit the generated files. Check that the nested programme URLs return HTTP 200 and that Render serves them rather than falling back to the homepage.

`seo.js` sets canonical and Open Graph URLs from the actual browser origin. For strongest crawler compatibility, replace these with absolute HTML canonical URLs after confirming the production domain.

## Google Search Console

Create or select the property for the real domain, use Google's DNS or HTML verification method, then submit `/sitemap.xml`. Inspect all five URLs. A verification token cannot be generated without the property owner completing Google's process.

## ChatGPT Search

The robots file explicitly allows Googlebot, OAI-SearchBot and Google-Extended. Google-Extended is a publisher preference affecting Gemini Apps grounding and future model training; it does not change Google Search indexing or ranking. Check any hosting firewall or CDN against OpenAI's published searchbot IP ranges. GPTBot is a separate training crawler; this change does not set a training-use preference.

## Content integrity

No programme duration, placement guarantee, performance statistics or unverified phone numbers were added. Confirm public contact details and participant photo permissions before publication. FAQ content is visible on each programme page; rich-result display is not guaranteed.

## Google AI discovery and measurement

Google Search AI Overviews and AI Mode use ordinary indexed Search content; no separate AI-specific schema or llms.txt is required. The programme pages retain visible FAQs but no longer use FAQPage schema, since Google removed the FAQ rich-result feature in 2026. Search Console now provides generative AI performance reporting. Check it after ownership verification; indexing and Gemini citations cannot be guaranteed. Review actual programme evidence and photo captions before adding more factual claims.
