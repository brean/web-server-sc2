import type SCCom from "$lib/com/SCCom";
import type IGameInfo from "$lib/interfaces/IGameInfo"
import type IGameStep from "$lib/interfaces/IGameStep"
import type IMap from "$lib/interfaces/IMap"

export const uiState = $state<{
  maps: { [name: string]: IMap },
  games: IGameInfo[],
  game_steps: { [game_id: string]: IGameStep[] }
  com?: SCCom
}>({
  maps: {},
  games: [],
  game_steps: {}
});