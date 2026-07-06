# Flat 4C — 2D Design Images

Rev B schematic drawings and captured renders for **Flat 4C · Warm Modern Heritage**.

## Generate images

```bash
cd flat4c && npm install && npx playwright install chromium && npm run capture
cd ../foyer && npm install && node capture.mjs
```

Output: `/opt/cursor/artifacts/flat4c/`

| File | Description |
|---|---|
| `flat4c_floor_plan.png` | Schematic 3BHK floor plan with finish zones |
| `flat4c_room_elevations.png` | Key room wall elevations (6 spaces) |
| `flat4c_material_board.png` | Material & finishes schedule board |
| `flat4c_lighting_matrix.png` | 4-layer lighting criteria diagram |
| `foyer_perspective.png` | 3D foyer perspective (Rev B) |
| `foyer_mural_wall.png` | W03 sepia toile mural wall |
| `foyer_console_detail.png` | V01 walnut console detail |
| `foyer_plan.png` | Foyer plan view |
