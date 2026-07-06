import { createServer } from 'http';
import { readFile, mkdir } from 'fs/promises';
import { join, extname } from 'path';
import { fileURLToPath } from 'url';
import { chromium } from 'playwright';

const __dirname = fileURLToPath(new URL('.', import.meta.url));
const PORT = 8787;
const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json' };

const server = createServer(async (req, res) => {
  const path = req.url === '/' ? '/index.html' : req.url.split('?')[0];
  try {
    const body = await readFile(join(__dirname, path));
    res.writeHead(200, { 'Content-Type': MIME[extname(path)] || 'text/plain' });
    res.end(body);
  } catch {
    res.writeHead(404);
    res.end('Not found');
  }
});

async function shot(page, fn, out) {
  await page.evaluate((name) => {
    document.getElementById('hud').style.display = 'none';
    document.getElementById('capture').style.display = 'none';
    document.getElementById('views').style.display = 'none';
    window[name]();
  }, fn);
  await page.waitForTimeout(800);
  await page.screenshot({ path: out, type: 'png' });
  console.log(`Saved ${out}`);
}

server.listen(PORT, async () => {
  await mkdir('/opt/cursor/artifacts/flat4c', { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto(`http://127.0.0.1:${PORT}/`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(2500);
  await shot(page, 'setView01', '/opt/cursor/artifacts/flat4c/foyer_perspective.png');
  await shot(page, 'setMuralView', '/opt/cursor/artifacts/flat4c/foyer_mural_wall.png');
  await shot(page, 'setConsoleView', '/opt/cursor/artifacts/flat4c/foyer_console_detail.png');
  await shot(page, 'setTopView', '/opt/cursor/artifacts/flat4c/foyer_plan.png');
  await browser.close();
  server.close();
});
