// data communication store
import IGameMeta from '$lib/model/IGameMeta';
import { writable } from 'svelte/store';
const games = writable<IGameMeta[]>([]);
export default games;