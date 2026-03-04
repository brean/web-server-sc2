import { get } from 'svelte/store';

import BaseCom from "./BaseCom";
import type IGameMeta from '$lib/interfaces/IGameMeta';
import type IMap from '$lib/interfaces/IMap';
import type IGameStep from '$lib/interfaces/IGameStep';

// Websocket communication class for basic control
// can only be called onMount!
export default class SCCom extends BaseCom {
  constructor() {
    super('web_client');
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
      case 'map':
        current_map.set(data as IMap)
        break;
      case 'game_started':
        const all_games = get(games)
        for (const g of all_games) {
          if (g.game_id === data.game_id) {
            g.started = true
            games.set(all_games);
          }
        }
        break;
      case 'step':
        current_step.set(data as IGameStep)
        break;
    }
    console.log(data);
  }
}
