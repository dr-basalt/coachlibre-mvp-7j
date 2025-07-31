import express from 'express';
import payload from 'payload';
import dotenv from 'dotenv';

dotenv.config();

const app = express();

// Redirection root vers admin
app.get('/', (_, res) => {
  res.redirect('/admin');
});

const start = async (): Promise<void> => {
  // Initialisation Payload
  await payload.init({
    secret: process.env.PAYLOAD_SECRET!,
    express: app,
    onInit: async () => {
      payload.logger.info(`Payload Admin URL: ${payload.getAdminURL()}`)
    },
  });

  // Ajout de routes API personnalisées
  app.get('/api/health', (req, res) => {
    res.json({ status: 'OK', timestamp: new Date().toISOString() });
  });

  const port = process.env.PORT || 3001;

  app.listen(port, async () => {
    payload.logger.info(`Server listening on port ${port}`);
  });
};

start();
