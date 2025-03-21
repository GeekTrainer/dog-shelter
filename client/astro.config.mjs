// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import svelte from '@astrojs/svelte';

import node from '@astrojs/node';
const API_SERVER_URL = process.env.API_SERVER_URL || 'http://localhost:5100';

// https://astro.build/config
export default defineConfig({
  vite: {
    plugins: [tailwindcss(), svelte()],
    server: {
      proxy: {
        '/api': {
          target: API_SERVER_URL,
          changeOrigin: true,
        }
      }
    }
  },

  adapter: node({
    mode: 'standalone'
  }),

  integrations: [svelte()]
});