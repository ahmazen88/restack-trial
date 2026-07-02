import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import {
  forestMuralTexture,
  woodGrainTexture,
  rugTexture,
  floorTexture,
  brassTexture,
} from './textures.js';

// Room dimensions from DWG proportions (metres)
const ROOM = { w: 4.2, d: 3.8, h: 3.0 };
const WALL_T = 0.12;

const IS_MOBILE = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

const renderer = new THREE.WebGLRenderer({
  antialias: !IS_MOBILE,
  preserveDrawingBuffer: true,
  powerPreference: IS_MOBILE ? 'low-power' : 'high-performance',
});
renderer.setPixelRatio(Math.min(window.devicePixelRatio, IS_MOBILE ? 1.5 : 2));
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.35;
document.body.appendChild(renderer.domElement);

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x3a3a3e);
scene.fog = new THREE.Fog(0x5a5a5e, 14, 24);

const camera = new THREE.PerspectiveCamera(48, window.innerWidth / window.innerHeight, 0.1, 40);
camera.position.set(-1.0, 1.68, -1.35);

const controls = new OrbitControls(camera, renderer.domElement);
controls.target.set(0.1, 1.15, 1.0);
controls.enableDamping = true;
controls.dampingFactor = IS_MOBILE ? 0.08 : 0.05;
controls.rotateSpeed = IS_MOBILE ? 0.5 : 1.0;
controls.enablePan = !IS_MOBILE;
controls.touches = { ONE: THREE.TOUCH.ROTATE, TWO: THREE.TOUCH.DOLLY_PAN };
controls.maxPolarAngle = Math.PI * 0.495;
controls.minDistance = 2.5;
controls.maxDistance = 10;
controls.update();

// Materials
const muralTex = forestMuralTexture();
muralTex.repeat.set(2.5, 1.2);

const muralMat = new THREE.MeshStandardMaterial({
  map: muralTex,
  roughness: 0.92,
  metalness: 0.0,
});

const floorMat = new THREE.MeshStandardMaterial({
  map: floorTexture(),
  roughness: 0.55,
  metalness: 0.05,
  color: 0x444448,
});

const woodMat = new THREE.MeshStandardMaterial({
  map: woodGrainTexture(false),
  roughness: 0.65,
  metalness: 0.02,
});

const darkWoodMat = new THREE.MeshStandardMaterial({
  map: woodGrainTexture(true),
  roughness: 0.7,
  metalness: 0.02,
});

const brassMat = new THREE.MeshStandardMaterial({
  map: brassTexture(),
  color: 0xd4af5a,
  roughness: 0.28,
  metalness: 0.85,
});

const frameMat = new THREE.MeshStandardMaterial({
  color: 0x5c3d28,
  roughness: 0.45,
  metalness: 0.35,
});

const chainMat = new THREE.MeshStandardMaterial({
  color: 0x1a1a1a,
  roughness: 0.35,
  metalness: 0.75,
});

const glassMat = new THREE.MeshPhysicalMaterial({
  color: 0xd8e4ee,
  roughness: 0.05,
  metalness: 0.0,
  transmission: 0.55,
  transparent: true,
  opacity: 0.75,
  thickness: 0.02,
});

const shadeMat = new THREE.MeshStandardMaterial({
  color: 0xf5f2ea,
  roughness: 0.88,
  metalness: 0.0,
  side: THREE.DoubleSide,
});

const rugMat = new THREE.MeshStandardMaterial({
  map: rugTexture(),
  roughness: 0.95,
  metalness: 0.0,
});

function box(w, h, d, mat, x, y, z, rx = 0, ry = 0, rz = 0) {
  const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), mat);
  m.position.set(x, y, z);
  m.rotation.set(rx, ry, rz);
  m.castShadow = true;
  m.receiveShadow = true;
  scene.add(m);
  return m;
}

function buildRoom() {
  const hw = ROOM.w / 2;
  const hd = ROOM.d / 2;

  // Floor
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(ROOM.w, ROOM.d), floorMat);
  floor.rotation.x = -Math.PI / 2;
  floor.receiveShadow = true;
  scene.add(floor);

  // Ceiling
  const ceil = new THREE.Mesh(new THREE.PlaneGeometry(ROOM.w, ROOM.d), muralMat.clone());
  ceil.rotation.x = Math.PI / 2;
  ceil.position.y = ROOM.h;
  scene.add(ceil);

  // Back wall (+Z)
  box(ROOM.w, ROOM.h, WALL_T, muralMat, 0, ROOM.h / 2, hd, 0, 0, 0);
  // Front wall (-Z)
  box(ROOM.w, ROOM.h, WALL_T, muralMat, 0, ROOM.h / 2, -hd, 0, 0, 0);
  // Right wall (+X)
  box(WALL_T, ROOM.h, ROOM.d, muralMat, hw, ROOM.h / 2, 0, 0, 0, 0);
  // Left wall (-X)
  box(WALL_T, ROOM.h, ROOM.d, muralMat, -hw, ROOM.h / 2, 0, 0, 0, 0);
}

function buildDoor() {
  const hw = ROOM.w / 2;
  const hd = ROOM.d / 2;
  const doorW = 0.95;
  const doorH = 2.15;
  const doorX = -hw + WALL_T / 2 + 0.02;
  const doorZ = -hd + 0.75;

  box(0.06, doorH, doorW, darkWoodMat, doorX, doorH / 2, doorZ);
  // Panels
  for (let row = 0; row < 2; row++) {
    for (let col = 0; col < 2; col++) {
      box(0.02, 0.72, 0.36, darkWoodMat,
        doorX + 0.04,
        0.55 + row * 0.95,
        doorZ - 0.22 + col * 0.44);
    }
  }
  // Knob
  const knob = new THREE.Mesh(
    new THREE.SphereGeometry(0.035, 16, 16),
    new THREE.MeshStandardMaterial({ color: 0xe8e8e8, metalness: 0.9, roughness: 0.2 }),
  );
  knob.position.set(doorX + 0.08, 1.0, doorZ + 0.35);
  scene.add(knob);
}

function buildWindow() {
  const hd = ROOM.d / 2;
  const winW = 1.55;
  const rectH = 1.25;
  const archR = winW / 2;
  const baseY = 1.15;
  const z = hd - WALL_T / 2 - 0.04;
  const totalH = rectH + archR;

  // Outer frame — lower rectangle
  box(winW + 0.1, rectH, 0.07, frameMat, 0, baseY + rectH / 2, z);
  box(winW + 0.1, 0.07, 0.07, frameMat, 0, baseY, z);
  box(0.07, rectH, 0.07, frameMat, -(winW + 0.1) / 2, baseY + rectH / 2, z);
  box(0.07, rectH, 0.07, frameMat, (winW + 0.1) / 2, baseY + rectH / 2, z);

  // Arch frame (half circle)
  const archShape = new THREE.Shape();
  archShape.absarc(0, 0, archR, 0, Math.PI, false);
  const archGeo = new THREE.TubeGeometry(
    new THREE.CatmullRomCurve3(
      Array.from({ length: 33 }, (_, i) => {
        const a = Math.PI * (i / 32);
        return new THREE.Vector3(Math.cos(a) * archR, Math.sin(a) * archR, 0);
      }),
    ),
    32, 0.035, 8, false,
  );
  const archMesh = new THREE.Mesh(archGeo, frameMat);
  archMesh.position.set(0, baseY + rectH, z);
  scene.add(archMesh);

  // Glass
  const glass = new THREE.Mesh(
    new THREE.PlaneGeometry(winW - 0.12, totalH - 0.12),
    glassMat,
  );
  glass.position.set(0, baseY + totalH / 2 - 0.05, z - 0.03);
  scene.add(glass);

  // 3×4 grid mullions (lower section)
  for (let c = 1; c < 3; c++) {
    const x = -winW / 2 + (winW * c) / 3;
    box(0.02, rectH - 0.08, 0.025, frameMat, x, baseY + rectH / 2, z - 0.02);
  }
  for (let r = 1; r < 4; r++) {
    const y = baseY + 0.04 + (rectH * r) / 4;
    box(winW - 0.12, 0.02, 0.025, frameMat, 0, y, z - 0.02);
  }

  // Radial mullions in arch
  for (let i = 1; i < 6; i++) {
    const a = Math.PI * (i / 6);
    const x0 = Math.cos(a) * 0.06;
    const y0 = Math.sin(a) * 0.06;
    const x1 = Math.cos(a) * (archR - 0.06);
    const y1 = Math.sin(a) * (archR - 0.06);
    const len = Math.hypot(x1 - x0, y1 - y0);
    const bar = new THREE.Mesh(new THREE.BoxGeometry(0.018, len, 0.025), frameMat);
    bar.position.set((x0 + x1) / 2, baseY + rectH + (y0 + y1) / 2, z - 0.02);
    bar.rotation.z = Math.atan2(x1 - x0, y1 - y0);
    scene.add(bar);
  }
}

function buildCabinet() {
  const hd = ROOM.d / 2;
  const cabW = 3.55;
  const cabH = 0.62;
  const cabD = 0.42;
  const z = hd - cabD / 2 - 0.05;
  const y = cabH / 2;
  const panelCount = 6;
  const panelW = cabW / panelCount;

  box(cabW, cabH, cabD, woodMat, 0, y, z);

  // Vertical chain strips between panels
  for (let i = 1; i < panelCount; i++) {
    const x = -cabW / 2 + panelW * i;
    box(0.035, cabH - 0.06, 0.04, chainMat, x, y, z + cabD / 2 + 0.01);

    // Chain links illusion
    for (let l = 0; l < 9; l++) {
      const link = new THREE.Mesh(
        new THREE.TorusGeometry(0.012, 0.004, 6, 12),
        chainMat,
      );
      link.position.set(x, 0.08 + l * 0.06, z + cabD / 2 + 0.025);
      link.rotation.y = Math.PI / 2;
      scene.add(link);
    }
  }

  // Panel seams
  for (let i = 1; i < panelCount; i++) {
    const x = -cabW / 2 + panelW * i;
    box(0.008, cabH - 0.04, cabD + 0.01, darkWoodMat, x, y, z);
  }

  // Sculptural object (left)
  const sculpt = new THREE.Mesh(
    new THREE.SphereGeometry(0.12, 16, 16),
    new THREE.MeshStandardMaterial({ color: 0x111111, roughness: 0.4, metalness: 0.1 }),
  );
  sculpt.scale.set(1.4, 0.7, 1.0);
  sculpt.position.set(-1.0, cabH + 0.08, z);
  sculpt.castShadow = true;
  scene.add(sculpt);

  // Open book (right)
  const bookBase = box(0.22, 0.025, 0.16, new THREE.MeshStandardMaterial({ color: 0xf0ebe0, roughness: 0.9 }), 1.15, cabH + 0.02, z);
  const bookL = new THREE.Mesh(
    new THREE.BoxGeometry(0.1, 0.02, 0.15),
    new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.95 }),
  );
  bookL.rotation.z = 0.35;
  bookL.position.set(1.08, cabH + 0.05, z);
  scene.add(bookL);
  const bookR = bookL.clone();
  bookR.rotation.z = -0.35;
  bookR.position.set(1.22, cabH + 0.05, z);
  scene.add(bookR);
}

function buildRug() {
  const rug = new THREE.Mesh(new THREE.PlaneGeometry(0.95, 2.65), rugMat);
  rug.rotation.x = -Math.PI / 2;
  rug.position.set(0.15, 0.006, 0.1);
  rug.receiveShadow = true;
  scene.add(rug);
}

function buildChandelier() {
  const group = new THREE.Group();
  group.position.set(0.1, ROOM.h - 0.15, 0.15);

  const stem = new THREE.Mesh(new THREE.CylinderGeometry(0.015, 0.02, 0.55, 12), brassMat);
  stem.position.y = -0.28;
  group.add(stem);

  const hub = new THREE.Mesh(new THREE.SphereGeometry(0.05, 16, 16), brassMat);
  hub.position.y = -0.52;
  group.add(hub);

  const armAngles = [0, Math.PI / 2, Math.PI, (3 * Math.PI) / 2, Math.PI / 4, (3 * Math.PI) / 4, (5 * Math.PI) / 4, (7 * Math.PI) / 4];
  const armHeights = [-0.48, -0.55, -0.5, -0.58, -0.52, -0.56, -0.49, -0.57];
  const armLens = [0.42, 0.38, 0.44, 0.36, 0.4, 0.37, 0.43, 0.39];

  armAngles.forEach((a, i) => {
    const len = armLens[i];
    const arm = new THREE.Mesh(new THREE.CylinderGeometry(0.006, 0.006, len, 8), brassMat);
    arm.rotation.z = Math.PI / 2;
    arm.rotation.y = a;
    arm.position.set(Math.cos(a) * len * 0.5, armHeights[i], Math.sin(a) * len * 0.5);
    group.add(arm);

    const shade = new THREE.Mesh(new THREE.ConeGeometry(0.09, 0.14, 20, 1, true), shadeMat);
    shade.position.set(Math.cos(a) * len, armHeights[i] - 0.1, Math.sin(a) * len);
    group.add(shade);

    const bulb = new THREE.PointLight(0xfff0d8, 0.35, 3.5);
    bulb.position.copy(shade.position);
    bulb.position.y -= 0.04;
    group.add(bulb);
  });

  scene.add(group);
}

function buildLighting() {
  scene.add(new THREE.AmbientLight(0xb0b4bc, 0.65));

  const sun = new THREE.DirectionalLight(0xfff5e8, 0.85);
  sun.position.set(-2, 4, 3);
  sun.castShadow = true;
  sun.shadow.mapSize.set(IS_MOBILE ? 1024 : 2048, IS_MOBILE ? 1024 : 2048);
  sun.shadow.camera.near = 0.5;
  sun.shadow.camera.far = 15;
  sun.shadow.camera.left = -5;
  sun.shadow.camera.right = 5;
  sun.shadow.camera.top = 5;
  sun.shadow.camera.bottom = -5;
  sun.shadow.bias = -0.0002;
  scene.add(sun);

  const fill = new THREE.DirectionalLight(0xc8d0e0, 0.45);
  fill.position.set(3, 2, -2);
  scene.add(fill);

  scene.add(new THREE.HemisphereLight(0xe8ecf4, 0x4a4a4e, 0.4));

  // Window glow
  const winLight = new THREE.RectAreaLight(0xe8f0ff, 3.2, 1.4, 1.6);
  winLight.position.set(0, 2.15, ROOM.d / 2 - 0.3);
  winLight.lookAt(0, 1.5, 0);
  scene.add(winLight);
}

buildRoom();
buildDoor();
buildWindow();
buildCabinet();
buildRug();
buildChandelier();
buildLighting();

function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}
animate();

// Match View 01 from DWG for static capture
export function setTopView() {
  controls.enabled = false;
  camera.position.set(0, 7.2, 0.001);
  camera.up.set(0, 0, -1);
  camera.lookAt(0, 0, 0);
  camera.updateProjectionMatrix();
}

export function setView01() {
  controls.enabled = true;
  camera.up.set(0, 1, 0);
  camera.position.set(-1.35, 1.62, -1.55);
  controls.target.set(0.05, 1.08, 0.85);
  controls.update();
}

function resize() {
  const w = window.innerWidth;
  const h = window.innerHeight || document.documentElement.clientHeight;
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
  renderer.setSize(w, h);
}

window.addEventListener('resize', resize);
window.addEventListener('orientationchange', () => setTimeout(resize, 200));
resize();

export function captureRender() {
  setView01();
  renderer.render(scene, camera);
  return renderer.domElement.toDataURL('image/png');
}

window.captureRender = captureRender;
window.setView01 = setView01;
window.setTopView = setTopView;
