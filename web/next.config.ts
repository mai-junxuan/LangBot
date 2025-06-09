import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  /* config options here */
  output: 'export',
  experimental: {
    missingSuspenseWithCSRBailout: false,
  },
} as any;

export default nextConfig;
