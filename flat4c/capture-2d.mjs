import { createServer } from 'http';
import { readFile } from 'fs/promises';
import { join, extname } from 'path';
import { fileURLToPath } from 'url';
import { mkdir } from 'fs/promises';
import { chromium } from 'playwright';

const __dirname = fileURLToPath(new URL('.', import.meta.url));
const OUT = '/opt/cursor/artifacts/flat4c';
const PORT = 8790;
const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json' };

const SHEETS = [
  { name: 'floor-plan', file: 'flat4c_floor_plan.png' },
  { name: 'elevations', file: 'flat4c_room_elevations.png' },
  { name: 'material-board', file: 'flat4c_material_board.png' },
  { name: 'lighting-matrix', file: 'flat4c_lighting_matrix.png' },
];

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

async function captureSheet(page, sheetName, outPath) {
  await page.evaluate((name) => window.showSheet(name), sheetName);
  await page.waitForTimeout(400);
  await page.screenshot({ path: outPath, type: 'png' });
  console.log(`Saved ${outPath}`);
}

await mkdir(OUT, { recursive: true });

server.listen(PORT, async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });
  await page.goto(`http://127.0.0.1:${PORT}/`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(800);

  for (const sheet of SHEETS) {
    await captureSheet(page, sheet.name, join(OUT, sheet.file));
  }

  await browser.close();
  server.close();
  console.log(`\nAll ${SHEETS.length} images saved to ${OUT}`);
});
