import { get } from 'svelte/store';

import BaseCom from "./BaseCom";

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
    console.log(data);
  }
}
