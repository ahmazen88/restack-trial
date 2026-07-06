import * as THREE from 'three';

function canvasTexture(draw, w = 512, h = 512) {
  const c = document.createElement('canvas');
  c.width = w;
  c.height = h;
  const ctx = c.getContext('2d');
  draw(ctx, w, h);
  const tex = new THREE.CanvasTexture(c);
  tex.wrapS = tex.wrapT = THREE.RepeatWrapping;
  tex.colorSpace = THREE.SRGBColorSpace;
  return tex;
}

export function sepiaToileTexture() {
  return canvasTexture((ctx, w, h) => {
    const g = ctx.createLinearGradient(0, 0, 0, h);
    g.addColorStop(0, '#d8ccc0');
    g.addColorStop(0.5, '#c4b4a0');
    g.addColorStop(1, '#a89888');
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, w, h);

    const rng = (seed) => {
      let s = seed;
      return () => {
        s = (s * 16807) % 2147483647;
        return (s - 1) / 2147483646;
      };
    };

    // Toile-style pastoral vignettes (sepia silhouettes)
    for (let s = 0; s < 6; s++) {
      const r = rng(s * 131 + 7);
      const cx = (s % 3) * (w / 3) + w / 6 + r() * 40;
      const cy = Math.floor(s / 3) * (h / 2) + h / 4 + r() * 30;
      const sc = 0.6 + r() * 0.5;

      ctx.fillStyle = `rgba(90, 72, 58, ${0.12 + r() * 0.1})`;
      ctx.beginPath();
      ctx.ellipse(cx, cy + 30 * sc, 45 * sc, 18 * sc, 0, 0, Math.PI * 2);
      ctx.fill();

      ctx.strokeStyle = `rgba(70, 55, 42, ${0.2 + r() * 0.15})`;
      ctx.lineWidth = 1.5 * sc;
      ctx.beginPath();
      ctx.moveTo(cx - 20 * sc, cy + 20 * sc);
      ctx.quadraticCurveTo(cx, cy - 40 * sc, cx + 25 * sc, cy + 15 * sc);
      ctx.stroke();

      for (let b = 0; b < 3; b++) {
        ctx.beginPath();
        ctx.arc(cx - 10 * sc + b * 12 * sc, cy - 5 * sc, 6 * sc, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(80, 65, 50, ${0.08})`;
        ctx.fill();
      }
    }

    // Ornate border frame hint
    ctx.strokeStyle = 'rgba(92, 61, 40, 0.35)';
    ctx.lineWidth = 12;
    ctx.strokeRect(24, 24, w - 48, h - 48);
    ctx.lineWidth = 2;
    ctx.strokeRect(40, 40, w - 80, h - 80);
  }, 1024, 1024);
}

/** @deprecated use sepiaToileTexture — kept for import compat */
export function forestMuralTexture() {
  return sepiaToileTexture();
}

export function woodGrainTexture(dark = false) {
  return canvasTexture((ctx, w, h) => {
    const base = dark ? [62, 42, 28] : [118, 82, 52];
    ctx.fillStyle = `rgb(${base[0]}, ${base[1]}, ${base[2]})`;
    ctx.fillRect(0, 0, w, h);

    for (let y = 0; y < h; y++) {
      const n = Math.sin(y * 0.08) * 8 + Math.sin(y * 0.021) * 14;
      const r = base[0] + n;
      const g = base[1] + n * 0.7;
      const b = base[2] + n * 0.4;
      ctx.fillStyle = `rgb(${r | 0}, ${g | 0}, ${b | 0})`;
      ctx.fillRect(0, y, w, 1);
    }

    for (let i = 0; i < 120; i++) {
      const y = Math.random() * h;
      ctx.strokeStyle = `rgba(0,0,0,${0.03 + Math.random() * 0.06})`;
      ctx.lineWidth = 0.5 + Math.random();
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.bezierCurveTo(w * 0.3, y + Math.random() * 6 - 3, w * 0.7, y + Math.random() * 6 - 3, w, y);
      ctx.stroke();
    }
  }, 512, 512);
}

export function rugTexture() {
  return canvasTexture((ctx, w, h) => {
    ctx.fillStyle = '#8a8680';
    ctx.fillRect(0, 0, w, h);

    for (let i = 0; i < 8000; i++) {
      const x = Math.random() * w;
      const y = Math.random() * h;
      const a = 0.04 + Math.random() * 0.12;
      const tone = 120 + Math.random() * 80;
      ctx.fillStyle = `rgba(${tone}, ${tone - 8}, ${tone - 18}, ${a})`;
      ctx.fillRect(x, y, 2 + Math.random() * 5, 1 + Math.random() * 3);
    }

    for (let i = 0; i < 40; i++) {
      ctx.strokeStyle = `rgba(200, 190, 175, ${0.05 + Math.random() * 0.08})`;
      ctx.lineWidth = 8 + Math.random() * 20;
      ctx.beginPath();
      const y = Math.random() * h;
      ctx.moveTo(0, y);
      ctx.lineTo(w, y + (Math.random() - 0.5) * 30);
      ctx.stroke();
    }

    const edge = ctx.createLinearGradient(0, 0, w, 0);
    edge.addColorStop(0, 'rgba(60,58,54,0.35)');
    edge.addColorStop(0.08, 'rgba(0,0,0,0)');
    edge.addColorStop(0.92, 'rgba(0,0,0,0)');
    edge.addColorStop(1, 'rgba(60,58,54,0.35)');
    ctx.fillStyle = edge;
    ctx.fillRect(0, 0, w, h);
  }, 1024, 512);
}

export function floorTexture() {
  return canvasTexture((ctx, w, h) => {
    ctx.fillStyle = '#3a3a3c';
    ctx.fillRect(0, 0, w, h);
    for (let i = 0; i < 3000; i++) {
      const g = 50 + Math.random() * 20;
      ctx.fillStyle = `rgba(${g}, ${g}, ${g + 2}, 0.15)`;
      ctx.fillRect(Math.random() * w, Math.random() * h, 2, 2);
    }
  }, 256, 256);
}

export function brassTexture() {
  return canvasTexture((ctx, w, h) => {
    const g = ctx.createLinearGradient(0, 0, w, h);
    g.addColorStop(0, '#c9a24e');
    g.addColorStop(0.5, '#e8cc7a');
    g.addColorStop(1, '#a88432');
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, w, h);
  }, 64, 64);
}
