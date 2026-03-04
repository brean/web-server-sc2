export default class BaseCom {
  websocket?: WebSocket;
  endpoint: string;
  queue: string[] = [];

  constructor(endpoint: string) {
    this.endpoint = endpoint;
    this.connect()
  }

  connect() {
    this.websocket = new WebSocket(this.endpoint);
    this.websocket.onmessage = this.handleMessage.bind(this);
    this.websocket.onopen = this.onOpen.bind(this);
  }

  send(msg: string) {
    if (!this.websocket) {
      this.connect();
      this.queue.push(msg);
      return
    }
    if (this.websocket.readyState !== this.websocket.OPEN) {
      this.queue.push(msg);
      return
    }
    this.websocket.send(msg);
  }

  onOpen() {
    if (!this.websocket) {
      return
    }
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