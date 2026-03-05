export default interface IGameInfo {
  game_id: string
  bot_name: string
  opponent_name: string
  map: string
  game_name?: string
  started: Date
  finished: Date
}
