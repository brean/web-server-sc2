// provide a list of games
import express from 'express';
import * as fs from 'fs';

// assuming the file is in the folder below, this is checked out besides the bot!
// TODO: configure different data provider and use a mongodb as alternative (?)
const BASE_PATH = `${__dirname}/../../../bot/data/replays`;

function handleWeb(app: express.Express) {
  app.get('/games', (req, res) => {
    const gameFiles = fs.readdirSync(BASE_PATH);
    const games: {}[] = [];
    gameFiles.forEach((filename) => {
      const stat = fs.statSync(`${BASE_PATH}/${filename}`);
      if (stat.isDirectory() || !filename.endsWith('.json') || !filename.startsWith('info_')) {
        return;
      }
      const data = fs.readFileSync(`${BASE_PATH}/${filename}`)
      games.push(JSON.parse(data.toString()))
    })
    res.json(games);
  });
  app.get('/game/:name', (req, res) => {
    const filename = `data_${req.params.name}.json`;
    if (fs.existsSync(`${BASE_PATH}/${filename}`)) {
      fs.readFile(`${BASE_PATH}/${filename}`, (err, data) => {
        return res.json(JSON.parse(data.toString()));
      });
    } else {
      res.json({
        ok: false,
        msg: 'file_not_found'
      });
    }
  })
};

export { handleWeb };