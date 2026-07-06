import { PALETTE } from './colors.js';
import { setupCanvas, clear, titleBlock, drawRect, drawArch, label } from './draw-utils.js';

const W = 1400;
const H = 900;
const ELEV_W = 620;
const ELEV_H = 280;
const GAP = 24;

function drawElevation(ctx, x, y, w, h, room) {
  drawRect(ctx, x, y, w, h, PALETTE.warmPutty, PALETTE.ink, 2);
  drawRect(ctx, x, y - 28, w, 28, PALETTE.matteWhite, PALETTE.ink, 1);

  room.elements.forEach((el) => {
    const ex = x + el.fx * w;
    const ey = y + el.fy * h;
    const ew = el.fw * w;
    const eh = el.fh * h;
    if (el.type === 'arch') {
      drawArch(ctx, ex + ew / 2, ey + eh, ew, eh, el.fill, PALETTE.ink);
    } else if (el.type === 'frame') {
      drawRect(ctx, ex, ey, ew, eh, el.fill, PALETTE.walnut, 2);
      drawRect(ctx, ex + 6, ey + 6, ew - 12, eh - 12, PALETTE.sepiaToileDark, PALETTE.walnut, 1);
    } else if (el.type === 'console') {
      drawRect(ctx, ex, ey, ew, eh, PALETTE.walnut, PALETTE.ink, 1.5);
      label(ctx, 'V01', ex + ew / 2, ey + eh / 2 + 4, 9, '#fff');
    } else if (el.type === 'tv') {
      drawRect(ctx, ex, ey, ew, eh, PALETTE.ink, PALETTE.ink, 1);
      drawRect(ctx, ex - 8, ey + eh, ew + 16, 12, PALETTE.walnut, PALETTE.ink, 1);
    } else if (el.type === 'art') {
      drawRect(ctx, ex, ey, ew, eh, PALETTE.limeTexture, PALETTE.ink, 1);
      ctx.strokeStyle = PALETTE.brass;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(ex - 4, ey - 8);
      ctx.lineTo(ex + ew + 4, ey - 8);
      ctx.stroke();
      label(ctx, 'Track accent', ex + ew / 2, ey - 14, 8, PALETTE.brass);
    } else if (el.type === 'cabinet') {
      drawRect(ctx, ex, ey, ew, eh, PALETTE.paleOak, PALETTE.ink, 1.5);
    } else if (el.type === 'counter') {
      drawRect(ctx, ex, ey, ew, 10, PALETTE.honedGranite, PALETTE.ink, 1);
      drawRect(ctx, ex, ey + 10, ew, eh - 10, PALETTE.paleOak, PALETTE.ink, 1);
    } else if (el.type === 'headboard') {
      drawRect(ctx, ex, ey, ew, eh, PALETTE.walnut, PALETTE.ink, 1.5);
      drawRect(ctx, ex + 10, ey + eh, 30, 18, PALETTE.walnutLight, PALETTE.ink, 1);
      drawRect(ctx, ex + ew - 40, ey + eh, 30, 18, PALETTE.walnutLight, PALETTE.ink, 1);
    } else if (el.type === 'bench') {
      drawRect(ctx, ex, ey, ew, eh, PALETTE.walnut, PALETTE.ink, 1);
    } else if (el.type === 'cove') {
      ctx.fillStyle = 'rgba(255, 220, 170, 0.35)';
      ctx.fillRect(ex, ey, ew, eh);
    } else if (el.type === 'sconce') {
      ctx.fillStyle = PALETTE.brass;
      ctx.beginPath();
      ctx.arc(ex, ey, 5, 0, Math.PI * 2);
      ctx.fill();
    } else {
      drawRect(ctx, ex, ey, ew, eh, el.fill, PALETTE.ink, 1);
    }
  });

  label(ctx, room.name, x + w / 2, y + h + 22, 12, PALETTE.ink);
  label(ctx, room.caption, x + w / 2, y + h + 38, 9, PALETTE.inkMuted);
}

const ROOMS = [
  {
    name: 'FOYER & ENTRANCE',
    caption: 'W03 sepia toile panel · V01 walnut console · arch motif · brass chandelier',
    elements: [
      { type: 'cove', fx: 0, fy: 0, fw: 1, fh: 0.06 },
      { type: 'frame', fx: 0.08, fy: 0.12, fw: 0.38, fh: 0.55, fill: PALETTE.sepiaToile },
      { type: 'arch', fx: 0.55, fy: 0.35, fw: 0.22, fh: 0.45, fill: '#D8E4EE' },
      { type: 'console', fx: 0.52, fy: 0.62, fw: 0.4, fh: 0.14 },
    ],
  },
  {
    name: 'LIVING ROOM',
    caption: 'Art wall primary · V01 floating TV console secondary · reading spot',
    elements: [
      { type: 'cove', fx: 0, fy: 0, fw: 1, fh: 0.05 },
      { type: 'art', fx: 0.06, fy: 0.15, fw: 0.42, fh: 0.45 },
      { type: 'tv', fx: 0.58, fy: 0.42, fw: 0.32, fh: 0.22 },
      { type: 'sconce', fx: 0.12, fy: 0.72 },
    ],
  },
  {
    name: 'DINING',
    caption: 'Statement pendants · cove perimeter · green accent on sightline',
    elements: [
      { type: 'cove', fx: 0, fy: 0, fw: 1, fh: 0.05 },
      { fill: PALETTE.accentGreen, fx: 0.42, fy: 0.55, fw: 0.08, fh: 0.25 },
      { fill: PALETTE.brass, fx: 0.38, fy: 0.08, fw: 0.04, fh: 0.12 },
      { fill: PALETTE.brass, fx: 0.48, fy: 0.06, fw: 0.04, fh: 0.14 },
      { fill: PALETTE.brass, fx: 0.58, fy: 0.08, fw: 0.04, fh: 0.12 },
    ],
  },
  {
    name: 'KITCHEN',
    caption: 'L01 Pale Oak full-height · S01 honed granite · S02 quartz splash',
    elements: [
      { type: 'counter', fx: 0.05, fy: 0.48, fw: 0.9, fh: 0.42 },
      { fill: PALETTE.paleQuartz, fx: 0.05, fy: 0.38, fw: 0.9, fh: 0.1 },
      { fill: 'rgba(255,230,180,0.4)', fx: 0.05, fy: 0.46, fw: 0.9, fh: 0.03 },
    ],
  },
  {
    name: 'MASTER BEDROOM',
    caption: 'V01 full-width headboard · floating side tables · window bench',
    elements: [
      { type: 'cove', fx: 0, fy: 0, fw: 1, fh: 0.05 },
      { type: 'headboard', fx: 0.1, fy: 0.35, fw: 0.8, fh: 0.28 },
      { type: 'bench', fx: 0.62, fy: 0.55, fw: 0.28, fh: 0.12 },
      { type: 'cabinet', fx: 0.78, fy: 0.2, fw: 0.18, fh: 0.65 },
    ],
  },
  {
    name: 'CHILDREN\'S ROOM',
    caption: 'Impact-resistant L01 · radiused edges · brass reading sconces',
    elements: [
      { type: 'cabinet', fx: 0.06, fy: 0.22, fw: 0.35, fh: 0.62 },
      { type: 'cabinet', fx: 0.58, fy: 0.22, fw: 0.36, fh: 0.62 },
      { type: 'sconce', fx: 0.2, fy: 0.55 },
      { type: 'sconce', fx: 0.78, fy: 0.55 },
      { fill: PALETTE.limeTexture, fx: 0.42, fy: 0.3, fw: 0.16, fh: 0.2 },
    ],
  },
];

export function renderElevations() {
  const ctx = setupCanvas('elevations', W, H);
  clear(ctx, W, H);
  titleBlock(ctx, W, 'ROOM ELEVATIONS — KEY SPACES', 'Schematic wall elevations · finish codes annotated');

  const cols = 2;
  const startX = 60;
  const startY = 120;

  ROOMS.forEach((room, i) => {
    const col = i % cols;
    const row = Math.floor(i / cols);
    const x = startX + col * (ELEV_W + GAP + 60);
    const y = startY + row * (ELEV_H + 70);
    drawElevation(ctx, x, y, ELEV_W, ELEV_H, room);
  });
}
