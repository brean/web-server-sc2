# Web Server to view and analyze StarCraft 2 bot logs.

For the backend TypeScript express.js is used to forward json files generated as logs by the bot and shows live data from current bot-runs with WebSockets.

For the frontend Svelte with TypeScript and Material-ui is used for the frontend.

## Development
### Installation
Option 1 - Using docker: Install docker, docker compose and terminator and just run `docker compose build`. For convenient development the source files of backend and frontend-svelte folders are mounted as volumens in their respective container.

Option 2 - Run directly on your machine: Go into the backend and frontend-svelte folder and install locally using `npm i -D`

### Running
Option 1 - Using docker: Start the `./start.bash`-script. After you close the terminator window the command `docker compose down` will kill/remove the docker container

Option 2 - Run directly on your machine: Run `npm run start` in the `server` folder and `npm run dev -- --open` in the `fontent-svelte` folder

## Deployment
ToDo!

## License
Distributed under the [3-clause BSD license](https://opensource.org/licenses/BSD-3-Clause).

## Maintainer

Andreas Bresser, self@andreasbresser.de

## Authors / Contributers

Authors and contributers are [listed on github](https://github.com/brean/web-server-sc2/graphs/contributors).