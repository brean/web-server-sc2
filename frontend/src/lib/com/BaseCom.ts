// Communication base class, handles incoming (or fake) data
// and forwards it to the right service.
import { get } from 'svelte/store';

export default class BaseCom {
  websocket: WebSocket;
  endpoint: string;
  queue: string[] = [];

  constructor(port: number, endpoint: string) {
    const hostname = window.location.hostname;
    this.endpoint = endpoint;
    this.websocket = new WebSocket(`ws://${hostname}:${port}/${endpoint}`);
    this.websocket.onmessage = this.handleMessage.bind(this);
    this.websocket.onopen = this.onOpen.bind(this);
  }

  send(msg: string) {
    if (this.websocket.readyState !== this.websocket.OPEN) {
      this.queue.push(msg);
      return
    }
    this.websocket.send(msg);
  }

  onOpen() {
    for (const msg of this.queue) {
      this.websocket.send(msg);
    }
    this.queue = [];
  }

  handleMessage(ev: MessageEvent) {
    // the server told us something
    throw new Error("Not implemented!");
  }
}
