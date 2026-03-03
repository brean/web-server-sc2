export default interface IGameStep {
  game_id: string
  iteration: number
  units: [x: number, y: number, type: number][]
  structures: [x: number, y: number, type: number][]
  enemy_units: [x: number, y: number, type: number][]
  enemy_structures: [x: number, y: number, type: number][]
}
