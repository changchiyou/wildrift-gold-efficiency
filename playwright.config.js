// @ts-check
import { defineConfig } from "@playwright/test";

// Serves the pre-built ./_site (build the site first: bundle exec jekyll build).
const PORT = Number(process.env.E2E_PORT || 4173);

export default defineConfig({
  testDir: "tests/e2e",
  timeout: 30_000,
  fullyParallel: true,
  reporter: process.env.CI ? "github" : "list",
  use: {
    baseURL: `http://127.0.0.1:${PORT}`,
    trace: "on-first-retry",
  },
  webServer: {
    command: `node tests/e2e/static-server.mjs ${PORT}`,
    url: `http://127.0.0.1:${PORT}/en-US/7.3a/`,
    reuseExistingServer: !process.env.CI,
  },
});
