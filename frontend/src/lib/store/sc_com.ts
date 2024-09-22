// data communication store
import { writable } from 'svelte/store';
import type SCCom from '$lib/com/SCCom';
const ws = writable<SCCom | undefined>(undefined);
export default ws;