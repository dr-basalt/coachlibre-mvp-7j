import { buildConfig } from 'payload/config';
import { mongooseAdapter } from '@payloadcms/db-mongodb';
import { webpackBundler } from '@payloadcms/bundler-webpack';
import { slateEditor } from '@payloadcms/richtext-slate';
import path from 'path';

// Collections
import Users from './collections/Users';
import Coaches from './collections/Coaches';
import Appointments from './collections/Appointments';
import Media from './collections/Media';

export default buildConfig({
  admin: {
    user: Users.slug,
    bundler: webpackBundler(),
  },
  editor: slateEditor({}),
  collections: [Users, Coaches, Appointments, Media],
  typescript: {
    outputFile: path.resolve(__dirname, 'payload-types.ts'),
  },
  graphQL: {
    schemaOutputFile: path.resolve(__dirname, 'generated-schema.graphql'),
  },
  db: mongooseAdapter({
    url: process.env.DATABASE_URL!,
  }),
  cors: [
    'http://localhost:3000',
    'https://*.coachlibre.com',
    'https://*.coachlibre.dev'
  ],
  csrf: [
    'http://localhost:3000',
    'https://*.coachlibre.com',
    'https://*.coachlibre.dev'
  ]
});
