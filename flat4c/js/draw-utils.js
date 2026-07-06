import { PALETTE } from './colors.js';

export function setupCanvas(id, w, h, dpr = 2) {
  const canvas = document.getElementById(id);
  canvas.width = w * dpr;
  canvas.height = h * dpr;
  canvas.style.width = `${w}px`;
  canvas.style.height = `${h}px`;
  const ctx = canvas.getContext('2d');
  ctx.scale(dpr, dpr);
  return ctx;
}

export function clear(ctx, w, h, bg = '#FAF8F5') {
  ctx.fillStyle = bg;
  ctx.fillRect(0, 0, w, h);
}

export function titleBlock(ctx, w, title, subtitle, rev = 'Rev B') {
  ctx.fillStyle = PALETTE.ink;
  ctx.font = '600 22px system-ui, sans-serif';
  ctx.fillText(title, 40, 48);
  ctx.fillStyle = PALETTE.inkMuted;
  ctx.font = '400 13px system-ui, sans-serif';
  ctx.fillText(subtitle, 40, 72);
  ctx.font = '500 11px system-ui, sans-serif';
  ctx.fillText(`FLAT 4C · ${rev} · WARM MODERN HERITAGE`, w - 280, 48);
  ctx.strokeStyle = PALETTE.grid;
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(40, 88);
  ctx.lineTo(w - 40, 88);
  ctx.stroke();
}

export function drawRect(ctx, x, y, w, h, fill, stroke = PALETTE.ink, lw = 1.5) {
  if (fill) {
    ctx.fillStyle = fill;
    ctx.fillRect(x, y, w, h);
  }
  if (stroke) {
    ctx.strokeStyle = stroke;
    ctx.lineWidth = lw;
    ctx.strokeRect(x, y, w, h);
  }
}

export function drawArch(ctx, cx, baseY, w, h, fill, stroke = PALETTE.ink) {
  const r = w / 2;
  ctx.beginPath();
  ctx.moveTo(cx - r, baseY);
  ctx.lineTo(cx - r, baseY - h + r);
  ctx.arc(cx, baseY - h + r, r, Math.PI, 0);
  ctx.lineTo(cx + r, baseY);
  ctx.closePath();
  if (fill) {
    ctx.fillStyle = fill;
    ctx.fill();
  }
  if (stroke) {
    ctx.strokeStyle = stroke;
    ctx.lineWidth = 1.5;
    ctx.stroke();
  }
}

export function drawHatch(ctx, x, y, w, h, color, spacing = 8) {
  ctx.save();
  ctx.beginPath();
  ctx.rect(x, y, w, h);
  ctx.clip();
  ctx.strokeStyle = color;
  ctx.lineWidth = 0.8;
  for (let i = -h; i < w + h; i += spacing) {
    ctx.beginPath();
    ctx.moveTo(x + i, y);
    ctx.lineTo(x + i + h, y + h);
    ctx.stroke();
  }
  ctx.restore();
}

export function label(ctx, text, x, y, size = 11, color = PALETTE.ink, align = 'center') {
  ctx.fillStyle = color;
  ctx.font = `${size}px system-ui, sans-serif`;
  ctx.textAlign = align;
  ctx.fillText(text, x, y);
}

export function dimensionLine(ctx, x1, y1, x2, y2, text, offset = 14) {
  const isHoriz = Math.abs(y2 - y1) < 2;
  ctx.strokeStyle = PALETTE.inkMuted;
  ctx.lineWidth = 0.75;
  ctx.fillStyle = PALETTE.inkMuted;
  ctx.font = '10px system-ui, sans-serif';
  ctx.textAlign = 'center';

  if (isHoriz) {
    const y = y1 - offset;
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x1, y);
    ctx.moveTo(x2, y2);
    ctx.lineTo(x2, y);
    ctx.moveTo(x1, y);
    ctx.lineTo(x2, y);
    ctx.stroke();
    ctx.fillText(text, (x1 + x2) / 2, y - 4);
  } else {
    const x = x1 - offset;
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x, y1);
    ctx.moveTo(x2, y2);
    ctx.lineTo(x, y2);
    ctx.moveTo(x, y1);
    ctx.lineTo(x, y2);
    ctx.stroke();
    ctx.save();
    ctx.translate(x - 6, (y1 + y2) / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText(text, 0, 0);
    ctx.restore();
  }
}
