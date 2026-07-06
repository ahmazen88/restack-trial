import { PALETTE } from './colors.js';
import { setupCanvas, clear, titleBlock, drawRect, label } from './draw-utils.js';

const W = 1400;
const H = 900;

const LAYERS = [
  {
    name: 'LAYER 1 — GENERAL AMBIENT COVES',
    spec: '2700 K · Dimmable · Deep-baffle low-glare',
    color: 'rgba(255, 220, 170, 0.55)',
    y: 0,
  },
  {
    name: 'LAYER 2 — ARCHITECTURAL ACCENT',
    spec: 'Track spots on artwork · CRI ≥ 95',
    color: 'rgba(212, 175, 120, 0.5)',
    y: 1,
  },
  {
    name: 'LAYER 3 — TASK CIRCUITS',
    spec: 'Under-cabinet LED · Vanity · Reading spots',
    color: 'rgba(180, 200, 220, 0.45)',
    y: 2,
  },
  {
    name: 'LAYER 4 — DECORATIVE ANCHORS',
    spec: 'Foyer table lamp · Dining pendants',
    color: 'rgba(184, 149, 107, 0.55)',
    y: 3,
  },
];

export function renderLightingMatrix() {
  const ctx = setupCanvas('lighting-matrix', W, H);
  clear(ctx, W, H);
  titleBlock(ctx, W, 'LIGHTING CRITERIA MATRIX', 'Multi-layer illumination — no single-source spaces');

  const ox = 120;
  const oy = 160;
  const bw = 900;
  const bh = 90;
  const gap = 16;

  LAYERS.forEach((layer, i) => {
    const y = oy + i * (bh + gap + 40);
    drawRect(ctx, ox, y, bw, bh, layer.color, PALETTE.ink, 2);
    label(ctx, layer.name, ox + bw / 2, y + bh / 2 - 8, 14, PALETTE.ink);
    label(ctx, layer.spec, ox + bw / 2, y + bh / 2 + 14, 11, PALETTE.inkMuted);

    if (i < LAYERS.length - 1) {
      ctx.strokeStyle = PALETTE.brass;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(ox + bw / 2, y + bh);
      ctx.lineTo(ox + bw / 2, y + bh + gap + 40);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(ox + bw / 2 - 8, y + bh + gap + 28);
      ctx.lineTo(ox + bw / 2, y + bh + gap + 40);
      ctx.lineTo(ox + bw / 2 + 8, y + bh + gap + 28);
      ctx.stroke();
    }
  });

  // Standards box
  const sx = 1080;
  const sy = 200;
  drawRect(ctx, sx, sy, 260, 200, '#FFFFFF', PALETTE.ink, 1.5);
  label(ctx, 'STANDARDS', sx + 20, sy + 28, 12, PALETTE.ink, 'left');
  label(ctx, 'Color temp: 2700 K (locked)', sx + 20, sy + 52, 10, PALETTE.inkMuted, 'left');
  label(ctx, 'General areas: CRI ≥ 90', sx + 20, sy + 72, 10, PALETTE.inkMuted, 'left');
  label(ctx, 'Task / art / vanity: CRI ≥ 95', sx + 20, sy + 92, 10, PALETTE.inkMuted, 'left');
  label(ctx, 'Hold Point 6:', sx + 20, sy + 120, 10, PALETTE.brass, 'left');
  label(ctx, 'Night-time glare audit', sx + 20, sy + 136, 10, PALETTE.inkMuted, 'left');
  label(ctx, 'before handover', sx + 20, sy + 152, 10, PALETTE.inkMuted, 'left');

  // Room application strip
  const rooms = ['Foyer', 'Living', 'Dining', 'Kitchen', 'Master', 'Children'];
  const rx = 120;
  const ry = H - 160;
  label(ctx, 'APPLICATION BY SPACE', rx, ry, 12, PALETTE.ink, 'left');
  rooms.forEach((r, i) => {
    const x = rx + i * 190;
    drawRect(ctx, x, ry + 16, 170, 70, PALETTE.warmPutty, PALETTE.ink, 1);
    label(ctx, r, x + 85, ry + 42, 11, PALETTE.ink);
    label(ctx, '4 layers', x + 85, ry + 58, 9, PALETTE.brass);
  });
}
