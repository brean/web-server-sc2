import { get } from 'svelte/store';

import BaseCom from "./BaseCom";
import IGameMeta from '$lib/model/IGameMeta';
import games from '$lib/store/games';

// Websocket communication class for basic control
// can only be called onMount!
export default class SCCom extends BaseCom {
  constructor() {
    super(8000, 'web_client');
  }

  handleMessage(ev: MessageEvent) {
    this.handleData(JSON.parse(ev.data));
  }

  handleData(data: any) {
    // receive data from server
    switch (data.type) {
      case 'new_game':
        const g = get(games);
        g.push(data as IGameMeta);
        games.set(g);
        break;
      case 'game_started':
        // TODO: find game with data.game_id and set started to true;
        break;
      case 'step':
        // TODO: call render callback from IGameStep
        break;
    }
    console.log(data);
  }
}
