import os
from pathlib import Path
from urllib.parse import urlparse
from xml.sax.saxutils import escape

origin = os.environ.get('SITE_URL', '').strip().rstrip('/')
parsed = urlparse(origin)
if parsed.scheme != 'https' or not parsed.netloc or parsed.path or parsed.query or parsed.fragment:
    raise SystemExit('Set SITE_URL to the verified HTTPS production origin')
paths = ['/', '/soft-skills-training/', '/communication-training/', '/faculty-development/', '/campus-to-corporate/']
root = Path(__file__).resolve().parent.parent
entries = '\n'.join('  <url><loc>' + escape(origin + path) + '</loc></url>' for path in paths)
(root / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + entries + '\n</urlset>\n', encoding='utf-8')
robots = root / 'robots.txt'
content = robots.read_text(encoding='utf-8')
content = '\n'.join(line for line in content.splitlines() if not line.startswith('Sitemap:'))
robots.write_text(content + '\nSitemap: ' + origin + '/sitemap.xml\n', encoding='utf-8')
print('Generated sitemap and robots for', origin)
