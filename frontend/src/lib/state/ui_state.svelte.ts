import type IGameMeta from "$lib/interfaces/IGameMeta"
import type IGameStep from "$lib/interfaces/IGameStep"
import type IMap from "$lib/interfaces/IMap"

export const uiState = $state<{
  maps: { [name: string]: IMap },
  games: IGameMeta[],
  game_steps: { [game_id: string]: IGameStep[] }
}>({
  maps: {},
  games: [],
  game_steps: {}
});