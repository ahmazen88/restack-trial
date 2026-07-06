import { FINISHES, PALETTE } from './colors.js';
import { setupCanvas, clear, titleBlock, drawRect, label } from './draw-utils.js';

const W = 1400;
const H = 900;

export function renderMaterialBoard() {
  const ctx = setupCanvas('material-board', W, H);
  clear(ctx, W, H);
  titleBlock(ctx, W, 'MATERIAL & FINISHES BOARD', 'Refined schedule — Rev B design lock');

  const cols = 4;
  const sw = 280;
  const sh = 200;
  const ox = 60;
  const oy = 120;
  const gapX = 24;
  const gapY = 28;

  FINISHES.forEach((f, i) => {
    const col = i % cols;
    const row = Math.floor(i / cols);
    const x = ox + col * (sw + gapX);
    const y = oy + row * (sh + gapY);

    drawRect(ctx, x, y, sw, sh * 0.55, f.color, PALETTE.ink, 1.5);
    drawRect(ctx, x, y + sh * 0.55, sw, sh * 0.45, '#FFFFFF', PALETTE.ink, 1);

    label(ctx, f.code, x + 12, y + sh * 0.55 + 22, 14, PALETTE.ink, 'left');
    label(ctx, f.name, x + 12, y + sh * 0.55 + 40, 11, PALETTE.ink, 'left');
    label(ctx, f.spec, x + 12, y + sh * 0.55 + 58, 9, PALETTE.inkMuted, 'left');
    label(ctx, f.loc, x + 12, y + sh * 0.55 + 74, 9, PALETTE.brass, 'left');
  });

  // Design intent strip
  drawRect(ctx, 60, H - 100, W - 120, 56, PALETTE.walnut, null);
  label(ctx, 'DESIGN INTENT: Warm Modern Heritage', 80, H - 72, 14, '#F5F0E8', 'left');
  label(ctx, 'Architectural clarity · Material consistency · 2700K lighting · Hospitality-grade craftsmanship', 80, H - 50, 10, '#D4C8B8', 'left');
}
