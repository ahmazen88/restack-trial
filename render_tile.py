#!/usr/bin/env python3
"""Procedural clean render of large-format glossy cream floor tile."""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

OUTPUT = Path("/opt/cursor/artifacts/tile_render.png")
WIDTH, HEIGHT = 2048, 1152

BASE = np.array([242, 240, 230], dtype=np.float32)
GROUT = np.array([210, 208, 200], dtype=np.float32)
ROUGHNESS = 0.06


def smoothstep(e0: float, e1: float, x: np.ndarray) -> np.ndarray:
    t = np.clip((x - e0) / (e1 - e0 + 1e-8), 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def render() -> Path:
    h, w = HEIGHT, WIDTH
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    nx = (xx / w) * 2.0 - 1.0
    ny = (yy / h) * 2.0 - 1.0

    horizon = 0.28
    depth = np.clip((ny - horizon) / (1.0 - horizon), 0.0, 1.0)
    persp = 1.0 / np.maximum(depth, 0.03)
    fx = nx * persp
    fz = (persp - 1.0) * 1.8

    tw, th, gw = 1.0, 2.0, 0.011
    cw, ch = tw + gw, th + gw
    tu = np.mod(fx + 8.0, cw)
    tv = np.mod(fz + 4.0, ch)
    grout = (tu < gw) | (tu > tw) | (tv < gw) | (tv > th)

    # Fine horizontal ribbing (visible in foreground)
    line_freq = 2.0 * math.pi / (2.8 + 5.0 * depth)
    ribs = 0.5 + 0.5 * np.sin(tv * line_freq)
    rib_shade = 1.0 - 0.022 * (1.0 - smoothstep(0.15, 0.85, ribs))

    # Base albedo
    rgb = np.zeros((h, w, 3), dtype=np.float32)
    tile_col = BASE / 255.0
    grout_col = GROUT / 255.0
    for c in range(3):
        rgb[:, :, c] = np.where(grout, grout_col[c], tile_col[c] * rib_shade)

    # Diffuse lighting
    diffuse = 0.52 + 0.48 * (1.0 - depth) ** 0.5
    rgb *= diffuse[:, :, None]

    # Glossy specular — window band left + soft overhead
    gloss = (1.0 - ROUGHNESS) ** 2.2
    win = np.exp(-((nx + 0.42) ** 2) / 0.055) * np.exp(-((ny - 0.18) ** 2) / 0.1)
    win *= (1.0 - depth) ** 2.0 * gloss * 0.95

    overhead = np.exp(-((nx) ** 2) / 0.5) * np.exp(-((ny + 0.05) ** 2) / 0.35)
    overhead *= (1.0 - depth) ** 0.9 * gloss * 0.25

    # Elongated reflection along tile length
    streak = 0.18 * gloss * (1.0 - depth) ** 1.4
    streak *= 0.6 + 0.4 * np.sin(fx * 1.8 + 0.5)

    spec = (win + overhead + streak)[:, :, None] * np.array([1.0, 0.99, 0.95])
    rgb += spec

    # Wall (upper region)
    wall_mask = ny < horizon
    wt = np.clip((horizon - ny) / horizon, 0.0, 1.0)
    wall = np.stack(
        [
            0.94 + 0.03 * (1 - wt),
            0.94 + 0.03 * (1 - wt),
            0.92 + 0.03 * (1 - wt),
        ],
        axis=-1,
    )
    rgb[wall_mask] = wall[wall_mask]

    # Floor mask with soft blend at horizon
    floor_w = smoothstep(horizon - 0.01, horizon + 0.04, ny)
    rgb = rgb * floor_w[:, :, None] + wall * (1.0 - floor_w[:, :, None])

    # Baseboard shadow
    shadow = smoothstep(horizon + 0.01, horizon + 0.08, ny) * (
        1.0 - smoothstep(horizon + 0.08, horizon + 0.18, ny)
    )
    rgb -= shadow[:, :, None] * 0.05

    # Subtle vignette
    d = np.sqrt(((xx - w * 0.5) / (w * 0.55)) ** 2 + ((yy - h * 0.62) / (h * 0.55)) ** 2)
    rgb *= (1.0 - 0.1 * smoothstep(0.5, 1.0, d))[:, :, None]

    rgb = np.clip(rgb, 0.0, 1.0)
    out = (rgb ** (1.0 / 2.2) * 255.0).astype(np.uint8)
    img = Image.fromarray(out, mode="RGB")
    img = img.filter(ImageFilter.UnsharpMask(radius=1.1, percent=85, threshold=1))

    # Minimal label
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, w, 56], fill=(248, 247, 244))
    draw.text((40, 16), "Cream Gloss Porcelain  60 × 120 cm", fill=(48, 48, 46))
    draw.text((40, 34), "#F2F0E6  ·  fine linear texture  ·  matching grout", fill=(110, 108, 104))

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUTPUT, quality=96)
    print(f"Saved {OUTPUT}")
    return OUTPUT


if __name__ == "__main__":
    render()
