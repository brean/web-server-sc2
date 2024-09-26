// current step
import IGameStep from '$lib/model/IGameStep';
import { writable } from 'svelte/store';
const current_step = writable<IGameStep>();
export default current_step;