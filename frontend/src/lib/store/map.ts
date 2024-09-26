// current Map
import IMap from '$lib/model/IMap';
import { writable } from 'svelte/store';
const current_map = writable<IMap>();
export default current_map;