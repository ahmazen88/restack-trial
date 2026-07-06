import { PALETTE } from './colors.js';
import { setupCanvas, clear, titleBlock, drawRect, drawArch, label, dimensionLine } from './draw-utils.js';

const W = 1400;
const H = 900;

export function renderFloorPlan() {
  const ctx = setupCanvas('floor-plan', W, H);
  clear(ctx, W, H);
  titleBlock(ctx, W, 'FLOOR PLAN — SCHEMATIC', '3BHK · ~1,834 sq.ft. · Not to scale — indicative layout');

  const ox = 120;
  const oy = 130;
  const scale = 5.2;

  const rooms = [
    { id: 'FOYER', x: 0, y: 0, w: 14, d: 10, fill: PALETTE.sepiaToile, note: 'W03 mural · V01 console' },
    { id: 'LIVING', x: 14, y: 0, w: 22, d: 18, fill: PALETTE.warmPutty, note: 'Art wall · V01 TV console' },
    { id: 'DINING', x: 36, y: 0, w: 14, d: 14, fill: PALETTE.warmPutty, note: 'Pendant · green accent' },
    { id: 'KITCHEN', x: 36, y: 14, w: 14, d: 12, fill: PALETTE.paleOak, note: 'L01 HPL · S01/S02' },
    { id: 'MASTER', x: 0, y: 10, w: 20, d: 18, fill: PALETTE.warmPutty, note: 'V01 headboard · window bench' },
    { id: 'MASTER BATH', x: 0, y: 28, w: 10, d: 8, fill: PALETTE.whiteQuartz, note: 'S03 vanity' },
    { id: 'BED 2', x: 20, y: 18, w: 16, d: 14, fill: PALETTE.warmPutty, note: 'L01 wardrobe' },
    { id: 'BED 3', x: 20, y: 32, w: 16, d: 12, fill: PALETTE.warmPutty, note: 'Children — adaptable' },
    { id: 'COMMON BATH', x: 36, y: 26, w: 10, d: 8, fill: PALETTE.whiteQuartz, note: 'S03 vanity' },
    { id: 'UTILITY', x: 46, y: 14, w: 6, d: 8, fill: PALETTE.paleOak, note: 'Full-height storage' },
  ];

  rooms.forEach((r) => {
    const px = ox + r.x * scale;
    const py = oy + r.y * scale;
    const pw = r.w * scale;
    const ph = r.d * scale;
    drawRect(ctx, px, py, pw, ph, r.fill, PALETTE.ink, 2);
    label(ctx, r.id, px + pw / 2, py + ph / 2 - 6, 12, PALETTE.ink);
    label(ctx, r.note, px + pw / 2, py + ph / 2 + 12, 9, PALETTE.inkMuted);
  });

  // Slatted threshold at dining transition
  const threshX = ox + 36 * scale;
  const threshY = oy;
  ctx.fillStyle = PALETTE.walnut;
  for (let i = 0; i < 14; i++) {
    ctx.fillRect(threshX - 4, threshY + i * (14 * scale / 14), 8, 3);
  }
  label(ctx, 'Slatted threshold', threshX + 20, threshY + 30, 9, PALETTE.walnut, 'left');

  // Entry arrow
  ctx.strokeStyle = PALETTE.brass;
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(ox - 30, oy + 5 * scale);
  ctx.lineTo(ox + 2, oy + 5 * scale);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(ox + 2, oy + 5 * scale);
  ctx.lineTo(ox - 6, oy + 5 * scale - 6);
  ctx.moveTo(ox + 2, oy + 5 * scale);
  ctx.lineTo(ox - 6, oy + 5 * scale + 6);
  ctx.stroke();
  label(ctx, 'ENTRY', ox - 50, oy + 5 * scale - 18, 10, PALETTE.brass);

  dimensionLine(ctx, ox, oy + 42 * scale + 20, ox + 52 * scale, oy + 42 * scale + 20, '~52\'-0" overall', 0);
  dimensionLine(ctx, ox - 30, oy, ox - 30, oy + 36 * scale, '~36\'-0"', 0);

  // Legend
  const lx = 980;
  const ly = 140;
  label(ctx, 'FINISH LEGEND', lx, ly, 12, PALETTE.ink, 'left');
  const legend = [
    [PALETTE.sepiaToile, 'W03 — Foyer mural zone'],
    [PALETTE.walnut, 'V01 — Hero joinery'],
    [PALETTE.paleOak, 'L01 — Cabinetry'],
    [PALETTE.warmPutty, 'W01 — Main walls'],
    [PALETTE.whiteQuartz, 'S03 — Wet areas'],
  ];
  legend.forEach(([c, t], i) => {
    drawRect(ctx, lx, ly + 20 + i * 28, 20, 16, c, PALETTE.ink, 1);
    label(ctx, t, lx + 30, ly + 32 + i * 28, 10, PALETTE.inkMuted, 'left');
  });

  label(ctx, 'North ↑', W / 2, H - 30, 11, PALETTE.inkMuted);
}
