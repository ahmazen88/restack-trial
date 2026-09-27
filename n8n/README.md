# n8n (Community, local)

Free self-hosted n8n. **No n8n Cloud account.** Unlimited workflows and executions. You only pay for this machine.

n8n still shows a **local owner** login. That password lives on this instance only. It is not an n8n.io signup.

## Start

Needs **Node.js 24+** (`n8n@2.40.7`). If `node` is older, `start.sh` downloads Node 24.21.0 into gitignored `n8n/.n8n-node/`. Docker is not required for this 2.x npm install.

```bash
cd n8n
chmod +x start.sh
./start.sh
```

Editor: [http://localhost:5678](http://localhost:5678)

Pinned version: `n8n@2.40.7`. Override with `N8N_VERSION=…`.

First start downloads n8n from npm and can take several minutes.

### Local owner

If `n8n/.local-owner.env` exists, `start.sh` pre-provisions:

- Email: `local@n8n.local`
- Password: see that file (gitignored)

If the file is missing, n8n shows a one-time setup screen. Use any email; it never leaves this instance. Password: 8+ characters, one number, one capital letter.

Copy `.env.example` if you want to set env vars yourself. Do not commit `.local-owner.env` or `.n8n-data/`.

## Hello workflow

[`workflows/hello-n8n.json`](workflows/hello-n8n.json)

Manual Trigger → HTTP Request (`GET https://httpbin.org/json`) → Set fields (`slideshow.title`, `slideshow.author`).

In the editor: **…** menu → **Import from File**. Then **Execute workflow**.

CLI (with n8n already running from the same data folder, in another terminal):

```bash
npx --yes n8n@2.40.7 import:workflow --input=workflows/hello-n8n.json
```

## What this is not

- Not n8n Cloud. No trial, no card, no `app.n8n.cloud` signup.
- Skip **Settings → Usage and plan → Unlock** unless you want the optional free “Registered Community” extras (folders / debug-in-editor). Flows run without it.
- n8n 3.0 is moving self-host to Docker-only. This folder uses 2.40.7 on npm on purpose.

## Learn next

1. Run Hello n8n in the editor.
2. [Build your first workflow](https://docs.n8n.io/build-your-first-workflow.md) on `localhost:5678`.
3. Free courses: [n8n Academy](https://n8n.io/education/).
