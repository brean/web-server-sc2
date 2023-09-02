import express from 'express';
import { handleWeb } from './handle_web';
import path from 'path';

function initExpress() {
  const port = Number(process.env.PORT || 4000) + 
  Number(process.env.NODE_APP_INSTANCE || 0);

  const app = express();
  app.use(express.json());

  const BASE_PATH = path.join(__dirname, '..');
  const STATIC_PATH = path.join(BASE_PATH, 'static');

  console.log(`[server] public path: ${STATIC_PATH}`)
  app.use('/', express.static(STATIC_PATH));

  app.get('/', (req, res) => {
    res.sendFile(path.join(STATIC_PATH, 'index.html'));
  });

  handleWeb(app);

  const server = app.listen(port, () => {
    console.log(`[server] Server is running on port: ${port}`);
  });

  return {app, server};
}

export {initExpress}