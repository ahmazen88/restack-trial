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

export function forestMuralTexture() {
  return canvasTexture((ctx, w, h) => {
    const g = ctx.createLinearGradient(0, 0, 0, h);
    g.addColorStop(0, '#d4d4d0');
    g.addColorStop(0.45, '#b8b8b4');
    g.addColorStop(1, '#9a9a96');
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, w, h);

    const rng = (seed) => {
      let s = seed;
      return () => {
        s = (s * 16807 + 0) % 2147483647;
        return (s - 1) / 2147483646;
      };
    };

    for (let i = 0; i < 38; i++) {
      const r = rng(i * 97 + 13);
      const x = r() * w;
      const baseW = 8 + r() * 22;
      const hScale = 0.55 + r() * 0.45;
      const trunkH = h * hScale;
      const gray = 55 + Math.floor(r() * 45);

      ctx.fillStyle = `rgb(${gray}, ${gray}, ${gray - 4})`;
      ctx.beginPath();
      ctx.moveTo(x - baseW * 0.35, h);
      ctx.lineTo(x - baseW * 0.12, h - trunkH * 0.55);
      ctx.lineTo(x, h - trunkH);
      ctx.lineTo(x + baseW * 0.12, h - trunkH * 0.55);
      ctx.lineTo(x + baseW * 0.35, h);
      ctx.fill();

      ctx.strokeStyle = `rgba(30, 30, 28, ${0.08 + r() * 0.12})`;
      ctx.lineWidth = 1 + r() * 2;
      for (let b = 0; b < 6; b++) {
        const by = h - trunkH * (0.2 + b * 0.12);
        ctx.beginPath();
        ctx.moveTo(x - baseW * 0.2, by);
        ctx.quadraticCurveTo(x + (r() - 0.5) * 30, by - 8, x + baseW * 0.25, by + 4);
        ctx.stroke();
      }
    }

    ctx.fillStyle = 'rgba(255,255,255,0.06)';
    ctx.fillRect(0, 0, w, h * 0.35);
  }, 1024, 1024);
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
